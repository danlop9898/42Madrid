/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dalopez3 <dalopez3@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/30 11:57:20 by dalopez3          #+#    #+#             */
/*   Updated: 2026/02/03 15:26:42 by dalopez3         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <stdarg.h>
# include <unistd.h>
# include <string.h>
# include <stdlib.h>

int	ft_printf(const char *p, ...);
int	ft_letter(va_list args, const char *p);
int	ft_put_hex(unsigned long n, char *base);
int	ft_put_unsigned(unsigned int n);
int	ft_functionsc(char spec, va_list args);
int	ft_putnbr_len(int n);
int	ft_functionxp(char spec, va_list args);
int	ft_null_or_not(unsigned long n);
int	ft_functionu(char spec, va_list args);
int	ft_strlen(char *str);
#endif