/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_ord1b.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dalopez3 <dalopez3@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/30 19:06:13 by dalopez3          #+#    #+#             */
/*   Updated: 2026/03/31 18:21:56 by dalopez3         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_move_min_to_top(t_node **a)
{
	int	len;
	int	minpos;
	int	moves;

	len = ft_nodesize(*a);
	minpos = ft_find_min(*a);
	if (minpos <= len / 2)
		while (minpos-- > 0)
			ft_ra(a);
	else
	{
		moves = len - minpos;
		while (moves-- > 0)
			ft_rra(a);
	}
}

void	ft_sort4_5(t_node **a, t_node **b)
{
	int	len;

	len = ft_nodesize(*a);
	while (len > 3)
	{
		ft_move_min_to_top(a);
		ft_pb(a, b);
		len--;
	}
	ft_sort3(a);
	if (ft_nodesize(*b) == 2 && (*b)->value < (*b)->next->value)
		ft_sb(b);
	while (*b)
		ft_pa(a, b);
}
