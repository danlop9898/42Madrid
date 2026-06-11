/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split_aux.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dalopez3 <dalopez3@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/30 16:56:06 by dalopez3          #+#    #+#             */
/*   Updated: 2026/03/30 18:08:29 by dalopez3         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

size_t	ft_strlen(char *str)
{
	size_t	i;

	i = 0;
	while (str[i])
		i++;
	return (i);
}

char	*f_empty_string(void)
{
	char	*substring;

	substring = malloc(1);
	if (!substring)
		return (NULL);
	substring[0] = '\0';
	return (substring);
}

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	size_t	lon;
	size_t	cont;
	char	*substring;

	if (!s)
		return (NULL);
	lon = ft_strlen((char *)s);
	if (start >= lon)
		return (f_empty_string());
	if (len > lon - start)
		len = lon - start;
	substring = malloc(len + 1);
	if (!substring)
		return (NULL);
	cont = 0;
	while (cont < len && s[start + cont])
	{
		substring[cont] = s[start + cont];
		cont++;
	}
	substring[cont] = '\0';
	return (substring);
}

void	*ft_calloc(size_t nmemb, size_t size)
{
	void	*d;
	size_t	totalsize;
	char	*datoscast;
	size_t	posarray;

	posarray = 0;
	totalsize = nmemb * size;
	if (size != 0 && totalsize / size != nmemb)
		return (NULL);
	d = malloc(totalsize);
	if (!d)
		return (NULL);
	datoscast = (char *)d;
	while (posarray < totalsize)
	{
		datoscast[posarray] = 0;
		posarray++;
	}
	return (d);
}

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
