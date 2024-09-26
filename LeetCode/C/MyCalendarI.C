#include <stdio.h>
#include <stdlib.h>

#define MAX_TIME 1000

typedef struct
{
    int size;
    int time[MAX_TIME][2];
} MyCalendar;

MyCalendar *myCalendarCreate()
{
    MyCalendar *calendar = malloc(sizeof(MyCalendar));
    memset(calendar, 0, sizeof(MyCalendar));
    return calendar;
}

bool myCalendarBook(MyCalendar *obj, int start, int end)
{
    if (obj->size != 0)
    {
        for (int i = 0; i < obj->size; i++)
        {
            int time[] = {0, 0};
            time[0] = obj->time[i][0];
            time[1] = obj->time[i][1];

            if (time[0] < end && start < time[1])
            {
                return false;
            }
        }
    }
    obj->time[obj->size][0] = start;
    obj->time[obj->size][1] = end;
    obj->size++;
    return true;
}

void myCalendarFree(MyCalendar *obj)
{
    free(obj);
}