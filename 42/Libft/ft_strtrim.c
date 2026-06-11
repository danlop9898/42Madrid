/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dalopez3 <dalopez3@student.42madrid.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/21 15:49:36 by dalopez3          #+#    #+#             */
/*   Updated: 2025/10/21 15:49:46 by dalopez3         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	f_start(const char *s1, const char *set)
{
	size_t	conts1;
	size_t	contset;
	int		bool;

	conts1 = 0;
	while (s1[conts1])
	{
		contset = 0;
		bool = 0;
		while (set[contset])
		{
			if (s1[conts1] == set[contset])
			{
				bool = 1;
				break ;
			}
			contset++;
		}
		if (bool == 0)
			break ;
		conts1++;
	}
	return (conts1);
}

static int	f_end(const char *s1, const char *set)
{
	int	conts1;
	int	contset;
	int	bool;

	if (s1[0] == '\0')
		return (0);
	conts1 = ft_strlen((char *)s1) - 1;
	while (conts1 >= 0)
	{
		contset = 0;
		bool = 0;
		while (set[contset])
		{
			if (s1[conts1] == set[contset])
			{
				bool = 1;
				break ;
			}
			contset++;
		}
		if (bool == 0)
			break ;
		conts1--;
	}
	return (conts1);
}

char	*ft_strtrim(char const *s1, char const *set)
{
	int		start;
	int		end;
	char	*res;
	int		len;

	if (!s1 || !set)
		return (NULL);
	start = f_start(s1, set);
	end = f_end(s1, set);
	if (start > end)
		return (ft_strdup(""));
	len = end - start + 1;
	res = malloc(len + 1);
	if (!res)
		return (NULL);
	ft_strlcpy(res, (char *)(s1 + start), len + 1);
	return (res);
}
