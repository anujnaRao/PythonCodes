import re
from collections import defaultdict

log = """ """
with open("/workspace/Projects/21DaysOfC++/file.txt", "r") as f:
    log = f.read()

def process_log(log):
    ip_counter = defaultdict(list)
    status_counter = defaultdict(int)
    total_count = 0
    for m in re.finditer(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - .*?HTTP/1.1" (\d+) (\d+)', log):
        total_count += 1
        ip = m[1]
        status = m[2]
        bytes = int(m[3])
        print(f"All data for: Ip: => {ip},Transferred => {bytes}")
        if bytes > 5000:
            print("Greater than 5000 transfer: ")
            print(f"Ip: => {ip},Transferred => {bytes}")
            bytes = bytes
            ip_counter[(ip, status)].append(bytes)
            status_counter[status] += 1
    print("------------------------------------")
    for k, v in ip_counter.items():
        count = len(v)
        # percentage = count/total_count
        total_bytes = sum(v)
        ip = k[0]
        status = k[1]
        print(
            f"Ip: => {ip}, Count => {count},Transferred => {total_bytes}")
        with open("/workspace/Projects/21DaysOfC++/fileNew.txt", "a") as f:
            f.write(f"Ip: => {ip}, Count => {count},Transferred => {total_bytes}")


# log = """
# 93.114.45.13 - - [17/May/2015:10:05:17 +0000] "GET /images/jordan-80.png HTTP/1.1" 200 616 "http://w...content-available-to-author-only...e.com/articles/dynamic-dns-with-dhcp/" "Mozilla/5.0 (X11; Linux x86_64; rv:25.0) Gecko/20100101 Firefox/25.0"
# 93.114.45.13 - - [17/May/2015:10:05:21 +0000] "GET /images/web/2009/banner.png HTTP/1.1" 200 315 "http://w...content-available-to-author-only...e.com/style2.css" "Mozilla/5.0 (X11; Linux x86_64; rv:25.0) Gecko/20100101 Firefox/25.0"
# 66.249.73.13 - - [17/May/2015:10:05:40 +0000] "GET /blog/tags/ipv6 HTTP/1.1" 200 12251 "-" "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25 (compatible; Googlebot/2.1;
# +http://www.google.com/bot.html)"
# 83.149.46.21 - - [17/May/2015:10:05:25 +0000] "GET /presentations/logstash-monitorama-2013/images/elasticsearch.png HTTP/1.1" 200 4326 "http://s...content-available-to-author-only...e.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
# 83.149.46.21 - - [17/May/2015:10:05:59 +0000] "GET /presentations/logstash-monitorama-2013/images/logstashbook.png HTTP/1.1" 200 54662 "http://s...content-available-to-author-only...e.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
# """

# with open("/workspace/Projects/21DaysOfC++/fileNew.txt", "w") as f:
#     f.write(log)

process_log(log)