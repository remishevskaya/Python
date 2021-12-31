f = open('nginx_logs.txt', 'r')
data = []
for line in f:
    remote_addr = line.split()[0]
    request_type = line.split()[5].replace('"', '')
    requested_resource = line.split()[6]
    data.append((remote_addr, request_type, requested_resource))
f.close()

print(data)
