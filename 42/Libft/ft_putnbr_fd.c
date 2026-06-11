/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dalopez3 <dalopez3@student.42madrid.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/17 10:54:38 by dalopez3          #+#    #+#             */
/*   Updated: 2025/10/17 10:54:46 by dalopez3         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_putnbr_fd(int n, int fd)
{
	long	l;
	long	div;

	l = n;
	div = 1;
	if (l < 0)
	{
		ft_putchar_fd('-', fd);
		l = -l;
	}
	if (l == 0)
		ft_putchar_fd('0', fd);
	else
	{
		while (l / div >= 10)
			div *= 10;
		while (div > 0)
		{
			ft_putchar_fd((l / div) + '0', fd);
			l %= div;
			div /= 10;
		}
	}
}
