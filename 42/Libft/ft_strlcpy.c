/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dalopez3 <dalopez3@student.42madrid.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 18:54:39 by dalopez3          #+#    #+#             */
/*   Updated: 2025/10/16 19:04:15 by dalopez3         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

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
