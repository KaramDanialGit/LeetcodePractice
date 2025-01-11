
#include <stdio.h>
#include <stdlib.h>

typedef struct ListNode
{
    int val;
    struct ListNode *prev;
    struct ListNode *next;
} ListNode;

void add_node(ListNode **head, ListNode *node)
{
    if ((*head)->next == *head)
    {
        (*head)->next = node;
        (*head)->prev = node;
        node->prev = *head;
        node->next = *head;
        return;
    }

    node->next = (*head)->next;
    node->next->prev = node;
    node->prev = *head;
    (*head)->next = node;
    return;
}

int main()
{
    ListNode *head = malloc(sizeof(ListNode));
    head->val = 0;
    head->prev = head;
    head->next = head;

    ListNode *n1 = malloc(sizeof(ListNode));
    n1->val = 1;
    n1->prev = NULL;
    n1->next = NULL;

    ListNode *n2 = malloc(sizeof(ListNode));
    n2->val = 2;
    n2->prev = NULL;
    n2->next = NULL;

    ListNode *n3 = malloc(sizeof(ListNode));
    n3->val = 3;
    n3->prev = NULL;
    n3->next = NULL;

    add_node(&head, n1);
    add_node(&head, n2);
    add_node(&head, n3);

    ListNode *current = head;

    while (current)
    {
        printf("%d\n", current->val);
        current = current->next;
    }

    return 0;
}