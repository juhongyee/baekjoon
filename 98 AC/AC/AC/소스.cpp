#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_NUMFUNC 100010
#define MAX_ARR 400010
typedef struct node* nodePointer;

typedef struct node
{
	int key;
	nodePointer llink;
	nodePointer rlink;
};

short int R = 0;
short int error = 0;
char c[20];
nodePointer createNode(int item);
void dinsert(nodePointer node, nodePointer newnode);
void ddelete(nodePointer node);
void make_like_first(char* p, nodePointer d_list, char*arr_first);
void print_node(nodePointer d_list);
void freeList(struct node* head);

int main()
{
	int n;
	int num_arr;//배열 길이
	scanf("%d", &n);//전체 실행 횟수

	for (int k = 0; k < n; k++)
	{
		//char배열 p 초기화 해줘야 함
		char* p;
		p = (char*)malloc(sizeof(char) * MAX_NUMFUNC);

		scanf("%s", p);//명령어 함수
		scanf("%d", &num_arr);//배열길이 입력
		
		char* arr_first; //배열 입력을 위한 포인터
		nodePointer d_list;//doubly linked list에 저장

		d_list = (nodePointer)malloc(sizeof(node)); //headnode 만들기
		d_list->key = 0;
		d_list->llink = d_list;
		d_list->rlink = d_list;

		arr_first = (char*)malloc(sizeof(char) * MAX_ARR);

		scanf("%s", arr_first);

		for (int j = 0; j < num_arr; j++)
		{
			char* arr;
			arr = (char*)malloc(sizeof(char) * 10);
			if (j == 0)
			{
				strcpy(arr, strtok(arr_first, ","));//처음은 copy시 i를 1로
				char c[20];

				if (num_arr != 1) {
					for (int i = 1;; i++) {
						if (arr[i] == '\0') break;
						c[i - 1] = arr[i];
					}
				}
				else
				{
					for (int i = 1;; i++) {
						if (arr[i] == '\0') break;
						c[i - 1] = arr[i];
					}
				}
				nodePointer temp = createNode(atoi(c));
				dinsert(d_list, temp);
				free(arr);
			}
			else
			{
				strcpy(arr, strtok(NULL, ","));
				nodePointer temp = createNode(atoi(arr));
				dinsert(d_list, temp);
				free(arr);
			}
		}

		for (int i = 0;; i++)
		{
			if (p[i] == '\0') break;
			switch (p[i])
			{
			case 'R':
				R = !R;
				break;
			case 'D':
				ddelete(d_list);
				break;
			}
		}

		print_node(d_list);
		make_like_first(p,d_list,arr_first);//error, R 초기GHK
	}
}

nodePointer createNode(int item)
{
	nodePointer temp;
	temp = (nodePointer)malloc(sizeof(node));
	temp->key = item;
	temp->llink = NULL;
	temp->rlink = NULL;

	return temp;
}

void dinsert(nodePointer node, nodePointer newnode)
{
	if (node->llink->key != 0) {
		newnode->llink = node->llink;
		newnode->rlink = node;
		node->llink->rlink = newnode;
		node->llink = newnode;
	}
	else
	{
		node->llink = newnode;
		node->rlink = newnode;
		newnode->rlink = node;
		newnode->llink = node;
	}
}

void ddelete(nodePointer node)
{
	if (node->rlink->key==0)
	{
		error = 1;
	}
	else
	{
		if (R == 0)//앞에서 지움
		{
			nodePointer temp = node->rlink;
			node->rlink = node->rlink->rlink;
			node->rlink->llink = node;
			free(temp);
		}
		else
		{
			nodePointer temp = node->llink;
			node->llink = node->llink->llink;
			node->llink->rlink = node;
			free(temp);
		}
	}
}

void print_node(nodePointer d_list)
{
	if (error == 1)
	{
		printf("error\n");
		return;
	}
	if (R == 0)
	{
		printf("[");
		for (nodePointer w = d_list->rlink; w->key != 0; w = w->rlink) {
			printf("%d", w->key);
			if(w->rlink->key != 0)
				printf(",");
		}
		printf("]\n");
		return;
	}
	else
	{
		printf("[");
		for (nodePointer w = d_list->llink; w->key != 0; w = w->llink) {
			printf("%d", w->key);
			if (w->llink->key != 0)
				printf(",");
		}
		printf("]\n");
		return;
	}
}

void make_like_first(char* p, nodePointer d_list, char* arr_first)
{
	R = 0;
	error = 0;

	free(p);
	free(arr_first);

	/*for (nodePointer w = d_list->llink; d_list->key == 0; w = w->llink)
	{
		free(w);
	}*/
	freeList(d_list);
}

void freeList(struct node* head)
{
	struct node* tmp;

	head->rlink->llink = NULL;
	while (head != NULL)
	{
		tmp = head;
		head = head->llink;
		free(tmp);
	}

}