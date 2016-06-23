# coding: utf-8
from sys import argv

romanTable = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
}

def convertToRoman(arabic):
    roman = ''

    while arabic >= romanTable['X']:
        roman += 'X'
        arabic = arabic - romanTable['X']

    while arabic >= romanTable['V']:
        roman += 'V'
        arabic = arabic - romanTable['V']


    roman += arabic * 'I'
    roman = roman.replace('VIIII','IX')
    roman = roman.replace('IIII','IV')
#    roman = roman.replace('IVI','V')
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
    13: 'XIII',
    14: 'XIV',
    15: 'XV',
    16: 'XVI',
    17: 'XVII',
    18: 'XVIII',
    19: 'XIX',
    20: 'XX',
    21: 'XXI',
    22: 'XXII',
    23: 'XXIII',
    24: 'XXIV',
    38: 'XXXVIII',
    39: 'XXXIX',
    40: 'XL',
    41: 'XLI'
    }

    for arabic, roman in testCases.iteritems():
        if convertToRoman(arabic) != roman:
            raise Exception('convertToRoman(%d) gave %s, expected %s' % (arabic, convertToRoman(arabic), roman))
    print('All tests passed.')

if argv[1] == '--test':
    testConvertToRoman()
else:
    print(convertToRoman(int(argv[2])))
