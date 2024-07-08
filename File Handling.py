
## read the complete data in the form of list


def read_log():
    with open("C:/Users/swarn/Downloads/access-log.txt") as a:
        records = []
        for line in a:
            clean_line = line.strip()
            if clean_line:
                words = clean_line.split()
                records.append(words)
        return records
print(read_log())



## access only ip address
def ip_address():
    data = read_log()
    _ip_address = []
    for item in data:
        _ip_address.append(item[0])
    return _ip_address
print(ip_address())


## access  unique ip address, means only once repeated

def uniqueip():
    data2 = ip_address()
    unique_ip_add = []
    for item in data2:
        if item not in unique_ip_add:
            unique_ip_add.append(item)
        else:
            continue
    return unique_ip_add
print(uniqueip())


## create the dict of in which ip address act as key and count act as value

def countip():
    data2 = ip_address()
    countofip = {}
    for item in data2:
        ip = item.strip()  # Remove newline characters
        if ip in countofip:
            countofip[ip]+=1
        else:
            countofip[ip] = 1
    return  countofip
print( countip())




