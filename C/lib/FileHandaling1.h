#include<stdio.h>
#include<string.h>

int FileHandaling1() {
    char letters[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; 
    char choice;
    int value;

    FILE *fp = fopen ("file.txt" , "a");

    if (fp == NULL) {
        printf("Error!");
    }

    printf("Enter your choice and the - Value: ");
    scanf("%c %d" , &choice , &value);

    for (int i = 0; i < 27; i++) {
        if (choice == letters[i]) {
            printf("%c" , letters[i] - value);

            fprintf(fp , "%c" , letters[i] - value);
        }
    }
}