#include<stdio.h>

#include<string.h>

#include<stdlib.h>

#include<time.h>

int main()
{


char R[]={'R', 'P','S'},UI,Comp;

int user=0,comp = 0,random;

printf("Enter \n R for rock \n P for Paper \n S for scissors \n E to exit");

while(UI!='E')
{
    system("clear");
    printf("\nEnter your choice:\n");
    scanf(" %c",&UI);
    srand(time(NULL));
    random=rand()%3;
    Comp = R[random];
    //printf("Your cholce %c\nComputers choice %c\n",UI,Comp);
    if(((UI=='R')&&(Comp=='S'))||((UI=='S')&&(Comp=='P'))||((UI=='P')&&(Comp=='R')))
    {
    user++;

    printf("Your choice %c\nComputers chotce %c\n", UI, Comp);

    printf("You got a point");
    printf("\n**************************************\n");
    printf("Your score: %d\nOpponents Score: %d",user,comp);
    }
    if(((UI=='S')&&(Comp=='R'))||((UI=='P')&&(Comp=='S'))||((UI=='R')&&(Comp=='P')))
    {
    comp++;

    printf("Your choice %c\nComputers choice %c\n", UI, Comp);
    printf("Opponent got a point");
    printf("\n**************************************\n");
    printf("Your score: %d\nOpponents Score: %d",user,comp);


    }

    if(UI==Comp)
    continue;
    }
    if(user>comp)

    printf("\nYou wins");

    else if(comp>user)
    printf("\nOpponent win");
    else
    printf("Game draw \n");
    } 
    