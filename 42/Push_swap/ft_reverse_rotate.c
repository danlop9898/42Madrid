/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_reverse_rotate.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dalopez3 <dalopez3@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/30 17:40:05 by dalopez3          #+#    #+#             */
/*   Updated: 2026/03/30 17:40:05 by dalopez3         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_reverse_rotate(t_node **x)
{
	t_node	*temp;
	t_node	*end;
	t_node	*penult;

	temp = *x;
	while (temp->next != NULL)
		temp = temp->next;
	end = temp;
	temp = *x;
	while (temp->next != end)
		temp = temp->next;
	penult = temp;
	temp = *x;
	end->next = temp;
	penult->next = NULL;
	*x = end;
}

void	ft_rra(t_node **a)
{
	ft_reverse_rotate(a);
	write (1, "rra\n", 4);
}

void	ft_rrb(t_node **b)
{
	ft_reverse_rotate(b);
	write (1, "rrb\n", 4);
}

void	ft_rrr(t_node **a, t_node **b)
{
	ft_reverse_rotate(a);
	ft_reverse_rotate(b);
	write (1, "rrr\n", 4);
}
