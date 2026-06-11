/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_substr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dalopez3 <dalopez3@student.42madrid.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/17 10:16:10 by dalopez3          #+#    #+#             */
/*   Updated: 2025/10/17 10:16:17 by dalopez3         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static char	*f_empty_string(void)
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
