/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ord1.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dalopez3 <dalopez3@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/19 16:14:44 by dalopez3          #+#    #+#             */
/*   Updated: 2026/03/19 16:14:44 by dalopez3         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	ft_nodesize(t_node *n)
{
	int	cont;

	cont = 0;
	while (n != NULL)
	{
		cont++;
		n = n->next;
	}
	return (cont);
}

int	ft_find_min(t_node *a)
{
	int		pos;
	int		minpos;
	int		minvalue;
	t_node	*tmp;

	pos = 0;
	minpos = 0;
	minvalue = a->value;
	tmp = a;
	while (tmp)
	{
		if (tmp->value < minvalue)
		{
			minvalue = tmp->value;
			minpos = pos;
		}
		tmp = tmp->next;
		pos++;
	}
	return (minpos);
}

void	ft_ord1(t_node **a, t_node **b)
{
	int	leng;

	leng = ft_nodesize(*a);
	if (leng == 2)
	{
		if ((*a)->value > (*a)->next->value)
			ft_sa(a);
	}
	if (leng == 3)
		ft_sort3(a);
	if (leng == 4 || leng == 5)
		ft_sort4_5(a, b);
}

void	ft_sort3(t_node **a)
{
	int	first;
	int	second;
	int	third;

	first = (*a)->value;
	second = (*a)->next->value;
	third = (*a)->next->next->value;
	if (first > second && second < third && first < third)
		ft_sa(a);
	else if (first > second && second > third)
	{
		ft_sa(a);
		ft_rra(a);
	}
	else if (first > second && second < third && first > third)
		ft_ra(a);
	else if (first < second && second > third && first < third)
	{
		ft_sa(a);
		ft_ra(a);
	}
	else if (first < second && second > third && first > third)
		ft_rra(a);
}
