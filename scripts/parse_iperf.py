import re, csv

with open('../data/iperf_output.txt') as f,open('../data/iperf_log.csv','w', newline='') as output:
    writer = csv.writer(output)
    writer.writerow(['time_sec', 'throughput_mbps'])

    for line in f:
        match = re.search(r'\[\s*\d+\]\s+'
                                r'([\d.]+)-\s*([\d.]+)\s+'  
                                r'sec\s+'
                                r'[\d.]+\s+[GM]Bytes\s+'    
                                r'([\d.]+)\s+'              
                                r'([MG])bits/sec', line)
        if match:
            mid_time = (float(match.group(1)) + float(match.group(2))) / 2
            throughput = float(match.group(3))
            writer.writerow([mid_time, throughput])