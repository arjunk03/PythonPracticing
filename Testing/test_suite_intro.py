import unittest


class TestString(unittest.TestCase):
    def runTest(self):
        self.assertEqual("a" * 4, "aaaa")


class TestUcase(unittest.TestCase):
    def runTest(self):
        self.assertEqual("gama".upper(), "GAMA")


if __name__ == "__main__":
    suite = unittest.TestSuite([TestString(), TestUcase()])
    unittest.TextTestRunner().run(suite)
