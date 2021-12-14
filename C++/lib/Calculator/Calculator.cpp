#include <stdio.h>
#include <conio.h>
#include <iomanip>
#include <iostream>
using namespace std;

int add(){
        cout << "\n\nEnter '0' to End addition";
        double var1 = 0 , var2 = 0;
        cout << "\nEnter any number: ";
        cin >> var1;
        if(var1 == 0){
            exit(0);
        }
    do{
        cout << fixed;
        cout << setprecision(2);
        cout << "Enter any number: ";
        cin >> var2;
        if(var2 == 0){
            cout << endl << var1;
            break;
        }
        var1 += var2;
    }while (1);
    getch();
    return 0;
}
int sub(){
        cout << "\n\nEnter '0' to End Subtraction";
        double var1 = 0 , var2 = 0;
        cout << "\nEnter any number: ";
        cin >> var1;
        if(var1 == 0){
            exit(0);
        }
    do{
        cout << fixed;
        cout << setprecision(2);
        cout << "Enter any number: ";
        cin >> var2;
        if(var2 == 0){
            cout << endl << var1;
            break;
        }
        var1 -= var2;
    }while (1);
    getch();
    return 0;
}
int div(){
        cout << "\n\nEnter '0' to End Division";
        double var1 = 0 , var2 = 0;
        cout << "\nEnter any number: ";
        cin >> var1;
        if(var1 == 0){
            exit(0);
        }
    do{
        cout << fixed;
        cout << setprecision(2);
        cout << "Enter any number: ";
        cin >> var2;
        if(var2 == 0){
            cout << endl << var1;
            break;
        }
        var1 /= var2;
    }while (1);
    getch();
    return 0;
}
int multi(){
        cout << "\n\nEnter '0' to End Multiplication";
        double var1 = 0 , var2 = 0;
        cout << "\nEnter any number: ";
        cin >> var1;
        if(var1 == 0){
            exit(0);
        }
    do{
        cout << fixed;
        cout << setprecision(2);
        cout << "Enter any number: ";
        cin >> var2;
        if(var2 == 0){
            cout << endl << var1;
            break;
        }
        var1 *= var2;
    }while (1);
    getch();
    return 0;
}

int main(){
	char choice;
    do{
        system ("color B");
        printf("\nMenu");
        printf ("\n\n0. Exit                    press '0' to Exit");
        printf("\n+. Addition                press '+' for Addition");
        printf("\n-. Subtraction             press '-' for Subtraction");
        printf("\n/. Division                press '/' for Division");
        printf("\nx. Multiplication          press 'x' for Multiplication");

        printf("\n\nEnter your choise: ");
        scanf ("%c" , &choice);

            if (choice == '+'){
                add();
            }else if (choice == '-'){
                sub();
            }else if (choice == '/'){
                div();
            }else if(choice == 'x'){
                multi();
            }else if (choice == '0'){
                exit(0);
            }
            system("cls");
    }while (1);
    return 0;
}
