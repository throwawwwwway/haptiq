import network as nt

nodeA = nt.Node(1, 2)
nodeB = nt.Node(4, 3)
link = nt.Link(nodeA, nodeB)
assert link.vector == [3, 1]
node_x = nt.Node(3, 0)
perpendicular_x = link.get_perpendicular(node_x)
assert perpendicular_x.vector == [1, -3]

node_y = nt.Node(1, 6)
perpendicular_y = link.get_perpendicular(node_y)
assert perpendicular_y.vector == perpendicular_x.vector

inter = link.get_intersection_point(perpendicular_x)
assert inter.x == 2.2 and inter.y > 2.4 and inter.y < 2.41

assert inter == link.get_intersection_point(perpendicular_y)