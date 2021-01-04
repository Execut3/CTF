#include <stdio.h>
#include <string.h>

int main()
{
	char inp[128], *pass = "APACTF{Ok4y_u_know_r3v3r53_bas!cs}";
	int i=0;
	
	printf("Please provide the serial number:");
	while(i<128)
	{
		if(scanf("%c", &inp[i])==EOF)
			break;
		if(inp[i]=='\n' || inp[i]=='\r' || inp[i]==0)
			break;
		i++;
	}
	inp[i] = 0;
	
	if(!strcmp(inp, pass))
		printf("Flag is %s\n", pass);
	else
		puts("Sorry... Serial number is invalid.");
	return 0;
}

