#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to address of first node
 * @number: number to insert in linked list
 *
 * Return: pointer of type listint_t
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr_node, *prev_node, *new_node;
	int counter;

	curr_node = *head;
	counter = 0;
	if (head == NULL)
		return (NULL);
	if (*head == NULL)
	{
		new_node = malloc(sizeof(listint_t));
		if (new_node == NULL)
			return (NULL);
		new_node->n = number;
		*head = new_node;
	}
	else
	{
		while (curr_node != NULL)
		{
			if (number < curr_node->n)
			{
				new_node = malloc(sizeof(listint_t));
				if (new_node == NULL)
					return (NULL);
				new_node->n = number;
				new_node->next = curr_node;
				if (counter == 0)
					*head = new_node;
				else
					prev_node->next = new_node;
				return (new_node);
			}
			prev_node = curr_node;
			curr_node = curr_node->next;
			counter++;
		}
		new_node = malloc(sizeof(listint_t));
		if (new_node == NULL)
			return (NULL);
		new_node->n = number;
		prev_node->next = new_node;
	}
	new_node->next = NULL;
	return (new_node);
}
