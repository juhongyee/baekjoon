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
int top = -1;
int** maze,**mark;
int EXIT_ROW, EXIT_COL;
bool found = false;

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
	return top < 0;
}
int IsFull()
{
	return (top >= (MAX_STACK_SIZE - 1));
}

void push(element item)
{
	if (IsFull())
	{
		printf("stack full\n");
	}
	
	stack[++top] = item;
}

element pop()
{
	if (IsEmpty())
	{
		printf("stack X\n");
	}

	return stack[top--];
}

int main()
{
	arrange_move();
	scan_maze();

	path();
	if (found)
		printf("%d", top + 3);
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

	mark[1][1] = 1;
	top = 0;
	stack[0].row = 1; stack[0].col = 1; stack[0].dir = 1;

	while (top > -1 && !found) {
		position = pop();
		row = position.row;
		col = position.col;
		dir = position.dir;

		while (dir < 4 && !found) {
			nextRow = row + move[dir].vert;
			nextCol = col + move[dir].horiz;

			if (nextRow == EXIT_ROW && nextCol == EXIT_COL)
				found = true;
			else if (maze[nextRow][nextCol] && !mark[nextRow][nextCol])
			{
				mark[nextRow][nextCol] = 1;
				position.row = row;
				position.col = col;
				position.dir = ++dir;
				push(position);
				row = nextRow; col = nextCol; dir = 0;
			}
			else ++dir;
		}
	}
}