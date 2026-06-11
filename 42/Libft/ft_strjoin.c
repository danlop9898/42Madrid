/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dalopez3 <dalopez3@student.42madrid.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/17 10:18:23 by dalopez3          #+#    #+#             */
/*   Updated: 2025/10/17 10:21:02 by dalopez3         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strjoin(char const *s1, char const *s2)
{
	char	*result;
	char	*s1cast;
	char	*s2cast;
	size_t	longs1;
	size_t	longs2;

	if (!s1 && !s2)
		return (NULL);
	if (!s1)
		return (ft_strdup(s2));
	if (!s2)
		return (ft_strdup(s1));
	s1cast = (char *)s1;
	s2cast = (char *)s2;
	longs1 = ft_strlen(s1cast);
	longs2 = ft_strlen(s2cast);
	result = malloc(longs1 + longs2 + 1);
	if (!result)
		return (NULL);
	ft_strlcpy(result, s1cast, longs1 + 1);
	ft_strlcpy(result + longs1, s2cast, longs2 + 1);
	return (result);
}
