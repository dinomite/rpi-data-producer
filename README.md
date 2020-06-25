# Startup script
Goes in /etc/systemd/system/multi-user.target.wants/data-producer.service

Then

    sudo systemctl --system daemon-reload

Manage with:

    sudo systemctl [start/stop] data-producer.service
