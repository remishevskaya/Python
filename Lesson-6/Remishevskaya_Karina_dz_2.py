f = open('nginx_logs.txt', 'r')
data = []
adresses = []
spamers = dict()
for line in f:
    remote_addr = line.split()[0]
    request_type = line.split()[5].replace('"', '')
    requested_resource = line.split()[6]
    data.append((remote_addr, request_type, requested_resource))
    adresses.append(remote_addr)
    spamers.setdefault(remote_addr, 0)
    spamers[remote_addr] += 1
f.close()

spamers = sorted(spamers.items(), key=lambda x: x[1], reverse=True)

print(spamers[0])
