#!/bin/bash

sudo ip route add 192.168.48.0/25 via 10.192.88.1

for Y in {71..90}; do
    if [ "$Y" -ne 88 ] && [ "$Y" -ne 89 ]; then
        sudo ip route add 10.192.$Y.0/30 via 10.192.88.1
    fi
done
