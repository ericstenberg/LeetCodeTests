#!/usr/bin/env python3

class Solution:
    def imageSmootherTests(self,M):

        # Insert your code here.

def main():

    testSolution = Solution()    

    testCases = [
[[130,110,93],[60,70,161],[14,57,159]],
[[0]],
[[1]],
[[255]],
[[1,0],[0,1]],
[[47,20,11,88],[232,45,67,89],[123,234,78,90],[111,222,41,84],[32,17,77,65],[0,0,0,0],[255,255,255,255],[125,124,32,65],[45,33,177,181]],
[[255,111,100,45,32],[254,255,90,56,9],[255,222,1,2,3]],
[[10,23]],
[[101],[28]],
[[10,23,101,28]],
[[10],[23],[101],[28]],
]
    testAnswers = [
[[92,104,108],[73,94,108],[50,86,111]],
[[0]],
[[1]],
[[255]],
[[0,0],[0,0]],
[[86,70,53,63],[116,95,80,70],[161,128,105,74],[123,103,100,72],[63,55,56,44],[93,99,102,108],[126,116,109,101],[139,144,153,160],[81,89,102,113]],
[[218,177,109,55,35],[225,171,98,37,24],[246,179,104,26,17]],
[[16,16]],
[[64],[64]],
[[16,44,50,64]],
[[16],[44],[50],[64]]
]
    i = 0

    for each in testCases:
        if testSolution.imageSmootherTests(each) == testAnswers[i]:
            print('PASS. Input: ' + repr(each))
        else:
            print('FAIL. Input: ' + repr(each) + '\nExpected: ' + repr(testAnswers[i]) + '\nOutcome: ' + repr(testSolution.imageSmootherTests(each)) + '\ntype(imageSmootherTests): ' + repr(type(testSolution.imageSmootherTests(each))) + '\ntype(testAnswers[i]): ' + repr(type(testAnswers[i])))
        i += 1

if __name__ == '__main__':
    main()
