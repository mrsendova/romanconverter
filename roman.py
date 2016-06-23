# coding: utf-8
from sys import argv

romanTable = {
    'I': 1,
    'V': 5,
    'X': 10,
}


def convertToRoman(arabic):
    roman = arabic * 'I'
    if arabic >= 5:
        roman = 'V' + (arabic - romanTable['V']) * 'I'

    roman = roman.replace('IIII','IV')
    return roman

def testConvertToRoman():
    testCases = {
    1: 'I',
    2: 'II',
    3: 'III',
    4: 'IV',
    5: 'V',
    6: 'VI',
    7: 'VII',
    8: 'VIII',
    9: 'IX',
    10: 'X',
    11: 'XI',
    12: 'XII',
    13: 'XII'
    }
    for arabic, roman in testCases.iteritems():
        if convertToRoman(arabic) != roman:
            raise Exception('convertToRoman(%d) gave %s, expected %s' % (arabic, convertToRoman(arabic), roman))
    print('All tests passed.')

if argv[1] == '--test':
    testConvertToRoman()
else:
    print(convertToRoman(int(argv[2])))
