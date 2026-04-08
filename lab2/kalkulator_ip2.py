import math

# =========================
# PODSTAWOWE FUNKCJE IP
# =========================

def ip_to_int(ip):
    a, b, c, d = map(int, ip.split("."))
    return (a << 24) | (b << 16) | (c << 8) | d


def int_to_ip(n):
    return f"{(n >> 24) & 255}.{(n >> 16) & 255}.{(n >> 8) & 255}.{n & 255}"


def get_mask(prefix):
    return (0xffffffff << (32 - prefix)) & 0xffffffff


def network_address(ip_int, prefix):
    return ip_int & get_mask(prefix)


def broadcast_address(network, prefix):
    mask = get_mask(prefix)
    return network | (~mask & 0xffffffff)


def hosts_count(prefix):
    return (2 ** (32 - prefix)) - 2


# =========================
# WYLICZANIE PREFIXU
# =========================

def needed_prefix(hosts):
    n = 0
    while (2 ** n - 2) < hosts:
        n += 1
    return 32 - n


# =========================
# VLSM (PODZIAŁ SIECI)
# =========================

def vlsm(network_ip, prefix, departments):
    net_int = ip_to_int(network_ip)
    current_ip = network_address(net_int, prefix)

    # sortowanie od największej podsieci
    departments.sort(key=lambda x: x[1], reverse=True)

    result = []

    for name, required_hosts in departments:
        pref = needed_prefix(required_hosts)
        size = 2 ** (32 - pref)

        net = current_ip
        broadcast = net + size - 1

        first = net + 1
        last = broadcast - 1

        available_hosts = hosts_count(pref)

        result.append({
            "name": name,
            "network": int_to_ip(net),
            "prefix": pref,
            "first": int_to_ip(first),
            "last": int_to_ip(last),
            "broadcast": int_to_ip(broadcast),
            "hosts": available_hosts,
            "required": required_hosts,
            "extra": available_hosts - required_hosts
        })

        current_ip = broadcast + 1

    return result, current_ip


# =========================
# DANE WEJŚCIOWE (NOWA WERSJA)
# =========================

network = "10.10.200.0"
prefix = 23

# (nazwa, liczba urządzeń bazowa)
base_departments = [
    ("Produkcja", 80),
    ("Administracja", 40),
    ("Dział techniczny", 25),
    ("Sprzedaż", 15),
    ("Zarząd", 8)
]

# =========================
# OVER-PROVISIONING
# =========================

departments = []

for name, base in base_departments:
    required = int(base * 1.5) + 1
    departments.append((name, required))


# =========================
# OBLICZENIA
# =========================

subnets, next_free_ip = vlsm(network, prefix, departments)

start = ip_to_int(network)
end = broadcast_address(start, prefix)

unused = end - next_free_ip + 1


# =========================
# WYNIKI
# =========================

print("=== PODZIAŁ PODSIECI ===\n")

for s in subnets:
    print(f"[{s['name']}]")
    print(f"  Sieć: {s['network']}/{s['prefix']}")
    print(f"  Pierwszy host: {s['first']}")
    print(f"  Ostatni host: {s['last']}")
    print(f"  Broadcast: {s['broadcast']}")
    print(f"  Hosty dostępne: {s['hosts']}")
    print(f"  Wymagane: {s['required']}")
    print(f"  Nadmiar: {s['extra']}")
    print()

print("=== NIEWYKORZYSTANE ADRESY ===")
print("Liczba adresów:", unused)


# =========================
# DRZEWKO (LEKKO ULEPSZONE)
# =========================

print("\n=== DRZEWKO ===")
print(f"{network}/{prefix}")

for i, s in enumerate(subnets):
    prefix_symbol = "└──" if i == len(subnets) - 1 else "├──"
    print(f"{prefix_symbol} {s['network']}/{s['prefix']} ({s['name']})")