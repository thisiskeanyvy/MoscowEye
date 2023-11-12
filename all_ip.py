import maxminddb

def get_ip_info():
    with maxminddb.open_database('GeoOpen-Country-ASN.mmdb') as reader:
        for i in range(256):
            for j in range(256):
                for k in range(256):
                    for l in range(256):
                        if i == 0:
                            i+=1
                        ip = f"{i}.{j}.{k}.{l}"
                        print(ip)
                        print(reader.get(ip))

if __name__ == "__main__":
    get_ip_info()