/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_aux.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dalopez3 <dalopez3@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/30 17:53:27 by dalopez3          #+#    #+#             */
/*   Updated: 2026/03/31 18:12:57 by dalopez3         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	add_node(t_node **a, int value)
{
	t_node	*new;
	t_node	*tmp;

	new = malloc(sizeof(t_node));
	if (!new)
		return ;
	new->value = value;
	new->index = -1;
	new->next = NULL;
	if (!*a)
		*a = new;
	else
	{
		tmp = *a;
		while (tmp->next)
			tmp = tmp->next;
		tmp->next = new;
	}
}

int	ft_duplicate_array(t_node *a)
{
	int		len;
	int		*arr;
	int		i;
	int		dup;
	t_node	*tmp;

	len = ft_nodesize(a);
	arr = malloc(sizeof(int) * len);
	i = 0;
	tmp = a;
	if (!arr)
		return (1);
	while (tmp)
	{
		arr[i++] = tmp->value;
		tmp = tmp->next;
	}
	dup = ft_duplicate(arr, len);
	free(arr);
	return (dup);
}

int	ft_is_sorted(t_node *a)
{
	t_node	*tmp;

	tmp = a;
	while (tmp && tmp->next)
	{
		if (tmp->value > tmp->next->value)
			return (0);
		tmp = tmp->next;
	}
	return (1);
}

void	free_stack(t_node **a)
{
	t_node	*tmp;

	while (*a)
	{
		tmp = (*a)->next;
		free(*a);
		*a = tmp;
	}
}

void	free_split(char **arr)
{
	int	i;

	i = 0;
	if (!arr)
		return ;
	while (arr[i])
	{
		free(arr[i]);
		i++;
	}
	free(arr);
}
