import unittest


class Testing(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("test".upper(), "TEST")

    def test_boolean(self):
        a = True
        b = True
        self.assertEqual(a, b)

    def test_is_upper(self):
        self.assertTrue("BET".isupper())
        self.assertFalse("Bet".isupper())


if __name__ == "__main__":
    unittest.main()
