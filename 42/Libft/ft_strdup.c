/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dalopez3 <dalopez3@student.42madrid.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/17 10:11:04 by dalopez3          #+#    #+#             */
/*   Updated: 2025/10/17 10:13:08 by dalopez3         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strdup(const char *s)
{
	char	*copy;
	size_t	tam;
	char	*scast;

	scast = (char *)s;
	tam = ft_strlen(scast);
	copy = malloc(tam + 1);
	if (!copy)
		return (NULL);
	copy = ft_memmove(copy, s, tam);
	copy[tam] = '\0';
	return (copy);
}
