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
    41: 'XLI',
    47: 'XLVII',
    49: 'XLIX',
    50: 'L',
    51: 'LI',
    52: 'LII',
    59: 'LIX',
    60: 'LX',
    61: 'LXI',
    80: 'LXXX',
    81: 'LXXXI',
    83: 'LXXXIII',
    89: 'LXXXIX',
    90: 'XC',
    91: 'XCI',
    92: 'XCII',
    95: 'XCV',
    97: 'XCVII',
    98: 'XCVIII',
    99: 'XCIX',
    100: 'C',
    101: 'CI',
    157: 'CLVII',
    179: 'CLXXIX',

    498: 'CDXCVIII'
    }

    for arabic, roman in testCases.iteritems():
        if convertToRoman(arabic) != roman:
            raise Exception('convertToRoman(%d) gave %s, expected %s' % (arabic, convertToRoman(arabic), roman))
    print('All tests passed.')

if argv[1] == '--test':
    testConvertToRoman()
else:
    print(convertToRoman(int(argv[2])))
