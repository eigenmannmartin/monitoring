# Monitoring

## mdadm

Install dependencies
```
apt-get install libsnmp-dev
```

Checkout git
```
git clone git@github.com:opennms-config-modules/snmp-swraid.git
cd snmp-swraid
ln -s /usr/include/net-snmp .
make
```

Copy mib library
```
cp -ar SWRAID-MIB.txt /usr/share/mibs/netsnmp/
cp -ar swRaidPlugin.so /usr/lib/
```

Edit /etc/snmp/snmpd.conf file and add:
```
dlmod swRaidMIB /usr/lib/swRaidPlugin.so
```

Restart SNMPD service
```
systemctl restart snmpd
```

Test snmp
```
snmpwalk -v2c -c public localhost .1.3.6.1.4.1.2021.13.18
```

## smart
Copy `smart-cron` and `smart.py` to `/opt/monitoring` and `snmp-smart`to `/etc/cron.hourly/`.
For prtg to work also copy `smart.sh` and `temp.sh` to `/var/prtg/scriptsxml`

