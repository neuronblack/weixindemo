import requests
import json
def chatting(msg,userid):
    data = {
        'key': '1c108d2c5b4d445a9533d64f93e08786',
        'info': msg,
        'userid': userid
    }
    jsondoc = requests.post('http://www.tuling123.com/openapi/api', data).text
    jsondata=json.loads(jsondoc)
    return jsondata['text']
