/*	Linked Lists
	Ex. {data, ptr}->{data,ptr}->{data,ptr}->NULL
	Data has to have an address, which is the ptr.

*/	

#include <stdio.h>
#include <stdlib.h>

typedef struct _ListItem { // define a struct _ListItem
	int data; // with int data
	struct ListItem *next; // create pointer to next item in linked list
} ListItem; // give it struct alias ListItem. This will be used to initialize other variables.

ListItem *createNode() {
	ListItem *newNode = (ListItem *) malloc(sizeof(ListItem));
	newNode->data = 0;
	newNode->next = NULL; // create pointer to next item in linked list
	return newNode;
}

ListItem *createNextNode(ListItem *head, int val) { // create function to create notes in linked list
	ListItem *temp, *p; // initialize temp and p as ListItem
	temp = createNode();
	temp->data = val; // set temp->data to given val
	if (!head) { // if the given head is NULL
		head = temp; // set the head to the temp location and data
	} else { // otherwise
		p = head; // set p equal to the head
		while (p->next != NULL) { // iterate through linked list. If the pointer to the next item is not NULL
			p = p->next; // set p to the next item
		}
		p = temp; // when the while loop is finished iterating, set p to temp, which sets p->data = val
	}

	return head;
}

struct ListNode* removeElementsTest(struct ListNode* head, int val) {
	return 0;    
}

int main(int argc, char *argv[]) {

	int i = 0, j = 10;
	ListItem *head;

	for (i = 0; i < j; i++) {
		head = createNextNode(head, i);
	}

	return 0;
}

// https://en.wikipedia.org/wiki/Linked_list
