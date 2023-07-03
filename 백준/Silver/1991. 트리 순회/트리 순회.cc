#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>


typedef struct node {
	char key;
	struct node* left;
	struct node* right;
}node;

//node_pointer tree;

struct node* tree;


node* create(char ch)
{
	node* newnode;
	newnode = (node*)malloc(sizeof(node));
	newnode->key = ch;
	newnode->left = NULL;
	newnode->right = NULL;
	return newnode;
}


node* search(node* tree, char ch)
{
	if (!tree) return NULL;

	if (tree->key == ch) return tree;

	else {
	node* tmp = search(tree->left, ch);
	if (tmp != NULL) return tmp;
	return search(tree->right, ch);
}
}

//트리 주우이
void inorder(node* tree)
{
	if (tree) {
		inorder(tree->left);
		printf("%c", tree->key);
		inorder(tree->right);
	}
}

//트리 전위
void preorder(node* tree)
{
	if (tree) {
		printf("%c", tree->key);
		preorder(tree->left);
		preorder(tree->right);
	}
}

//트리 후위
void postorder(node* tree)
{
	if (tree) {
		postorder(tree->left);
		postorder(tree->right);
		printf("%c", tree->key);
	}
}

int main()
{
	node* parent;
	node* left;
	node* right;
	int n, i;
	scanf("%d", &n);
	getchar();

	for (i = 0; i < n; i++)
	{
		char x, y, z;


		scanf("%c %c %c", &x, &y, &z);
		getchar();

		
		if (i == 0) {
			parent = create(x);
			tree = parent;
		}
		//이후에
		else parent = search(tree, x);



		if (y != '.') {
			left = create(y);
			parent->left = left;
		}
		if (z != '.') {
			right = create(z);
			parent->right = right;
		}
	}

	preorder(tree); printf("\n");
	inorder(tree); printf("\n");
	postorder(tree); printf("\n");
	return 0;
}