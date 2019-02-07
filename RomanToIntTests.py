class Soln:
    def romanToIntTest(self, s: 'str') -> 'int':

    # Insert your code here

def main():
    testClass = Soln()

    testCasesAnswers = {'I':1, 'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,
'MMMCMXCIX':3999,'CDLXXXV':485,'DCCLXXVII':777,'MMCMXCIV':2994,'MMI':2001,
'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900,'CCC':300,'IIII':None,
'VV':None,'XXXX':None,'LL':None,'CCCC':None,'DD':None}

    for case in testCasesAnswers:
        result = testClass.romanToIntTest(case)
        expected = testCasesAnswers[case]
        if result == expected:
            print(f'PASS | Input: {case} | Result: {result}')
        else:
            print(f'FAIL | Input: {case} | Expected: {expected} | Result: {result}')

    return 0

if __name__ == '__main__':
    main()
