#include <stdio.h>

void win() {
    printf("Well done!\n");
}

int main () {
    char *input = "";
    printf("Address of win function is at %p\n",win);
    char array[64] = {0};
    char *ptr = array;
    volatile int (*fp)();
    fp = 0;
    
    for (int i = 0; input[i] != '\0'; i++) {
        if (input[i] == '>') {
            ++ptr;
        } else if (input[i] == '<') {
            --ptr;
        } else if (input[i] == '+') {
            ++*ptr;
        } else if (input[i] == '-') {
            --*ptr;
        } else if (input[i] == '.' ) {
            putchar(*ptr);
        } else if (input[i] == ',') {
            *ptr = getchar();
        } else if (input[i] == '[') {
            continue;
        } else if (input[i] == ']' && *ptr) {   
            int loop = 1;
            while (loop > 0) {
                input[i] = input[--i];
                if (input[i] == '[') {
                    loop--;
                } else if (input[i] == ']') {
                    loop++;
                }
            }
        }
    }
    printf("\nJumping to address 0x%08x\n",fp);
    fp();
    return 0;
}
