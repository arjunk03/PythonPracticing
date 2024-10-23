import unittest

from student import Student


class Testing(unittest.TestCase):
    def setUp(self):
        print("setup method")
        self.stud1 = Student("Arjun", "k", 10)

    def tearDown(self):
        print("teardown method")
        pass

    def test_student(self):
        self.assertEqual(self.stud1.mail, "Arjun_k@gmail.com")

    def test_stipend(self):
        stud1 = Student("Arjun", "k", 10)
        self.assertEqual(self.stud1.mail, "Arjun_k@gmail.com")


if __name__ == "__main__":
    unittest.main()
