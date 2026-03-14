import psutil
import time
import os
import threading

threshold = 75

# Artificial CPU load function
def cpu_stress():
    while True:
        x = 0
        for i in range(10000000):
            x += i * i


# Start 2 stress threads
for _ in range(2):
    threading.Thread(target=cpu_stress, daemon=True).start()

while True:
    cpu = psutil.cpu_percent(interval=2)
    print("CPU Usage:", cpu)

    if cpu > threshold:
        print("CPU usage exceeded 75%. Starting Cloud scaling...")

        os.system(
            "gcloud compute instances create ml-cloud-srvr "
            "--zone=us-central1-a "
            "--machine-type=e2-micro "
            "--image-family=ubuntu-2204-lts "
            "--image-project=ubuntu-os-cloud"
        )

        break

    time.sleep(3)
