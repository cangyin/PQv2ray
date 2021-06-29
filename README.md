# A complex config generator for Qv2ray, in Python.

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/cangyin/PQv2ray/pack%20python%20script?logo=GitHub&style=flat-square)
![GitHub all releases](https://img.shields.io/github/downloads/cangyin/PQv2ray/total?style=flat-square)

## Development Purpose of the Tool

Help users get started with Qv2ray's complex configuration more easily.

## Examples

### Balancers
- most basic balancer
![most basic balancer](demos/screenshots/most%20basic%20balancer.png)

- most basic balancer with 2 inbound ports (HTTP + SOCKS5)
![most basic balancer with 2 inbounds](demos/screenshots/most%20basic%20balancer%20(2%20inbounds).png)

- basic balancer with bypass rules
![basic balancer with bypass rules](demos/screenshots/basic%20balancer%20(with%20bypass%20rules).png)

- balancer with complete Qv2ray route settings
![balancer with complete Qv2ray route settings](demos/screenshots/balancer%20(with%20complete%20Qv2ray%20route%20settings).png)


### Multi-Ports
- most basic multi-port
![most basic multi-port](demos/screenshots/most%20basic%20multi-port.png)

- multiple balancers with complete Qv2ray route settings
![multiple balancers with complete Qv2ray route settings](demos/screenshots/multiple%20balancer%20with%20complete%20Qv2ray%20route%20settings.png)

- 56 SOCKS5 inbounds and 56 outbounds
![56 SOCKS5 inbounds and 56 outbounds](demos/screenshots/56%20SOCKS5%20inbounds%20and%2056%20outbounds.png)


## Installation
```cmd
pip install -r requirements.txt
```

## Pre-built Binaries
just download from releases (Windows only).

## Platform
PQv2ray is only tested on Windows, currently. But it should work on Linux easily with no major bugs.
