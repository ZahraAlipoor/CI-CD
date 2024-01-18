import unittest

class TestGenderDetection(unittest.TestCase):
    def test_detect_gender(self):
        self.assertEqual(detect_gender("Alice"), "Female", "Expected female")
        self.assertEqual(detect_gender("Michael"), "Male", "Expected male")
        self.assertEqual(detect_gender("Sam"), "Unknown", "Expected unknown")

if __name__ == '__main__':
    unittest.main()
