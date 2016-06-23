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

    roman = roman.replace('VIIII','IX')
    roman = roman.replace('IIII','IV')
    roman = roman.replace('LXXXX', 'XC')
    roman = roman.replace('XXXX', 'XL')
    roman = roman.replace('DCCCC', 'CM')
    roman = roman.replace('CCCC', 'CD')

    return roman

def testConvertToRoman():
    arabic = 0
    with open('cases.txt') as f:
        for line in f:
            line = line.rstrip('\n')
            arabic += 1
            if convertToRoman(arabic) != line:
                raise Exception('convertToRoman(%d) gave %s, expected %s' % (arabic, convertToRoman(arabic), line))

        print('All tests passed.')

if argv[1] == '--test':
    testConvertToRoman()
else:
    print(convertToRoman(int(argv[2])))
