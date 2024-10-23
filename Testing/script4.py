import unittest

import area


class Testing(unittest.TestCase):
    def test_triangle(self):
        self.assertEqual(area.triangle(10, 5), 25)

    def test_rectangle(self):
        self.assertEqual(area.rectangle(10, 5), 50)

    def test_square(self):
        self.assertEqual(area.square(7), 49)

    def test_error1(self):
        self.assertRaises(ValueError, area.square, 3)

    def test_error2(self):
        with self.assertRaises(ValueError):
            area.square(3)

    @unittest.skip("Skiping the test case")
    def test_error3(self):
        with self.assertRaises(ValueError):
            area.square(4)


if __name__ == "__main__":
    unittest.main()
