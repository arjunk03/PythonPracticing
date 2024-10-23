import unittest

from student import Student


class Testing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\n setup class method")

    @classmethod
    def tearDownClass(cls):
        print("teardown class")

    def setUp(self):
        print("\nsetup method")
        self.stud1 = Student("Arjun", "k", 10)

    def tearDown(self):
        print("teardown method")
        pass

    def test_student(self):
        print("test_student")
        self.assertEqual(self.stud1.mail, "Arjun_k@gmail.com")

    def test_stipend(self):
        print("test_stipend")
        self.assertEqual(self.stud1.mail, "Arjun_k@gmail.com")


if __name__ == "__main__":
    unittest.main()
