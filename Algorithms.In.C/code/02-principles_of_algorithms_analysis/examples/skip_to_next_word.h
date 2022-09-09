#ifndef SKIP_TO_NEXT_WORD
#define SKIP_TO_NEXT_WORD

#include <stdio.h>
#include <ctype.h>

inline void skip_to_next_word()
{
	while (!isspace(getchar()))
			;
}

#endif
