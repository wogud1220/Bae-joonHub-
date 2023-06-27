#define _CRT_SECURE_NO_WARNINGS
#define MAX(a,b) (((a)>(b))?(a):(b))
#define MAX_DEGREE 101
#include <stdio.h>
#include <string.h>
int main() {
	int x = 0;
	int y = 0;
	scanf("%d",&x);
	scanf("%d",&y);
	if (x > 0 && y > 0) printf("1");
	if (x > 0 && y < 0) printf("4");
	if (x < 0 && y > 0) printf("2");
	if (x < 0 && y < 0) printf("3");

	return 0;
}