class ListNode: # Creates a ListNode object
    def __init__(self,x):
        self.val = x
        self.next = None

def addNode(head,value): # Adds ListNode to singly linked list
    temp = ListNode(value)
    if head == None:
        head = temp
    else:
        p = head
        while p.next != None:
            p = p.next
        p.next = temp
    return head

def readList(head): # Reads ListNodes from singly linked list
    output = []
    if head == []:
        return output
    p = head
    while p.next != None:
        output.append(p.val)
        p = p.next
    output.append(p.val)

    return output

class Soln:
    def mergeTwoListsTest(self, l1: ' ListNode', l2: ' ListNode') -> ' ListNode':

    # Insert your code here.

def main():
    testClass = Soln()

    testAnswersCases = [[[4,5,7,9,9],[1,3,5,6,9],[1,3,4,5,5,6,7,9,9,9]],
[[0,10,100,1000],[-1000,-100,-10],[-1000,-100,-10,0,10,100,1000]],
[[0],[0],[0,0]],
[[10,100],[-1000,-100,-10,0,1000],[-1000,-100,-10,0,10,100,1000]],
[[3,5,7],[],[3,5,7]],
[[],[3,5,7],[3,5,7]],
[[],[],[]]]

    for inputLists in testAnswersCases:
        listOne = None
        listTwo = None
        for elementOne in inputLists[0]:
            listOne = addNode(listOne,elementOne)
        for elementTwo in inputLists[1]:
            listTwo = addNode(listTwo,elementTwo)

        combinedLinkedList = testClass.mergeTwoListsTest(listOne,listTwo)
        combinedList = readList(combinedLinkedList)

        if combinedList == inputLists[2]:
            print(f'PASS | Inputs: {inputLists[0],inputLists[1]} | Result: {combinedList}')
        else:
            print(f'FAIL | Inputs: {inputLists[0],inputLists[1]} | Expected: {inputLists[2]} | Result: {combinedList}')

    return 0 

if __name__ == '__main__':
    main()
