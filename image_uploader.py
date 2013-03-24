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
    f = open(path, 'rb')
    image = base64.b64encode(f.read())
    return image

def postImage(image):
    payload = {'image': image}
    headers = {'Authorization': 'Client-ID {0}'.format(client_id)}
    request = requests.post(upload_url, data=payload, headers=headers)
    data = json.loads(request.text)
    return data

def getURL(data):
    if data['success'] == True:
        url = data['data']['link']
        print('Your image is located at:\n%s' % (url))
    else:
        print('Upload failed.')

def main():
    path = getPath()
    image = getImage(path)
    data = postImage(image)
    getURL(data)


main()
