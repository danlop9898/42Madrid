/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putendl_fd.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dalopez3 <dalopez3@student.42madrid.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/17 10:53:34 by dalopez3          #+#    #+#             */
/*   Updated: 2025/10/17 10:53:43 by dalopez3         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_putendl_fd(char *s, int fd)
{
	size_t	size;
	size_t	cont;

	size = ft_strlen(s);
	cont = 0;
	while (cont < size)
	{
		write(fd, &s[cont], 1);
		cont++;
	}
	write(fd, "\n", 1);
}
