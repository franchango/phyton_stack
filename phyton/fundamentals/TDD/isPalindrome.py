"""
SCENARIO: Input a palindrome word
"""

import unittest


c1= "OJO"   #declarar y asignar una variable de cadena
class Testing(unittest.TestCase):
#La definición de la función isPalindrome
    def isPalindrome(c):
        if c == c[::-1]:
            testValue = True
            print("Si! {} es palabra Palindrome {}".format(c,c))
        else:
            print("No! {} es palabra Palindrome {}".format(c,c))
    isPalindrome((c1))      #llamando a la función

if __name__ == '__main__':
    unittest.main()