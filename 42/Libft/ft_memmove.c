/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dalopez3 <dalopez3@student.42madrid.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 18:40:24 by dalopez3          #+#    #+#             */
/*   Updated: 2025/10/16 18:50:53 by dalopez3         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memmove(void *dest, const void *src, size_t num)
{
	char		*dest1;
	const char	*copy;

	dest1 = dest;
	copy = src;
	if (!dest && !src)
		return (NULL);
	if (dest < src)
		ft_memcpy(dest1, copy, num);
	else if (dest > src)
	{
		while (num > 0)
		{
			num--;
			dest1[num] = copy[num];
		}
	}
	return (dest);
}
