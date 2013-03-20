import requests
import base64
import json


client_id = 'effd0a07a1436c4'
upload_url = 'https://api.imgur.com/3/image'


def getPath():
    print('Enter the file path of the image to be uploaded:')
    path = input()
    return path

def getImage(path):
    image = open(path, 'rb')
    return image

def encodeImage(image):
    encoded_image = base64.b64encode(image.read())
    return encoded_image

def postImage(encoded_image):
    payload = {'image': encoded_image}
    headers = {'Authorization': 'Client-ID {0}'.format(client_id)}
    print(headers)
    request = requests.post(upload_url, data=payload, headers=headers)
    data = json.loads(request.text)
    return data

def getURL(data):
    if data['success'] == True:
        return data['data']['link']
    else:
        return 'Upload failed.'

def printURL(url):
    print('Your image is located at: %s' % (url))


path = getPath()
image = getImage(path)
encoded_image = encodeImage(image)
data = postImage(encoded_image)
url = getURL(data)
printURL(url)
