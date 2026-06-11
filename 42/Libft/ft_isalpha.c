/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isalpha.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dalopez3 <dalopez3@student.42madrid.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 17:50:11 by dalopez3          #+#    #+#             */
/*   Updated: 2025/10/16 17:50:22 by dalopez3         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_isalpha(int c)
{
	int	control;

	control = 0;
	if ((c < 'a' || c > 'z') && (c < 'A' || c > 'Z'))
		control++;
	if (control == 0)
		return (1);
	else
		return (0);
}
