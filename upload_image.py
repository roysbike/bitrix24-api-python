#!/usr/bin/python3

import base64
import requests
import pyqrcode
import io

c = pyqrcode.create("3658")
s = io.BytesIO()
c.png(s,scale=5)
image_64_encode = base64.b64encode(s.getvalue()).decode("ascii")

url = "https://bitrix.com/rest/8/token/"

big_code = pyqrcode.create('3658', error='H', version=1, mode='binary')
big_code.png('3658.png', scale=10, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xff])

data = {
   "id":"3658",
    'fields':{'UF_CRM_1604413825641':{'fileData':['3658.png', image_64_encode ]}}
}
response = requests.post(url+"crm.deal.update",json=data)
result=response.json()
print(result)
