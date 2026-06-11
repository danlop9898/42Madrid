*Este proyecto a sido creado como parte del plan de estudios 42 por dalopez3*

# Descripción

El proyecto **push_swap** pide que ordenemos de menor a mayor **x** números utilizando 2 pilas **(a, b)** y un conjunto limitado de operaciones o movimientos.

Este ejercicio no es un ejercicio algorítmico de ordenación tradicional ya que también hay que hacerlo con el mínimo de movimientos posibles.

## Movimientos

Solo podemos utilizar los siguientes movimientos:

- sa (swap a): Intercambia los dos primeros números de la pila a. Si solo hay un número o está vacia no hace nada.
- sb (swap b):  Intercambia los dos primeros números de la pila b. Si solo hay un número o está vacia no hace nada.
- ss (swap a, b): Hace sa y sb a la vez.

a = [**1**,**2**,3,4,5];
b = [ , , , , ];
-----------------
a = [**2**,**1**,3,4,5];
b = [ , , , , ];
-----------------

- pa (push a): Toma el primer numero que está en b y lo coloca al principio de a. Si b está vacio no hace nada.
- pb (push b): Toma el primer numero que está en a y lo coloca al principio de b. Si a está vacio no hace nada

a = [**1**,2,3,4,5];
b = [ , , , , ];
-----------------
a = [2,3,4,5, ];
b = [**1**, , , , ];
------------------

- ra (rotate a): Despalza todos los numeros de la pila a una posición adelante. El primer numero pasa a ser el último.
- rb (rotate b): Despalza todos los numeros de la pila b una posición adelante. El primer numero pasa a ser el último.
- rr (rotate a, b): Hace ra y rb a la vez.

a = [1,2,3,4,5];
b = [ , , , , ];
-----------------
a = [2,3,4,5,1];
b = [ , , , , ];
------------------

- rra (reverse rotate a): Desplaza todos los numeros de la pila a una posición hacia atrás. El último número se convierte en el primero.
- rrb (reverse rotate b): Desplaza todos los numeros de la pila b una posición hacia atrás. El último número se convierte en el primero.
- rrr (reverse rotate a, b): Hace rra y rrb a la vez.

a = [1,2,3,4,5];
b = [ , , , , ];
-----------------
a = [5,1,2,3,4];
b = [ , , , , ];
------------------

# Instrucciones

Este programa se compila con make.

Tiene varios ficheros:

## ft_swap

Este fichero se encarga de hacer los movimientos sa, sb y ss. Creamos la función principal donde hacemos swap y después creamos las funciones sa, sb y ss donde hacemos la llamada y el print.

**ft_swap**

Creamos dos variables t_node para guardar la primera y la segunda posición (first y second). 
En el if controlamos que no esté vacio o que solo haya un nodo. 
Igualamos las variables first al primer nodo y second al segundo nodo. 
Cambiamos donde apuntan los nodos a las nuevas posiciones y por últmo actualizamos el puntero x al nuevo primer nodo que es el nodo second.

```
void	ft_swap(t_node **x)
{
	t_node	*first;
	t_node	*second;

	if (!*x || !(*x)->next)
		return ;
	first = *x;
	second = (*x)->next;
	first->next = second->next;
	second->next = first;
	*x = second;
}
```

**ft_sa, ft_sb y ft_ss**

Estas tres funciones llaman a la función ft_swap y hacen su respectivo write.

```
void    ft_sa(t_node **a)
{
	ft_swap(a);
	write (1, "sa\n", 3);
}

void	ft_sb(t_node **b)
{
	ft_swap(b);
	write (1, "sb\n", 3);
}

void	ft_ss(t_node **a, t_node **b)
{
	ft_swap(a);
	ft_swap(b);
	write (1, "ss\n", 3);
}
```

## ft_push

Este fichero se encarga de hacer los movimientos de push (pa y pb).

**ft_pa**

Esta función se encarga de hacer el pa.
Crearemos dos nodos, afirst y bfirst.
Comprobamos en el if que b no esté vacio.
Igualamos las variable a la primera variable de cada pila.
Le indicamos que el primer nodo de b va a ser el segundo nodo de b
Indicamos que bfirst va a apuntar a afirst (bfirst -> afirst)
Ahora el primer numero de la pila a va a ser bfirst.
Por último escribimos pa.

