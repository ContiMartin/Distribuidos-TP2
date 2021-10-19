import sys
from Cliente_P2 import Client

import ntplib
from time import ctime
c = ntplib.NTPClient()
print(c)
response = c.request('ar.pool.ntp.org', version=3)
print(response)
response.offset
print(response)