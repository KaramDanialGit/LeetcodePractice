#include <stdio.h>
#include <stdlib.h>

int *findThePrefixCommonArray(int *A, int ASize, int *B, int BSize, int *returnSize)
{
    int *result = (int *)malloc(sizeof(int) * ASize);
    *returnSize = ASize;
    int *seenInA = (int *)calloc(1001, sizeof(int));
    int *seenInB = (int *)calloc(1001, sizeof(int));

    for (int i = 0; i < ASize; i++)
    {
        seenInA[A[i]] = 1;
        seenInB[B[i]] = 1;

        int commonCount = 0;
        for (int j = 0; j <= i; j++)
        {
            if (seenInA[A[j]] && seenInB[A[j]])
            {
                commonCount++;
            }
        }

        result[i] = commonCount;
    }

    free(seenInA);
    free(seenInB);

    return result;
}