```
void	ft_pa(t_node **a, t_node **b)
{
	t_node	*afirst;
	t_node	*bfirst;

	if (!(*b))
		return ;
	afirst = *a;
	bfirst = *b;
	*b = bfirst->next;
	bfirst->next = afirst;
	*a = bfirst;
	write (1, "pa\n", 3);
}
```

**ft_pb**

Esta función se encarga de hacer el pb.
Crearemos dos nodos, afirst y bfirst.
Comprobamos en el if que a no esté vacio.
Igualamos las variable a la primera variable de cada pila.
Le indicamos que el primer nodo de a va a ser el segundo nodo de a
Indicamos que afirst va a apuntar a bfirst (afirst -> bfirst)
Ahora el primer numero de la pila a va a ser afirst.
Por último escribimos pb.

```
void	ft_pb(t_node **a, t_node **b)
{
	t_node	*afirst;
	t_node	*bfirst;

	if (!(*a))
		return ;
	afirst = *a;
	bfirst = *b;
	*a = afirst->next;
	
	afirst->next = bfirst;
	*b = afirst;
	write (1, "pb\n", 3);
}
```

## ft_rotate

Este fichero se encarga de hacer el movimiento rotate (ra, rb y rr).

**ft_rotate**

Esta función se encarga de hacer el movimiento rotate.
Creamos dos nodos, first y temp.
Hacemos el if para ver si x está vacio o solo tiene un nodo. Si se cumple el if hacemos el return.
Igualamos first y temp a *x.
Con el while llegamos al último nodo y metemos el valor del último nodo en temp.
Le indicamos que ahora x* apuntará a lo que es el segundo nodo. (Porque al hacer el rotate ese nodo estará el primero).
Ahora cambiamos los nodos, temp apuntará a first y first apuntará a NULL.

```
void	ft_rotate(t_node **x)
{
    t_node  *first;
    t_node  *temp;

    if(!x || !*x || !(*x)->next)
        return ;
    temp = *x;
    first = *x;
    while(temp->next != NULL)
        temp = temp->next;
    *x = first->next;
    temp->next = first;
    first->next = NULL;
}
```

**ft_ra, ft_rb y ft_rr**

Estas funciones llaman a ft_rotate y hacen sus respectivos writes.

```
void    ft_ra(t_node **a)
{
    ft_rotate(a);
    write (1, "ra\n", 3);
}
void    ft_rb(t_node **b)
{
    ft_rotate(b);
    write (1, "rb\n", 3);
}

void    ft_rr(t_node **a, t_node **b)
{
    ft_rotate(a);
    ft_rotate(b);
    write (1, "rr\n", 3);
}
```

## ft_reverse_rotate 

Este archivo se encarga de hacer el movimiento reverse rotate

**ft_reverse_rotate**

Esta función hace el reverse rotate.
Creamos 3 nodos, temp, end y penult.
Metemos en temp el valor de *x.
Con el while y con temp recorremos la lista hasta llegar al último nodo y guardamos el último nodo en end.
Volvemos a reiniciar temp igualandolo a x.
Con otro while y temp recorremos la lista hasta llegar al nodo anterior a end y lo guardamos en penult.
Reiniciamos otra vez temp.
Ahora indicamos que end apunte a temp y penult a NULL.
*x apuntará al primer nodo que es end.

```
void    ft_reverse_rotate(t_node **x)
{
	t_node  *temp;
    t_node  *end;
    t_node  *penult;

    temp = *x;
    while(temp->next != NULL)
        temp = temp->next;
    end = temp;
    temp = *x;

    while(temp->next != end)
        temp = temp->next;
    penult = temp;

    temp = *x;
    end->next = temp;
    penult->next = NULL;
    *x = end;
}
```

**ft_rra, ft_rrb y ft_rrr**

Estas funciones llamarán a ft_reverse_rotate y harán sus respectivos writes.

```
void    ft_rra(t_node **a)
{
    ft_reverse_rotate(a);
    write (1, "rra\n", 4);
}

void    ft_rrb(t_node **b)
{
   ft_reverse_rotate(b);
    write (1, "rrb\n", 4);
}

void    ft_rrr(t_node **a, t_node **b)
{
    ft_reverse_rotate(a);
    ft_reverse_rotate(b);
    write (1, "rrr\n", 4);
}
```
## ft_ord1a

