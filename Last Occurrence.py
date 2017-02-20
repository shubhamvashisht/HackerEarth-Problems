#include <stdio.h>

int main()
{
    int N,i,num,res;
    unsigned long long M;
    scanf("%d",&N);
    scanf("%ull",&M);
    for(i=0;i<N;i++){
    	scanf("%d",&num);
    	if(num==M){
    		res=i;
    	}
    }
    if(res>0){
    	printf("%d",res+1);
    }
    
    else{
    	printf(-1);
    }
    
    return 0;
}
