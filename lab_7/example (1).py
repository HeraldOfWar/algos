import sys
sys.setrecursionlimit(5000)

def graph_pesh(first_cell):
    global cells_sh
    global graph_for_pawn
    a, b = list(first_cell)[0], list(first_cell)[1]
    ind_cells = cells_sh.index(a)
    a = int(b)
    graph_for_pesh[first_cell] = []

    if 1 <= a + 1 <= 8 and 0 <= ind_cells <= 7:
        new_cell = cells_sh[ind_cells] + str(a + 1)
        graph_for_pesh[first_cell] = list(graph_for_pesh[first_cell]) + [new_cell]

    if not graph_for_pesh[first_cell]:
        del graph_for_pesh[first_cell]
    else:
        for i in list(graph_for_pesh[first_cell]):
            if i in graph_for_pesh.keys():
                continue
            else:
                graph_pesh(i)


def graph_lad(first_cell):
    global cells_sh
    global graph_for_rook
    a, b = list(first_cell)[0], list(first_cell)[1]
    ind_cells = cells_sh.index(a)
    a = int(b)
    graph_for_lad[first_cell] = []

    if 1 <= a + 1 <= 8 and 0 <= ind_cells <= 7:
        new_cell = cells_sh[ind_cells] + str(a + 1)
        graph_for_lad[first_cell] = list(graph_for_lad[first_cell]) + [new_cell]
    if 1 <= a <= 8 and 0 <= ind_cells + 1 <= 7:
        new_cell = cells_sh[ind_cells + 1] + str(a)
        graph_for_lad[first_cell] = list(graph_for_lad[first_cell]) + [new_cell]
    if 1 <= a <= 8 and 0 <= ind_cells - 1 <= 7:
        new_cell = cells_sh[ind_cells - 1] + str(a)
        graph_for_lad[first_cell] = list(graph_for_lad[first_cell]) + [new_cell]

    if not graph_for_lad[first_cell]:
        del graph_for_lad[first_cell]
    else:
        for i in list(graph_for_lad[first_cell]):
            if i in graph_for_lad.keys():
                continue
            else:
                graph_lad(i)


def graph_horse(first_cell):
    global cells_sh
    global graph_for_knight
    a, b = list(first_cell)[0], list(first_cell)[1]
    ind_cells = cells_sh.index(a)
    a = int(b)
    graph_for_horse[first_cell] = []

    if 1 <= a + 1 <= 8 and 0 <= ind_cells - 2 <= 7:
        new_cell = cells_sh[ind_cells - 2] + str(a + 1)
        graph_for_horse[first_cell] = list(graph_for_horse[first_cell]) + [new_cell]
    if 1 <= a - 1 <= 8 and 0 <= ind_cells - 2 <= 7:
        new_cell = cells_sh[ind_cells - 2] + str(a - 1)
        graph_for_horse[first_cell] = list(graph_for_horse[first_cell]) + [new_cell]
    if 1 <= a + 1 <= 8 and 0 <= ind_cells + 2 <= 7:
        new_cell = cells_sh[ind_cells + 2] + str(a + 1)
        graph_for_horse[first_cell] = list(graph_for_horse[first_cell]) + [new_cell]
    if 1 <= a - 1 <= 8 and 0 <= ind_cells + 2 <= 7:
        new_cell = cells_sh[ind_cells + 2] + str(a - 1)
        graph_for_horse[first_cell] = list(graph_for_horse[first_cell]) + [new_cell]

    if not graph_for_horse[first_cell]:
        del graph_for_horse[first_cell]
    else:
        for i in list(graph_for_horse[first_cell]):
            if i in graph_for_horse.keys():
                continue
            else:
                graph_horse(i)


def graph_eleph(first_cell):
    global cells_sh
    global graph_for_bishop
    a, b = list(first_cell)[0], list(first_cell)[1]
    ind_cells = cells_sh.index(a)
    a = int(b)
    graph_for_eleph[first_cell] = []

    if 1 <= a + 1 <= 8 and 0 <= ind_cells - 1 <= 7:
        new_cell = cells_sh[ind_cells - 1] + str(a + 1)
        graph_for_eleph[first_cell] = list(graph_for_eleph[first_cell]) + [new_cell]
    if 1 <= a + 1 <= 8 and 0 <= ind_cells + 1 <= 7:
        new_cell = cells_sh[ind_cells + 1] + str(a + 1)
        graph_for_eleph[first_cell] = list(graph_for_eleph[first_cell]) + [new_cell]

    if not graph_for_eleph[first_cell]:
        del graph_for_eleph[first_cell]
    else:
        for i in list(graph_for_eleph[first_cell]):
            if i in graph_for_eleph.keys():
                continue
            else:
                graph_eleph(i)


