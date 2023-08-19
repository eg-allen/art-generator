import requests
import random

def getObject():
    objId = random.choice(allObjIds)
    myObject = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/objects/' + str(objId))
    objectBody = myObject.json()
    return objectBody

def getImageLink(object):
    imageLink = object['primaryImage']
    return imageLink

response_API = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/objects?departmentIds=11|19|21')
body = response_API.json()
allObjIds = body['objectIDs']

myObject = getObject()
myImageLink = getImageLink(myObject)

while myImageLink == '':
    myObject = getObject()
    myImageLink = getImageLink(myObject)


print("Title: " + myObject['title'])
print('Artist: ' + myObject['artistDisplayName'])
print('Year: ' + str(myObject['objectBeginDate']) + ' - ' + str(myObject['objectEndDate']))
print('Department: ' + myObject['department'])
print(myImageLink)

data = requests.get(myImageLink).content
f = open('art-img.jpg', 'wb')
f.write(data)
f.close
