from flask import Flask, request, jsonify
import requests
from twilio.rest import Client as twilioClient
from twilio.twiml.messaging_response import MessagingResponse
import openai
import os
from requests.auth import HTTPBasicAuth
import boto3

app = Flask(__name__)

session = boto3.Session(aws_access_key_id="AKIAUMSOFBNDASSYLGHI", aws_secret_access_key="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", region_name="us-east-1")
account_id = 'AC19a50712bcf8f7a88c103640c6bb3c41'
auth_token = '4d345de218c6c6d39fdc5b332cb77cec'
client = twilioClient(account_id, auth_token)


openai.api_key = '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'

rek_client = session.client('rekognition')


def detect_labels_local_file(local_image_path):
    with open(local_image_path, 'rb') as image_file:
        image_bytes = image_file.read()

    response = rek_client.detect_text(
        Image={
            'Bytes': image_bytes
        }
    )

    text_detections = response['TextDetections']
    text_arr = []
    for text in text_detections:
        if text['DetectedText'] not in text_arr:
            text_arr.append(text['DetectedText'])

    return ' '.join(text_arr)


def get_media(media_url, user):
    response = requests.get(
        media_url,
        auth=HTTPBasicAuth(account_id, auth_token)
    )

    file_name = user[1:] + media_url.split('/')[-1] + '.jpg'

    if response.status_code == 200:
        with open(file_name, 'wb') as f:
            f.write(response.content)
        return 'Image saved.'
    else:
        return 'Failed to download image.'

@app.route('/webhook', methods=['POST'])
def webhook():
    sender_number = request.form.get('From','') 
    sender_message = request.form.get('Body','')
    num_media = int(request.values.get('NumMedia', 0))

    chatgpt_inp = ''

    if num_media == 0:
        chatgpt_inp = sender_message
    else:
        image_url = request.values.get('MediaUrl0')
        file_name = sender_number[1:] + image_url.split('/')[-1] + '.jpg'
        image_res = get_media(image_url,sender_number)
        output_res = detect_labels_local_file(file_name)
        chatgpt_inp = output_res
        os.remove(file_name)

    if chatgpt_inp != '':
        response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=chatgpt_inp,
        max_tokens=150
        ).choices[0].text.strip()

    client.messages.create(
        to=sender_number,
        from_='+18882924143',
        body=response
    )
    return request.data

if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0', port='3000')