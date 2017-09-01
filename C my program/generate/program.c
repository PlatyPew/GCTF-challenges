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
	printf("Flag: %c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",71,67,84,70,123,99,95,109,52,110,95,55,48,95,55,104,51,95,114,51,53,99,117,51,125);
}
