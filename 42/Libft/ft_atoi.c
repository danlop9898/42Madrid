/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dalopez3 <dalopez3@student.42madrid.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/20 18:54:42 by dalopez3          #+#    #+#             */
/*   Updated: 2025/10/20 18:54:46 by dalopez3         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

int	ft_atoi(const char *str)
{
	int	cont;
	int	sign;
	int	res;

	cont = 0;
	sign = 1;
	res = 0;
	if (!str)
		return (0);
	while ((str[cont] >= 9 && str[cont] <= 13) || str[cont] == 32)
		cont++;
	if (str[cont] == '+')
		cont++;
	else if (str[cont] == '-')
	{
		sign = -1;
		cont++;
	}
	while (str[cont] >= '0' && str[cont] <= '9')
	{
		res = res * 10 + (str[cont] - '0');
		cont++;
	}
	return (res * sign);
}
