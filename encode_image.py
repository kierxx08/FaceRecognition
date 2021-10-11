import sys
import cv2
import face_recognition
import requests
import json

image_url = ""
for url in sys.argv[1:]:
    image_url += url

load_image_url = face_recognition.load_image_file(image_url)
encodings = face_recognition.face_encodings(load_image_url)
myobj = {}

if len(encodings) > 0:
    load_image_url = cv2.cvtColor(load_image_url, cv2.COLOR_BGR2RGB)
    encode_image = face_recognition.face_encodings(load_image_url)[0]
    count = 0
    myobj['error'] = 'false'
    while count < 128:
        myobj[str(count)] = str(encode_image[count])
        count = count + 1
else:
    myobj['error'] = 'true'

# print(myobj)
json = json.dumps(myobj)
print(json)
