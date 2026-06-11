/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_comp3.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dalopez3 <dalopez3@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/30 18:14:06 by dalopez3          #+#    #+#             */
/*   Updated: 2026/03/31 17:57:39 by dalopez3         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_process_arg(char *arg, t_node **a)
{
	int		j;
	char	**nums;

	nums = ft_split(arg, ' ');
	if (!nums)
		return ;
	j = 0;
	while (nums[j])
	{
		if (!ft_valid_number(nums[j]))
		{
			write(2, "Error\n", 6);
			free_split(nums);
			free_stack(a);
			exit(1);
		}
		ft_overflow(nums[j]);
		add_node(a, ft_atoi(nums[j]));
		j++;
	}
	free_split(nums);
}

void	ft_parse_args(int argc, char **argv, t_node **a)
{
	int	i;

	i = 1;
	while (i < argc)
	{
		ft_process_arg(argv[i], a);
		i++;
	}
}
