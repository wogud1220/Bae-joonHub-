
#define MAX(a,b) (((a)>(b))?(a):(b))
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main() {

	int x, y, z;
	scanf("%d",&x);
	scanf("%d",&y);
	scanf("%d",&z);
	if (x == y && x==z)printf("%d", 10000 + x * 1000);	//다 같을 때


	else if (x == y && x != z)
		printf("%d", 1000 + x * 100);
	else if (x == z && x != y)
		printf("%d", 1000 + x * 100);
	else if (y==z && x!=y)
		printf("%d", 1000 + y * 100);

	else if (x != y && x != z && y != z) {	//셋 다 다를 때
		int max = MAX(x, y);
		int max2 = MAX(max, z);
		printf("%d", max2 * 100);
	}

	return 0;
}