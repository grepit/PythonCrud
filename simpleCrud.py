#!/usr/bin/env python3
import http.client
import json

print("\n GET example")
conn = http.client.HTTPSConnection("httpbin.org")
conn.request("GET", "/get")
response = conn.getresponse()
data = response.read().decode('utf-8')
print(response.status, response.reason)
print(data)


print("\n POST example")
conn = http.client.HTTPSConnection('httpbin.org')
headers = {'Content-type': 'application/json'}
post_body = {'text': 'testing post'}
json_data = json.dumps(post_body)
conn.request('POST', '/post', json_data, headers)
response = conn.getresponse()
print(response.read().decode())
print(response.status, response.reason)


print("\n PUT example ")
conn = http.client.HTTPSConnection('httpbin.org')
headers = {'Content-type': 'application/json'}
post_body ={'text': 'testing put'}
json_data = json.dumps(post_body)
conn.request('PUT', '/put', json_data, headers)
response = conn.getresponse()
print(response.read().decode(), response.reason)
print(response.status, response.reason)


print("\n delete example")
conn = http.client.HTTPSConnection('httpbin.org')
headers = {'Content-type': 'application/json'}
post_body ={'text': 'testing delete'}
json_data = json.dumps(post_body)
conn.request('DELETE', '/delete', json_data, headers)
response = conn.getresponse()
print(response.read().decode(), response.reason)
print(response.status, response.reason)
