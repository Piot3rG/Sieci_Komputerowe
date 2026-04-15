# 📡 Podstawowe polecenia sieciowe – Ubuntu 24.04 (VirtualBox)

## 1. Lista interfejsów sieciowych

**Źródło:**
```bash
ip -br link
```

**Odpowiedź:**
```text
lo       UNKNOWN        00:00:00:00:00:00
enp0s3   UP             08:00:27:66:77:19
```

---

## 2. Adres MAC routera (bramy)

**Źródło:**
```bash
ip route
ip neigh
```

**Odpowiedź:**
```text
default via 10.0.2.2 dev enp0s3
10.0.2.2 dev enp0s3 lladdr 52:55:0a:00:02:02 REACHABLE
```

---

## 3. Zmiana adresu MAC

**Źródło:**
```bash
sudo ip link set dev enp0s3 down
sudo ip link set dev enp0s3 address 02:11:22:33:44:55
sudo ip link set dev enp0s3 up
```

**Odpowiedź:**
```text
Adres MAC interfejsu enp0s3 został zmieniony (polecenie nie zwraca wyniku w konsoli).
```

---

## 4. Ping całej podsieci

**Źródło:**
```bash
nmap -sn 10.0.2.0/24
```

**Odpowiedź:**
```text
Nmap scan report for piotrek-vb (10.0.2.16)
Host is up (0.00042s latency).

Nmap done: 256 IP addresses (1 host up)
```

---

## 5. Skan podsieci – port 22

**Źródło:**
```bash
nmap -p 22 10.0.2.0/24
```

**Odpowiedź:**
```text
PORT   STATE  SERVICE
22/tcp closed ssh
```

---

## 6. Skan portów na localhost (lo)

**Źródło:**
```bash
nmap -p- 127.0.0.1
```

**Odpowiedź:**
```text
PORT      STATE SERVICE
631/tcp   open  ipp
5432/tcp  open  postgresql
27017/tcp open  mongod
```

---

## 7. Otwarte porty + PID + program

**Źródło:**
```bash
ss -tulpn
```

**Odpowiedź:**
```text
tcp LISTEN 127.0.0.1:631
tcp LISTEN 127.0.0.1:27017
tcp LISTEN 127.0.0.1:5432
```

---

## 8. Trasa domyślna

**Źródło:**
```bash
ip route
```

**Odpowiedź:**
```text
default via 10.0.2.2 dev enp0s3
```

---

## 9. Trasa do kosmatka.pl

**Źródło:**
```bash
traceroute kosmatka.pl
```

**Odpowiedź:**
```text
1  10.0.2.2 (_gateway)
2–30 brak odpowiedzi (* * *)
```

---

## 10. Serwer DNS w systemie

**Źródło:**
```bash
cat /etc/resolv.conf
```

**Odpowiedź:**
```text
nameserver 127.0.0.53
```

---

## 11. Statyczne wpisy DNS

**Źródło:**
```bash
cat /etc/hosts
```

**Odpowiedź:**
```text
127.0.0.1 localhost
127.0.1.1 piotrek-vb
::1 ip6-localhost ip6-loopback
```

---

## 12. Rekord MX kosmatka.pl (DNS 8.8.8.8)

**Źródło:**
```bash
dig @8.8.8.8 kosmatka.pl MX
```

**Odpowiedź:**
```text
kosmatka.pl. IN MX 10 mx2.privateemail.com.
kosmatka.pl. IN MX 10 mx1.privateemail.com.
```

---

## 13. IPv6 google.pl

**Źródło:**
```bash
dig google.pl AAAA
```

**Odpowiedź:**
```text
google.pl. IN AAAA 2a00:1450:4025:807::5e
```

---

## 14. Rejestracja domeny kosmatka.pl

**Źródło:**
```bash
whois kosmatka.pl
```

**Odpowiedź:**
```text
created:        2022.12.02
renewal date:   2032.12.02
```

---

## 15. Lista usuniętych domen .pl

**Źródło:**
https://www.dropped.pl/dzisiejsze/

**Odpowiedź:**
```text
Strona zawiera listę domen .pl usuniętych w dniu dzisiejszym.
```
