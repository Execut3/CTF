# LFI1

## level: **easy** 

Simple old-school LFI challenge. I know it's Lame to see this kind of problems in real world now, but what if we DO!:)

```docker
docker build -t lfi1 .
docker run -d -p 8000:80 lfi1 
```

and access challenge through browser with this address: ```http://localhost:8000```