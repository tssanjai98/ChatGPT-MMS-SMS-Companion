# ChatGPT MMS-SMS Companion

This project is a Flask application that integrates Twilio's messaging API with OpenAI's GPT-3 model and AWS Rekognition for image processing. It provides an endpoint to handle incoming messages from Twilio, processes them either as text input for OpenAI's GPT-3 or as images using AWS Rekognition for text detection, and sends a response back to the sender.

## Features

- Handle incoming SMS and MMS using Twilio Webhooks
- Process text messages using OpenAI's GPT-3 model
- Detect text in images using AWS Rekognition
- Send automated responses back to the user

## Prerequisites

- Python 3.x
- Flask
- Twilio account with a configured phone number
- OpenAI API access
- AWS account with access to Rekognition service
- Boto3 (AWS SDK for Python)

## Installation

To set up this project locally, follow these steps:

1. Clone the repository

2. Install the required dependencies

  ```pip install -r requirements.txt```

3. Start the Flask server

  ```python main.py```

## Usage
Once the Flask server is running, it will listen for incoming webhook events from Twilio. Send an SMS or MMS to the Twilio number configured for this application. The Flask app will process the message and send an appropriate response back.

## Endpoints
``` POST /webhook: ``` 
Webhook endpoint for Twilio to send messages to, which are then processed by the application.

## AWS Rekognition
The application uses AWS Rekognition to detect text in images. Ensure that your AWS account has permissions set for the Rekognition service.

## OpenAI
Text messages are processed using OpenAI's GPT-3 model to generate human-like text responses.

## Twilio
SMS and MMS messages are received and sent using Twilio's messaging API.

## Deployment
This project is deployed on AWS using EC2 and CloudFront
