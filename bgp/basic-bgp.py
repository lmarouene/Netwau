from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import *
from jinja2 import Template
import yaml
import sys

Junos_hosts = [ ‘vMX-1’ , ’vMX-2’ ]
for host in junos_hosts:
       try:
             # Open and read the YAML file.
             myfile = host + ‘.yml’
             with open (myfile, ‘r’) as fh:
                       data = yaml.load(fh.read())
             # Open and read the Jinja2 template file.
             with open (‘Confi_file_bgp.j2’, ‘r’) as t_fh:
                        t_format = t_fh.read()

   # Associate the t_format template with the Jinja2 module
       template = Template(t_format)
       # Merge the data with the template 
       myConfig = template.render(data)

       dev = Device(host=host, user=‘lab’, password=‘lab123’)
       dev.open()
       config = Config(dev)
       config.lock()
       config.load(myConfig, merge=True, format=“text”)
       config.pdiff()
       config.commit()
       dev.close()
except LockError as e:
        print “The config database was locked!”
except ConnectionTimeoutError as e:
        print “Connection timed out!”
       config.unlock()
                        
