#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - checks if linked list has loop
 * @list: list to check
 * Return: 1 if theres a loop
 */
int check_cycle(listint_t *list)
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

