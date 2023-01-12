#include <stdio.h>

char secret[] = {0x8b, 0xaf, 0x11, 0x77, 0xb7, 0xa0, 0x60, 0x23, 0x67, 0x12, 0x54, 0xc1, 0x42, 0x83, 0x23, 0x11, 0x73};
const int secret_len = 17;

void generateMyFlag(int iterations)
    {
        for (int i = 0; i < secret_len - 1; i++)
        {
            for (int j = 0; j < iterations; j++)
            {
                secret[i] ^= 19 & secret[i+1];    
                secret[i] += 32 | secret[i+1];
                secret[i] ^= 27 & secret[i+1];
                secret[i] += 56 | secret[i+1];
                secret[i] ^= 42 & secret[i+1];
                secret[i] += 43 | secret[i+1];
                secret[i] ^= 95 & secret[i+1];
                secret[i] += 74 | secret[i+1];
                secret[i] ^= 69 & secret[i+1];
                secret[i] += 31 | secret[i+1];
            }
        }
    }


int main ()
    {
        printf("Hi!\nPlease provide the correct key to get the flag?\n");
        char* buffer;
        buffer =  (char*) malloc(secret_len + 1);
        if (buffer == NULL)
        {
        printf("Cannot allocate any memory space. Please try later.");
            return -1;
        }
        memset(buffer, 0, secret_len + 1);

        fgets(buffer, secret_len + 1, stdin);
        generateMyFlag(657);

        if (strcmp(buffer, secret) == 0)
            printf("Nice job, Your flag is APACTF{%s}\n", secret);
        else
            printf("Wrong, Please try again to get the flag.!\n");
    
        free(buffer);
        return 0;
    }