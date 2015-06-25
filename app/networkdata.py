from app.network import Node, Link, Network


def whole_network():
    a = Node(2, 2)
    b = Node(7, 2)
    c = Node(4, 4)
    d = Node(7, 4)
    e = Node(11, 4)
    f = Node(12, 3)
    g = Node(2, 8)
    h = Node(9, 6)
    i = Node(11, 8)
    j = Node(2, 6)
    links = [
        Link(a, b),
        Link(a, c),
        Link(a, j),
        Link(b, d),
        Link(c, d),
        Link(a, j),
        Link(d, h),
        Link(d, e),
        Link(e, f),
        Link(h, f),
        Link(h, i),
        Link(j, g),
        Link(j, h)
    ]
    return Network(
        [a, b, c, d, e, f, g, h, i, j],
        links
    )

def exp1_network():
    home = Node(5, 8)
    cinema = Node(8, 7)
    police = Node(7, 3)
    market = Node(14, 5)
    city_hall = Node(15, 10)
    school = Node(7, 12)
    tower = Node(3, 15)

    links = [
        Link(home, cinema),
        Link(home, police),
        Link(cinema, police),
        Link(police, market),
        Link(market, city_hall),
        Link(school, city_hall),
        Link(home, school)
    ]

    return Network(
        [home, cinema, police, market, city_hall, school, tower],
        links
    )


def conc1_network():
    sophie = Node(6, 2)
    mathiew = Node(2, 6)
    jean = Node(10, 6)
    martin = Node(2, 10)
    harold = Node(10, 10)
    helene = Node(14, 10)
    julie = Node(10, 14)
    marie = Node(14, 14)

    links = [
        Link(sophie, mathiew),
        Link(sophie, jean),
        Link(jean, mathiew),
        Link(martin, mathiew),
        Link(jean, harold),
        Link(jean, helene),
        Link(mathiew, harold),
        Link(harold, julie),
        Link(helene, marie),
        Link(julie, marie)
    ]
    return Network(
        [sophie, mathiew, jean, martin, harold, helene, julie, marie],
        links
    )


def labyrinth_network():
    node_a = Node(3, 3)
    node_b = Node(6, 3)
    node_c = Node(6, 6)
    node_d = Node(3, 6)
    node_e = Node(9, 3)
    node_f = Node(12, 6)
    node_g = Node(9, 9)
    node_h = Node(12, 9)
    node_i = Node(15, 9)

    links = [
        Link(node_a, node_b),
        Link(node_b, node_c),
        Link(node_d, node_c),
        Link(node_e, node_c),
        Link(node_b, node_e),
        Link(node_e, node_f),
        Link(node_f, node_g),
        Link(node_h, node_f),
        Link(node_h, node_g),
        Link(node_h, node_i)
    ]
    return Network(
        [
            node_a, node_b, node_c, node_d,
            node_e, node_f, node_g, node_h, node_i
        ],
        links
    )


def triangle_network():
    node_a = Node(3, 3)
    node_b = Node(12, 6)
    node_c = Node(6, 12)
    node_e = Node(6, 6)
    node_f = Node(14, 14)

    link_1 = Link(node_a, node_b, 'AB')
    link_2 = Link(node_b, node_c, 'BC')
    link_3 = Link(node_c, node_a, 'AC')

    return Network(
        [node_a, node_b, node_c, node_e, node_f],
        [link_1, link_2, link_3]
    )


def one_node_network():
    return Network([Node(5, 5)], [])


def two_nodes_network():
    return Network([Node(5, 5), Node(10, 10)], [])


def horizontal_network():
    a = Node(2, 8)
    b = Node(15, 8)
    return Network([a, b], [Link(a, b)], [])


def vertical_network():
    a = Node(7, 2)
    b = Node(7, 15)
    return Network([a, b], [Link(a, b)], [])


def all_networks():
    return {
        "one node": one_node_network(),
        "two nodes": two_nodes_network(),
        "triangle": triangle_network(),
        "horizontal line": horizontal_network(),
        "vertical line": vertical_network(),
        "whole network": whole_network()
        # "labyrinth": labyrinth_network(),
        # "concrete 1": conc1_network(),
        # "explanatory 1": exp1_network()
    }
