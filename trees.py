

class Node:
    def __init__(self, value: int, connected_nodes: list = None) -> None:
        self.value = value
        self.connected_nodes = connected_nodes or []

    def __str__(self):
        return f"Node: {self.value}"

    def connect_nodes(self, a: "Node"):
        self.connected_nodes.append(a)
        a.connected_nodes.append(self)

class Tree:
    def __init__(self, nodes_list: list[Node]) -> None:
        self.nodes_list = nodes_list
        self.sorted_tree = []

    def depth_first(self) -> None:
        starting_node = self.nodes_list[0]
        self.sorted_tree.append(starting_node)
        self.depth_first_visit(starting_node)

    def depth_first_visit(self, node) -> None:
        for connected_node in node.connected_nodes:
            if connected_node not in self.sorted_tree:
                self.sorted_tree.append(connected_node)
                self.depth_first_visit(connected_node)

    def breadth_first(self) -> None:
        node_queue = []
        starting_node = self.nodes_list[0]
        self.sorted_tree.append(starting_node)
        node_queue.append(starting_node)
        while len(node_queue) > 0:
            current_node = node_queue[0]
            node_queue.pop(0)
            for connected_node in current_node.connected_nodes:
                if not connected_node in self.sorted_tree:
                    self.sorted_tree.append(connected_node)
                    node_queue.append(connected_node)

# TEST CASES
n1  = Node(1)
n2  = Node(2)
n3  = Node(3)
n4  = Node(4)
n5  = Node(5)
n6  = Node(6)
n7  = Node(7)
n8  = Node(8)
n9  = Node(9)
n10 = Node(10)
n11 = Node(11)
n12 = Node(12)
n13 = Node(13)

# Build connections
n1.connect_nodes(n2)
n1.connect_nodes(n3)
n1.connect_nodes(n4)

n2.connect_nodes(n5)
n2.connect_nodes(n6)

n5.connect_nodes(n10)

n6.connect_nodes(n11)
n6.connect_nodes(n12)

n3.connect_nodes(n7)

n4.connect_nodes(n8)
n4.connect_nodes(n9)

n9.connect_nodes(n13)

# Collect nodes if needed
nodes = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13]

Depth_Tree = Tree(nodes)
Depth_Tree.depth_first()
print("DEPTH FIRST")
for item in Depth_Tree.sorted_tree:
    print(item)
Breadth_Tree = Tree(nodes)
Breadth_Tree.breadth_first()
print("BREADTH FIRST")
for item in Breadth_Tree.sorted_tree:
    print(item)

