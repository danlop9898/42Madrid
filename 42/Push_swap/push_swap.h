/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dalopez3 <dalopez3@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/19 16:18:45 by dalopez3          #+#    #+#             */
/*   Updated: 2026/03/19 16:18:45 by dalopez3         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include <stdarg.h>
# include <unistd.h>
# include <string.h>
# include <stdlib.h>

typedef struct s_node
{
	int				value;
	int				index;
	struct s_node	*next;
}	t_node;

int		ft_duplicate(int *arr, int size);
int		ft_valid_number(char *arr);
long	ft_atolong(const char *str);
void	ft_overflow(const char *str);
int		ft_nodesize(t_node *n);
int		ft_find_min(t_node *a);
void	ft_ord1(t_node **a, t_node **b);
void	ft_sort3(t_node **a);
void	ft_sort4_5(t_node **a, t_node **b);
void	ft_index_array(t_node **a);
void	ft_bubble(int *arr, int leng);
void	ft_new_index(int *arr, t_node **a, int leng);
int		ft_num_bits(int leng);
void	ft_radix_sort(t_node **a, t_node **b, int nbits);
void	ft_pa(t_node **a, t_node **b);
void	ft_pb(t_node **a, t_node **b);
void	ft_reverse_rotate(t_node **x);
void	ft_rra(t_node **a);
void	ft_rrb(t_node **b);
void	ft_rrr(t_node **a, t_node **b);
void	ft_rotate(t_node **x);
void	ft_ra(t_node **a);
void	ft_rb(t_node **b);
void	ft_rr(t_node **a, t_node **b);
void	ft_swap(t_node **x);
void	ft_sa(t_node **a);
void	ft_sb(t_node **b);
void	ft_ss(t_node **a, t_node **b);
void	ft_parse_args(int argc, char **argv, t_node **a);
int		countword(char const *s, char c);
char	*extractword(char const *s, char c, int *index);
void	free1(char **arr, int i);
char	**ft_split(char const *s, char c);
size_t	ft_strlen(char *str);
char	*f_empty_string(void);
char	*ft_substr(char const *s, unsigned int start, size_t len);
void	*ft_calloc(size_t nmemb, size_t size);
int		main(int argc, char **argv);
int		ft_duplicate_array(t_node *a);
int		ft_is_sorted(t_node *a);
void	free_stack(t_node **a);
int		ft_atoi(const char *str);
void	add_node(t_node **a, int value);
void	free_split(char **arr);
int		ft_run_push_swap(int argc, char **argv, t_node **a, t_node **b);
void	ft_process_arg(char *arg, t_node **a);
void	ft_move_min_to_top(t_node **a);
#endif
