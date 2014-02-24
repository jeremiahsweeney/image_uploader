import requests
import base64
import json


# Imgur API
client_id = 'effd0a07a1436c4'
upload_url = 'https://api.imgur.com/3/image'


def get_path():
    path = input('Enter the file path of the image to be uploaded: ')
    return path

def get_image(path):
    f = open(path, 'rb')
    image = base64.b64encode(f.read())
    return image

def post_image(image):
    payload = {'image': image}
    headers = {'Authorization': 'Client-ID {0}'.format(client_id)}
    request = requests.post(upload_url, data=payload, headers=headers)
    data = json.loads(request.text)
    return data

def get_URL(data):
    if data['success'] == True:
        url = data['data']['link']
        print('Your image is located at:\n%s' % (url))
    else:
        print('Upload failed.')


path = get_path()
image = get_image(path)
data = post_image(image)
get_URL(data)


