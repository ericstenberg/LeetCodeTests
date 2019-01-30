/*	Linked Lists
	Ex. {data, ptr}->{data,ptr}->{data,ptr}->NULL
	Data has to have an address, which is the ptr.

*/	

#include <stdio.h>
#include <stdlib.h>

typedef struct _ListNode { // define a struct _ListNode
	int data; // with int data
	struct _ListNode *next; // create pointer to next item in linked list. When creating a struct within a struct that is of the same type, always use the struct name and not the alias.
} ListNode; // give it struct alias ListNode. This will be used to initialize other variables.

struct ListNode* removeElementsTest(struct ListNode* head, int val) {

	// Insert your code here.

	return 0;
   
}

ListNode *createNode() {
	ListNode *newNode = (ListNode *) malloc(sizeof(ListNode));
	newNode->data = 0;
	newNode->next = NULL; // create pointer to next item in linked list
	return newNode;
}

ListNode *createNextNode(ListNode *head, int val) { // create function to create notes in linked list
	ListNode *temp, *p; // initialize temp and p as ListNode
	temp = createNode();
	temp->data = val; // set temp->data to given val. temp->next has no value...yet. temp->data has an address. This address is pointed to by temp->next
	//printf("%p\n",&(temp->data));
	if (!head) { // if the given head is NULL
		head = temp; // set the head to the temp location and data
	} else { // otherwise
		p = head; // set p equal to the head
		while (p->next != NULL) { // iterate through linked list. If the pointer to the next item is not NULL
			p = p->next; // set p to the next item.  Getting assignment from incompatible pointer type warning.
		}
		p = temp; // when the while loop is finished iterating, set p to temp, which sets p->data = val
	}

	return head;
}

void iterateNextNode(ListNode *head) {
	ListNode *p;
	if (!head) {
		printf("Linked list does not exist.");
	} else { 
		p = head;
		while (p->next != NULL) {
			printf("%d\n",p->data);
			p = p->next;
		}
	}
}

int main(int argc, char *argv[]) {

	int i = 0, j = 10;
	ListNode *head;

	head = createNode();

	for (i = 0; i < j; i++) {
		head = createNextNode(head, i);
	}

	iterateNextNode(head);
	
	return 0;
}

// https://en.wikipedia.org/wiki/Linked_list
