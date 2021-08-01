#include <stdio.h>

void main() {
	int i, begin, end, sum;


	printf("This program sums all integers between two numbers as well as two numbers.\n");
	printf("Insert two integers>> ");
	scanf("%d%d", &begin, &end);
	for (i=begin; i<end+1; i++) sum = sum + i;
	printf("sum from %d to %d is %d\n", begin, end, sum);
}
