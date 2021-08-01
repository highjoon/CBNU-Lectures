#include <stdio.h>
 
main()
 {
     int i, cnt, sum=0, avg=0;
     int max = 0, min=1;
     int in[100];
    
     printf("정수 개수 입력");
     scanf("%d",&cnt);

     for(i=1;i<=cnt;i++)
     { 
        
         scanf("%d",&in[i]);
         sum+=in[i];
         if(in[i]>max)
             max=in[i];
         if(in[i]<min)
             min=in[i];
    }
    sum=max+min;
    avg=sum/(cnt-2);
    printf("최대값 : %d, 최소값 : %d, 합계 : %d, 평균 : %d",max,min,sum,avg);     
     
 }
