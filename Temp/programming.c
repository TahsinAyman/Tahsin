#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#include<string.h>

char choice[] = "0";
char c[] = "0";

void Startup();
void cSetup();
void CppStartup();
void JavaStartup();
void PythonStartup();
void HtmlStartup();

int main() {
	Startup();
	return 0;
}

void Startup() {

	while (1)
	{
		printf("0. type \"Exit\" to Exit\n");
		printf("1. type \"C\" for doing C programming\n");
		printf("2. type \"C++\" for doing C++ programming\n");
		printf("3. type \"HTML\" for doing Java programming\n");
		printf("4. type \"Java\" for doing Java programming\n");
		printf("5. type \"Python\" for doing Python programming\n");
		printf("6. type \"Django\" for doing Django programming\n");
		printf("7. type \"Update\" for Updateing the Workspace\n");
		printf("8. type \"cmd\" for Opening Command prompt\n");
		printf("9. type \"Pulling\" for Pulling the changes of the workspace\n\n");

		printf("Enter your choice: ");
		scanf("%s", &c);

		system("cls");

		if (strcmp(c, "C") == 0)
		{
			cSetup();
		}
		else if (strcmp(c, "C++") == 0)
		{
			CppStartup();
		}
		else if (strcmp(c, "Java") == 0)
		{
			JavaStartup();
		}
		else if (strcmp(c, "Python") == 0)
		{
			PythonStartup();
		}
		else if (strcmp(c, "HTML") == 0)
		{
			HtmlStartup();
		}
		else if (strcmp(c, "Update") == 0) {
			system("Update.bat");
		}
		else if (strcmp(c, "Pulling") == 0) {
			system("Pulling.bat");
		}
		else if (strcmp(c, "Exit") == 0) {
			exit(0);
		}
		else if (strcmp(c, "Django") == 0) {
			system("code DJango\\");
		}
		else if (strcmp(c, "cmd") == 0) {
			system("cls");
			system("cmd");
		}
		else
		{
			printf("Error!");
			getch();
			system("cls");
			Startup();
		}
	}
}

void cSetup()
{
	while (1)
	{
		printf("1. type \"Back\" to go to the Main Menu\n");
		printf("2. type \"codeblocks\" to open with Codeblocks\n");
		printf("3. type \"vscode\" to open with Visual Studio code\n");
		printf("4. type \"notepad\" to open with Notepad\n");
		printf("5. type \"notepad++\" to open with Notepad++\n");
		printf("6. type \"Vim\" to open with Vim Editor\n");
		printf("7. type \"Nano\" to open with Nano Editor\n");
		printf("8. type \"Sublime\" to open with Sublime Editor\n\n");

		printf("Enter your choice: ");
		scanf("%s", &choice);

		if (strcmp(choice, "codeblocks") == 0)
		{
			system("codeblocks C\\App.c");
			exit(0);
		}
		else if (strcmp(choice, "vscode") == 0)
		{
			system("code C\\");
			exit(0);
		}
		else if (strcmp(choice, "notepad") == 0)
		{
			system("notepad C\\App.c");
			exit(0);
		}
		else if (strcmp(choice, "notepad++") == 0)
		{
			system("notepad++ C\\App.c");
			exit(0);
		}
		else if (strcmp(choice, "Vim") == 0) {
			system("start vim C\\");
			exit(0);
		}
		else if (strcmp(choice, "Nano") == 0) {
			system("start nano C\\App.c");
			exit(0);
		}
		else if (strcmp(choice, "Back") == 0) {
			system("cls");
			Startup();
		}
		else if (strcmp(choice, "Sublime") == 0)
		{
			system("sublime_text");
			exit(0);
		}
		else
		{
			printf("Error!");
			getch();
			system("cls");
			cSetup();
		}
	}
}

void CppStartup() {
	while (1)
	{
		printf("1. type \"Back\" to go to the Main Menu\n");
		printf("2. type \"codeblocks\" to open with Codeblocks\n");
		printf("3. type \"vscode\" to open with Visual Studio code\n");
		printf("4. type \"notepad\" to open with Notepad code\n");
		printf("5. type \"notepad++\" to open with Notepad++ code\n");
		printf("6. type \"Vim\" to open with Vim Editor\n");
		printf("7. type \"Nano\" to open with Nano Editor\n");
		printf("8. type \"Sublime\" to open with Sublime Editor\n\n");


		printf("Enter your choice: ");
		scanf("%s", &choice);

		if (strcmp(choice, "codeblocks") == 0)
		{
			system("codeblocks \"C++\\App.cpp\"");
			exit(0);
		}
		else if (strcmp(choice, "vscode") == 0)
		{
			system("code \"C++\"\\");
			exit(0);
		}
		else if (strcmp(choice, "notepad") == 0)
		{
			system("notepad \"C++\\App.cpp\"");
			exit(0);
		}
		else if (strcmp(choice, "notepad++") == 0)
		{
			system("notepad++ \"C++\\App.cpp\"");
			exit(0);
		}
		else if (strcmp(choice, "Vim") == 0) {
			system("start vim \"C++\\");
			exit(0);
		}
		else if (strcmp(choice, "Nano") == 0) {
			system("start nano \"C++\\App.cpp\"");
			exit(0);
		}
		else if (strcmp(choice, "Back") == 0) {
			system("cls");
			Startup();
		}
		else if (strcmp(choice, "Sublime") == 0)
		{
			system("sublime_text");
			exit(0);
		}
		else
		{
			printf("Error!");
			getch();
			system("cls");
			CppStartup();
		}
	}
}

