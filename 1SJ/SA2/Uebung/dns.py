with open("dnsqueries.txt", "r") as f:
    lines = f.readlines()

dstfile = open("anfragen.txt", "ab")
# print(dns)
# queries=dns.split("\n")
# print(dns)
data = 0
for line in lines:
    anfrage = line.split(".")[0]
    # print(anfrage)
    test = int(anfrage).to_bytes(1, 'big')
    print(test)
    # data=data.join(test)
    # dstfile.write(test)
dstfile.close()

ex
