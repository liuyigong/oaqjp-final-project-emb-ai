import requests
import json

def emotion_detector(text_to_analyze):
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    inputs= {"raw_document": {"text": text_to_analyze}}
    response=requests.post(url,headers=headers,json=inputs)
    if response.status_code==200:
        result=json.loads(response.text)['emotionPredictions'][0]['emotion']
        dominant=max(result,key=result.get)
        result['dominant_emotion']=dominant
    else:
        result={
                'anger': None,
                'disgust': None, 
                'fear': None, 
                'joy': None, 
                'sadness': None, 
                'dominant_emotion': None}
    return result
