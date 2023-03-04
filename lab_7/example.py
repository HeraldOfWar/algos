import sys
sys.setrecursionlimit(5000)


def graph_pawn(first_cell):
    global cells_sh
    global graph_for_pawn
    a, b = list(first_cell)[0], list(first_cell)[1]
    ind_cells = cells_sh.index(a)
    a = int(b)
    graph_for_pawn[first_cell] = []

    if 1 <= a + 1 <= 8 and 0 <= ind_cells <= 7:
        new_cell = cells_sh[ind_cells] + str(a + 1)
        graph_for_pawn[first_cell] = list(graph_for_pawn[first_cell]) + [new_cell]

    if not graph_for_pawn[first_cell]:
        del graph_for_pawn[first_cell]
    else:
        for i in list(graph_for_pawn[first_cell]):
            if i in graph_for_pawn.keys():
                continue
            else:
                graph_pawn(i)


def graph_rook(first_cell):
    global cells_sh
    global graph_for_rook
    a, b = list(first_cell)[0], list(first_cell)[1]
    ind_cells = cells_sh.index(a)
    a = int(b)
    graph_for_rook[first_cell] = []

    if 1 <= a + 1 <= 8 and 0 <= ind_cells <= 7:
        new_cell = cells_sh[ind_cells] + str(a + 1)
        graph_for_rook[first_cell] = list(graph_for_rook[first_cell]) + [new_cell]
    if 1 <= a <= 8 and 0 <= ind_cells + 1 <= 7:
        new_cell = cells_sh[ind_cells + 1] + str(a)
        graph_for_rook[first_cell] = list(graph_for_rook[first_cell]) + [new_cell]
    if 1 <= a <= 8 and 0 <= ind_cells - 1 <= 7:
        new_cell = cells_sh[ind_cells - 1] + str(a)
        graph_for_rook[first_cell] = list(graph_for_rook[first_cell]) + [new_cell]

    if not graph_for_rook[first_cell]:
        del graph_for_rook[first_cell]
    else:
        for i in list(graph_for_rook[first_cell]):
            if i in graph_for_rook.keys():
                continue
            else:
                graph_rook(i)


def graph_knight(first_cell):
    global cells_sh
    global graph_for_knight
    a, b = list(first_cell)[0], list(first_cell)[1]
    ind_cells = cells_sh.index(a)
    a = int(b)
    graph_for_knight[first_cell] = []

    if 1 <= a + 1 <= 8 and 0 <= ind_cells - 2 <= 7:
        new_cell = cells_sh[ind_cells - 2] + str(a + 1)
        graph_for_knight[first_cell] = list(graph_for_knight[first_cell]) + [new_cell]
    if 1 <= a - 1 <= 8 and 0 <= ind_cells - 2 <= 7:
        new_cell = cells_sh[ind_cells - 2] + str(a - 1)
        graph_for_knight[first_cell] = list(graph_for_knight[first_cell]) + [new_cell]
    if 1 <= a + 1 <= 8 and 0 <= ind_cells + 2 <= 7:
        new_cell = cells_sh[ind_cells + 2] + str(a + 1)
        graph_for_knight[first_cell] = list(graph_for_knight[first_cell]) + [new_cell]
    if 1 <= a - 1 <= 8 and 0 <= ind_cells + 2 <= 7:
        new_cell = cells_sh[ind_cells + 2] + str(a - 1)
        graph_for_knight[first_cell] = list(graph_for_knight[first_cell]) + [new_cell]

    if not graph_for_knight[first_cell]:
        del graph_for_knight[first_cell]
    else:
        for i in list(graph_for_knight[first_cell]):
            if i in graph_for_knight.keys():
                continue
            else:
                graph_knight(i)


def graph_bishop(first_cell):
    global cells_sh
    global graph_for_bishop
    a, b = list(first_cell)[0], list(first_cell)[1]
    ind_cells = cells_sh.index(a)
    a = int(b)
    graph_for_bishop[first_cell] = []

    if 1 <= a + 1 <= 8 and 0 <= ind_cells - 1 <= 7:
        new_cell = cells_sh[ind_cells - 1] + str(a + 1)
        graph_for_bishop[first_cell] = list(graph_for_bishop[first_cell]) + [new_cell]
    if 1 <= a + 1 <= 8 and 0 <= ind_cells + 1 <= 7:
        new_cell = cells_sh[ind_cells + 1] + str(a + 1)
        graph_for_bishop[first_cell] = list(graph_for_bishop[first_cell]) + [new_cell]

    if not graph_for_bishop[first_cell]:
        del graph_for_bishop[first_cell]
    else:
        for i in list(graph_for_bishop[first_cell]):
            if i in graph_for_bishop.keys():
                continue
            else:
                graph_bishop(i)


def graph_queen(first_cell):
    global cells_sh
    global graph_for_queen
    a, b = list(first_cell)[0], list(first_cell)[1]
    ind_cells = cells_sh.index(a)
    a = int(b)
    graph_for_queen[first_cell] = []

    if 1 <= a <= 8 and 0 <= ind_cells - 1 <= 7:
        new_cell = cells_sh[ind_cells - 1] + str(a)
        graph_for_queen[first_cell] = list(graph_for_queen[first_cell]) + [new_cell]
    if 1 <= a + 1 <= 8 and 0 <= ind_cells - 1 <= 7:
        new_cell = cells_sh[ind_cells - 1] + str(a + 1)
        graph_for_queen[first_cell] = list(graph_for_queen[first_cell]) + [new_cell]
    if 1 <= a + 1 <= 8 and 0 <= ind_cells <= 7:
        new_cell = cells_sh[ind_cells] + str(a + 1)
        graph_for_queen[first_cell] = list(graph_for_queen[first_cell]) + [new_cell]
    if 1 <= a + 1 <= 8 and 0 <= ind_cells + 1 <= 7:
        new_cell = cells_sh[ind_cells + 1] + str(a + 1)
        graph_for_queen[first_cell] = list(graph_for_queen[first_cell]) + [new_cell]
    if 1 <= a <= 8 and 0 <= ind_cells + 1 <= 7:
        new_cell = cells_sh[ind_cells + 1] + str(a)
        graph_for_queen[first_cell] = list(graph_for_queen[first_cell]) + [new_cell]

    if not graph_for_queen[first_cell]:
        del graph_for_queen[first_cell]
    else:
        for i in list(graph_for_queen[first_cell]):
            if i in graph_for_queen.keys():
                continue
            else:
                graph_queen(i)


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


def boer_mur(s1, s2):
    for i in range(1, len(s2), 2):
        a, b = s2[i - 1], s2[i]
        for j in range(1, len(s1)):
            a1, b1 = s1[j - 1], s1[j]
            if b == b1:
                if a == a1:
                    print(a + b, end=' ')
                else:
                    if a1 in str(i):
                        continue
                    else:
                        j += 1
            else:
                if b1 in str(i):
                    continue
                else:
                    j += 2
