import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):

    def test_joy(self):
        result = emotion_detector("I am glad this happened")
        self.assertIsNotNone(result)
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_anger(self):
        result = emotion_detector("I am really angry about this")
        self.assertIsNotNone(result)
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_disgust(self):
        result = emotion_detector("I feel disgusted by this")
        self.assertIsNotNone(result)
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_sadness(self):
        result = emotion_detector("I am feeling sad")
        self.assertIsNotNone(result)
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_fear(self):
        result = emotion_detector("I am afraid of this")
        self.assertIsNotNone(result)
        self.assertEqual(result["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main()
