#include <stdio.h>
static inline double add_double(double a, double b) {
return a + b;
}

int main()
{
unsigned int i;
double a = 0.0;

for (i = 0; i < 1000000; i++) {
a += 1.0;
add_double(a, a);
}
printf("%f\n",a);
}
