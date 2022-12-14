from lab_5.utils.generators import generate_maze_graph
from lab_5.utils.animations import GraphAnimator
from lab_5.utils.finder import find_path

graph, start_node, target_node, maze_list = generate_maze_graph()

graph_animator = GraphAnimator(graph, start_node, target_node,
                               is_maze=True, maze_list=maze_list,
                               show_datastructure=False)

find_path(graph, start_node, target_node, 'AStarQueue', graph_animator)
