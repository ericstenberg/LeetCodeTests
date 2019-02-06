import sys

class Soln:
    def reverseTest(self,x: 'int') -> 'int':

	# Insert your code here.       

def main():

    testClass = Soln()

    testCases = [1,0,10,100,1000,10000,100000,-10,-100,-1000,-10000,-100000,-2147483648,2147483647,121,-121,37482,-748,2223,sys.maxsize+1,-sys.maxsize-2,1797394023,-2147483412,2147483412,-1797394023,1563847412
]

    testAnswers = [1,0,1,1,1,1,1,-1,-1,-1,-1,-1,0,0,121,-121,28473,-847,3222,0,0,0,-2143847412,2143847412,0,0]

    for case in testCases:
        result = testClass.reverseTest(case)
        expected = testAnswers[testCases.index(case)]
        if result == expected:
            print(f'PASS | Case: {case} | Result: {result}')
        else:
            print(f'FAIL | Case: {case} | Expected: {expected} | Result: {result}')

    return 0

if __name__ == '__main__':
    main()
