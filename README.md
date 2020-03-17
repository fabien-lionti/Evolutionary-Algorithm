# Evolutionary-Algorithm
Evolutionary algorithm library

Test code : 

```python
def fitness(variables):
    x = variables[0]
    return x**4

pso = PSO(fitness_function = fitness, c1 = 1, c2 = 1, nb_iteration = 400, nb_particle = 1000, sigma = (-100,100))
res = pso.fit()
print(res)
```
