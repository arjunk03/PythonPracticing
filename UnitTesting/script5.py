import unittest

from student import Student


class Testing(unittest.TestCase):
    def test_student(self):
        stud1 = Student("Arjun", "k", 10)
        self.assertEqual(stud1.mail, "Arjun_k@gmail.com")

    def test_stipend(self):
        stud1 = Student("Arjun", "k", 10)
        self.assertEqual(stud1.mail, "Arjun_k@gmail.com")


if __name__ == "__main__":
    unittest.main()
