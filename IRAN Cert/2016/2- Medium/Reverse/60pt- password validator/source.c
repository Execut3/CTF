#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *key = "\x40\x51\x40\x42\x55\x47\x7a\x4e\x6a\x35\x78\x5e\x42\x69\x68\x32\x67\x5e\x54\x66\x31\x75\x5e\x6c\x64\x5e\x60\x66\x60\x68\x6f\x7c";

void fail(char *s)
{
	puts(s);
	exit(1);
}

int main()
{
	char a[30];
	int i;
	
	scanf("%s", a);
	if(strlen(a) != strlen(key))
		fail("Sorry, But the provied password is not the same length as FLAG!");
	
	for(i=0;i<strlen(key);i++)
		if((key[i]^0x01) != a[i])
			fail("Sorry, But It's not the Password that i expected");
			
	printf("Nice job, Flag is %s\n", &a);
	
	return 0;
}
