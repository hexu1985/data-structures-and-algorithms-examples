CC = gcc
CFLAGS = -g3 -Wall -Wextra
LDFLAGS = 
LDLIBS = 

PROGS =	testlist

.PHONY: all
all: $(PROGS)
	@echo "build OK!"

clean:
	@$(RM) $(PROGS) *.o
	@echo "clean OK!"

testlist: testlist.o list.o
	$(CC) -o $@ $^ $(LDFLAGS) $(LDLIBS)


