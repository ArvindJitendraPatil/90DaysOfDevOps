from flask import Flask, render_template, jsonify
import psutil
import socket
import platform
import requests
import time
import sys
import os
from datetime import datetime

app = Flask(__name__)


def get_metadata(path):
    try:
        token = requests.put(
            "http://169.254.169.254/latest/api/token",
            headers={"X-aws-ec2-metadata-token-ttl-seconds": "21600"},
            timeout=2
        ).text

        return requests.get(
            f"http://169.254.169.254/latest/meta-data/{path}",
            headers={"X-aws-ec2-metadata-token": token},
            timeout=2
        ).text
    except:
        return "N/A"


@app.route("/")
def dashboard():
    hostname = socket.gethostname()

    cpu = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count()
    cpu_freq = round(psutil.cpu_freq().current, 2) if psutil.cpu_freq() else 0

    mem = psutil.virtual_memory()
    memory = mem.percent
    memory_total = round(mem.total / (1024**3), 2)
    memory_available = round(mem.available / (1024**3), 2)

    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    disk_total = round(disk.total / (1024**3), 2)
    disk_free = round(disk.free / (1024**3), 2)

    uptime_seconds = int(time.time() - psutil.boot_time())
    uptime = f"{uptime_seconds//86400}d {(uptime_seconds%86400)//3600}h"

    os_name = platform.system()
    os_version = platform.release()
    python_version = sys.version.split()[0]

    net = psutil.net_io_counters()
    bytes_sent = round(net.bytes_sent / (1024**2), 2)
    bytes_recv = round(net.bytes_recv / (1024**2), 2)

    try:
        load1, load5, load15 = os.getloadavg()
    except:
        load1 = load5 = load15 = 0

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    boot_time = datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")

    instance_id = get_metadata("instance-id")
    instance_type = get_metadata("instance-type")
    availability_zone = get_metadata("placement/availability-zone")
    public_ip = get_metadata("public-ipv4")

    return render_template(
        "index.html",
        hostname=hostname,
        cpu=cpu,
        cpu_count=cpu_count,
        cpu_freq=cpu_freq,
        memory=memory,
        memory_total=memory_total,
        memory_available=memory_available,
        disk=disk_usage,
        disk_total=disk_total,
        disk_free=disk_free,
        uptime=uptime,
        os_name=os_name,
        os_version=os_version,
        python_version=python_version,
        bytes_sent=bytes_sent,
        bytes_recv=bytes_recv,
        load1=load1,
        load5=load5,
        load15=load15,
        current_time=current_time,
        boot_time=boot_time,
        instance_id=instance_id,
        instance_type=instance_type,
        availability_zone=availability_zone,
        public_ip=public_ip
    )


@app.route("/health")
def health():
    return jsonify({
        "status": "UP",
        "host": socket.gethostname()
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
