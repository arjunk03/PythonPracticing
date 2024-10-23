import unittest


class TestMul(unittest.TestCase):
    def runTest(self):
        self.assertEqual((3 * 5), 15)


class TestAdd(unittest.TestCase):
    def runTest(self):
        self.assertEqual((3 + 5), 8)


class Simple(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, 1)

    def test_2(self):
        self.assertEqual(1, 2)

    @unittest.skip("skip testes")
    def test_3(self):
        self.assertEqual(1, 1)


if __name__ == "__main__":
    # suite = unittest.TestSuite()

    # suite.addTest(TestMul())

    #
    suite = unittest.makeSuite(Simple, "test")
    suite.addTests([TestMul(), TestAdd()])
    result = unittest.TextTestRunner(verbosity=3).run(suite)

    print("Errors :", result.errors)
    print("\n failures :", result.failures)
    print("skipped :", result.skipped)
    print("No of test :", result.testsRun)
    print("was it succcessful :", result.wasSuccessful())
