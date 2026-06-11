/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   fprint.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dalopez3 <dalopez3@student.42madrid.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/20 17:58:38 by dalopez3          #+#    #+#             */
/*   Updated: 2026/01/20 17:58:47 by dalopez3         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_printf(const char *p, ...)
{
	va_list		args;
	int			count;

	va_start (args, p);
	count = 0;
	while (*p)
	{
		if (*p == '%')
		{
			p++;
			count += ft_letter(args, p);
		}
		else
		{
			write(1, p, 1);
			count++;
		}
		p++;
	}
	va_end(args);
	return (count);
}

int	ft_letter(va_list args, const char *p)
{
	int	count;
	int	n;

	count = 0;
	if (*p == 's' || *p == 'c' || *p == '%')
		count += ft_functionsc(*p, args);
	else if (*p == 'd' || *p == 'i')
	{
		n = va_arg(args, int);
		count += ft_putnbr_len(n);
	}
	else if (*p == 'x' || *p == 'X' || *p == 'p')
		count += ft_functionxp(*p, args);
	else if (*p == 'u')
		count += ft_functionu(*p, args);
	return (count);
}

int	ft_put_hex(unsigned long n, char *base)
{
	int		len;
	char	c;

	len = 0;
	if (n >= 16)
		len += ft_put_hex(n / 16, base);
	c = base[n % 16];
	write (1, &c, 1);
	len++;
	return (len);
}

int	ft_put_unsigned(unsigned int n)
{
	int		len;
	char	c;

	len = 0;
	if (n >= 10)
		len += ft_put_unsigned(n / 10);
	c = (n % 10) + '0';
	write (1, &c, 1);
	len++;
	return (len);
}

int	ft_null_or_not(unsigned long n)
{
	int	len;

	len = 0;
	if (n == 0)
	{
		write (1, "(nil)", 5);
		len = 5;
	}
	else
	{
		write (1, "0x", 2);
		len = 2 + ft_put_hex(n, "0123456789abcdef");
	}
	return (len);
}
