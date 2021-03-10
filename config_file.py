# @Author: jamil
# @Date:   2021-03-10T14:17:04-06:00
# @Last modified by:   jamil
# @Last modified time: 2021-03-10T14:21:08-06:00



host_conf = ['en','config t','vlan create 238 name "lsii-firewall-inside" type port-mstprstp 0','vlan i-sid 238 800100','vlan create 239 name "lte-management" type port-mstprstp 0',
'vlan i-sid 239 800200','end','save config','show vlan i-sid','exit']
