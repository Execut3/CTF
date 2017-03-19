python generator.py $1
chmod -R 700 .

for i in `seq 0 $(($1-1))`
do
	file=$RANDOM
	gcc team$i/rev300.c -oteam$i/r300$file -s
	echo 'INSERT INTO `rev300` (`teamID`, `file`) VALUES ('$(($i+1))', '"'"'http://file.0xdeffbeef.com/r300'$file"'"');' >> rev300.sql
done