Este archivo se encargará de la ordenación si hay 5 nodos o menos

**ft_nodesize**

Esta función se encarga de contar los nodos que hay en la lista.
Creamos un int (cont) y lo igualamos a 0.
Con un while le indicamos que mientras no llegue a NULL aumente cont y pase al siguiente nodo.
Cuando acabe el bucle retornamos NULL.

```
int	ft_nodesize(t_node *n)
{
	int	cont;

	cont = 0;
	while (n != NULL)
	{
		cont++;
		n = n->next;
	}
	return (cont);
}
```

**ft_find_min**

Esta función busca el número mas pequeño.
Creamos int pos = 0 (posicion actual).
Creamos int minpos = 0 (guarda la posición del valor más pequeño encontrado)
Creamos int minvalue = a->value (mínimo valor actual)
Creamos t_node *tmp = a (para recorrer la lista)
Con el while recorremos todos los nodos. 
Si en el if encuentra un valor más pequeño que minvalue actualizamos minvalue y posvalue.
Avanzamos al siguiente nodo y aumentamos la posición.
Al final retornamos minpos.

```
int	find_min(t_node *a)
{
	int		pos;
	int		minpos;
	int		minvalue;
	t_node	*tmp;

	pos = 0;
	minpos = 0;
	minvalue = a->value;
	tmp = a;
	while (tmp)
	{
		if (tmp->value < minvalue)
		{
			minvalue = tmp->value;
			minpos = pos;
		}
		tmp = tmp->next;
		pos++;
	}
	return (minpos);
}
```

**ft_ord1**

Esta función es la principal, es la que se eccarga de llamar a las demás funciones.
Creamos int leng que será igual a lo que retorne la función ft_nodesize.
Si leng es igual a 2 con el if mira cual es menor y lo ordena.
Si es 3 llama a la función sort3 y si es 4 o 5 llama a la función sort4_5

```
void	ord1(t_node **a, t_node **b)
{
	int	leng;

	leng = ft_nodesize(*a);
	if (leng == 2)
	{
		if ((*a)->value > (*a)->next->value)
			ft_sa(a);
	}
	if (leng == 3)
		sort3(a);
	if (leng == 4 || leng == 5)
		sort4_5(a, b);
}
```
**ft_sort3**

Esta función se encarga de ordenar los números si hay 3 números.
Creamos 3 ints y fuardamos el valor de los 3 números (first, second y third).
Según los casos que haya (6 casos) los ordenamos de menor a mayor.

```
void	ft_sort3(t_node **a)
{
	int	first;
	int	second;
	int	third;

	first = (*a)->value;
	second = (*a)->next->value;
	third = (*a)->next->next->value;
	if (first > second && second < third && first < third)
		ft_sa(a);
	else if (first > second && second > third)
	{
		ft_sa(a);
		ft_rra(a);
	}
	else if (first > second && second < third && first > third)
		ft_ra(a);
	else if (first < second && second > third && first < third)
	{
		ft_sa(a);
		ft_ra(a);
	}
	else if (first < second && second > third && first > third)
		ft_rra(a);
}

```

## ft_ord1b

Este archivo se encarga de ordenar los números si son 4 o 5 números.

**ft_move_min_to_top**

Esta función mueve el mínimo número.
Creamos 3 ints:
len que será la longitud
minpos que será el mínimo
moves calcula los movimientos
sacamos la longitud de len
sacamos la posición del más pequeño.
Si estña en la primera mitad hacemos ra tantas veces como la posición del min
Si está en la segunda mitad calculamos los movimientos que sera la longitud menos la posición mínima y hacemos rra.

´´´
void	ft_move_min_to_top(t_node **a)
{
	int	len;
	int	minpos;
	int	moves;

	len = ft_nodesize(*a);
	minpos = ft_find_min(*a);
	if (minpos <= len / 2)
		while (minpos-- > 0)
			ft_ra(a);
	else
	{
		moves = len - minpos;
		while (moves-- > 0)
			ft_rra(a);
	}
}
´´´

**ft_sort4_5**

