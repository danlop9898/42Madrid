/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_push.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dalopez3 <dalopez3@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/30 17:39:46 by dalopez3          #+#    #+#             */
/*   Updated: 2026/03/30 17:39:46 by dalopez3         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_pa(t_node **a, t_node **b)
{
	t_node	*afirst;
	t_node	*bfirst;

	if (!(*b))
		return ;
	afirst = *a;
	bfirst = *b;
	*b = bfirst->next;
	bfirst->next = afirst;
	*a = bfirst;
	write (1, "pa\n", 3);
}

void	ft_pb(t_node **a, t_node **b)
{
	t_node	*afirst;
	t_node	*bfirst;

	if (!(*a))
		return ;
	afirst = *a;
	bfirst = *b;
	*a = afirst->next;
	afirst->next = bfirst;
	*b = afirst;
	write (1, "pb\n", 3);
}
