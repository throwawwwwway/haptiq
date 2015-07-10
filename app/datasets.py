from app.network import Node, Link, Network
from app.actuator import Actuator, Button
from app.interactions import HaptiQInteract, VoiceInteract, KeyboardInteract


# --------------    Networks   --------------


def whole_network():
    a, b, c, d = Node(3, 4), Node(10.5, 4), Node(6, 8), Node(10.5, 8)
    e, f, g, h = Node(16.5, 8), Node(18, 6), Node(3, 16), Node(13.5, 12)
    i, j = Node(16.5, 16), Node(3, 12)
    return Network(
        [a, b, c, d, e, f, g, h, i, j],
        [
            Link(a, b), Link(a, c), Link(a, j), Link(b, d), Link(c, d),
            Link(a, j), Link(d, h), Link(d, e), Link(e, f), Link(h, f),
            Link(h, i), Link(j, g), Link(j, h)
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
        'HaptiQ': HaptiQInteract(),
        'Voice': VoiceInteract(),
        'Keyboard': KeyboardInteract()
    }
