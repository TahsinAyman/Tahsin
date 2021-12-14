#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

typedef struct
{
    int id;
    char name[20];
}Student;

FILE *fp;
Student s;
Student std;

void readStudent();
void saveStudent();
void delStudent();
void updateStudent();
int  dupicateStudentIDcheck(int id);

int fileMain()
{
    int c;

    do{
        printf ("0. Exit\n");
        printf ("1. Create Student\n");
        printf ("2. List of Student\n");
        printf ("3. Delete Student Info\n");
        printf ("4. Update Student Information\n\n");

        printf ("Enter choice: ");
        scanf ("%d" , &c);

        system ("cls");

        switch(c)
        {
            case 1:
                saveStudent();
                break;

            case 2:
                readStudent();
                break;
            case 3:
                delStudent();
                break;
            case 4:
                updateStudent();
                break;
            case 0:
                exit(0);
                break;

            default:
                printf ("Error! your choice was wrong");
                printf ("\nPress any key to Exit...");
                getch();

        }
        system("cls");
    }while(!c == 0);
    return 0;
}

void readStudent()
{
        int c;

        printf ("Enter Authorizer code: ");
        scanf ("%d" , &c);


        fp = fopen("file.txt" , "r");

        if(c == 2569)
        {
            while(fread(&std , sizeof(std) , 1 , fp))
            {
                printf ("ID: %d\nName:%s\n\n" , std.id , std.name);
            }
        }
        else
        {
            printf ("Wrong Authorizer code");
        }
        fclose(fp);
        printf ("\nPress any key to Exit...");
        getch();
}

void saveStudent()
{

        printf("\n\nEnter ID: ");
        scanf ("%d" , &s.id);

        if (dupicateStudentIDcheck(s.id))
        {
            printf ("Error! Duplicate Student ID");
        }
        else
        {
            fp = fopen("file.txt" , "a");

            fflush(stdin);
            printf("Enter name: ");
            scanf("%[^\n]s" , &s.name);
            fwrite(&s , sizeof(s) , 1 ,  fp);

            fclose(fp);
        }

    printf ("\nPress any key to Exit...");
    getch();

}

void delStudent()
{
    int id;
    int c;

    printf ("Enter Authorizer code: ");
    scanf ("%d" , &c);
    printf ("\n");

    if (c == 2569)
    {
        printf ("Enter Student ID to delete: ");
        scanf ("%d" , &id);

        fp = fopen("file.txt" , "r");
        FILE *fptemp = fopen("TempFile.txt" , "w");

        while(fread(&std , sizeof(std) , 1 , fp))
        {
            if (id != std.id)
            {
                fwrite(&std , sizeof(std) , 1 ,  fptemp);
            }
        }
        fclose(fptemp);
        fclose(fp);

        fptemp = fopen("TempFile.txt" , "r");
        fp = fopen("file.txt" , "w");

        while(fread(&std , sizeof(std) , 1 , fptemp))
        {
             fwrite(&std , sizeof(std) , 1 , fp);
        }

        fclose(fptemp);
        fclose(fp);

        system ("del TempFile.txt");
    }
    else
    {
        printf ("Wrong Authorizer Code");
    }

}

void updateStudent()
{
    int id;

    printf ("Enter Student ID to Update: ");
    scanf ("%d" , &id);

    fp = fopen("file.txt" , "r");
    FILE *fptemp = fopen("TempFile.txt" , "w");

    while(fread(&std , sizeof(std) , 1 , fp))
    {
        if (id == std.id)
        {
            fflush(stdin);
            printf ("Enter name: ");
            scanf ("%[^\n]s" , &std.name);
        }
        fwrite(&std , sizeof(std) , 1 ,  fptemp);
    }
    fclose(fptemp);
    fclose(fp);

    fptemp = fopen("TempFile.txt" , "r");
    fp = fopen("file.txt" , "w");

    while(fread(&std , sizeof(std) , 1 , fptemp))
    {
         fwrite(&std , sizeof(std) , 1 , fp);
    }

    fclose(fptemp);
    fclose(fp);

}

int dupicateStudentIDcheck(int id)
{
    int found = 0;

    fp = fopen("file.txt" , "r");

    while(fread(&std , sizeof(std) , 1 , fp))
    {
        if (id == std.id)
        {
            found = 1;
        }
    }
    fclose(fp);
    return found;
}
