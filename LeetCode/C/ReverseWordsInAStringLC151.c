void reverse(int start, int end, char *s)
{
    int p1 = start;
    int p2 = end;

    while (p1 < p2)
    {
        char temp = s[p1];
        s[p1] = s[p2];
        s[p2] = temp;
        p1++;
        p2--;
    }
}

char *reverseWords(char *s)
{
    int start = 0;
    int end = strlen(s) - 1;

    while (s[start] == ' ')
    {
        start++;
    }

    while (s[end] == ' ')
    {
        end--;
    }

    int index = 0;
    for (int i = start; i <= end; i++)
    {
        if (s[i] != ' ')
        {
            s[index++] = s[i];
        }
        else if (s[i] == ' ' && (i > start && s[i - 1] != ' '))
        {
            s[index++] = ' ';
        }
    }
    s[index] = '\0';
    reverse(0, index - 1, s);

    int ptr1 = 0;
    for (int i = 0; i <= index; i++)
    {
        if (s[i] == ' ' || s[i] == '\0')
        {
            reverse(ptr1, i - 1, s);
            ptr1 = i + 1;
        }
    }

    return s;
}