#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int myAtoi(char* str) {

	// Insert your code here.

}

int main (int argc, char *argv[]) {
	
	char *testCases[] ={"1","+1","-1","241","-234","999999999999999999999","-9999999999999999999","++1","+-1","3.13464","-23.456","     42","     -42"," words and 987","4193 with words","673      ","-231    "," -78","  +90","+12      ","--487329","-234-","+23456-","   231  "," 6543   567","------","      ","++++++","-123","-2147483647","2147483648","2147483646","-2147483649","-10","10","+10","-100","100","+100","-11","11","+11","-101","101","+101","010","-010","+010"};

	int testAnswers[] = {1,1,-1,241,-234,INT_MAX,INT_MIN,0,0,3,-23,42,-42,0,4193,673,-231,-78,90,12,0,-234,23456,231,6543,0,0,0,-123,-2147483647,INT_MAX,2147483646,INT_MIN,-10,10,10,-100,100,100,-11,11,11,-101,101,101,10,-10,10};

	int i = 0,j = 48;

	for (i = 0; i < j; i++) {
		if (testAnswers[i] == myAtoi(testCases[i])) {
			printf("PASS. Input: '%s'.\n",testCases[i]);
		} else {
			printf("FAIL. Input: '%s'. Outcome: %d. Expected: %d\n",testCases[i],myAtoi(testCases[i]),testAnswers[i]);
		}
	}

	return 0;
}
