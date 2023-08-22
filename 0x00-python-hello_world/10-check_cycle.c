#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle
 * @list:  pointer to head node of singly linked list
 *
 * Return: 0 (if there is no cycle), 1 (if there is a cycle)
 */
int check_cycle(listint_t *list)
{
	listint_t *current_node, *test_node;

	if (list == NULL)
		return (0);
	current_node = list;
	while (current_node != NULL)
	{
		test_node = current_node;
		while (test_node != NULL)
		{
			if (current_node == test_node->next)
				return (1);
			test_node = test_node->next;
		}
		current_node = current_node->next;
	}
	return (0);
}
