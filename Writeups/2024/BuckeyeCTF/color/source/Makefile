all: clean color

dist: clean color
	zip export.zip color color.c Makefile Dockerfile

color: color.c
	gcc -w color.c -o color

clean:
	rm -f color export.zip
