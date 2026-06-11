/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dalopez3 <dalopez3@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/21 15:32:44 by dalopez3          #+#    #+#             */
/*   Updated: 2026/01/27 13:29:11 by dalopez3         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char	*ft_endline(char **temp)
{
	char	*new_temp;
	char	*line;
	int		len;
	char	*pos;

	pos = ft_strchr(*temp, '\n');
	len = pos - *temp + 1;
	line = malloc(len + 1);
	if (!line)
		return (NULL);
	ft_strlcpy(line, *temp, len + 1);
	new_temp = ft_strdup(pos + 1);
	if (!new_temp)
	{
		free(line);
		return (NULL);
	}
	free(*temp);
	*temp = new_temp;
	return (line);
}

char	*ft_byteszero(char **temp)
{
	char	*line;

	line = ft_strdup(*temp);
	if (!line)
		return (NULL);
	free(*temp);
	*temp = NULL;
	return (line);
}

char	*get_next_line(int fd)
{
	static char	*temp;
	char		buffer[BUFFER_SIZE + 1];
	char		*new_temp;
	ssize_t		bytes;

	while (1)
	{
		bytes = read(fd, buffer, BUFFER_SIZE);
		if (bytes < 0)
			return (NULL);
		if (bytes == 0 && (temp == NULL || *temp == '\0'))
			return (free(temp), NULL);
		buffer[bytes] = '\0';
		if (temp == NULL)
			temp = ft_strdup(buffer);
		else
		{
			new_temp = ft_strjoin(temp, buffer);
			temp = new_temp;
		}
		if (ft_strchr(temp, '\n'))
			return (ft_endline(&temp));
		if (bytes == 0)
			return (ft_byteszero(&temp));
	}
}

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

void	*ft_memcpy(void *dest, const void *src, size_t n)
{
	char		*dest1;
	const char	*copy;
	size_t		cont;

	if (!dest && !src)
		return (NULL);
	dest1 = dest;
	copy = src;
	cont = 0;
	while (cont < n)
	{
		dest1[cont] = copy[cont];
		cont++;
	}
	return (dest);
}
