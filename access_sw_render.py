import jinja2
import os
from itertools import izip
 
loader = jinja2.FileSystemLoader(os.getcwd())

jenv = jinja2.Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)

template = jenv.get_template('access_sw_template.j2')

hostname_input = raw_input (' enter access switch hostname:')
core_hostname_input = raw_input (' enter core switch hostname:')
stack_input = raw_input (' enter number of stack members 1-5:')
pid_input = raw_input (' enter product ID e.g c9300-48uxm or WS-C3850-12X48U or type the PID:')
region_input = raw_input (' choose a region: AU,Asia,EU,ME:')
location_input = raw_input (' enter site location e.g Melbourne:')
SCBN_input = raw_input (' enter site SCBN e.g 212:')
MID_input = raw_input (' enter site MID range 101-149:')
vlan_input = raw_input (' enter standard vlan Id,Name e.g 10,Management,101,Data-A:WiFi,102,Data-B,201,UC-A,150,DCS,172,WAP,11,WT,12,WPT:IPTV,182,VC:Australia,240,TelePresence: ')
tac_input = raw_input (' enter TACACS Key:')
vlan_data = vlan_input.split(',')
i = iter(vlan_data)
vlanDict = dict(izip(i, i))


 
print template.render(HOSTNAME=hostname_input ,CORE_SW_HOSTNAME=core_hostname_input ,STACK=stack_input ,PID=pid_input ,REGION=region_input ,LOCATION=location_input, SCBN=SCBN_input, MID=MID_input, vlanDict=vlanDict, TACACS_KEY=tac_input)

