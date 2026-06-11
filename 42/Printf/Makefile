NAME = libftprintf.a
CC = cc
CFLAGS = -Wall -Wextra -Werror
SRC = printf.c printf_aux.c
OBJ = $(SRC:.c=.o)

all: $(NAME)

$(NAME): $(OBJ)
	ar rcs $(NAME) $(OBJ)

clean: 
	rm -f $(OBJ)

fclean:
	rm -f $(OBJ) $(NAME)

re: fclean all

.PHONY: re clean fclean all