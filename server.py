
"""Flask server for the Emotion Detection application."""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Render the main emotion detection page."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """Analyze text and return emotion scores and the dominant emotion."""
    text_to_analyze = request.args.get("textToAnalyze", "")

    if not text_to_analyze.strip():
        return "Please enter some text before submitting.", 400

    result = emotion_detector(text_to_analyze)

    if result is None:
        return "Emotion detection service is unavailable.", 502

    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
