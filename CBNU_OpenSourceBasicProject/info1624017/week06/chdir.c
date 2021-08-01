#include <stdio.h>
#include <sys/stat.h>

void main(int argc, char *argv[]) {
   struct stat buf;
   char *ftype;

   for(int i=1; i<argc; i++) {
      printf(“%s: “, argv[i];
      lstat(argv[i], &buf);
      if (S_ISREG(buf.st_mode)) ftype = “regular”;
      else if (S_ISDIR(buf.st_mode)) ftype = “directory”;
      else ftype = “other file type”;
      printf(“%s\n”, ftype);
   }
}

