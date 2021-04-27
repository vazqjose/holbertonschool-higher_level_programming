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
			return(1);
		}
	}
	return(0);
}

