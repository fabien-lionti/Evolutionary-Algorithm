import numpy as np

class particle:

    def __init__(self, **parameters_range):
        self.parameters = parameters_range
        self.best_position = None
        self.position = self.init_position()
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
        if p_best < self.best_position or self.best_position == None :
            self.best_position = p_best
            return

        #  v[] = v[] + c1 * rand() * (pbest[] - present[]) + c2 * rand() * (gbest[] - present[]) (a)
        # present[] = persent[] + v[] (b)
    def update_position(self, c1, c2, g_best, p_best):
        rand1 = np.random.uniform(0, 1)
        rand2 = np.random.uniform(0, 1)
        self.update_best_position(p_best)
        self.velocity = self.velocity + c1 * rand1 * (self.best_position - self.position) \
                        + c2 * rand2 * (g_best - self.position)
        self.position = self.position + self.velocity
        return

    def get_position(self):
        return self.position

class PSO :

    def __init__(self, c1, c2, nb_iteration, nb_particle, **parameters_range):
        self.c1 = c1
        self.c2 = c2
        self.nb_iteration = nb_iteration
        self.nb_particles = nb_particle
        self.parameters_range = parameters_range
        self.particles =
        return

    def init_particle(self, **parameters_range):
        return [particle for i in range(self.nb_particles)]

np.random.uniform(0, 1)

p = particle(max_velocity=10, sigma=(0,10), truc=(1,10))
print(p.get_position())

p.random_walk()
print(p.get_position())

p.random_walk()
print(p.get_position())
