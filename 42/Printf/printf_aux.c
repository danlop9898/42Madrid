/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   printf_aux.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dalopez3 <dalopez3@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/20 18:00:43 by dalopez3          #+#    #+#             */
/*   Updated: 2026/02/03 15:19:48 by dalopez3         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_functionsc(char spec, va_list args)
{
	int		len;
	char	c;
	char	*s;

	len = 0;
	if (spec == 's')
	{
		s = va_arg(args, char *);
		if (!s)
			s = "(null)";
		len = ft_strlen(s);
		write(1, s, ft_strlen(s));
	}
	else if (spec == 'c')
	{
		c = (char)va_arg(args, int);
		len = 1;
		write(1, &c, 1);
	}
	else if (spec == '%')
	{
		len = 1;
		write(1, "%", 1);
	}
	return (len);
}

int	ft_putnbr_len(int n)
{
	long	l;
	int		len;

	l = n;
	len = 0;
	if (l < 0)
	{
		write(1, "-", 1);
		l = -l;
		len++;
	}
	if (l >= 10)
		len += ft_putnbr_len(l / 10);
	write (1, &"0123456789"[l % 10], 1);
	len++;
	return (len);
}

int	ft_functionxp(char spec, va_list args)
{
	unsigned long	n;
	int				len;

	len = 0;
	if (spec == 'x')
	{
		n = va_arg(args, unsigned int);
		len = ft_put_hex(n, "0123456789abcdef");
	}
	else if (spec == 'X')
	{
		n = va_arg(args, unsigned int);
		len = ft_put_hex(n, "0123456789ABCDEF");
	}
	else if (spec == 'p')
	{
		n = va_arg(args, unsigned long);
		len = ft_null_or_not(n);
	}
	return (len);
}

int	ft_functionu(char spec, va_list args)
{
	unsigned int	n;

	if (spec == 'u')
	{
		n = va_arg(args, unsigned int);
		return (ft_put_unsigned (n));
	}
	return (0);
}

int	ft_strlen(char *str)
{
	int	i;

	i = 0;
	while (str[i])
		i++;
	return (i);
}
