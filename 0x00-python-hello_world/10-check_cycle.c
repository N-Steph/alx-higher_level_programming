#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle
 * @list:  pointer to head node of singly linked list
 *
 * Return: 0 (if there is no cycle), 1 (if there is a cycle)
 */
int check_cycle(listint_t *list)
{
	listint_t *current_node;
	listint_t *address[SIZE];
	int i, j;

	for (i = 0; i < SIZE; i++)
		address[i] = NULL;
	if (list == NULL)
		return (0);
	current_node = list;
	j = 0;
	while (current_node != NULL)
	{
		for (i =0; i < j; i++)
		{
			if (address[i] == current_node)
				return (1);
		}
		address[j] = current_node;
		j++;
		current_node = current_node->next;
	}
	return (0);
}
