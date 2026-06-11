/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_swap.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dalopez3 <dalopez3@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/30 17:40:24 by dalopez3          #+#    #+#             */
/*   Updated: 2026/03/30 17:40:24 by dalopez3         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_swap(t_node **x)
{
	t_node	*first;
	t_node	*second;

	if (!*x || !(*x)->next)
		return ;
	first = *x;
	second = (*x)->next;
	first->next = second->next;
	second->next = first;
	*x = second;
}

void	ft_sa(t_node **a)
{
	ft_swap(a);
	write (1, "sa\n", 3);
}

void	ft_sb(t_node **b)
{
	ft_swap(b);
	write (1, "sb\n", 3);
}

void	ft_ss(t_node **a, t_node **b)
{
	ft_swap(a);
	ft_swap(b);
	write (1, "ss\n", 3);
}
