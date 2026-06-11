/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dalopez3 <dalopez3@student.42madrid.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/17 10:08:40 by dalopez3          #+#    #+#             */
/*   Updated: 2025/10/17 10:09:18 by dalopez3         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_calloc(size_t nmemb, size_t size)
{
	void	*d;
	size_t	totalsize;
	char	*datoscast;
	size_t	posarray;

	posarray = 0;
	totalsize = nmemb * size;
	if (size != 0 && totalsize / size != nmemb)
		return (NULL);
	d = malloc(totalsize);
	if (!d)
		return (NULL);
	datoscast = (char *)d;
	while (posarray < totalsize)
	{
		datoscast[posarray] = 0;
		posarray++;
	}
	return (d);
}