def graph_ferz(first_cell):
    global cells_sh
    global graph_for_queen
    a, b = list(first_cell)[0], list(first_cell)[1]
    ind_cells = cells_sh.index(a)
    a = int(b)
    graph_for_ferz[first_cell] = []

    if 1 <= a <= 8 and 0 <= ind_cells - 1 <= 7:
        new_cell = cells_sh[ind_cells - 1] + str(a)
        graph_for_ferz[first_cell] = list(graph_for_ferz[first_cell]) + [new_cell]
    if 1 <= a + 1 <= 8 and 0 <= ind_cells - 1 <= 7:
        new_cell = cells_sh[ind_cells - 1] + str(a + 1)
        graph_for_ferz[first_cell] = list(graph_for_ferz[first_cell]) + [new_cell]
    if 1 <= a + 1 <= 8 and 0 <= ind_cells <= 7:
        new_cell = cells_sh[ind_cells] + str(a + 1)
        graph_for_ferz[first_cell] = list(graph_for_ferz[first_cell]) + [new_cell]
    if 1 <= a + 1 <= 8 and 0 <= ind_cells + 1 <= 7:
        new_cell = cells_sh[ind_cells + 1] + str(a + 1)
        graph_for_ferz[first_cell] = list(graph_for_ferz[first_cell]) + [new_cell]
    if 1 <= a <= 8 and 0 <= ind_cells + 1 <= 7:
        new_cell = cells_sh[ind_cells + 1] + str(a)
        graph_for_ferz[first_cell] = list(graph_for_ferz[first_cell]) + [new_cell]

    if not graph_for_ferz[first_cell]:
        del graph_for_ferz[first_cell]
    else:
        for i in list(graph_for_ferz[first_cell]):
            if i in graph_for_ferz.keys():
                continue
            else:
                graph_ferz(i)


def graph_king(first_cell):
    global cells_sh
    global graph_for_king
    a, b = list(first_cell)[0], list(first_cell)[1]
    ind_cells = cells_sh.index(a)
    a = int(b)
    graph_for_king[first_cell] = []

    if 1 <= a <= 8 and 0 <= ind_cells - 1 <= 7:
        new_cell = cells_sh[ind_cells - 1] + str(a)
        graph_for_king[first_cell] = list(graph_for_king[first_cell]) + [new_cell]
    if 1 <= a + 1 <= 8 and 0 <= ind_cells - 1 <= 7:
        new_cell = cells_sh[ind_cells - 1] + str(a + 1)
        graph_for_king[first_cell] = list(graph_for_king[first_cell]) + [new_cell]
    if 1 <= a + 1 <= 8 and 0 <= ind_cells <= 7:
        new_cell = cells_sh[ind_cells] + str(a + 1)
        graph_for_king[first_cell] = list(graph_for_king[first_cell]) + [new_cell]
    if 1 <= a + 1 <= 8 and 0 <= ind_cells + 1 <= 7:
        new_cell = cells_sh[ind_cells + 1] + str(a + 1)
        graph_for_king[first_cell] = list(graph_for_king[first_cell]) + [new_cell]
    if 1 <= a <= 8 and 0 <= ind_cells + 1 <= 7:
        new_cell = cells_sh[ind_cells + 1] + str(a)
        graph_for_king[first_cell] = list(graph_for_king[first_cell]) + [new_cell]

    if not graph_for_king[first_cell]:
        del graph_for_king[first_cell]
    else:
        for i in list(graph_for_king[first_cell]):
            if i in graph_for_king.keys():
                continue
            else:
                graph_king(i)

graph_for_pawn = dict()
graph_for_rook = dict()
graph_for_knight = dict()
graph_for_bishop = dict()
graph_for_queen = dict()
graph_for_king = dict()
cells_sh = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


print("P - пешка, L - ладья, H - конь, S - слон, F - ферзь, K - король")
first_graph = dict()
second_graph = dict()
vid_1 = input("Введите 1 фигуру:")
vid_2 = input("Введите 2 фигуру:")

coord_start = input("Введите начальную клетку:")
coord_end = input("Введите конечную клетку:")

if vid_1 == 'P':
    graph_pesh(coord_start)
    first_graph = graph_for_pawn
elif vid_1 == 'L':
    graph_lad(coord_start)
    first_graph = graph_for_rook
elif vid_1 == 'H':
    graph_horse(coord_start)
    first_graph = graph_for_knight
elif vid_1 == 'S':
    graph_eleph(coord_start)
    first_graph = graph_for_bishop
elif vid_1 == 'F':
    graph_ferz(coord_start)
    first_graph = graph_for_queen
elif vid_1 == 'K':
    graph_king(coord_start)
    first_graph = graph_for_king

if vid_2 == 'P':
    graph_pesh(coord_start)
    second_graph = graph_for_pawn
elif vid_2 == 'L':
    graph_lad(coord_start)
    second_graph = graph_for_rook
elif vid_2 == 'H':
    graph_horse(coord_start)
    second_graph = graph_for_knight
elif vid_2 == 'S':
    graph_eleph(coord_start)
    second_graph = graph_for_bishop
elif vid_2 == 'F':
    graph_ferz(coord_start)
    second_graph = graph_for_queen
elif vid_2 == 'K':
    graph_king(coord_start)
    second_graph = graph_for_king


print(first_graph)
print(second_graph)

