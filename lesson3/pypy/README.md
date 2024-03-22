# PyPy

* [PyPy](https://en.wikipedia.org/wiki/PyPy)
* [Just-in-time (JIT) compilation](https://en.wikipedia.org/wiki/Just-in-time_compilation)
* [Ouroboros](https://en.wikipedia.org/wiki/Ouroboros)
* [Self-reference](https://en.wikipedia.org/wiki/Self-reference)
  * [Douglas Hofstadter](https://en.wikipedia.org/wiki/Douglas_Hofstadter), *[Gödel, Escher, Bach](https://en.wikipedia.org/wiki/G%C3%B6del,_Escher,_Bach) (GEB): an Eternal Golden Braid&mdash;a Metaphorical [Fugue](https://en.wikipedia.org/wiki/Fugue) on Minds and Machines in the Spirit of [Lewis Carroll](https://en.wikipedia.org/wiki/Lewis_Carroll)*, 1979
    * Proposed and discussed the concept of a [strange loop](https://en.wikipedia.org/wiki/Strange_loop) to demonstrate how the properties of self-referential systems such as [Gödel's incompleteness theorems](https://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems) can be used to describe the unique properties of minds that animate beings can come out of inanimate matter
  * Douglas Hofstadter, *[I Am a Strange Loop](https://en.wikipedia.org/wiki/I_Am_a_Strange_Loop)*, 2007
* [Paradox](https://en.wikipedia.org/wiki/Paradox)
  * [Chicken or the egg](https://en.wikipedia.org/wiki/Chicken_or_the_egg)
  * [Bootstrapping](https://en.wikipedia.org/wiki/Bootstrapping)
  * [Catch-22 (logic)](https://en.wikipedia.org/wiki/Catch-22_(logic))
* [Profiling](https://en.wikipedia.org/wiki/Profiling_(computer_programming))

Most Python code runs well on PyPy except for code that depends on [CPython](https://en.wikipedia.org/wiki/CPython) extensions, which either does not work or incurs some overhead when run in PyPy.

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
