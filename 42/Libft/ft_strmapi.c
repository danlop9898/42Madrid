/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strmapi.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dalopez3 <dalopez3@student.42madrid.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/17 10:43:15 by dalopez3          #+#    #+#             */
/*   Updated: 2025/10/17 10:44:08 by dalopez3         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strmapi(char const *s, char (*f)(unsigned int, char))
{
	char	*result;
	char	*scast;
	size_t	size;
	size_t	cont;

	cont = 0;
	scast = (char *)s;
	size = ft_strlen(scast);
	result = malloc(size + 1);
	if (!result)
		return (NULL);
	while (cont < size)
	{
		result[cont] = f(cont, s[cont]);
		cont++;
	}
	result[cont] = '\0';
	return (result);
}
