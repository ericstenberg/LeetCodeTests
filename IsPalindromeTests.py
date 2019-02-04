class Soln:
    def isPalindromeTest(self,x):

	# Insert your code here.      

def main():
    testClass = Soln()

    testCases = [121,-121,0,1,10,11,202,3003,3020,sys.maxsize,-(sys.maxsize)-1,100,1000,10000,100000,1000000]

    testAnswers = [True,False,True,True,False,True,True,True,False,False,False,False,False,False,False,False]

    for case in testCases:
        result = testClass.isPalindromeTest(case)
        expectedResult = testAnswers[testCases.index(case)]
        if result == testAnswers[testCases.index(case)]:
            print('PASS. Input: ',case,'Result: ',result)
        else:
            print('FAIL. Input: ',case,'Expected: ',expectedResult,'Result: ',result)

    return 0

if __name__ == '__main__':
    main()


# Any number between 0 and 9 will be true
# All two-digit numbers except those n % 11 == 0 will be false
# Anything with a negative number will be false
# Anything that hits the upper limit or lower limit will be false
