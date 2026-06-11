/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dalopez3 <dalopez3@student.42madrid.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 19:37:22 by dalopez3          #+#    #+#             */
/*   Updated: 2025/10/16 19:38:29 by dalopez3         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strrchr(const char *s, int c)
{
	int			cont;
	const char	*last;

	last = NULL;
	cont = 0;
	while (s[cont] != '\0')
	{
		if (s[cont] == (char)c)
			last = &s[cont];
		cont++;
	}
	if (c == '\0')
		return ((char *)&s[cont]);
	return ((char *)last);
}
