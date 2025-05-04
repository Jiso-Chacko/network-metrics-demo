import subprocess, time, csv

def ping(host='8.8.8.8', count=1):
    result = subprocess.run(['ping', '-c', str(count), host], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    output = result.stdout.decode()
    try:
        latency = float(output.split('time=')[-1].split()[0])
        return latency
    except:
        return None

with open('data/ping_log.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['timestamp', 'latency_ms'])
    while True:
        latency = ping()
        if latency:
            writer.writerow([time.time(), latency])
            f.flush()
        time.sleep(5)
