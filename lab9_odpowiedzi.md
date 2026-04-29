# utworzenie interfejsu mostka
`sudo ip link add name br0 type bridge`

# dodanie fizycznych interfejsów do mostka
```
sudo ip link set eth0 master br0
sudo ip link set eth1 master br0
```


# podniesienie interfejsów
```
sudo ip link set dev br0 up
sudo ip link set dev eth0 up
sudo ip link set dev eth1 up

sudo systemctl stop NetworkManager
sudo ip addr flush dev eth0
sudo ip addr flush dev eth1

sudo dhcpcd br0
```

# zawartosc /etc/dnsmasq.conf
```
# interfejs
interface=br0
bind-interfaces

# upstream DNS (OpenDNS)
server=208.67.222.222
server=208.67.220.220

# cache
cache-size=1000

# logowanie
log-queries
log-facility=/tmp/dns.log

# statyczne rekordy
address=/k1.lan/192.168.48.71
address=/k2.lan/192.168.48.72
address=/k3.lan/192.168.48.73
address=/k4.lan/192.168.48.74
address=/k5.lan/192.168.48.75
address=/k6.lan/192.168.48.76
address=/k7.lan/192.168.48.77
address=/k8.lan/192.168.48.78
address=/k9.lan/192.168.48.79
address=/k10.lan/192.168.48.80
address=/k11.lan/192.168.48.81
address=/k12.lan/192.168.48.82
address=/k13.lan/192.168.48.83
address=/k14.lan/192.168.48.84
address=/k15.lan/192.168.48.85
address=/k16.lan/192.168.48.86
address=/k17.lan/192.168.48.87
address=/k18.lan/192.168.48.88
address=/k19.lan/192.168.48.89
address=/k20.lan/192.168.48.90

# blokada TikTok
address=/kosmatka.pl/0.0.0.0
address=/www.tiktok.com/0.0.0.0
address=/www.kosmatka.pl/0.0.0.0
address=/tiktok.com/0.0.0.0
