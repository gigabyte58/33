import os, platform
try:
    import requests
except:
    os.system('pip install requests')
    os.system('pip install bs4')
    os.system('pip install futures')
 
import requests
bit = platform.architecture()[0]
if bit == '32bit':
    __import__('ub').check()
 
