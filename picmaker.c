#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>

int main(){
    
    int fd = open("image.ppm", O_CREAT | O_RDWR);
    
    char buff1[100];
    strcpy(buff1, "P3\n500 500\n255\n");
    write(fd, buff1, sizeof(buff1));
    
    for(int x = 0; x < 500; x++){
        int buff[1500];
        for(int y = 0; y < 1500; y++){
            buff[y] = 100;
        }
        write(fd, buff, sizeof(buff));
    }
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    return 0;
}
