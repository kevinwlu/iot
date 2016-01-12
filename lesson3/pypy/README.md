$ gcc -o test test.c

$ time ./test

1000000.000000

real	0m0.071s

user	0m0.060s

sys	0m0.000s

$ time pypy test.py

1000000.0

real	0m0.400s

user	0m0.370s

sys	0m0.020s

$ time python test.py

1000000.0

real	0m4.102s

user	0m4.080s

sys	0m0.010s
