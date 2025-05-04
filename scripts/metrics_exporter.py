from prometheus_client import start_http_server, Gauge
import subprocess, time

latency_gauge = Gauge('ping_latency_ms', 'ping latency to 8.8.8.8')

def get_ping():
    try:
        result = subprocess.run(['ping', '-c', '1', '8.8.8.8'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        output = result.stdout.decode()
        latency = float(output.split('time=')[-1].split()[0])
        return latency
    except:
        return None

if __name__ == '__main__':
    start_http_server(8000)
    while True:
        latency = get_ping()
        if latency:
            latency_gauge.set(latency)
        time.sleep(5)