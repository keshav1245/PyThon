import unittest
import capitalize

class TestCap(unittest.TestCase):
	def test_one_word(self):
		text = "python"
		result = capitalize.capText(text)
		self.assertEqual(result,"Python")

	def test_multi_words(self):
		text = "python is great"
		result = capitalize.capText(text)
		self.assertEqual(result,"Python Is Great")


if __name__ == "__main__":
	unittest.main()