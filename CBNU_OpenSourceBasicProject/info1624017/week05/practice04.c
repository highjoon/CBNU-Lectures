#include <stdio.h>
#include <stdlib.h>

typedef int element;
typedef struct ListNode {
	element data;
	struct ListNode *link;
}ListNode;

void error(char *message)
{
	fprintf(stderr, "%s\n", message);
	exit(1);
}

void insert_node(ListNode **phead, ListNode *p, ListNode *new_node)
{
	if (*phead == NULL) {
		new_node->link = NULL;
		*phead = new_node;
	}
	else if (p == NULL) {
		new_node->link = *phead;
		*phead = new_node;
	}
	else {
		new_node->link = p->link;
		p->link = new_node;
	}
}

void display(ListNode *head)
{
	ListNode *p = head;
	while (p != NULL) {
		printf("%d->", p->data);
		p = p->link;
	}
	printf("\n");
}

ListNode * insertion_sort(ListNode *phead)
{
	ListNode *p, *temp;
	p = phead;

	while (p->link != NULL) {
		if (p->data > p->link->data)
		{
			temp = p->link;
			p->link = p->link->link;
			temp->link = phead;
			phead = p = temp;
			display(phead);
			printf("\n");
			continue;
		}
		p = p->link;
	}
	return phead;
}

ListNode *create_node(element data, ListNode *link)
{
	ListNode *new_node;
	new_node = (ListNode *)malloc(sizeof(ListNode));
	if (new_node == NULL) error("메모리 할당 에러");
	new_node->data = data;
	new_node->link = link;
	return (new_node);
}

int main(void)
{
	ListNode *list1 = NULL;
	int i;
	for (i = 0; i < 8; i++)
		insert_node(&list1, NULL, create_node(rand() % 15, NULL));
	list1 = insertion_sort(list1);
	printf("------최종 정렬------\n");
	display(list1);

	return 0;
}
