# Import libraries
import requests, json

def emotion_detector(text_to_analyze):
    # URL for the Emotion Detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Define headers for the request
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Define input JSON for the request
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Make the POST request to the Emotion Detection service
    response = requests.post(url, headers=headers, json=input_json)

    # Print the response content for debugging
    print(response.content)

    # Check if the response is valid
    if response.status_code == 200:
        response_data = response.json()
        if 'emotionPredictions' in response_data:
            # Extract the emotion data
            emotion_data = response_data['emotionPredictions'][0]['emotion']
            # Determine the dominant emotion
            dominant_emotion = max(emotion_data, key=emotion_data.get)
            return {
                'anger': emotion_data['anger'],
                'disgust': emotion_data['disgust'],
                'fear': emotion_data['fear'],
                'joy': emotion_data['joy'],
                'sadness': emotion_data['sadness'],
                'dominant_emotion': dominant_emotion
            }
        else:
            print("Error: 'emotionPredictions' attribute not found in response")
            return None
    else:
        print(f"Error: Received response with status code {response.status_code}")
        return None