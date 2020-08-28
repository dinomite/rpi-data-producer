#!/usr/bin/env python3
import json
import subprocess

from http.server import BaseHTTPRequestHandler,HTTPServer
from w1thermsensor import W1ThermSensor, SensorNotReadyError, NoSensorFoundError


def get_1w_sensor(sensor_id):
    try:
        return W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, sensor_id)
    except NoSensorFoundError as e:
        logger.error("Sensor " + sensor_id + " not found", e)
        exit(1)


class HttpHandler(BaseHTTPRequestHandler):
    def do_GET(s):
        s.send_response(200)
        s.send_header('Content-type', 'application/json')
        s.end_headers()

        response = []
        for node_name, sensors in nodes.items():
            for sensor_name, (group, data_type, value_lambda) in nodes.items():
                response.append({'group': group, 'name': sensor_name, 'type': data_type, 'value': value_lambda()})

        s.wfile.write(json.dumps(response).encode())


nodes = {
    'attic_temp': ("ENVIRONMENT", "IntSensor", lambda: round(get_1w_sensor("0416561dedff").get_temperature(W1ThermSensor.DEGREES_F) - 3)),
    'rpi_zero_cpu_temp': ("DEVICE", "DoubleSensor", lambda: float(subprocess.getoutput('vcgencmd measure_temp').split('=')[1].split("'")[0]))
}


httpd = HTTPServer(('', 8000), HttpHandler)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
httpd.server_close()
