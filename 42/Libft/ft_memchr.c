/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dalopez3 <dalopez3@student.42madrid.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 19:44:57 by dalopez3          #+#    #+#             */
/*   Updated: 2025/10/16 19:46:16 by dalopez3         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memchr(const void *s, int c, size_t n)
{
	size_t				cont;
	const unsigned char	*cad;

	cont = 0;
	cad = s;
	while (cont < n)
	{
		if (cad[cont] == (unsigned char)c)
			return ((void *)&cad[cont]);
		cont++;
	}
	return (NULL);
}
