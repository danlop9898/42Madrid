/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dalopez3 <dalopez3@student.42madrid.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/17 10:37:21 by dalopez3          #+#    #+#             */
/*   Updated: 2025/10/17 10:40:09 by dalopez3         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static char	*f_control(int n1)
{
	char	*result;

	if (n1 == 0)
	{
		result = malloc(2);
		if (!result)
			return (NULL);
		result[0] = '0';
		result[1] = '\0';
		return (result);
	}
	return (NULL);
}

static void	f_aux(char *result, long n1, int neg, int lon)
{
	while (n1 != 0)
	{
		result[lon + neg - 1] = (n1 % 10) + '0';
		n1 = n1 / 10;
		lon--;
	}
	if (neg != 0)
		result[0] = '-';
}

static int	f_countdigit(int n)
{
	int	lon;

	lon = 0;
	while (n != 0)
	{
		n = n / 10;
		lon++;
	}
	return (lon);
}

char	*ft_itoa(int n)
{
	char	*result;
	long	n1;
	int		neg;
	int		lon;

	n1 = n;
	neg = 0;
	result = f_control(n1);
	if (result != NULL)
		return (result);
	if (n1 < 0)
	{
		neg = 1;
		n1 = -n1;
	}
	lon = f_countdigit(n1);
	result = malloc(lon + neg + 1);
	if (!result)
		return (NULL);
	result[lon + neg] = '\0';
	f_aux(result, n1, neg, lon);
	return (result);
}
