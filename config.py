# -*- coding: utf-8 -*-

# api_key you got from @botfather for your bot
apikey = ""

# ACL for controll the repeater (your own ID should in here) (ID is NOT @username)
grant = [123456789]

# ID des Botowner / der Botowner (die bekommen Nachrichten über Statusänderungen)
owner = [123456789]

# Call of repeater
botcall = "BOTCALL"

# Liste mit zu prüfenden Prozessen
prozesse=["MMDVMHost","DMRGateway","YSFGateway","ircddbgatewayd"]

# ID des Repeaters
dmrid = "47110815"

# folder which contains mmdvm-logs
mmdvmlogs = "/var/log/mmdvm"
mmprefix = "MMDVM"

# folder wich contains the dmr-gw logfiles
gwlogs = "/var/log/mmdvm"
gwprefix = "DMRGateway"

# how to start mmdvm
mmdvmaufruf = "/usr/bin/screen /home/pi/MMDVMHost/MMDVMHost /home/pi/MMDVMHost/MMDVM-DB0SBN.ini"
# how to start dmrgw should it be active?
dmrgwaufruf = "/usr/bin/screen /home/pi/DMRGateway/DMRGateway /home/pi/DMRGateway/DMRGateway.ini"
dmrgwaktiv = 1
# how to start ysfgw
ysfgw = "sudo /etc/init.d/YSFGateway.sh start"
ysfgwaktiv = 1
# how to start ircdbbgw
ircdbbgw = "sudo /etc/init.d/ircddbgateway start"
ircdbbgwaktiv = 1

logfile = "botlog.txt"
userfile = "users.csv"

# define pathes to 1-wire sensor data
sensors = [
  ["/sys/bus/w1/devices/28-24d329126461/w1_slave","TX Temp"],
  ["/sys/bus/w1/devices/28-a78d29126461/w1_slave","NT Temp"]
]

# define gpio ports
gpioports = [
  # [gpio number,"name",invers]
  [11,"TX",0],
  [12,"RX",0],
  [13,"NS1",0],
]