Esta función ordena los números si son 4 o 5 números.
Creamos un int (len) para la longitud.
En len metemos la longitud usando la función ft_nodesize.
Hacemos un bucle y mientras len sea maytor a 3 usamos ft_move_min_to_top para quitar el mínimo, hacemos el movimiento pb y restamos una a len.
Cuando quedan 3 usamos la ordenacion sort3.
Con el if comprobamos que estén en orden correcto en la pila b (si no se mueve con sb).
Hacemos un while hasta que b esté vacio usando pa.

´´´
void	ft_sort4_5(t_node **a, t_node **b)
{
	int	len;

	len = ft_nodesize(*a);
	while (len > 3)
	{
		ft_move_min_to_top(a);
		ft_pb(a, b);
		len--;
	}
	sort3(a);
	if (ft_nodesize(*b) == 2 && (*b)->value < (*b)->next->value)
		ft_sb(b);
	while (*b)
		ft_pa(a, b);
}
´´´
## ft_ord2

Este archivo se encarga de ordenar los números si son más de 5 números. Usaremos el método de ordenación sort.

**ft_index_array**

Esta función sirve para meter los valores de los nodos en un array.
Creamos la siguientes variables:
int leng para la longitud.
int *arr será el array donde meteremoslos números.
int cont será un contador.
node *n que lo utilizaremos para recorrer los nodos.
En leng guardamos la longitud de la lista utilizando ft_nodesize.
En arr creamos el espacio que necesita com malloc y leng.
Si arr falla hacemos return.
Inicializamos el contador a 0 y igualamos n a *a para que tenga el primer nodo.
En el bucle cogemos el primer valor del nodo y lo meetemos en la primera posición del array. Aumentamos el contador y pasamos al siguiente nodo.
Después llamamos a las funciones ft_bubble, ft_new_index y hacemos free.

´´´
void	ft_index_array(t_node **a)
{
	int		leng;
	int		*arr;
	int		cont;
	t_node	*n;

	leng = ft_nodesize(*a);
	arr = malloc(sizeof(int) * leng);
	if (!arr)
		return ;
	cont = 0;
	n = *a;
	while (cont < leng)
	{
		arr[cont] = n->value;
		cont++;
		n = n->next;
	}
	ft_bubble(arr, leng);
	ft_new_index(arr, a, leng);
	free(arr);
}
´´´

**ft_bubble**

Esta función ordenará el array utilizando el método burbuja.
Creamos 3 int (dos contadores y una temporal).
Iniciaizamos los contadores a 0.
Tendremos un bucle dentro del otro.
El bucle exterior hará que el bucle interior se repita x veces donde x es la longitud del array.
El bucle interior es un bucle que se hará hasta que llegue a la longitud - 1 del array.
El bucle interior mirará si el número actual es mayor que el siguiente, si es así usando una variable temporal para no perder el valor cambiará sus puestos.
Cuando acabe el bucle interior su recorrido se aumentará en uno el contador del bucle exterior y se pondrña a 0 el contador del bucle inferior.

´´´
void	ft_bubble(int *arr, int leng)
{
	int	cont1;
	int	cont2;
	int	temp;

	cont1 = 0;
	cont2 = 0;
	while (cont2 < leng)
	{
		while (cont1 < leng - 1)
		{
			if (arr[cont1] > arr[cont1 + 1])
			{
				temp = arr[cont1];
				arr[cont1] = arr[cont1 + 1];
				arr[cont1 + 1] = temp;
			}
			cont1++;
		}
		cont1 = 0;
		cont2++;
	}
}
´´´

**ft_nex_index**

Esta función se encarga de actualizar el index de los nodos (el puesto donde deberían de estar)
Crearemos dos int (contadores) y un nodo.
Inicializamos los contadores a 0 y con n apuntamos al primer nodo. 
El primer while va a recorrer todos los nodos de la lista.
El segundo while busca que el primer VALOR del array en los nodos. Cuando lo encuentra le pone el valor del cont al index (0 ,1 ,2 ... final) y sale del bucle inferior.
Se aumenta el contador exterior, se pasa al siguiente nodo y se restablece el contador inferior.
Aumenta el contador del bucle exterior y así hasta que salga de los dos bucles.

