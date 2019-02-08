class Soln:
    def intToRomanTest(self,num: 'int') -> 'str':

	# Insert your code here.

def main():

    testClass = Soln()

    testCasesAnswers = {'1': 'I', '5': 'V', '10': 'X', '50': 'L', '100': 'C', '500': 'D', '1000': 'M', '3999': 'MMMCMXCIX', '485': 'CDLXXXV', '777': 'DCCLXXVII', '2994': 'MMCMXCIV', '2001': 'MMI', '4': 'IV', '9': 'IX', '40': 'XL', '90': 'XC', '400': 'CD', '900': 'CM', '300': 'CCC','3000':'MMM'}

    for case in testCasesAnswers:
        result = testClass.intToRomanTest(int(case))
        expected = testCasesAnswers[case]

        if result == expected:
            print(f'PASS | Input: {case} | Result: {result}')
        else:
            print(f'FAIL | Input: {case} | Expected: {expected} | Result: {result}')

    return 0

if __name__ == '__main__':
    main()
