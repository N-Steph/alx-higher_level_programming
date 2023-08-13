#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to address of first node
 * @number: number to insert in linked list
 *
 * Return: pointer of type listint_t
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *next_node, *prev_node, new_node;

	if (head == NULL)
		return (NULL);
	if (*head == NULL)
	{
		new_node = malloc(sizeof(listint_t));
		if (new_node == NULL)
			return (NULL);
		new_node->n = number;
		*head = new_node;
		new_node->next = NULL;
		return (new_node);
	}
	next_node = *head;
	prev_node = *head;
	while (next_node != NULL)
	{
		if (next_node->n <= number)
		{
			new_node = malloc(sizeof(listint_t));/* Not freed */
			if (new_node == NULL)
				return (NULL);
			new_node->n = number;
			prev_node->next = new_node;
			new_node->next = next_node;
			return (new_node);
		}
		prev_node = next_node;
		next_node = next->next
	}
	new_node = malloc(sizof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	prev_node->next = new_node;
	new_node->next = NULL;
	return (new_node);
}
