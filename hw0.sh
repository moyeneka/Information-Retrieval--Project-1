#! /bin/bash

echo '---running'
for i in $1/*.html; do
	python3 "nltk test.py" $i $2;
done;

cd $2
cat * > alltokens.txt
sort alltokens.txt > alltokens_sorted.txt
uniq -c alltokens_sorted.txt > alltokens_count.txt
sort -n alltokens_count.txt > alltokens_count_s.txt