´´´
void	ft_new_index(int *arr, t_node **a, int leng)
{
	int		contnode;
	int		cont1;
	t_node	*n;

	contnode = 0;
	cont1 = 0;
	n = *a;
	while (contnode < leng)
	{
		while (cont1 < leng)
		{
			if (arr[cont1] == n->value)
			{
				n->index = cont1;
				break ;
			}
			cont1++;
		}
		cont1 = 0;
		n = n->next;
		contnode++;
	}
}
´´´

**ft_num_bytes**

Esta función saca los números de bits de los índices.
Creamos dos ints (maxindex y nbits).
Inicializamos nbits a 0 y maxindex será leng -1. 
En el while desplaza los bits de maxindex a nbits para contar cuantos se necesitan.

Loop:

0	4 >> 0 = 4	4 != 0 ✅ → nbits++ → 1

1	4 >> 1 = 2	2 != 0 ✅ → nbits++ → 2

2	4 >> 2 = 1	1 != 0 ✅ → nbits++ → 3

3	4 >> 3 = 0	0 != 0 ❌ → stop

´´´
int	ft_num_bits(int leng)
{
	int	maxindex;
	int	nbits;

	nbits = 0;
	maxindex = leng - 1;
	while (maxindex >> nbits != 0)
		nbits++;
	return (nbits);
}
´´´

**ft_radix_sort**

Esta función es la que ordena los números.
Crearemos 3 ints (i, count y size).
Inicializamos i a 0. Será el contador del bucle externo.
Sacamos el tamaño del nodo.
Recorremos los bits.
En el if desplazamos el indice i bits a la derecha. Si es 1 hacemos ra y si es 0 hacemos pa. Después devolvemos lo que hay en la pila b con pa.

Bit 0 (LSB):

3 → 11 → bit0 = 1 → ra → A: [0,2,1,3]

0 → 00 → bit0 = 0 → pb → A: [2,1,3], B: [0]

2 → 10 → bit0 = 0 → pb → A: [1,3], B: [2,0]

1 → 01 → bit0 = 1 → ra → A: [3,1]

Devolvemos B a A:

A: [2,0,3,1], B: []

´´´
void	ft_radix_sort(t_node **a, t_node **b, int nbits)
{
	int	i;
	int	count;
	int	size;

	i = 0;
	while (i < nbits)
	{
		count = 0;
		size = ft_nodesize(*a);
		while (count < size)
		{
			if (((*a)->index >> i) & 1)
				ft_ra(a);
			else
				ft_pb(a, b);
			count++;
		}
		while (*b)
			ft_pa(a, b);
		i++;
	}
}
´´´

## ft_comp

Este fichero se encargará de las comprobaciones.

**ft_duplicate**

Esta función mirará si hay números duplicados.
Usaremos dos contadores. 
Inicializamos cont1 a 0.
El while exterior acabará cuando se recorra todo el array.
Inicializmos cont2 que será uno mñas que cont1.
Con otro while y un if miramos si los dos números que serían el actual y el siguiente son iguales. Si son igulaes retorna 1 si todo está bien retorna 0.

´´´
int	ft_duplicate(int *arr, int size)
{
	int	cont1;
	int	cont2;

	cont1 = 0;
	while (cont1 < size)
	{
		cont2 = cont1 + 1;
		while (cont2 < size)
		{
			if (arr[cont1] == arr[cont2])
				return (1);
			cont2++;
		}
		cont1++;
	}
	return (0);
}
´´´

**ft_valid_number**

Esta función comprueba que sea un número válido.
Creamos un contador y lo inicializamos a 0.
Si tiene un + o - en la primera posición aumentamos 1 en contador.
En el if comprueba que haya más caracteres.
En el while comprueba que todo lo que haya sea números y retorna 1.

´´´
int	ft_valid_number(char *arr)
{
	int	cont;

	cont = 0;
	if (arr[cont] == '+' || arr[cont] == '-')
		cont++;
	if (!arr[cont])
		return (0);
	while (arr[cont])
	{
		if (arr[cont] < '0' || arr[cont] > '9')
			return (0);
		cont++;
	}
	return (1);
}
´´´

**ft_atolong**

Esta función cambia las variables a long.
Creamos res = 0, sign = 1 y cont = 0.
Miramos el signo  y si es - cambiamos sign a -1.
En un while cogemos res y lo igualamos a res * 10 y se le resta 0 para transformarlo.
Después retornamos  res * sign.

