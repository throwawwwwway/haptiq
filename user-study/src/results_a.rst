************
User Study A
************

Introduction
============
This reports describes briefly the procotol followed and presents the data collected with their results. This user study aims to compare different sets of tactile signals in order to evaluate which would be the most suited for graph exploration. Two sets of tactile signals has been developed: one is purely mapping what is under the device (M) when the second adds some guidance (G). These two sets - M and G, are the result of multiple enhancement after each iteration where the users have reported their struggles and where we have observed their difficulties in adopting these sets of tactile signals.

Hypothesis
==========
We are looking for an answer on the best set of tactile signals, in order to prove or disprove the usability of one we will start with the following statement. With the end results, we would then be able to confirm or deny our hypothesis.


1. The set G is more **efficient** than M.
2. The set G is more **satisfying** than M.


Interactions
============

Mapping set of tactile signals
------------------------------

The behavior is following these rules:

- When the device is pointing to a node, the actuator uplifted indicate the connexion with other node. The other actuators are left down.
- When the device is pointing to a link between two nodes, the actuators corresponding to the direction of this link are up, the others down.
- When the device is pointing nothing, the actuators are left down.

.. figure:: ressources/m_on_node.png
   :height: 250px
   :align: center
   :width: 250px

   Figure 1: Tactile signal when device is pointing to a node

.. figure:: ressources/m_on_link.png
   :height: 250px
   :align: center
   :width: 250px
   
   Figure 2: Tactile signal when device is pointing to a link

Guidance set of tactile signals
-------------------------------

The behavior is following the same behavior as the Mapping one, but adds a guidance when near link.

- When the device is near a link, the actuator going towards that link is oscilatting up and down. The rest of the actuators are left down.

.. figure:: ressources/g_near_link.png
   :height: 250px
   :width: 250px
   :align: center

   Tactile signal when device is near a link


Protocol
========

The subjects were informed about the HaptiQ project and the purpose of this evaluation. They were given a disclaimer to read and sign, before starting the experiment. A quick form was then given to check out any familiarities with haptic devices. Before the eye mask is put, they were told that they could leave the experiment at any given time without justification and they also remove the mask if they were feeling uncomfortable.

Then they were told to manipulate the device in order to feel it without tactile signal and also it allowed them to get a mental representation of the frame that is used for tracking the position. When done, a training network is loaded with one of the mappings. I then describe the set of tactile signals before letting the exploration. I emphasize on the importance that this is for understanding the way the interaction is working, so I encouraged questions. When ready, I loaded a second graph that is used as a blank test; we then agreed on the way the subject is more familiar describing the network eg. "central node with one connection to the North and one to the South-East". I then told them that there would be six similar tasks to perform as fast as possible.

The graphs used were always a central node in the center of the frame with one, two or three connections around it. These graphs are generated randomly given the number of nodes. The six tasks were a random order of the following graphs:

- one graph with one connection
- three graphs with two connections
- two graphs with three connections

.. figure:: ressources/possible_graphs.png
   :height: 250px
   :width: 250px
   :align: aligned-center

They were then asked to fill out a SUS questionnaire and were invited to share their remarks.
When both of the interaction technique were evaluated, they were then asked to say which would be the most convenient one.


Data
====

t is for time (in s) and a is for answer (true or false)
SUS score is out of 100
Score is 1 for when the set is preferred, 0 otherwise
Ratio is time inside the network on the total time of the experiment (1 means always on network)
Distance is the total distance traveled with the device (in px)


On subjects
-----------

+---------+------------------+-----+--------+-----------------------------------+-------------------+-----------+
| Subject | Date             | Age | gender | Right handed                      | Haptic experience | Frequency |
+=========+==================+=====+========+===================================+===================+===========+
| EB      | 06/08/2014 17:44 | 22  | F      | Yes                               | Little            | Rare      |
+---------+------------------+-----+--------+-----------------------------------+-------------------+-----------+
| HX      | 14/08/2015 13:45 | 27  | M      | Yes                               | None              | /         |
+---------+------------------+-----+--------+-----------------------------------+-------------------+-----------+
| AL      | 17/08/2015 18:41 | 24  | M      | No, but uses right hand for mouse | Little            | Rare      |
+---------+------------------+-----+--------+-----------------------------------+-------------------+-----------+
| SB      | 19/08/2015 13:50 | 25  | F      | No, but uses right hand for mouse | None              | /         |
+---------+------------------+-----+--------+-----------------------------------+-------------------+-----------+


