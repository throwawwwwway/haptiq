from app.network import Node, Link, Network
from app.actuator import Actuator, Button
from app.interactions import DefaultInteract, VoiceInteract, KeyboardInteract,\
    OscillateMapping, OscillateGuidance

# --------------    Networks   --------------

# --------    One connection graph   --------


def n():
    a, b = Node(10, 10), Node(10, 8.5)
    return Network([a, b], [Link(a, b)])


def ne():
    a, b = Node(10, 10), Node(11, 9)
    return Network([a, b], [Link(a, b)])


def e():
    a, b = Node(10, 10), Node(11.5, 10)
    return Network([a, b], [Link(a, b)])


def se():
    a, b = Node(10, 10), Node(11, 11)
    return Network([a, b], [Link(a, b)])


def s():
    a, b = Node(10, 10), Node(10, 11.5)
    return Network([a, b], [Link(a, b)])


def sw():
    a, b = Node(10, 10), Node(9, 11)
    return Network([a, b], [Link(a, b)])


def w():
    a, b = Node(10, 10), Node(8.5, 10)
    return Network([a, b], [Link(a, b)])


def nw():
    a, b = Node(10, 10), Node(9, 9)
    return Network([a, b], [Link(a, b)])


# --------   Two connections graph   --------


def a1():
    c, d = Node(10, 4), Node(8, 6)
    e, f, g = Node(11, 6), Node(9, 8), Node(11, 9)
    return Network(
        [c, d, e, f, g],
        [Link(c, d), Link(d, e), Link(e, g), Link(e, f)]
    )


def a2():
    c, d = Node(10, 4), Node(8, 6)
    e, f, g = Node(8, 9), Node(10, 7), Node(11, 9)
    return Network(
        [c, d, e, f, g],
        [Link(c, d), Link(d, e), Link(e, g), Link(e, f)]
    )


def b1():
    a, b = Node(7 + 3, 1 + 3), Node(7 + 3, 4 + 3)
    c, d = Node(4 + 3, 4 + 3), Node(10 + 3, 4 + 3)
    e = Node(8 + 3, 6 + 3)
    return Network(
        [a, b, c, d, e],
        [Link(a, b), Link(b, c), Link(b, d), Link(d, e)]
    )


def b2():
    a, b = Node(7 + 3, 1 + 3), Node(7 + 3, 4 + 3)
    c, d = Node(4 + 3, 4 + 3), Node(10 + 3, 4 + 3)
    e = Node(10 + 3, 7 + 3)
    return Network(
        [a, b, c, d, e],
        [Link(a, b), Link(b, c), Link(b, d), Link(d, e)]
    )


def c1():
    c, d = Node(10, 4), Node(8, 6)
    e, f, g = Node(10, 8), Node(5, 6), Node(5, 9)
    return Network(
        [c, d, e, f, g],
        [Link(c, d), Link(d, e), Link(d, f), Link(f, g)]
    )


def c2():
    c, d = Node(10, 4), Node(8, 6)
    e, f, g = Node(10, 8), Node(8, 9), Node(5, 9)
    return Network(
        [c, d, e, f, g],
        [Link(c, d), Link(d, e), Link(d, f), Link(f, g)]
    )


def d1():
    c, d = Node(4 + 3, 4), Node(4 + 3, 7)
    e, f, g = Node(6 + 3, 9), Node(8 + 3, 7), Node(9 + 3, 9)
    return Network(
        [c, d, e, f, g],
        [Link(c, d), Link(d, e), Link(e, f), Link(e, g)]
    )


def d2():
    c, d = Node(4 + 3, 4), Node(6 + 3, 6)
    e, f, g = Node(6 + 3, 9), Node(8 + 3, 7), Node(9 + 3, 9)
    return Network(
        [c, d, e, f, g],
        [Link(c, d), Link(d, e), Link(e, f), Link(e, g)]
    )


def e1():
    c, d = Node(4 + 4, 4), Node(4 + 4, 7)
    e, f, g = Node(6 + 4, 9), Node(3 + 4, 9), Node(9 + 4, 9)
    return Network(
        [c, d, e, f, g],
        [Link(c, d), Link(d, e), Link(e, f), Link(e, g)]
    )


