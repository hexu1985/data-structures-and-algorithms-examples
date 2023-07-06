CC = gcc
CFLAGS = -g3 -Wall -Wextra
LDFLAGS = 
LDLIBS = 

PROGS =	testlist teststkl

.PHONY: all
all: $(PROGS)
	@echo "build OK!"

clean:
	@$(RM) $(PROGS) *.o
	@echo "clean OK!"

testlist: testlist.o list.o
	$(CC) -o $@ $^ $(LDFLAGS) $(LDLIBS)

teststkl: teststkl.o stackli.o
	$(CC) -o $@ $^ $(LDFLAGS) $(LDLIBS)


