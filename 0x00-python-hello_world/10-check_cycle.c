#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - Checks if a singly linked list has a cycle
 * @list: List to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *head = list;
	listint_t *tail = list;

	while (tail != NULL && tail->next != NULL)
	{
		head = head->next;
		tail = tail->next->next;

		if (head == tail)
			return (1);
	}
	return (0);
}
