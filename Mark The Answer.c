#include <stdio.h>
 
int main()
{
   unsigned int N,count=0,marks=0,q;
    unsigned int X;
    scanf("%d",&N);
    scanf("%d",&X);
    for(int i=0;i<N;i++){
        scanf("%d",&q);
        if(q>X){
            count++;
        }
        if(count==2){
            break;
        }
        marks++;
    }
    if(count==0){
        printf("%d",marks);
    }
    else{
        printf("%d",marks-1);
    }
    return 0;
}