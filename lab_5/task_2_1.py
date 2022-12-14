from lab_5.utils.generators import generate_simple_graph
from lab_5.utils.animations import GraphAnimator
from lab_5.utils.finder import find_path

graph, start_node, target_node = generate_simple_graph('graph_for_task_2_1')

graph_animator = GraphAnimator(graph, start_node, target_node, show_controls=True)

find_path(graph, start_node, target_node, 'Stack', graph_animator)

