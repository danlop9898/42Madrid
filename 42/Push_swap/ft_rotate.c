/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_rotate.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dalopez3 <dalopez3@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/30 17:40:12 by dalopez3          #+#    #+#             */
/*   Updated: 2026/03/30 17:40:12 by dalopez3         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_rotate(t_node **x)
{
	t_node	*first;
	t_node	*temp;

	if (!x || !*x || !(*x)->next)
		return ;
	temp = *x;
	first = *x;
	while (temp->next != NULL)
		temp = temp->next;
	*x = first->next;
	temp->next = first;
	first->next = NULL;
}

void	ft_ra(t_node **a)
{
	ft_rotate(a);
	write (1, "ra\n", 3);
}

void	ft_rb(t_node **b)
{
	ft_rotate(b);
	write (1, "rb\n", 3);
}

void	ft_rr(t_node **a, t_node **b)
{
	ft_rotate(a);
	ft_rotate(b);
	write (1, "rr\n", 3);
}
