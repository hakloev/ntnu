CC=gcc

.PHONY: clean all

all : benchmark
	./benchmark

benchmark : benchmark.o
	$(CC) -o benchmark benchmark.o

benchmark.o : benchmark.c
	$(CC) -c -Wall -O2 benchmark.c
	
clean:
	-rm -rf *.o 
	-rm -rf benchmark

