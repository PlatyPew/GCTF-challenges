#include <stdio.h>

void winner();

int main() {
	char buffer[] = "If only getting the key were as easy as typing strings";
	int input;
	scanf("%d",&input);
	if(input == 0xdeadbabe) {
		winner();
	} else {
		printf("Segmatation fault\n");
	}
}

void winner() {
	printf("Key is: %c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",55,49,109,51,32,102,48,114,32,108,117,110,99,104);
}