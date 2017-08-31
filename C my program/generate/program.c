#include <stdio.h>

void winner();

int main() {
	char *buffer = "GCTF{This is not an actual flag get rekt lol. I like fidget spinners}";
	int input;
	printf("I have chosen a number between 0 to 10000. Can you guess what it is?\n> ");
	scanf("%d",&input);
	if(input == 9001) {
		winner();
	} else {
	printf("Segmatation Fault\n");
	}
}

void winner() {
	printf("Flag: %c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",102,108,97,103,123,116,104,105,115,95,105,115,95,97,95,102,108,97,103,125);
}
