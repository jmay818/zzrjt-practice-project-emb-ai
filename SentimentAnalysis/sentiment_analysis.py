import requests
import json

def sentiment_analyzer(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    body = { "raw_document": { "text": text_to_analyse }}
    header = { "grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock" }
    response = requests.post(url, json=body, headers=header)
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        label = formatted_response["documentSentiment"]["label"]
        score = formatted_response["documentSentiment"]["score"]
        return { "label": label, "score": score }
    else:
        return { "label": None, "score": None }
