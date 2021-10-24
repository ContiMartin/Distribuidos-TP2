import sys
from Cliente_P2 import ClienteNTP

import ntplib
from time import ctime

c = ntplib.NTPClient()
print(c)
response = c.request('ar.pool.ntp.org', version=1)
print(response)
response.offset
print(response)
print (response.offset)