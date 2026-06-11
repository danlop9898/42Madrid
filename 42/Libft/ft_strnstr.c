/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dalopez3 <dalopez3@student.42madrid.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 19:52:33 by dalopez3          #+#    #+#             */
/*   Updated: 2025/10/16 19:53:52 by dalopez3         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strnstr(const char *big, const char *little, size_t len)
{
	size_t	cont;
	size_t	contlittle;
	size_t	tamlittle;

	cont = 0;
	if (*little == '\0')
		return ((char *)big);
	tamlittle = ft_strlen((char *)little);
	while (big[cont] != '\0' && cont + tamlittle <= len)
	{
		contlittle = 0;
		while (little[contlittle] != '\0'
			&& big[cont + contlittle] == little[contlittle])
			contlittle++;
		if (contlittle == tamlittle)
			return ((char *)&big[cont]);
		cont++;
	}
	return (NULL);
}
