#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char** argv){
    int c;
    while( (c=getchar()) != EOF ){
        if(c >=32) c = c ^ 1;
	putchar(c);
}

return EXIT_SUCCESS;
}

$ gcc test.c -o test
$ cat test.c | ./test | ./test

