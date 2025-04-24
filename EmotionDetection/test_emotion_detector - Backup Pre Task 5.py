from emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        #Sample Input text
        input = 'I am so happy I am doing this'
        print(input)
        
        # Test with a sample input
        result_1 = emotion_detector('input')
        
        # Print the result to see the detailed emotion scores
        print(result_1)

        # Check if the result is not None
        self.assertIsNotNone(result_1, "The result should not be None")
        
        # Check if the result contains the expected keys
        self.assertIn('dominant_emotion', result_1, "The result should contain 'dominant_emotion'")
        
        # Adjust the expected emotion based on the service's output
        expected_emotion = 'joy'  # Replace with the correct expected emotion
        self.assertEqual(result_1['dominant_emotion'], expected_emotion)
