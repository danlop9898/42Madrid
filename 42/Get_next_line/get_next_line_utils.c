/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dalopez3 <dalopez3@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/21 15:33:59 by dalopez3          #+#    #+#             */
/*   Updated: 2026/01/27 13:29:51 by dalopez3         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char	*ft_strchr(const char *s, int c)
{
	int	cont;

	cont = 0;
	while (s[cont] != '\0')
	{
		if (s[cont] == (char)c)
			return ((char *)&s[cont]);
		cont++;
	}
	if (c == '\0')
	{
		return ((char *)&s[cont]);
	}
	return (NULL);
}

char	*ft_strjoin(char *s1, char const *s2)
{
	char	*result;
	char	*s1cast;
	char	*s2cast;
	size_t	longs1;
	size_t	longs2;

	if (!s1 && !s2)
		return (NULL);
	if (!s1)
		return (ft_strdup(s2));
	if (!s2)
		return (ft_strdup(s1));
	s1cast = (char *)s1;
	s2cast = (char *)s2;
	longs1 = ft_strlen(s1cast);
	longs2 = ft_strlen(s2cast);
	result = malloc(longs1 + longs2 + 1);
	if (!result)
		return (NULL);
	ft_strlcpy(result, s1cast, longs1 + 1);
	ft_strlcpy(result + longs1, s2cast, longs2 + 1);
	free(s1);
	return (result);
}

size_t	ft_strlcpy(char *dest, char *src, size_t size)
{
	size_t	cont;
	size_t	size1;

	size1 = ft_strlen(src);
	cont = 0;
	if (size > 0)
	{
		while (src[cont] && cont < size - 1)
		{
			dest[cont] = src[cont];
			cont++;
		}
		dest[cont] = '\0';
	}
	return (size1);
}

char	*ft_strdup(const char *s)
{
	char	*copy;
	size_t	tam;
	char	*scast;

	tam = 0;
	scast = (char *)s;
	while (scast[tam])
		tam++;
	copy = malloc(tam + 1);
	if (!copy)
	{
		free(copy);
		return (NULL);
	}
	copy = ft_memmove(copy, s, tam);
	copy[tam] = '\0';
	return (copy);
}

size_t	ft_strlen(char *str)
{
	size_t	i;

	i = 0;
	while (str[i])
		i++;
	return (i);
}
