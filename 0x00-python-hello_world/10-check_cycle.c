#include "lists.h"
/**
 * listint_t_len - counts the number of node in a listint_t list
 * @list: pointer to head node of listint_t list
 *
 * Return: number of node
 */
size_t listint_t_len(listint_t *list)
{
	size_t num_node;
	listint_t *curr_node;

	if (list == NULL)
		return (0);
	curr_node = list;
	num_node = 0;
	while (curr_node != NULL)
	{
		++num_node;
		curr_node = curr_node->next;
	}
	return (num_node);
}

/**
 * check_cycle - Checks if a singly linked list has a cycle
 * @list:  pointer to head node of singly linked list
 *
 * Return: 0 (if there is no cycle), 1 (if there is a cycle)
 */
int check_cycle(listint_t *list)
{
	size_t num; /* number of nodes */
	size_t i;

	if (list == NULL)
		return (0);
	num = listint_t_len(list);
	for (i = 0; i < num; i++)
		node = node->next;
	if (node->next == list)
		return (1);
	return (0);
}
