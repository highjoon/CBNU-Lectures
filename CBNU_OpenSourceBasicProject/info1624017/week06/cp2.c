#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>

int main(int argc, char **argv)
{
    char ch;
    int src, dst;

    if (argc != 3)
    {
        printf("argument error\n");
        printf("usage: ./a.out src dest\n");
    }
    src = open(argv[1], O_RDONLY);
    dst = open(argv[2], O_WRONLY | O_CREAT | O_TRUNC, 0644);

    while (read(src, &ch, 1))
        write(dst, &ch, 1);

    close(src);
    close(dst);
    return 0;
}
