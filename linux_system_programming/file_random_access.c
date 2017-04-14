#include <fcntl.h>
#include <unistd.h>

struct myrecord {
    int id;
    char name[50];
};


void main()
{
    int fd, size = sizeof(struct myrecord);
    struct myrecord info;

    if ((fd = open("comp3410_datafile", O_RDWR)) < 0) {
	perror("comp3410_datafile");
	exit(1);
    }
    lseek(fd, size, SEEK_SET);
    read(fd, &info, size);

    info.id = 999;
    lseek(fd, -size, SEEK_CUR);
    write(fd, &info, size);

    close(fd);

}


