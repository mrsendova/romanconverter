import unittest
import roman

class SimpleTest(unittest.TestCase):
    def testConvertToRoman(self):
        arabic = 0
        with open('cases.txt') as f:
            for line in f:
                line = line.rstrip('\n')
                arabic += 1
                self.assertTrue(roman.convertToRoman(arabic) == line)

    def testConvertToArabic(self):
        testCases = {
            'I': 1,
        }

        for case in testCases:
            self.assertTrue(roman.convertToArabic(case) == testCases[case])

if __name__ == '__main__':
    unittest.main()
