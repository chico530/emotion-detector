import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    # URL of the sentiment analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header)

    # Convert the response text into a dictionary
    formatted_response = json.loads(response.text)

    # Extract the required set of emotions
    if response.status_code == 200:
        emotion = formatted_response["emotionPredictions"][0]["emotion"]
        
        anger_score = emotion["anger"]
        disgust_score = emotion["disgust"]
        fear_score = emotion["fear"]
        joy_score = emotion["joy"]
        sadness_score = emotion["sadness"]

        dominant_emotion = max(emotion, key=emotion.get)

    elif response.status_code == 500:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None

    # Return the response text from the API
    return {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_emotion
    }