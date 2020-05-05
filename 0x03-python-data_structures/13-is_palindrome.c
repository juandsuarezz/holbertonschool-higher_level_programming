#include "lists.h"
/**
 * palindrome_recursion - Iterates a list recursively
 * @head: head of the list
 * @tail: iterates to the end of the list
 * Return: 1 if a palindrome, 0 if not a palindrome
 */

int palindrome_recursion(listint_t **head, listint_t *tail)
{
	if (tail == NULL)
		return (1);

	if (palindrome_recursion(head, tail->next) == 1 && (*head)->n == tail->n)
	{
		(*head) = (*head)->next;
		return (1);
	}

	else
		return (0);
}


/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: head of the list
 * Return: 1 if a palindrome, 0 if not a palindrome
 */

int is_palindrome(listint_t **head)
{
	if (*head == NULL)
		return (1);

	if ((*head)->next == NULL)
		return (1);

	return (palindrome_recursion(head, *head));
}
