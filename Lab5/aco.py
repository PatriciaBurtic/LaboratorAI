import random

#HARTA

class World(object):
    def __init__(self, param):
        """
        :param cost_matrix: matricea de costuri
        :param noCities: numarul de orase
        initializam o matrice cu o cantitate initiala de feromon de 1/noCities^2
        """
        self.matrix = param["cost_matrix"]
        self.noCities = param["noCities"]
        self.pheromone = [[1 / (self.noCities * self.noCities) for j in range(self.noCities)] for i in range(self.noCities)]


#ALGORITM

class ACO(object):
    def __init__(self, param):
        """
        :param ant_count: numarul de furnici
        :param generations: numarul de generatii
        :param alpha: controleaza importanta urmei (cate furnici au mai trecut pe muchia respectiva)
        :param beta: controleaza importanta vizibilitatii (cat de aproape se afla următorul oras)
        :param rho: coeficient de degradare a feromonului
        :param q: intensitatea feromonului lasat de o furnica
        """
        self.Q = param["q"]
        self.rho = param["rho"]
        self.beta = param["beta"]
        self.alpha = param["alpha"]
        self.ant_count = param["ant_count"]
        self.generations = param["generations"]

    def _update_pheromone(self, World: World, ants: list):
        #pagina 38
        for i, row in enumerate(World.pheromone):
            for j, col in enumerate(row):
                World.pheromone[i][j] *= self.rho
                for ant in ants:
                    World.pheromone[i][j] += ant.pheromone_delta[i][j]

    def solve(self, World: World):
        best_cost = float('inf')
        best_solution = []
        for gen in range(self.generations):
            ants = [_Ant(self, World) for i in range(self.ant_count)]
            for ant in ants:
                for i in range(World.noCities - 1):
                    ant._select_next()
                
                ant.total_cost += World.matrix[ant.tabu[-1]][ant.tabu[0]] #adaugam si costul de a merge din ulimul oras pana la primul
                
                if ant.total_cost < best_cost:
                    print("--------------------------------------------------------------------")
                    print("Cost: "+str(ant.total_cost)+" \nPath: "+str(ant.tabu))
                    #tinem minte cea mai buna solutie
                    best_cost = ant.total_cost
                    best_solution = ant.tabu
                # update la feromon pentru o furnica
                ant._update_pheromone_delta()

            #update la feromon pentru o generatie
            self._update_pheromone(World, ants)

        return best_solution, best_cost



#FURNICILE

class _Ant(object):
    def __init__(self, aco, world):
        self.colony = aco
        self.World = world
        self.total_cost = 0.0 #lungimea (costul) turului efectuat de a k-a furnica
        self.tabu = []  # o lista care contine orasele in care furnica nu se mai poate deplasa, adica au fost deja vizitate
        self.pheromone_delta = []  # cantitatea unitara de feromoni lasata de a k-a furnica pe harta
        self.allowed = [i for i in range(world.noCities)]  # orasele nevizitate inca, adica permise
        self.eta = [[0 if i == j else 1 / world.matrix[i][j] for j in range(world.noCities)] for i in
                    range(world.noCities)]  # vizibilitatea din orasul i spre orasul j (1/dij)
        start = 0  # orasul de start
        self.tabu.append(start)
        self.current = start #orasul curent in care se afla furnica
        self.allowed.remove(start)

    def _select_next(self):
        #pagina 37
        sum = 0
        for i in self.allowed:
            sum += self.World.pheromone[self.current][i] ** self.colony.alpha * self.eta[self.current][i] ** self.colony.beta
        probabilities = [0 for i in range(self.World.noCities)]  # initializam probabilitatiile cu 0
        for i in range(self.World.noCities):
            if i in self.allowed: #daca i e permis
                probabilities[i] = self.World.pheromone[self.current][i] ** self.colony.alpha * self.eta[self.current][i] ** self.colony.beta / sum
        # selectam urmatorul oras cu ruleta probabilitatilor
        nextCity = 0
        rand = random.random()
        for i, probability in enumerate(probabilities):
            rand -= probability
            if rand <= 0:
                nextCity = i
                break

        self.allowed.remove(nextCity)
        self.tabu.append(nextCity)
        self.total_cost += self.World.matrix[self.current][nextCity] #recaluleaza costul total curent
        self.current = nextCity #orasul curent este setat cu cel selectat

    def _update_pheromone_delta(self):
        #pagina 40
        self.pheromone_delta = [[0 for j in range(self.World.noCities)] for i in range(self.World.noCities)]
        for x in range(1, len(self.tabu)):
            #Se calculează cantitatea unitară de feromoni lăsată de a k-a furnică pe muchia (ij)
            i = self.tabu[x - 1]
            j = self.tabu[x]
            self.pheromone_delta[i][j] = self.colony.Q / self.total_cost
            