import requests


def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    response = requests.post(
        url,
        headers=headers,
        json={"raw_document": {"text": text_to_analyze}}
    )

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    if response.status_code == 200:
        data = response.json()
        emotions = data["emotionPredictions"][0]["emotion"]

        emotions["dominant_emotion"] = max(
            ["anger", "disgust", "fear", "joy", "sadness"],
            key=lambda emotion: emotions[emotion]
        )

        return emotions

    return None