Data
----

+---------+-----+------+-------+--------+----------+----+----+----+----+
| Subject | Obs | Conf | Trial | TM     | TG       | RM | RG | DM | DG |
+=========+=====+======+=======+========+==========+====+====+====+====+
| EB      | /   | 1    | 1     | 111    | 50       |    |    |    |    |
| EB      | /   | 2    | 1     | 37     | 31.5     |    |    |    |    |
| EB      | /   | 2    | 2     | 16.5   | 40       |    |    |    |    |
| EB      | /   | 2    | 3     | 52.5   | 43       |    |    |    |    |
| EB      | /   | 3    | 1     | 13     | 10       |    |    |    |    |
| EB      | /   | 3    | 2     | 8.3    | NG(16.3) |    |    |    |    |
+---------+-----+------+-------+--------+----------+----+----+----+----+
| HX      | /   | 1    | 1     | 43     | 51       |    |    |    |    |
| HX      | /   | 2    | 1     | 38.5   | 22       |    |    |    |    |
| HX      | /   | 2    | 2     | 26     | 21.5     |    |    |    |    |
| HX      | /   | 2    | 3     | 19     | 29.5     |    |    |    |    |
| HX      | /   | 3    | 1     | 12.3   | 25.7     |    |    |    |    |
| HX      | /   | 3    | 2     | 19.7   | 33.3     |    |    |    |    |
+---------+-----+------+-------+--------+----------+----+----+----+----+
| AL      | /   | 1    | 1     | 45     | 41       |    |    |    |    |
| AL      | /   | 2    | 1     | 12.5   | 8.5      |    |    |    |    |
| AL      | /   | 2    | 2     | 18.5   | 36       |    |    |    |    |
| AL      | /   | 2    | 3     | 26     | 18.7     |    |    |    |    |
| AL      | /   | 3    | 1     | NG(22) | 18.7     |    |    |    |    |
| AL      | /   | 3    | 2     | 25     | NG(19.7) |    |    |    |    |
+---------+-----+------+-------+--------+----------+----+----+----+----+
| SD      | /   | 1    | 1     | 79     | 24       |    |    |    |    |
| SD      | /   | 2    | 1     | 28     | 20.5     |    |    |    |    |
| SD      | /   | 2    | 2     | 32     | 16.5     |    |    |    |    |
| SD      | /   | 2    | 3     | 25.5   | 21.5     |    |    |    |    |
| SD      | /   | 3    | 1     | 33.3   | 20.7     |    |    |    |    |
| SD      | /   | 3    | 2     | 23     | NG(22.7) |    |    |    |    |
+---------+-----+------+-------+--------+----------+----+----+----+----+

Feedbacks
---------

+---------+------+------+----+----+
| Subject | SUSM | SUSG | SM | SG |
+=========+======+======+====+====+
| EB      | 85   | 92.5 | 0  | 1  |
| HX      | 75   | 95   | 0  | 1  |
| AL      | 67.5 | 77.5 | 0  | 1  |
| SD      | 77.5 | 92.5 | 0  | 1  |
+---------+------+------+----+----+

Remarks
-------

On interaction M
^^^^^^^^^^^^^^^^

- always felt lost, needed to perform a search pattern
- not useful
- thought sometimes it was not working, because of lack of interaction

On interaction G
^^^^^^^^^^^^^^^^

- good tactile feeling
- with training could be expert x2
- less workload
- covers everything needed

General remarks
^^^^^^^^^^^^^^^

- confusing horizontal lines with diagonal ones x3
- tiring (cannot rest your hand)
- needed some time to learn how to use the tactons
- not easy to recognize directions
- needed to check one by one all the actuators
- it felt shy, so I needed to adapt to feel it properly x2
- device felt fragile
- needed to raise and land hand to avoid stucking actuators
- too much friction for moving
- felt like orientation drifting
- sound was helping (conforting my own track because of rythm, easier to differentiate from node to link) x4
- sensitivity felt uneven x2

Suggestions
^^^^^^^^^^^

- could have a cover x2
- better to have a horizontal reference x2
- having a multi-point interactions (like drawing with the pen on the hand)
- change tactile sensation of diagonals
- oscilations should be faster
- would be easier to differentiate node and link with a vibror


Results
=======

TODO