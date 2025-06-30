from SentimentAnalysis.sentiment_analysis import sentiment_analyzer # Import the function from the package
import unittest # Import the unittest library

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        # Expected Positive
        result_1 = sentiment_analyzer('I love working with Python.')
        # Expected Negative
        result_2 = sentiment_analyzer('I hate working with Python')
        # Expected Neutral
        result_3 = sentiment_analyzer('I am neutral on Python.')
        # Test Positive
        self.assertEqual(result_1['label'], 'SENT_POSITIVE')
        # Test Negative
        self.assertEqual(result_2['label'], 'SENT_NEGATIVE')
        # Test Neutral
        self.assertEqual(result_3['label'], 'SENT_NEUTRAL')

unittest.main()