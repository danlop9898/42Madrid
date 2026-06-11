/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dalopez3 <dalopez3@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/19 18:31:08 by dalopez3          #+#    #+#             */
/*   Updated: 2026/03/31 18:22:15 by dalopez3         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	ft_run_push_swap(int argc, char **argv, t_node **a, t_node **b)
{
	int	nbits;

	ft_parse_args(argc, argv, a);
	if (ft_duplicate_array(*a))
	{
		free_stack(a);
		return (1);
	}
	if (ft_is_sorted(*a))
	{
		free_stack(a);
		return (0);
	}
	ft_index_array(a);
	if (ft_nodesize(*a) <= 5)
		ft_ord1(a, b);
	else
	{
		nbits = ft_num_bits(ft_nodesize(*a));
		ft_radix_sort(a, b, nbits);
	}
	return (0);
}

int	main(int argc, char **argv)
{
	t_node	*a;
	t_node	*b;
	int		res;

	a = NULL;
	b = NULL;
	if (argc < 2)
		return (0);
	res = ft_run_push_swap(argc, argv, &a, &b);
	free_stack(&a);
	return (res);
}
