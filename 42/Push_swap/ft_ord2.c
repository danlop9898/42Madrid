/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_ord2.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dalopez3 <dalopez3@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/24 10:27:16 by dalopez3          #+#    #+#             */
/*   Updated: 2026/03/31 17:07:08 by dalopez3         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_index_array(t_node **a)
{
	int		leng;
	int		*arr;
	int		cont;
	t_node	*n;

	leng = ft_nodesize(*a);
	arr = malloc(sizeof(int) * leng);
	if (!arr)
		return ;
	cont = 0;
	n = *a;
	while (cont < leng)
	{
		arr[cont] = n->value;
		cont++;
		n = n->next;
	}
	ft_bubble(arr, leng);
	ft_new_index(arr, a, leng);
	free(arr);
}

void	ft_bubble(int *arr, int leng)
{
	int	cont1;
	int	cont2;
	int	temp;

	cont1 = 0;
	cont2 = 0;
	while (cont2 < leng)
	{
		while (cont1 < leng - 1)
		{
			if (arr[cont1] > arr[cont1 + 1])
			{
				temp = arr[cont1];
				arr[cont1] = arr[cont1 + 1];
				arr[cont1 + 1] = temp;
			}
			cont1++;
		}
		cont1 = 0;
		cont2++;
	}
}

void	ft_new_index(int *arr, t_node **a, int leng)
{
	int		contnode;
	int		cont1;
	t_node	*n;

	contnode = 0;
	cont1 = 0;
	n = *a;
	while (contnode < leng)
	{
		while (cont1 < leng)
		{
			if (arr[cont1] == n->value)
			{
				n->index = cont1;
				break ;
			}
			cont1++;
		}
		cont1 = 0;
		n = n->next;
		contnode++;
	}
}

int	ft_num_bits(int leng)
{
	int	maxindex;
	int	nbits;

	nbits = 0;
	maxindex = leng - 1;
	while (maxindex >> nbits != 0)
		nbits++;
	return (nbits);
}

void	ft_radix_sort(t_node **a, t_node **b, int nbits)
{
	int	i;
	int	count;
	int	size;

	i = 0;
	while (i < nbits)
	{
		count = 0;
		size = ft_nodesize(*a);
		while (count < size)
		{
			if (((*a)->index >> i) & 1)
				ft_ra(a);
			else
				ft_pb(a, b);
			count++;
		}
		while (*b)
			ft_pa(a, b);
		i++;
	}
}
