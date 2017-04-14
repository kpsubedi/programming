#include <stdlib.h>
#include <fcntl.h>
#define BUFFSIZE 16384

void main()
{
    int fdin, fdout; /* INPUT and OUTPUT descriptors */
    char buff[BUFFSIZE];
    int count;

    if ((fdin = open("comp3410", O_RDONLY)) < 0) {
	perror("comp3410");
	exit(1);
    }
    if ((fdout = open("comp3410_copy", O_WRONLY | O_CREAT, 0644)) < 0 ) {
	perror("comp3410_copy");
	exit(2);
    }

    while ((count = read(fdin, buff, BUFFSIZE)) > 0)
	write(fdout, buff, count);

    close(fdin);
    close(fdout);
}

