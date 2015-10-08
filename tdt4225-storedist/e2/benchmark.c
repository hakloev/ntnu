#include <sys/types.h>
#include <sys/stat.h> /* struct stat */
#include <sys/time.h> /* gettimeofday etc */
#include <fcntl.h> /* fcntl, fflush etc */
#include <unistd.h> 
#include <stdio.h> 
#include <errno.h> 
#include <string.h> /* printf etc */
#include <math.h> /* Pow operator */

/* For preprocessoring */ 
#define ONE_GIGABYTE pow(1024, 3) /* Size of one GB in B */ 
#define FILENAME "data.out"

/* Global variables */ 
struct stat fi;
blksize_t BLOCKSIZE; /* Keeps the blocksize for the current filesystem */

/* Functions */
void print_time_for_interval(struct timeval *start, struct timeval *end, int gb); 
void seq_write(int gb);

int main(int argc, char** argv) {
	stat("/", &fi); /* System stat struct for root */
	BLOCKSIZE = fi.st_blksize; /* Set filesystem blocksize */

	printf("HFS Plus\t Throughput\t Time\n"); 
	printf("---------------------------------\n");
	
	for (int i = 0; i < 6; i++) {
		seq_write(pow(2, i));
	}

	unlink(FILENAME); /* Delete the file after all files written, since we are done with it */
}

void seq_write(int gb) {
	struct timeval start, end;
	FILE *fp; 
	char block[BLOCKSIZE];
	memset(block, '#', BLOCKSIZE);
	
	int length = (gb * ONE_GIGABYTE) / BLOCKSIZE;

	fp = fopen(FILENAME, "w+"); 
	gettimeofday(&start, NULL);
	for (int i = 0; i < length; i++) {
		fwrite(block, BLOCKSIZE, 1, fp);
	}
	gettimeofday(&end, NULL);
	fclose(fp);	

	print_time_for_interval(&start, &end, gb);
}

void print_time_for_interval(struct timeval *start, struct timeval *end, int gb) {
	double time_in_ms; 
	long start_t = start->tv_sec * 1000000 + start->tv_usec;
	long end_t = end->tv_sec * 1000000 + end->tv_usec;;
	time_in_ms = ((end_t - start_t) / 1000000.0) * 1000.0 ;
	printf("%2d GB\t %3d MB/s\t %5d ms\n", gb, (int)(gb * (1000*1000) / (time_in_ms)), (int)time_in_ms);
}
