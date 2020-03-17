import numpy as np

class particle:

    def __init__(self, **parameters_range):
        self.parameters = parameters_range
        self.position = self.init_position()
        self.best_position = self.position
        self.fitness = None
        self.velocity = None
        return

    def init_position(self):
        n = len(self.parameters)
        labels = self.parameters.keys()
        position = np.zeros(n)
        for i in enumerate(labels):
            min = self.parameters[i[1]][0]
            max = self.parameters[i[1]][1]
            position[i[0]] = np.random.uniform(min, max)
        return position

    def update_best_position(self, p_best):
        if p_best < self.best_position:
            self.best_position = p_best
            return

        #  v[] = v[] + c1 * rand() * (pbest[] - present[]) + c2 * rand() * (gbest[] - present[]) (a)
        # present[] = persent[] + v[] (b)
    def update_position(self, c1, c2, g_best):
        rand1 = np.random.uniform(0, 1)
        rand2 = np.random.uniform(0, 1)
        self.update_best_position()
        self.velocity = self.velocity + c1 * rand1 * (self.best_position - self.position) \
                        + c2 * rand2 * (g_best - self.position)
        self.position = self.position + self.velocity
        return

    def get_position(self):
        return self.position

    def set_fitness(self,fitness):
        self.fitness = fitness

class PSO :

    def __init__(self, fitness_function, c1, c2, nb_iteration, nb_particle, **parameters_range):
        self.c1 = c1
        self.c2 = c2
        self.nb_iteration = nb_iteration
        self.nb_particles = nb_particle
        self.parameters_range = parameters_range
        self.particles = self.init_particle(**parameters_range)
        self.fitness_function = fitness_function
        self.g_best_index = None
        self.score = None
        return

    def init_particle(self, **parameters_range):
        return [particle(**parameters_range) for i in range(self.nb_particles)]

    def update_fitness(self):
        self.score = np.array([self.fitness_function(self.particles[i].get_position()) for i in range(self.nb_particles)])
        for i in range(self.nb_particles) : self.particles[i].set_fitness(self.score[i])
        return

    def update_global_best(self):
        self.g_best_index = np.argmax(self.score)
        return

    def fit(self):
        for i in range(self.nb_iteration):
            self.update_fitness()
            self.update_global_best()
            global_best_position = self.particles[self.g_best_index].get_position()
            self.particles[i].update_position(self.c1, self.c2, global_best_position, )
        return

def fitness(variables):
    x = variables[0]
    return x**2

pso = PSO(fitness_function = fitness ,c1 = 1,c2 = 1, nb_iteration = 1,nb_particle = 10, sigma = (10,15))
pso.update_global_best()