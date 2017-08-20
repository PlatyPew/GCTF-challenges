#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
	if (argc < 2) {
		printf("Requires argv[1] as password\n");
	} else if (strcmp(argv[1],"ze_f1ag_iz_n0t_f4r_aw4y_if_y0u_believ3") == 0) {
		system("cat flag.txt");
	} else {
		printf("Incorrect password!\n");
	}
}
