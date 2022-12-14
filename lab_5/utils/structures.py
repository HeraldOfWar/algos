from heapq import heappop, heappush
from math import sqrt
from networkx import Graph


class AbstractNodeStorageClass:
    def __init__(self):
        self.nodes = []

    def get_first(self):
        return self.nodes.pop(0)

    def insert(self, node_number):
        self.nodes.append(node_number)

    def is_empty(self):
        return len(self.nodes) == 0


class Stack(AbstractNodeStorageClass):
    """
        Стек работает по принципу LIFO - первым возвращается
        последний добавленный элемент.
    """

    def get_first(self):
        return self.nodes.pop()


class Queue(AbstractNodeStorageClass):
    """
        Очередь работает по принципу FIFO - первым возвращается
        элемент, добавленный раньше всех.
    """

    pass


class DijkstraQueue(AbstractNodeStorageClass):
    """
        Очередь с приоритетом. Внутри метода get_first() выбирается
        узел с минимальным расстоянием distance от начального узла.
    """

    def __init__(self, distances):
        super().__init__()
        self.distances = distances

    def get_first(self):
        closest_node_distance, closest_node = heappop(self.nodes)
        return closest_node

    def insert(self, element):
        heappush(self.nodes, (self.distances[element], element))


class AStarQueue(AbstractNodeStorageClass):
    """
        Очередь с приоритетом для алгоритма А*.
        В методе get_first() выбирается узел, для которого минимальна
        сумма расстояния до начального узла и оценки расстояния
        (оценивается евклидова норма) до конечного узла.
    """

    def __init__(self, graph, distances, goal_node):
        super().__init__()
        self.graph = graph
        self.x_goal, self.y_goal = graph.nodes[goal_node]['position']
        self.distances = distances

    def calc_heuristic(self, node):
        x_node, y_node = self.graph.nodes[node]['position']
        estimated_distance_to_goal = sqrt(
            (x_node - self.x_goal) ** 2 +
            (y_node - self.y_goal) ** 2
        )
        return estimated_distance_to_goal

    def get_first(self):
        optimal_node_value, optimal_node = heappop(self.nodes)
        return optimal_node

    def insert(self, element):
        heappush(self.nodes,
                 (self.distances[element] +
                  self.calc_heuristic(element), element)
                 )