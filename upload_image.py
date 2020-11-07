#!/usr/bin/python3

import base64
import requests
import pyqrcode
url = "https://url/rest/8/token/"

#try:
     #Direct link image
big_code = pyqrcode.create('3658', error='H', version=1, mode='binary')
big_code.png('3658.png', scale=10, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xff])

#file_url = "https://url/3658.png"
#image_64_encode = str(base64.b64encode(requests.get(file_url).content))[2:-1]
image_64_encode = base64.b64encode(open("3658.png", "rb").read()).decode('utf-8')

data = {
    "id":"3658",
    'fields':{'UF_CRM_1604413825641':{'fileData':['3658.png', image_64_encode ]}}
}
response = requests.post(url+"crm.deal.update",json=data)
result=response.json()
print(result)
