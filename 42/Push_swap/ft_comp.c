/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_comp.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dalopez3 <dalopez3@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/24 11:01:38 by dalopez3          #+#    #+#             */
/*   Updated: 2026/03/31 17:45:18 by dalopez3         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	ft_duplicate(int *arr, int size)
{
	int	cont1;
	int	cont2;

	cont1 = 0;
	while (cont1 < size)
	{
		cont2 = cont1 + 1;
		while (cont2 < size)
		{
			if (arr[cont1] == arr[cont2])
				return (1);
			cont2++;
		}
		cont1++;
	}
	return (0);
}

int	ft_valid_number(char *arr)
{
	int	cont;

	cont = 0;
	if (arr[cont] == '+' || arr[cont] == '-')
		cont++;
	if (!arr[cont])
		return (0);
	while (arr[cont])
	{
		if (arr[cont] < '0' || arr[cont] > '9')
			return (0);
		cont++;
	}
	return (1);
}

long	ft_atolong(const char *str)
{
	long	res;
	int		sign;
	int		cont;

	res = 0;
	sign = 1;
	cont = 0;
	if (str[cont] == '+' || str[cont] == '-')
	{
		if (str[cont] == '-')
			sign = -1;
		cont++;
	}
	while (str[cont])
	{
		res = res * 10 + (str[cont] - '0');
		cont++;
	}
	res = res * sign;
	return (res);
}

void	ft_overflow(const char *str)
{
	long	num;

	num = ft_atolong(str);
	if (num < -2147483648 || num > 2147483647)
	{
		write(2, "Error\n", 6);
		exit (1);
	}
}
