#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle
 * @list:  pointer to head node of singly linked list
 *
 * Return: 0 (if there is no cycle), 1 (if there is a cycle)
 */
int check_cycle(listint_t *list)
{
	listint_t *node;

	if (list == NULL)
		return (0);
	node = list;
	while (node != NULL)
	{
		node = node->next;
		if (node == list)
			return (1);
	}
	return (0);
}
