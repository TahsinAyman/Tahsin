#include <stdio.h>
#include<time.h>

static void delay(long milliseconds){
    milliseconds += clock();
    while( clock() < milliseconds);
}

void Grettings(char * msg, int sec, int isCount){
	char ch[] = {'/','|','\\','-'};
	int j=0;
	if(isCount)
		for(int i=sec*10; i>=0; i--){
			printf("%s %2d\r",msg,i);
			delay(100);
		}
	else
		for(int i=0; i<=sec*10; i++){		
			if(i%4 == 0)
				j = 0;
			printf("%s %c\r",msg,ch[j++]);
			delay(100);
		}
}

void progressBar(int times){
	delay(100);
	printf("%c", 219);
	if(times-->0)progressBar(times);	
}

int timer(int time){
	for (time; time>=0; time--){
		printf ("\r%9d" , time);
		delay (1000);
	}
	printf ("%c" , 7);
	printf ("\n");
	return 0;
}