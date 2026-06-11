/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dalopez3 <dalopez3@student.42madrid.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 19:48:39 by dalopez3          #+#    #+#             */
/*   Updated: 2025/10/16 19:48:49 by dalopez3         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_memcmp(const void *s1, const void *s2, size_t n)
{
	size_t				cont;
	int					res;
	const unsigned char	*s1cast;
	const unsigned char	*s2cast;

	cont = 0;
	res = 0;
	s1cast = (const unsigned char *)s1;
	s2cast = (const unsigned char *)s2;
	while (cont < n)
	{
		if (s1cast[cont] != s2cast[cont])
		{
			res = s1cast[cont] - s2cast[cont];
			return (res);
		}
		cont++;
	}
	return (0);
}
