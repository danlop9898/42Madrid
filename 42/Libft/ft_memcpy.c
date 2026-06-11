/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dalopez3 <dalopez3@student.42madrid.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 18:30:53 by dalopez3          #+#    #+#             */
/*   Updated: 2025/10/16 18:31:20 by dalopez3         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memcpy(void *dest, const void *src, size_t n)
{
	char		*dest1;
	const char	*copy;
	size_t		cont;

	if (!dest && !src)
		return (NULL);
	dest1 = dest;
	copy = src;
	cont = 0;
	while (cont < n)
	{
		dest1[cont] = copy[cont];
		cont++;
	}
	return (dest);
}
