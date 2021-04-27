#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int check_cycle(listint_t *list)
/*void findloop(struct node *head)*/
{
	struct node *slow, *fast;
	slow = fast = list;

	while(slow && fast && fast->next)
	{
		slow = slow->next;
		fast  = fast->next->next;
		if (slow == fast)
		{
			printf("Linked list has a cycle\n");
			return;
		}
	}
	printf("Linked list has no cycle\n");
}

