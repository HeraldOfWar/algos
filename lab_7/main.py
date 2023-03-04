from random import choice
from example import *
from lab_5.utils.generators import print_path

desk = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8',
        'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8',
        'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8',
        'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8',
        'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8',
        'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8',
        'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8',
        'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8']

figures = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']

figure_paths = {
    'pawn': graph_pawn,
    'knight': graph_knight,
    'bishop': graph_bishop,
    'rook': graph_rook,
    'queen': graph_queen,
    'king': graph_king
}

while True:
    start_node, target_node, *pawn_nodes = [choice(desk) for i in range(8)]
    if start_node != target_node and start_node not in pawn_nodes and target_node not in pawn_nodes \
            and int(start_node[1]) <= int(target_node[1]):
        print('Начальная точка:', start_node)
        print('Конечная точка:', target_node)
        print('Пешки:', pawn_nodes)
        break

f1, f2 = choice(figures), choice(figures)
print('Выбранные фигуры:', f1.capitalize(), f2.capitalize())
print()
figure_paths[f1](start_node), figure_paths[f2](start_node)

figure_paths = {
    'pawn': graph_for_pawn,
    'knight': graph_for_knight,
    'bishop': graph_for_bishop,
    'rook': graph_for_rook,
    'queen': graph_for_queen,
    'king': graph_for_king
}

f1_path, f2_path = figure_paths[f1], figure_paths[f2]

color = {}
dist = {}
parent = dict()
nodes_storage = []
nodes_storage.append(start_node)
dist[start_node] = 0
color[start_node] = 'white'
flag = False
path1 = ''
while nodes_storage:
    current_node = nodes_storage.pop(0)
    try:
        neighbours = list(f1_path[current_node])
    except KeyError:
        if current_node == target_node:
            print(f'{f1.capitalize()}:', end=' ')
            path1 = print_path(target_node, parent)
            flag = True
            break
        continue
    if current_node == target_node:
        print(f'{f1.capitalize()}:', end=' ')
        path1 = print_path(target_node, parent)
        flag = True
        break
    for node_to_go in neighbours:
        if node_to_go in pawn_nodes:
            continue
        if node_to_go not in color.keys():
            color[node_to_go] = 'grey'
            parent[node_to_go] = current_node
            dist[node_to_go] = dist[current_node] + 1
            nodes_storage.append(node_to_go)
        else:
            if dist[current_node] + 1 < dist[node_to_go]:
                dist[node_to_go] = dist[current_node] + 1
    color[current_node] = 'black'
if not flag:
    print(f'{f1.capitalize()} не может добраться до конечной точки!')

color = {}
dist = {}
parent = dict()
nodes_storage = []
nodes_storage.append(start_node)
dist[start_node] = 0
color[start_node] = 'white'
flag = False
path2 = ''
while nodes_storage:
    current_node = nodes_storage.pop(0)
    try:
        neighbours = list(f2_path[current_node])
    except KeyError:
        continue
    for node_to_go in neighbours:
        if current_node == target_node:
            print(f'{f2.capitalize()}:', end=' ')
            path2 = print_path(target_node, parent)
            flag = True
            break
        if node_to_go in pawn_nodes:
            continue
        if node_to_go not in color.keys():
            color[node_to_go] = 'grey'
            parent[node_to_go] = current_node
            dist[node_to_go] = dist[current_node] + 1
            nodes_storage.append(node_to_go)
        else:
            if dist[current_node] + 1 < dist[node_to_go]:
                dist[node_to_go] = dist[current_node] + 1
    color[current_node] = 'black'
if not flag:
    print(f'{f2.capitalize()} не может добраться до конечной точки!')


if path1 and path2:
    print()
    print('Совпавшие точки: ', end='')
    boer_mur(''.join(path1.split(' -> '))[2:-2], ''.join(path2.split(' -> '))[2:-2])

