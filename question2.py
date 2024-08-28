import psutil 
import time

def monitor_cpu_usage():
    try:
        print ("Monitoring CPU usage...\n")
        cpu_usage = psutil.cpu_percent()
        cpu_threshold = 85.0
        print(f"CPU utilization: {cpu_usage}%")
        if (cpu_usage > cpu_threshold):
            print("Alert! CPU usage exceeds threshold: 85%")
        else:
            print("CPU is running well.")
    except (psutil.Error, Exception) as e:
        print(f"An error occurred while monitoring CPU usage: {e}")

while True:
    monitor_cpu_usage()
    time.sleep(1)
    print("\n========================\n")