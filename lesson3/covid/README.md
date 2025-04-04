# Mathematical Modeling of Infectious Disease

* [COVID-19](https://en.wikipedia.org/wiki/COVID-19)
* [Fast Grants](https://en.wikipedia.org/wiki/Fast_Grants)
* [Mathematical models](https://en.wikipedia.org/wiki/Mathematical_modelling_of_infectious_disease) can project how [infectious diseases](https://en.wikipedia.org/wiki/Infection) progress to show the likely outcome of an [epidemic](https://en.wikipedia.org/wiki/Epidemic) and help inform public health interventions
* Models use some basic assumptions and mathematics to find parameters for various infectious diseases and use those parameters to calculate the effects of different interventions such as mass [vaccination](https://en.wikipedia.org/wiki/Vaccination) programs
* Trained as a physician, [Daniel Bernoulli](https://en.wikipedia.org/wiki/Daniel_Bernoulli) 1700—1782 created a mathematical model to defend the practice of inoculating against [smallpox](https://en.wikipedia.org/wiki/Smallpox) in 1766
* A simple epidemic models describes the relationship between susceptible, infected, and immune individuals in a population, P = (R<sup>N</sup>-1)/2
* The [basic reproduction number](https://en.wikipedia.org/wiki/Basic_reproduction_number) R of an infection is the expected number of cases directly generated by one case in a population where all P individuals are susceptible to infection, and the [serial interval](https://en.wikipedia.org/wiki/Serial_interval) S is the time between successive cases in a chain of N = log<sub>R</sub>(2P+1) generations to infect the entire population
* For the [US population](https://www.worldometers.info/world-population/us-population/) P = 333 938 907, R = 3, S = 4 days, it takes approximately 74 days to infect the whole population

```sh
$ python3
>>> import math
>>> math.log(2*333938907+1,3)
18.495711373962646
>>> 4*math.log(2*333938907+1,3)
73.98284549585058
>>> exit()
$ cd ~/iot/covid
$ python3 covid.py 334193280 3 4
Population      = 334193280
Infection rate  = 3
Serial interval = 4
Time to infect  = 73.98561788488546
$ python3 covid-19.py
Enter population: 334233448
Enter infection rate: 3
Enter serial interval: 4
Time to infect: 73.98605547946643
$ 
```
