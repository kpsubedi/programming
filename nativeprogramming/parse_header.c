#include <stdio.h>
#include <stdlib.h>
#include <mach-o/loader.h>
#include <mach-o/swap.h>

void dump_segments(FILE *);
uint32_t read_magic(FILE *, int);


int main(int argc, char **argv) {
    const char *inputfile = argv[1];
    FILE *obj_file = fopen(inputfile, "rb");
    dump_segments(obj_file);
    fclose(obj_file);

    return 0;
}

void dump_segments(FILE *obj_file) {
    uint32_t magic = read_magic(obj_file, 0);
    printf("Magic: %x\n", magic);
}

uint32_t read_magic(FILE *obj_file, int offset){
    uint32_t magic;
    fseek(obj_file, offset, SEEK_SET);
    fread(&magic, sizeof(uint32_t), 1, obj_file);
    return magic;
}
