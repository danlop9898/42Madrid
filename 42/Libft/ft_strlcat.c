/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dalopez3 <dalopez3@student.42madrid.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 19:10:26 by dalopez3          #+#    #+#             */
/*   Updated: 2025/10/16 19:22:15 by dalopez3         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_strlcat(char *dst, const char *src, size_t size)
{
	size_t	contdest;
	size_t	contsrc;
	size_t	totaldst;
	size_t	totalsrc;

	contdest = 0;
	contsrc = 0;
	totaldst = ft_strlen(dst);
	totalsrc = ft_strlen((char *)src);
	if (size <= totaldst)
		return (size + totalsrc);
	while (dst[contdest] != '\0')
		contdest++;
	while (src[contsrc] != '\0' && (contdest + contsrc) < (size - 1))
	{
		dst[contdest + contsrc] = src[contsrc];
		contsrc++;
	}
	dst[contdest + contsrc] = '\0';
	return (totaldst + totalsrc);
}
