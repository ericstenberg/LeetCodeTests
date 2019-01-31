/*	Linked Lists
	Ex. {data, ptr}->{data,ptr}->{data,ptr}->NULL
	Data has to have an address, which is the ptr.

*/	

#include <stdio.h>
#include <stdlib.h>

typedef struct _ListNode { // define a struct _ListNode
	int data; // with int data
	// create pointer to next item in linked list. When creating a struct within a struct that is of the same type, always use the struct name and not the alias.
	struct _ListNode *next; 
} ListNode; // give it struct alias ListNode. This will be used to initialize other variables.

struct ListNode* removeElementsTest(struct ListNode* head, int val) {

	// Insert your code here.

	return 0;
   
}

ListNode *createNode() {
	// allocate memory for new node
	ListNode *newNode = (ListNode *) malloc(sizeof(ListNode));
	// set data to 0
	newNode->data = 0;
	// create pointer to next item in linked list
	newNode->next = NULL; 
	return newNode;
}

ListNode *createNextNode(ListNode *head, int val) { // create function to create notes in linked list
	ListNode *temp, *p; // initialize temp and p as ListNode
	// temp is getting next address each time	
	temp = createNode();
	temp->data = val; // set temp->data to given val. temp->next has no value...yet. temp->data has an address. This address is pointed to by temp->next
	if (!head) { // if the given head is NULL
		// if (!(head->data)) --> segmentation fault (reaching for memory that is not there.)
		// (!head) --> function passes this point once. (!head) works.
		head = temp; // set the head to the temp location and data
	} else {
		p = head; // set p equal to the head
		while (p->next) p = p->next; // iterate through linked list. If the pointer to the next item is not NULL. set p to the next item.
		p->next = temp; // when the while loop is finished iterating, set p->next to temp, which gives the address of temp, which carries the data and the pointer to NULL
	}

	return head;
}

void iterateNextNode(ListNode *head) { // create function to iterate through each node in the list and print it
	ListNode *p;
	if (!head) {
		printf("Linked list does not exist.");
	} else { 
		p = head;
 		while (p->next) {
			printf("%d\n",p->data);
			p = p->next;
		}
		printf("%d\n",p->data); // due to p->next pointing to NULL before 
	}
}

int main(int argc, char *argv[]) {

	int i = 0, j = 10;
	ListNode *head;

	for (i = 0; i < j; i++) {
		head = createNextNode(head, i);
	}

	iterateNextNode(head);

	free(head);
	
	return 0;
}

// https://en.wikipedia.org/wiki/Linked_list
