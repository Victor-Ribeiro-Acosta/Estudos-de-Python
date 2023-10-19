
import urllib
from urllib import request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except:
    print("\033[31:40mO site Pudim não encotra-se disponivel no momento\033[m")
else:
    print('\033[34:40mO site está disponível\033[m')