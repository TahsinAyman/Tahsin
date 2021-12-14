#include<stdio.h>

int ArrayPracticeCourse1() {
	
	int n;
	int f;
	int find;
	
	printf ("Enter how many Number and how many to find: ");
	scanf ("%d %d" , &n , &f);
	
	int number[n];
	
	for (int i = 0; i < n; i++) {
		printf ("Enter Number Data[%d]: " , i + 1);
		scanf ("%d" , &number[i]);
	}
	
	
	for (int i = 0; i < f; i++) {
		printf ("Find Number: ");
		scanf ("%d" , &find);
	}
	
	printf ("\n\nOutput:\n\n");
	
	for (int i = 0; i < n; i++) { 
		if (0 < find || find < n) {
			printf ("Correct: %d\n" , number[i]);
		}
	}
	return 0;
}