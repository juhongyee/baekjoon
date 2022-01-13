#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_STACK_SIZE 10000
typedef struct
{
	short int vert;
	short int horiz;

} offsets;

typedef struct
{
	short int row;
	short int col;
	short int dir;
}element;

offsets move[8];
element stack[MAX_STACK_SIZE];
int front = -1;
int rear = -1;
int** maze,**mark;
int EXIT_ROW, EXIT_COL;
bool found = false;
int check[101][101] = { 0 };

void arrange_move() {
	move[0].vert = 0;
	move[0].horiz = 1;
	move[1].vert = 1;
	move[1].horiz = 0;
	move[2].vert = 0;
	move[2].horiz = -1;
	move[3].vert = -1;
	move[3].horiz = 0;

}

void scan_maze();
void path();
int IsEmpty()
{
	return front==rear;
}
int IsFull()
{
	return (rear >= (MAX_STACK_SIZE - 1));
}

void push(element item)
{
	if (IsFull())
	{
		printf("queue full\n");
	}
	
	stack[++rear] = item;
}

element pop()
{
	if (IsEmpty())
	{
		printf("queue X\n");
	}

	return stack[++front];
}

int main()
{
	arrange_move();
	scan_maze();

	path();
	if (found) {
		printf("%d",check[EXIT_ROW][EXIT_COL]);
	}//이걸로 출력 예정
		
	free(maze);
	free(mark);
}

void scan_maze()
{
	int row, col;
	scanf("%d %d", &row, &col);
	EXIT_ROW = row;
	EXIT_COL = col;
	maze = (int**)calloc(row + 2, sizeof(int*));
	mark = (int**)calloc(row + 2, sizeof(int*));

	for (int i = 0; i < row + 2; i++)
	{
		maze[i] = (int*)calloc(col + 2, sizeof(int));
		mark[i] = (int*)calloc(col + 2, sizeof(int));
	}
	
	for (int i = 1; i <= row; i++)
	{
		char* temp;
		temp = (char*)malloc((col + 1) * sizeof(char));
		scanf("%s", temp);

		for (int j = 1; j <= col; j++)
		{
			maze[i][j] = temp[j - 1] - '0';
		}
		free(temp);
	}
}

void path()
{
	int row, col, nextRow, nextCol, dir;
	element position;
	int count = 1;

	mark[1][1] = 1;
	check[1][1] = 1;
	rear = 0;
	stack[0].row = 1; stack[0].col = 1; stack[0].dir = 0;

	while (!IsEmpty()&&!found) {
		position = pop();
		row = position.row;
		col = position.col;
		dir = position.dir;

		while (dir < 4 && !found) {
			nextRow = row + move[dir].vert;
			nextCol = col + move[dir].horiz;

			if (nextRow == EXIT_ROW && nextCol == EXIT_COL) {
				check[nextRow][nextCol] = check[row][col] + 1;
				found = true;
			}
			else if (maze[nextRow][nextCol] && !mark[nextRow][nextCol])
			{
				check[nextRow][nextCol] = check[row][col] + 1;
				mark[nextRow][nextCol] = 1;
				position.row = nextRow;
				position.col = nextCol;
				position.dir = 0;
				push(position);
				++dir;
			}
			else ++dir;
		}
	}
}