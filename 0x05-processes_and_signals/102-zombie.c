#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - Loops indefinitely
 *
 * Return: Always 0
 */
int infinite_while(void)
{
	while (1)
		sleep(1);

	return (0);
}

/**
 * main - Creates 5 zombie processes
 *
 * Return: Always 0
 */
int main(void)
{
	int i = 5;
	pid_t zombie;

	while (i--)
	{
		zombie = fork();
		if (!zombie)
			return (0);

		printf("Zombie process created, PID: %d\n", zombie);
	}

	infinite_while();

	return (0);
}
