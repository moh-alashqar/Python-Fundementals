import unittest
# Units
def reverse_list(list):
    for i in range(int(len(list)/2)):
        list[i], list[len(list)-1-i] = list[len(list)-1-i], list[i]
    return list

def is_palindrome(string):
        return string == string[::-1]

def coins(num):
    list = [None, None, None, None]
    list[0], num = divmod(num, 25)
    list[1], num = divmod(num, 10)
    list[2], num = divmod(num, 5)
    list[3] = num
    return list

def get_factorial(num):
    factorial = 1
    for i in range(num, 0, -1):
        factorial *= i
    return factorial


def get_fabonacci(num):
    fabonacci = [0, 1]
    for i in range(2, num):
        fabonacci.append(fabonacci[i-1] + fabonacci[i-2])
    return fabonacci


# Units Tests
class units_tests(unittest.TestCase):
# Reverse List Tests
    def test1_reverse_list(self):
        self.assertEqual(reverse_list([1, 2, 3, 4]), [4, 3, 2, 1])
    
    def test2_reverse_list(self):
        self.assertEqual(reverse_list([10, 11, 15, 20]), [20, 15, 11, 10])

    def test3_reverse_list(self):
        self.assertEqual(reverse_list([12, 10000, 1510514, 516510651, 516056510, 5610444, 55]), [55, 5610444, 516056510, 516510651, 1510514, 10000, 12])

    def test4_reverse_list(self):
        self.assertEqual(reverse_list([-20, -50, -1]), [-1, -50, -20])

# Is Palindrome Tests
    def test1_is_palindrome(self):
        self.assertFalse(is_palindrome("car"))

    def test2_is_palindrome(self):
        self.assertTrue(is_palindrome("level"))

    def test3_is_palindrome(self):
        self.assertTrue(is_palindrome("radar"))

    def test4_is_palindrome(self):
        self.assertFalse(is_palindrome("Tomato"))

    def test5_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))

# Coins Tests
    def test1_coins(self):
        self.assertEqual(coins(87), [3, 1, 0, 2])

    def test2_coins(self):
        self.assertEqual(coins(95), [3, 2, 0, 0])

    def test3_coins(self):
        self.assertEqual(coins(215), [8, 1, 1, 0])

    def test4_coins(self):
        self.assertEqual(coins(56), [2, 0, 1, 1])

    def test5_coins(self):
        self.assertEqual(coins(140), [5, 1, 1, 0])

# Get Factorial Tests
    def test1_get_factorial(self):
        self.assertEqual(get_factorial(10), 3628800)

    def test2_get_factorial(self):
        self.assertEqual(get_factorial(5), 120)

    def test3_get_factorial(self):
        self.assertEqual(get_factorial(7), 5040)

# Get Fabonacci Tests
    def test1_get_fabonacci(self):
        self.assertEqual(get_fabonacci(15), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377])

    def test2_get_fabonacci(self):
        self.assertEqual(get_fabonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    def test3_get_fabonacci(self):
        self.assertEqual(get_fabonacci(5), [0, 1, 1, 2, 3])

    def setUp(self):
        print("Setup is running!")

    def tearDown(self):
        print("TearDown is running!")

if __name__ == '__main__':
    unittest.main()
    print(__name__)