def e2():
    c, d = Node(4 + 4, 4), Node(6 + 4, 6)
    e, f, g = Node(6 + 4, 9), Node(3 + 4, 9), Node(9 + 4, 9)
    return Network(
        [c, d, e, f, g],
        [Link(c, d), Link(d, e), Link(e, f), Link(e, g)]
    )


def f1():
    c, d = Node(7, 6), Node(10, 6)
    e, f, g = Node(13, 6), Node(8, 8), Node(11, 8)
    return Network(
        [c, d, e, f, g],
        [Link(c, d), Link(d, e), Link(d, f), Link(f, g)]
    )


def f2():
    c, d = Node(10, 3), Node(10, 6)
    e, f, g = Node(8 + 5, 6), Node(3 + 5, 8), Node(6 + 5, 8)
    return Network(
        [c, d, e, f, g],
        [Link(c, d), Link(d, e), Link(d, f), Link(f, g)]
    )


def whole_network():
    a, b, c, d = Node(3, 4), Node(10.5, 4), Node(6, 8), Node(10.5, 8)
    e, f, g, h = Node(16.5, 8), Node(18, 6), Node(3, 16), Node(13.5, 12)
    i, j = Node(16.5, 16), Node(3, 12)
    return Network(
        [a, b, c, d, e, f, g, h, i, j],
        [
            Link(a, b), Link(a, c), Link(a, j), Link(b, d), Link(c, d),
            Link(d, h), Link(d, e), Link(e, f), Link(h, i), Link(j, g),
            Link(j, h), Link(h, e)
        ]
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
    a = Node(6, 8)
    b = Node(10, 8)
    return Network([a, b], [Link(a, b)])


def vertical_network():
    a = Node(10, 6)
    b = Node(10, 10)
    return Network([a, b], [Link(a, b)])


def l_network():
    a = Node(10, 10, 'Paris')
    b, c = Node(10, 7, 'Lille'), Node(13, 10, 'Strasbourg')
    return Network(
        [a, b, c],
        [Link(a, b), Link(a, c)]
    )


def all_networks():
    return {
        # "one node": one_node_network(),
        # "two nodes": two_nodes_network(),
        # "triangle": triangle_network(),
        # "horizontal line": horizontal_network(),
        # "vertical line": vertical_network(),
        # "whole network": whole_network(),
        "default": Network(),
        "l": l_network(),
        "gen 0 connection": None,
        "gen 1 connection": None,
        "gen 2 connections": None,
        "gen 3 connections": None
    }


# --------------    Actuators   --------------


def actuators_4():
    east = Actuator('East', 0)
    north = Actuator('North', 90)
    west = Actuator(180, 'West')
    south = Actuator('South', 270)
    return [east, north, west, south]


def actuators_8():
    east = Actuator('East', 0)
    north_east = Actuator('North-East', 45)
    north = Actuator('North', 90)
    north_west = Actuator('North-West', 135)
    west = Actuator('West', 180)
    south_west = Actuator('South-West', 225)
    south = Actuator('South', 270)
    south_east = Actuator('South-East', 315)
    return [
        east, north_east, north, north_west,
        west, south_west, south, south_east]


def actuators_9():
    east = Actuator('East', 0)
    north_east = Actuator('North-East', 45)
    north = Actuator('North', 90)
    north_west = Actuator('North-West', 135)
    west = Actuator('West', 180)
    south_west = Actuator('South-West', 225)
    south = Actuator('South', 270)
    south_east = Actuator('South-East', 315)
    button = Button('center')
    return [
        east, north_east, north, north_west,
        west, south_west, south, south_east, button]


# --------------    Interactions   --------------


def all_interactions():
    return {
        'HaptiQ_oscillate_mapping': OscillateMapping(),
        'HaptiQ_oscillate_guidance': OscillateGuidance(),
        'Voice': VoiceInteract(),
        'Keyboard': KeyboardInteract(),
        'default': DefaultInteract(),
    }
