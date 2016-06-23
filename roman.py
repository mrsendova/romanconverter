# coding: utf-8
from sys import argv

romanTable = [
    ('M', 1000),
    ('D', 500),
    ('C', 100),
    ('L', 50),
    ('X', 10),
    ('V', 5),
    ('I', 1)
];

def convertToRoman(arabic):
    roman = ''

    for pair in romanTable:
        numeral, value = pair
        while arabic >= value:
            roman += numeral
            arabic = arabic - value

    patterns = ['VIX', 'LXC', 'DCM']

    for pattern in patterns:
        roman = roman.replace(pattern[0] + pattern[1] * 4,pattern[1] + pattern[2])
        roman = roman.replace(pattern[1] * 4, pattern[1] + pattern[0])

    return roman
def convertToArabic(roman):
    return 1

def testConvertToRoman():
    arabic = 0
    with open('cases.txt') as f:
        for line in f:
            line = line.rstrip('\n')
            arabic += 1
            if convertToRoman(arabic) != line:
                raise Exception('convertToRoman(%d) gave %s, expected %s' % (arabic, convertToRoman(arabic), line))

        print('All tests passed.')

def testConvertToArabic():
    testCases = {
        'I': 1,
        'II': 2,
        'III': 3,
        'IX': 9
    }

    for case in testCases:
        if testCases[case] != convertToArabic(case):
            raise Exception('convertToArabic(%d) gave %s, expected %s' % (case, convertToArabic(case), testCases[case]))

if __name__ == '__main__':
    if argv[1] == '--test':
        testConvertToRoman()
        testConvertToArabic()
    else:
        print(convertToRoman(int(argv[2])))
