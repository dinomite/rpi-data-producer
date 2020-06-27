# Startup script
Link to /etc/systemd/system/data-producer.service

Then

    sudo systemctl --system daemon-reload
    sudo systemctl enable data-producer.service

Manage with:

    sudo systemctl [start/stop] data-producer.service
