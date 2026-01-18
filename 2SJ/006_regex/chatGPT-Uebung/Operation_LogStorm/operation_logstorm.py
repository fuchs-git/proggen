import re

def file_read(name):
    with open(name, encoding='utf8') as f:
        return f.read()

auth_log = file_read(r'ctf_auth.log')
vpn_log = file_read('ctf_vpn.log')
web_log = file_read('ctf_web.log')

# Aufgabe 1
print(len(auth_log.split('\n')))
print(len(vpn_log.split('\n')))
print(len(web_log.split('\n')))

# Aufgabe 2
# 2026-01-12T18:04:08+01:00 ad-01 sshd[83870]: Failed password for svc_monitor from 10.63.7.125 port 47320 ssh2
pattern = r'^.*?Failed password for ([a-zA-Z_.]*) from ([\d\.]*) port ([0-9]*) (.*)$'
treffer = re.findall(pattern, auth_log, flags=re.MULTILINE)

ip_list = {}

for user, ip, port, service in treffer:
    ip_list[ip] = ip_list.get(ip, 0) +1

print(*sorted(ip_list.items(), key=lambda x:x[1], reverse=True)[:3], sep='\n')

# Aufgabe 3
pattern = r'^.*?(Accepted password|Accepted publickey).*?from 198.51.100.23.*$'
treffer = re.finditer(pattern, auth_log, flags=re.MULTILINE)

for match in treffer:
    print(match.group())

# Aufgabe 4
pattern = r'^.*?sudo.*?$'
treffer = re.findall(pattern, auth_log, flags=re.MULTILINE)
print(treffer)

# Aufgabe 5 und 6
# 198.51.100.23 - - [12/Jan/2026:21:18:11 +0100] "POST /api/export HTTP/1.1" 200 1684827 "-" "python-requests/2.31.0" X-Note="FLAG{REG"
pattern = r'^.*?export.*?X-Note="(.*)"'
treffer = re.findall(pattern, web_log, flags=re.MULTILINE)
print(*treffer, sep='')

# Aufgabe 7
# 2026-01-12T20:00:09+01:00 vpn-01 vpn: user=l.neumann src=10.94.67.134 event=KEEPALIVE bytes_in=24148 bytes_out=1199 session=430707 msg="vpn-event"
pattern = r'2026-01-12T.*(user=.*) src=198.51.100.23 (event=TUNNEL_UP) (bytes_in=\d*) (bytes_out=\d*).*?$'
treffer = re.findall(pattern, vpn_log, flags=re.MULTILINE)
print(*treffer, sep='\n')

