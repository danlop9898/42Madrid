NAME = push_swap
CC = cc
CFLAGS = -Wall -Wextra -Werror
SRC = ft_comp.c ft_ord1a.c ft_ord1b.c ft_ord2.c ft_push.c ft_reverse_rotate.c ft_rotate.c ft_swap.c ft_comp2.c ft_split_aux.c ft_aux.c ft_comp3.c main.c
OBJ = $(SRC:.c=.o)

all: $(NAME)

$(NAME): $(OBJ)
	$(CC) $(CFLAGS) $(OBJ) -o $(NAME)

clean:
	rm -f $(OBJ)

fclean:
	rm -f $(OBJ)  $(NAME)

re: fclean all

.PHONY: re clean fclean all