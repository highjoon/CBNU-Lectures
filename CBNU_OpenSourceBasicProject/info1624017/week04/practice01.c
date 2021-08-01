#include <stdio.h>

void main() {

	void selectionSort(int arr[], int size) {
 		int minIndex;
		int i,j;
		for (i=0; i<size-1; i++) {
			minIndex=i;
			for (j=i+1; j<size; j++)
				if (arr[j] < arr[minIndex])
					minIndex = j;

		swap(&arr[i], &arr[minIndex]);
		}
	}
}

