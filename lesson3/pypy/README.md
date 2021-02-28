# PyPy

Most Python code runs well on [PyPy](https://en.wikipedia.org/wiki/PyPy) except for code that depends on [CPython](https://en.wikipedia.org/wiki/CPython) extensions, which either does not work or incurs some overhead when run in PyPy.

```sh
$ gcc -o test test.c

$ time ./test

$ time pypy test.py

$ time python test.py

$ time python3 test.py

$ pypy -m cProfile test.py

$ python -m cProfile test.py

$ python3 -m cProfile test.py
```
