#include<stdio.h>
void judge(int Z,int number[]);
void printMAX(int number[]);

int main(){
	int i,n,N,Z,number[10]={0};
	scanf("%d",&n);
	for(i=0;i<n;i++){
		scanf("%d",&Z);
		judge(Z,number);
	}
	printMAX(number);
	return 0;
}

void judge(int Z,int number[]){
	if(Z==0) number[0]++;
	while(Z){
		number[Z%10]++;
		Z/=10;
	}
}

void printMAX(int number[]){
	int i,MAX=0;
	for(i=0;i<=9;i++){
		if(number[i]>MAX){
			MAX=number[i];
		}
	}
	printf("%d:",MAX);
	for(i=0;i<=9;i++){
		if(number[i]==MAX) printf(" %d",i);
	}
}