void JavaStartup() {
	while (1)
	{
		printf("1. type \"Back\" to go to the Main Menu\n");
		printf("2. type \"eclipse\" to open with Eclipse IDE\n");
		printf("3. type \"vscode\" to open with Visual Studio code\n");
		printf("3. type \"IntelliJ\" to open with IntelliJ IDEA\n");
		printf("4. type \"notepad\" to open with Notepad++\n");
		printf("5. type \"notepad++\" to open with Notepad++\n");
		printf("6. type \"Vim\" to open with Vim Editor\n");
		printf("7. type \"Nano\" to open with Nano Editor\n");
		printf("8. type \"Sublime\" to open with Sublime Editor\n\n");

		printf("Enter your choice: ");
		scanf("%s", &choice);

		if (strcmp(choice, "eclipse") == 0)
		{
			system("eclipse");
			exit(0);
		}
		else if (strcmp(choice, "vscode") == 0)
		{
			system("code Java\\");
			exit(0);
		}
		else if (strcmp(choice, "notepad") == 0)
		{
			system("notepad Java\\src\\root\\App.java");
			exit(0);
		}
		else if (strcmp(choice, "notepad++") == 0)
		{
			system("notepad++ Java\\src\\root\\App.java");
			exit(0);
		}
		else if (strcmp(choice, "Vim") == 0) {
			system("start vim Java\\");
			exit(0);
		}
		else if (strcmp(choice, "Nano") == 0) {
			system("start nano Java\\src\\root\\App.java");
			exit(0);
		}
		else if (strcmp(choice, "IntelliJ") == 0) {
			system("idea64");
			exit(0);
		}
		else if (strcmp(choice, "Back") == 0) {
			system("cls");
			Startup();
		}
		else if (strcmp(choice, "Sublime") == 0)
		{
			system("sublime_text");
			exit(0);
		}
		else
		{
			printf("Error!");
			getch();
			system("cls");
			JavaStartup();
		}
	}
}

void PythonStartup()
{
	while (1)
	{
		printf("1. type \"Back\" to go to the Main Menu\n");
		printf("2. type \"vscode\" to open with Visual Studio code\n");
		printf("3. type \"notepad\" to open with Notepad code\n");
		printf("4. type \"notepad++\" to open with Notepad++ code\n");
		printf("5. type \"Vim\" to open with Vim Editor\n");
		printf("6. type \"PyCharm\" to open with PyCharm Editor\n");
		printf("7. type \"Nano\" to open with Nano Editor\n");
		printf("8. type \"Sublime\" to open with Sublime Editor\n\n");

		printf("Enter your choice: ");
		scanf("%s", &choice);

		if (strcmp(choice, "vscode") == 0)
		{
			system("code Python\\");
			exit(0);
		}
		else if (strcmp(choice, "notepad") == 0)
		{
			system("notepad Python\\root\\App.py");
			exit(0);
		}
		else if (strcmp(choice, "notepad++") == 0)
		{
			system("notepad++ Python\\root\\App.py");
			exit(0);
		}
		else if (strcmp(choice, "Vim") == 0) {
			system("start vim Python\\");
			exit(0);
		}
		else if (strcmp(choice, "Nano") == 0) {
			system("start nano Python\\root\\App.py");
			exit(0);
		}
		else if (strcmp(choice, "PyCharm") == 0)
		{
			system("pycharm64");
			exit(0);
		}
		else if (strcmp(choice, "Back") == 0) {
			system("cls");
			Startup();
		}
		else if (strcmp(choice, "Sublime") == 0)
		{
			system("sublime_text");
			exit(0);
		}
		else
		{
			printf("Error!");
			getch();
			system("cls");
			PythonStartup();
		}
	}
}

void HtmlStartup()
{
	while (1)
	{
		printf("1. type \"Back\" to go to the Main Menu\n");
		printf("2. type \"vscode\" to open with Visual Studio code\n");
		printf("3. type \"notepad\" to open with Notepad code\n");
		printf("4. type \"notepad++\" to open with Notepad++ code\n");
		printf("5. type \"Vim\" to open with Vim Editor\n");
		printf("6. type \"Nano\" to open with Nano Editor\n\n");
		printf("7. type \"Sublime\" to open with Sublime Editor\n\n");

		printf("Enter your choice: ");
		scanf("%s", &choice);

		if (strcmp(choice, "vscode") == 0)
		{
			system("code HTML\\");
			exit(0);
		}
		else if (strcmp(choice, "notepad") == 0)
		{
			system("notepad HTML\\App.html");
			exit(0);
		}
		else if (strcmp(choice, "notepad++") == 0)
		{
			system("notepad++ HTML\\App.html");
			exit(0);
		}
		else if (strcmp(choice, "Vim") == 0) {
			system("Temp\\vimhtml.bat");
			exit(0);
		}
		else if (strcmp(choice, "Nano") == 0) {
			system("start nano HTML\\App.html");
			exit(0);
		}
		else if (strcmp(choice, "Back") == 0) {
			system("cls");
			Startup();
		}
		else if (strcmp(choice, "Sublime"))
		{
			system("sublime_text");
			exit(0);
		}
		else
		{
			printf("Error!");
			getch();
			system("cls");
			PythonStartup();
		}
	}
}
