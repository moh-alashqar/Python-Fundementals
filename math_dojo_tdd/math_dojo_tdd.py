import unittest
class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num
        for i in range(len(nums)):
            self.result += nums[i]
        return self.result

    def subtract(self, num, *nums):
        self.result -= num
        for i in range(len(nums)):
            self.result -= nums[i]
        return self.result

class MathDojoTest(unittest.TestCase):
    def setUp(self):
        print("Setting Up!")
        self.md = MathDojo()

    def tearDown(self):
        print("Tearing Down!")

    def test1_math_dojo(self):
        self.assertEqual(self.md.add(1, 2, 5, 5, 5, 5), 23)
        self.assertEqual(self.md.add(1, 2, 5), 31)
        self.assertEqual(self.md.subtract(5, 10), 16)
        self.assertEqual(self.md.add(100), 116)
        self.assertEqual(self.md.subtract(31, 5, 2), 78)

if __name__ == "__main__":
    unittest.main()