#include<stdio.h>

int main() {
    // ╔ ═ ╗ ║ ╚ ╝
	int matrix;
	printf("Enter the Value of Box: ");
	scanf("%d", &matrix);
	
	printf("%c", -55);
	for (int top = 1; top <= matrix / 2 + 1; top++) {
		printf("%c", -51);
	}
	printf("%c", -69);

	for (int row = 1; row <= matrix / 2 + 1; row++)
	{
		printf("%c", -70);
		for (int col = 1; col < matrix / 2 + 1; col++)
		{
			printf(" ");
		}
		printf("%c\n", -70);
		
	}
	
	
	
	
}
