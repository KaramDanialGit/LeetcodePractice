#include <stdio.h>
#include <stdlib.h>

struct List
{
    int *array;
    int index;
    int capacity;
};

void init(struct List *list, int capacity)
{
    list->array = malloc(sizeof(int) * capacity);
    list->index = 0;
    list->capacity = capacity;
}

void append(struct List *list, int val)
{
    if (list->index == list->capacity)
    {
        list->capacity = list->capacity * 2;
        list->array = realloc(list->array, sizeof(int) * list->capacity);
    }

    list->array[list->index] = val;
    list->index++;
}

void pop(struct List *list)
{
    if (list->index == 0)
        return;
    list->index--;
}

void print_list(struct List *list)
{
    for (int i = 0; i < list->index; i++)
    {
        printf("%d ", list->array[i]);
    }
}

int main()
{
    struct List *myList = malloc(sizeof(struct List));
    init(myList, 10);

    for (int i = 0; i < 20; i++)
    {
        append(myList, i);
    }

    pop(myList);
    print_list(myList);

    return 0;
}
