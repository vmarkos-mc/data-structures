#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <unistd.h>
#include <string.h>
 
#define SIZE 256
 
int main() {
    int shm_fd = shm_open("/demo_shm", O_CREAT | O_RDWR, 0666);
    ftruncate(shm_fd, SIZE);
 
    char *memory = mmap(0, SIZE, PROT_WRITE, MAP_SHARED, shm_fd, 0);
 
    // Store secret
    strcpy(&memory[100], "TOP_SECRET_PASSWORD");
 
    // Access flag (0 = deny)
    memory[50] = 0;
 
    printf("Victim: Secret stored. Access = DENIED\n");
 
    sleep(10); // give attacker time
 
    if (memory[50] == 1) {
        printf("Victim: Access GRANTED (!!!)\n");
    } else {
        printf("Victim: Access still DENIED\n");
    }
 
    shm_unlink("/demo_shm");
    return 0;
}