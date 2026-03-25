ip_value = "192.168.240.0/26"
ip_value = ip_value.split("/")
ip = ip_value[0].split(".")
a = int(ip[0])
b = int(ip[1])
c = int(ip[2])
d = int(ip[3])

prefix = int(ip_value[1])

ip_int = (a << 24) | (b << 16) | (c << 8) | d

mask_bin = "1"*prefix + "0"*(32-prefix)
mask = int(mask_bin, 2)

network = ip_int & mask
broadcast = network | (~mask & 0xffffffff)

first_host = network + 1
last_host = broadcast - 1

hosts = (2 ** (32-prefix)) - 2


def print_ip(n):
    print(
        (n >> 24) & 255,
        (n >> 16) & 255,
        (n >> 8) & 255,
        n & 255,
        sep="."
    )


def print_bin(n):
    print(".".join(f"{(n >> i) & 255:08b}" for i in [24,16,8,0]))


print("Adres sieci:")
print_ip(network)
print_bin(network)

print("\nMaska podsieci:")
print_ip(mask)
print_bin(mask)

print("\nLiczba hostów:", hosts)

print("\nPierwszy host:")
print_ip(first_host)
print_bin(first_host)

print("\nOstatni host:")
print_ip(last_host)
print_bin(last_host)

print("\nBroadcast:")
print_ip(broadcast)
print_bin(broadcast)
