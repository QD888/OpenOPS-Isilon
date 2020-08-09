# OpenOPS - Isilon, Dell EMC Isilon Monitor
# Isilon: Isilon 3 Nodes
# OneFS Version: 8.1.2.0
# Programe: Python 3.8
# Stage: prototype
# Author: QD888
# Tested: 9th Aug. 2020
# Get REST api URI
# https://IP address:8080/platform

# Import libraries
import requests
from requests.auth import HTTPBasicAuth
import json
import urllib
from urllib.parse import urlencode
from urllib.parse import quote
import http.cookies

# Set up endpoint and authentication credentials
endpoint = 'https://IP address:8080'


# Prepare authentication, create a session
username = 'username'
password = 'password'
auth = HTTPBasicAuth(username, password)

api = '/session/1/session'
url = endpoint + api
headers = {
    'Accept': "application/json",
    'Content-Type': "application/json",
    'Accept-Language': 'en-US',
}
data = {
  'username' : username,
  'password' : password,
  'services' : ['platform', 'namespace']
}
response = requests.post(url, headers=headers, json=data, verify=False)
print(response.headers)

# Get Session cookies value, if you want use it.
sessCookies = response.headers['Set-Cookie']
parsed_cookie = http.cookies.BaseCookie()
parsed_cookie.load(rawdata = sessCookies)
sessCookies = parsed_cookie['isisessid'].coded_value

sessCookies = 'isisessid=' + sessCookies
print(sessCookies)

# Get response, example: Device information
api = '/platform/3/cluster/nodes'
url = endpoint + api
resDevice = requests.get(url, headers=headers, auth=auth, verify=False)
print(resDevice.text)


# Get response, Example: NIC status
api = '/platform/4/network/interfaces'
url = endpoint + api
resNIC = requests.get(url, headers=headers, auth=auth, verify=False)
print(resNIC.text)

# Get response, Example: NFS exports summary
api = '/platform/2/protocols/nfs/exports-summary'
url = endpoint + api
resNFSnum = requests.get(url, headers=headers, auth=auth, verify=False)
print(resNFSnum.text)

# Get response, Example: SMB shares summary
api = '/platform/1/protocols/smb/shares-summary'
url = endpoint + api
resSMBnum = requests.get(url, headers=headers, auth=auth, verify=False)
print(resSMBnum.text)


# Get response, example: quotas
api = '/platform/1/quota/quotas'
url = endpoint + api
resQuo = requests.get(url, headers=headers, auth=auth, verify=False)
print(resQuo.text)


# Get response, keys
# api = '/platform/1/statistics/keys'
# Get response, CPU status
# api = '/4/statistics/summary/workload'
# Get response, Capacity
# api = '/3/storagepool/storagepools'
# Get response, System summary
# api = '/platform/3/statistics/summary/system'
