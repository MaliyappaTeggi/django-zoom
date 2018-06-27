# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render
import jwt
import requests
from pprint import pprint
import json

def create_meeting(request):
   key = 'VMxrz4XZDWHHTnHVVBqLCF9Kl5tteRABZBtN'
   encoded = jwt.encode({"iss": "4NNh0JdORM6yV5aPSv14Aw",
    "exp": 1496091964000}, key, algorithm='HS256')
   print(encoded)
   # url="https://api.zoom.us/v2/users?access_token={}".format(encoded)
   url="https://api.zoom.us/v2/users/manjunath@searchtek.in/meetings?access_token={}".format(encoded)
   # url="http://httpbin.org/post, data={'key': 'value'}"
   print(url)
   data={
    "topic":"mymeeting",
    "type":2,
    "start_time":"2018-06-27T11:50:00",
    "duration":60,
    "timezone":"Asia/Calcutta",
    "settings":{
     "participant_video":True,
     "use_pmi":True
    }
   }
   response = requests.post(url, json=data)
   # response = requests.get(url)
   print(response)
   data2 = response.json()
   pprint(data2)
   return HttpResponse("zoom api")
def add_registrant(request):
    key = 'VMxrz4XZDWHHTnHVVBqLCF9Kl5tteRABZBtN'
    token= jwt.encode({"iss": "4NNh0JdORM6yV5aPSv14Aw",
                          "exp": 1496091964000}, key, algorithm='HS256')
    print(token)
    url="https://api.zoom.us/v2/webhooks/options?access_token={}".format(token)

    response=requests.patch(url, json={'version':'v2'})
    print(response)
    data = response.json()
    pprint(data)
    return HttpResponse("add registrant successusfull")

