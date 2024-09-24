# ICMP Flood

This Python script is designed to execute an ICMP Flood attack, a type of Denial-of-Service (DoS) attack that inundates a specified target IP address with numerous ICMP packets. The script employs IP spoofing to mask the source IP address of the packets, making it more challenging to trace the attack back to its origin. It requires root privileges to run and can target any specified IP address, defaulting to the local gateway if no arguments are provided.

### install

```bash
git clone https://github.com/savasick/icmpflood.git
cd icmpflood
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

### usage

send to router-IP (Can disrupt LAN network and make it unavailable)
```bash
sudo python3 icmpflood.py
```

send to 192.168.5.110-IP
```bash
sudo python icmpflood.py 192.168.5.110
```

send to GitHub's IP (not recommended and illegal):
```bash
sudo python icmpflood.py 140.82.121.3
```