´´´
long	ft_atolong(const char *str)
{
	long	res;
	int		sign;
	int		cont;

	res = 0;
	sign = 1;
	cont = 0;
	if (str[cont] == '+' || str[cont] == '-')
	{
		if (str[cont] == '-')
			sign = -1;
		cont++;
	}
	while (str[cont])
	{
		res = res * 10 + (str[cont] - '0');
		cont++;
	}
	return (res * sign);
}
´´´

**ft_overflow**

Esta función comprueba el overflow del número.
Creamos un long (num) y lo pasamos por la función ft_atolong.
Con el if vemos si hay overflow y escribimos el error.
write 2 es el estandar de errores y exit 1 es la salida de errores.

´´´
void	ft_overflow(const char *str)
{
	long	num;

	num = ft_atolong(str);
	if (num < -2147483648 || num > 2147483647)
	{
		write(2, "Error\n", 6);
		exit (1);
	}
}
´´´
## ft_comp2

Este fichero sigue con las comprobaciones.
Este fichero contiene el ft_split que se necesitará para als comprobaciones.

## ft_comp3

Este fichero sigue con las comprobaciones.

**ft_process_arg**

Separa la cadena en números individuales.
Creamos un int (j) y un char ** (nums).
nums será lo que retorne ft_split y si estña vacio hacemos un return.
Con el while le pasamos a cada numero la función ft_valid_number para ver que sea un número. Si no hacemos free y salimos. 
Miramos que quepa en el int y creamos un nodo convertido a int.

´´´
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
´´´

**ft_parse_args**

Esta función centraliza la lectura de argumentos.
Inicializamos i a 1 porque 0 es el nombre del programa. Por cada argumento hace el ft_process_arg.

´´´
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
´´´

## main

Este archivo tendrá el main.

**ft_run_push_swap**

Esta función hace todas las comprobaciones.
Hacemos el parseo y lo agrega.
Mira si hay duplicados. Si hay duplicados retorna 1 y hace free.
Si está ordenado libera y retorna 0.
Prepara los indices.
Al final escoje el método de ordenación.

´´´
int	ft_run_push_swap(int argc, char **argv, t_node **a, t_node **b)
{
	int	nbits;

	ft_parse_args(argc, argv, a);
	if (duplicate_array(*a))
	{
		free_stack(a);
		return (1);
	}
	if (ft_is_sorted(*a))
	{
		free_stack(a);
		return (0);
	}
	ft_index_array(a);
	if (ft_nodesize(*a) <= 5)
		ord1(a, b);
	else
	{
		nbits = ft_num_bits(ft_nodesize(*a));
		ft_radix_sort(a, b, nbits);
	}
	return (0);
}
´´´

** main

El main.
Comprueba que haya más de 1 argumento. 
Llama a ft_run_push_swap y hace free.

´´´
int	main(int argc, char **argv)
{
	t_node	*a;
	t_node	*b;
	int		res;

	a = NULL;
	b = NULL;
	if (argc < 2)
		return (0);
	res = ft_run_push_swap(argc, argv, &a, &b);
	free_stack(&a);
	return (res);
}
´´´

## ft_aux

Mira los duplicados en el array.
Con len sacamos la longitud.
Creamos el array com malloc.
Con el while recorremos cada nodo y copiamos los valores a los nodos. 
Miramos si hay duplicados y retorna 0 o 1.

´´´
int	ft_duplicate_array(t_node *a)
{
	int		len;
	int		*arr;
	int		i;
	int		dup;
	t_node	*tmp;

	len = ft_nodesize(a);
	arr = malloc(sizeof(int) * len);
	i = 0;
	tmp = a;
	if (!arr)
		return (1);
	while (tmp)
	{
		arr[i++] = tmp->value;
		tmp = tmp->next;
	}
	dup = ft_duplicate(arr, len);
	free(arr);
	return (dup);
}
´´´

**ft_is_sorted**

Comprueba que esté ordenado o no.
Con un while recorremos los nodos. 
En cuanto haya uno mayor sale del bucle y eso es que no estñan ordenados.

´´´
int	ft_is_sorted(t_node *a)
{
	t_node	*tmp;

	tmp = a;
	while (tmp && tmp->next)
	{
		if (tmp->value > tmp->next->value)
			return (0);
		tmp = tmp->next;
	}
	return (1);
}
´´´