import numpy as np

class particle:

    def __init__(self, fitness_function, **parameters_range):
        self.parameters = parameters_range
        self.fitness_function = fitness_function
        self.position = self.init_position()
        self.fitness = self.fitness_function(self.position)
        self.best_position = self.position
        self.global_best_position = None
        self.velocity = 0
        return

    def init_position(self):
        n = len(self.parameters)
        labels = self.parameters.keys()
        position = np.zeros(n)
        for i in enumerate(labels):
            min = self.parameters[i[1]][0]
            max = self.parameters[i[1]][1]
            position[i[0]] = np.random.uniform(min, max)
        #print("Position : "+str(position))
        return position

    def update_best_position(self):
        new_fitness = self.fitness_function(self.position)
        if self.fitness > new_fitness:
            self.best_position = self.position
        self.fitness = new_fitness
        return

    def update_position(self, c1, c2):
        rand1 = np.random.uniform(0, 1)
        rand2 = np.random.uniform(0, 1)
        self.velocity = self.velocity + c1 * rand1 * (self.best_position - self.position) \
                        + c2 * rand2 * (self.global_best_position - self.position)
        self.position = self.position + self.velocity
        self.update_best_position()
        return

    def get_position(self):
        return self.position

    def set_global_best_position(self, g_best):
        self.global_best_position = g_best

class PSO :

    def __init__(self, fitness_function, c1, c2, nb_iteration, nb_particle, **parameters_range):
        self.c1 = c1
        self.c2 = c2
        self.nb_iteration = nb_iteration
        self.nb_particles = nb_particle
        self.parameters_range = parameters_range
        self.fitness_function = fitness_function
        self.particles = self.init_particle(**parameters_range)
        self.g_best_index = None
        self.fitness = None
        return

    def init_particle(self, **parameters_range):
        return [particle(self.fitness_function,**parameters_range) for i in range(self.nb_particles)]

    def update_global_best_position(self):
        fitness = [self.particles[i].fitness for i in range(self.nb_particles)]
        self.g_best_index = np.argmin(fitness)
        return

    def set_global_best_position(self):
        self.update_global_best_position()                                      # Find index of the fittest particle
        global_best_position = self.particles[self.g_best_index].get_position() # Give the best position among swarm
        for i in range(self.nb_particles):                                      # Set for each particle the best
            self.particles[i].set_global_best_position(global_best_position)    # position found by the swarm
        return

    def update_particle_position(self):
        for i in range(self.nb_particles):
            self.particles[i].update_position(self.c1, self.c2)
        return

    def fit(self):
        res = {}
        for i in range(self.nb_iteration):
            self.set_global_best_position()
            self.update_particle_position()
            self.update_global_best_position()
        for i in enumerate(self.parameters_range.keys()):
           res[i[1]] = self.particles[self.g_best_index].get_position()[i[0]]
        return res

        #for j in range(self.nb_particles):
        #    print("j :" + str(j) +" : " + str(self.particles[j].fitness))
        #print("best index"+str(self.g_best_index))


def fitness(variables):
    x = variables[0]
    y = variables[1]
    return x**4+y**8

pso = PSO(fitness_function = fitness, c1 = 1, c2 = 1, nb_iteration = 10, nb_particle = 1000, sigma = (-100,100), beta = (-100,100))
res = pso.fit()
print(res)




