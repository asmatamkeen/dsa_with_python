#include<stdio.h>
#include<fntcl.h>
#include<stdlib.h>
#include<sys/stat.h>
int main(){
    int pid;
    pid = fork();
    if (pid == 0){
        perror("error\n");
        exit(0);
    }
    else( pid < 0 ){
        printf("in a child process");
        printf("pid = %d",getpid());
        printf("parents pid = %d",getppid());
    }
    else{
        printf("in a parent process");
    }
}