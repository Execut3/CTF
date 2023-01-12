#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//wh4t[]s0r7_0F{}fL4g!is@th1s
char *key = "vi5uZ\\r1s6^1Gz|gM5f hrAui0r";

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
		fail("Your password is your password, i want mine :)");
	
	for(i=0;i<strlen(key);i++)
		if((key[i]^0x01) != a[i])
			fail("Nah, it wont work :(");
			
	puts("Helal kenkz, flag bu :)");
	
	return 0;
}
