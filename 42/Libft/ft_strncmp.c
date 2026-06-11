/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncmp.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dalopez3 <dalopez3@student.42madrid.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 19:41:23 by dalopez3          #+#    #+#             */
/*   Updated: 2025/10/16 19:41:42 by dalopez3         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_strncmp(const char *s1, const char *s2, size_t n)
{
	size_t	cont;
	int		res;

	cont = 0;
	res = 0;
	while (cont < n)
	{
		if ((unsigned char)s1[cont] != (unsigned char)s2[cont]
			|| s1[cont] == '\0' || s2[cont] == '\0')
		{
			res = ((unsigned char)s1[cont] - (unsigned char)s2[cont]);
			return (res);
		}
		cont++;
	}
	return (0);
}
