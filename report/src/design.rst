.. 10p <=> 3000w

Design
======
.. Our design should therefore meet the requirements previously stated.

Tactile vector based devices are uncommon in haptics research, our aim is to provide some feedback on their usage for graph exploration. Yet, the key points are to design a device that is affordable and easily reproductible. Our design path also expects to reach the opensource community in order to ease further contributions.
In this chapter, I will discuss the different choices that have been made in order to build a functionnal prototype for our research.


Global design
-------------

The HaptiQ is an enhanced mouse in which tactile feedbacks helps graph exploration. These feedbacks are giving by actuators on the top of the device forming a star shape and are in contact with the hands. Moving the device is an input data provided by the user, just as if we were to move a mouse. This motion is then tracked and processed by a software layer that will trigger a certain tactile signal, called tacton. The device will move the actuators according to this tacton singal.

Although this is the main workflow for the HaptiQ, we do want to be able to compare this interaction to other techniques. This is why special efforts have been made for the software part that I will detail.

The feelings that the users experienced by using this device - the tactons, have a direct impact on the usability of the whole system. Human Computer Interactions (HCI) skills have been applied in order to make sure that the final tactons are suited for the task of graph exploration. 

Although important, these tactons are supported and limited by the hardware. It has required various skills in order to build the case, assemble the electronic components and set up every actuator. Many collaborators have been involved in this process - and I could not thank them enough.

.. TODO: figure representing the global scheme

`Figure x`_ represents the glogal structure of the HaptiQ. We have a first agent that takes care of tracking 




Design of the software
----------------------

The software is the agent that enables interactions for graph exploration. The application is flexible enough and provide an easy way to change the tacton on demand. The architecture has also been thought in order to facilitate a change of interaction technique, again on demand. This needed flexibility is due to the fact that we are focusing on the usability of the HaptiQ; and this can only be done by comparing it with other interaction techniques. The result is a particular cross-platform software that can be used in various context for graph exploration: for instance it is actually possible to use it with directional keys or by pointing.

The final and current state of the software has been achieved by an iterative exploratory approach and many refactoring. This has led to three main threads (Input listener, Graphic User Interface or GUI, Interaction executer) communicating through four main components (Network, Interaction, Device).


Network component
^^^^^^^^^^^^^^^^^

This component is used as the container of all the geometric logic that are involved in graph exploration. More precisely, it contains the collection of Nodes and Links that respectively inherit the functions for Points and Lines. These collections can be processed by the GUI and appear on the screen.
An existing libraries that provides functions for graphs and network manipulation was considered [#]_. Our needs were too perticular in order to use such an extern ressource easily and on the same time, the computation complexity for our need remained sufficiently low to be easily done during this internship.

.. TODO: figure showing up a graph

.. [#] https://networkx.github.io/


Interaction component
^^^^^^^^^^^^^^^^^^^^^

A graph exploration require two things, what is explored - the network, and how -the interaction. This component has came late in the development process as the first objective was to make the HaptiQ work and then enable multiple interaction techniques: which requires more thinking and a better outlook.
The interaction component makes sure that all the derives interactions follows these three basics functionalities:

- open: which will verify if the system meets the requirements for this interaction and therefore avoid any error
- process: is called by the interaction thread every loop turn; it computes the appropriate output from a given situation and executes it
- closed: which would close the remaining process linked to this interction opened during its usage

By such a structure, it was easy to adapt the HaptiQ interaction previously made and at the same time offering a standard way of creating an interaction technique. Besides, it offers a control over the execution time which is necessary for our user study.

During open, this component makes sure that a network is available. For more specific interaction like the HaptiQ, it checks the availability of the device component. This is how the input is made available during process for computation.

Building this interface has turned a first restricted version of the software into an evolutive program that can now accept various interaction techniques. Future collaboration has been made available by this refactoring.

.. TODO: figure showing the three phases of usage of an interaction

Device component
^^^^^^^^^^^^^^^^

The device component is a virtual representation of the HaptiQ. It has therefore a position, an orientation and the state of each of the actuators. Each actuator is characterized by an angle or a direction - like North which would be equivalent to 90°, that is fixed and a level - between 0 and 100, that can be changed.

As it is a representation of the device, all the interaction techniques that are dealing with the HaptiQ are using this component as the reference for the position. More than a representation of the current state, it is actually the state in which the HaptiQ should be. Attribute like the position are directly depending on the user and can only be updated, but it is a security regarding the levels of the actuators. It happens that the HaptiQ does not execute the latest tactons and gets stucked in an other state which does not match the real situation. Using this device component as the reference for the level of each actuator makes the system less prone to context errors.

.. TODO: figure representing all the actuators

Input tracker
^^^^^^^^^^^^^

This is the thread that is constantly listening to the information regarding the HaptiQ. These information are shared by the TUIO protocol. It simply means that the information is formatted in certain rules which makes the parsing process easier. The tracker receives a variety of data in the form of chains of characters. Because they follow some patterns, it is possible to extract the key information which consists of a variety of points. These points are then parsed to a handler that compute them in order to obtain a center point and an orientation. The position and the orientation of the device component are then updated.

Basing the position of our device on the computation of data sent with a high debit does lead to some incoherences. This issue has been solved by adding on the tracker a checker that allows only valid position.

Graphical User Interface
^^^^^^^^^^^^^^^^^^^^^^^^

The GUI or simply called *view* in the program, represents the network loaded visually as seen on figure x. It serves as the reference for which network and which interaction are being currently in use. A new network can be loaded on live, this allows future applications of the HaptiQ in which a user could change it himself.

.. TODO: figure of the immediate change

It also includes a special window that acts as a visual representation of the tactons currently in use for the device. This has been extensively useful during the development phase in which sets of tactons were visually tried before any further development. This could be seen as the low fidelity prototype format of tactile interactions as it gives a genreal hint of how the tacton will react; yet, the lack of sensation makes it a very low fidelity.

.. TODO: figure representing all the actuators

Interaction processor
^^^^^^^^^^^^^^^^^^^^^

This thread checks which interaction is selected by the view and will call the *process* method for that interaction. For each time the interaction is changed, this processor will make sure the previous one gets closed properly and the new one *open* - as described in the interaction component.


.. TODO: figure representing all the components and threads together


Design of the tactons
---------------------

For our device, a tacton is the position of all the actuators for a given time or for a short lapse of time. This time would be the evolution of the levels until they repeat the pattern - like an oscillation. The tacton is the language in which we are communicating what is drawn under the pointing device. It could be a node, a link or nothing at all - but each one of these situation leads to completely different tactil signals and needs to be easily recognisable. One of the goal of the internship is to evaluate the usability of each tactons.

In order to establish the most suited sets of tactons, I have proceeded by iteration. I will explain in the following  section the three main steps that have guided me towards the current version which is still being tested as I am writting this report. 


First iteration of tactons
^^^^^^^^^^^^^^^^^^^^^^^^^^

The first version to be evaluated by walkthrough and rapid testing arrived the 8th of April 2015 [#]_. Because of the early version of this interaction, links were not integrated yet.
The tactons to be generated depend on the following rules:

- near a node, the tacton indicates the closest nodes by up and down oscillations. Actuators moved this way are the two closest angles, so if the node is at 40°, the North (90°) and the East (0°) actuators gets moved.
- on a node, the tacton indicates the closest nodes by being fully up. The concerned actuators are the same as previously.

The intention in this set of tactons was to encode as much information as possible. By using this perticular set of tactons, one would know when he would be near a node because the oscillations would begin; at the same time you would still know about nearby nodes. You could easily distinguish when you are on a node 

That was in theory, while experimenting roughly with my low fidelity feedback, the subjects were feeling lost during the whole exploration process inspite of me showing where were the ndoes. The following interviews have revealed the reasons:

- there was far too much information at a giving time
- the interactions felt unatural
- it was impossible to tell how many nodes were nearby

Although this interaction was highly depreciated, the task of know whetether or not we were on a node or not was done accurately. A first contribution from this first iteration is the efficient distinction provided by static versus oscillation. This characteristic has been preserved through the versions. A second one would be the fact that having more than one actuator guiding a single node was too complex too be easily processed by the user. This aspect has been taken into account in the next iterations.

.. TODO: figure showing the impossibility to understand how many nodes, plus static vs oscillation

.. [#] https://github.com/asiegfried/vegham/tree/v0.1/app

Second iteration of tactons
^^^^^^^^^^^^^^^^^^^^^^^^^^^

One week later, I have drastically changed the tactons in order to find a simpler way to provide feedback. This has resulted into a minimalistic format [#]_.

.. [#] https://github.com/asiegfried/vegham/tree/v0.2/app

- near a node, the tacton indicates the direction towards it with a certain intensity. Only one actuator is moved for this tacton, it is the one closer to the angle. For instance for a node at 40° it will be just the East (0°) actuator. The intensity is inversly proportional to the distance. The closer, the higher the level would be.
- on a node, all the actuators are higher than normal.
  
This interaction takes into account what has been remarked in the first iteration. One actuator is for one node. Oscillation were reserved purposely for the links, that have not been integrated to the software at that time.

Another walkthrough has been tried on this interaction in order to detect usability errors and just in general seeking other ideas. This interaction has received several positive feedbacks. The sudden change for when the pointer is on node makes the message very clear. The growing intensity also indicated well the exploration. The major issue remained the fact that these tests were based on visualisation as a proxy of what the tactile sensations would be. Obviously these two senses cannot be considered equivalent for my tactons; I had then reached a limit for my low fidelity prototyping.

Yet, I have understood that simpler is generally better when it comes to provide guidance. This aspect has motivated my further interaction. The major contribution of this iteration has been the importance to keep a clear contrast between the two situations: on node and not on a node. Since the major difficulty is to find the network, it must be very clear for the user when it is over a node or not. It accentuates a mental marker on that very specific zone, it is also reasuring to have such a clear and distinct tactile feedback.

.. TODO: figure showing the evolution of a node getting closer

Final general of tactons
^^^^^^^^^^^^^^^^^^^^^^^^

A few other tactons have been developed while waiting the HatpiQ to be build. After some hardware issues (that will be presented in Implementation), I was able to provide the real sensation of the HaptiQ and this was highly valuable in order to seek the features that would lead to a suitable tactons.

After several tries through the hardware capacities and my self judgment, I came up with a last generation of four sets of tactons. The goal was to compare them in a user study and being able to justify the most appropriate one for graph exploration. During the first tries out of this user study, I had to withdraw two of them as they appeared to be completely unusable for the required task. Two of my collaborators, one visually impaired one not have experienced the same struggles in using some of these tacton sets.
Among other issues, the users felt overwhelmed with the tactile information - like arriving on a node, all the actuators were moving at the same time. And also, it appeared that the intensity that felt like an interesting idea in the second iteration, turned out to be completely unperceptable in the real situation. We can sum up that the main reason why they were not efficient is because of their lack of simplicity and consistency. I had to remove them in order to focus on the most promising ones.

The two remaining tacton sets are the result of an iterative exploratory and are to be compared in a usability study. One can be considered as a direct mapping of the underneath situation when the second provides an additional guidance.

Mapping
"""""""

This tacton sets simply encodes into tactile feedbacks what is directly underneath the device. It has been narrowed to three very strict rules:

- on a node, the actuators which direction corresponds to the direction of a connected node are up, the rest are down.
- on a link, the actuators which direction are parallel to the direction of the link are oscillating up and down on an high level, the rest are left down.
- on nothing, all the actuators are down.

When moving the device onto a node, some actuators goes from a down level to a up level: their is a high contrast between these two tactile situations which respects the criteria of a high contrast found during the second iteration. We have also made good usage of the duality of static versus oscillation as they both encode distinct facets of the exploration. Static is for the nodes and emphasize on pausing and maybe remembering this perticular point. Whereas, oscillations are for travelling between nodes and this constant feedback of the direction to go can be seen as an encouragment to proceed.


Guidance
""""""""

Very close to the previous set of tactons, Guidance offers just one more rule in order to help keeping track of the network.

- on a node, the actuators which direction corresponds to the direction of a connected node are up, the rest are down.
- on a link, the actuators which direction are parallel to the direction of the link are oscillating up and down, the rest are left down.
- near a link, the one actuator which direction is the closest to which the link is, oscillates in a low level.
- on nothing and near nothing, all the actuators are down.

Just as the Mapping set, this one respects the criteria established during the two previous iterations: high contrast and static versus oscillation for two different exploration phases. It includes a quick guidance that helps user to return quickly on their track. Even though a new tacton is used, the help provided can be worth it. The questions rised by this alternative are untangled in the Evaluation chapter.

.. TODO: figure of each context + for which it is applied

Remarks
^^^^^^^

I have not talked about a basic criteria which is to prevent a single tacton signal representing two distinct situations. It is the first level towards consistency, obviously.
As one would notice, the sets have been constantly moving towards simplicity and contrast. One can argue that providing guidance is obviously more usable, but since the beginning of my internship I have been surprised by the difficulty of finding the key elements for a good tactile sensation. I have not taken this for granted and this is why I felt the user study is justified. Besides, providing some analyse feedbacks on the differences of mapping versus guidance can surely be seen as a minor contribution in the understanding of tactile feedback based on vector for graph exploration.
We may appreciate the fact that, as an engineer it is easy to see many different ways to encode in tactons the underneath situation of a pointing device. As challenging as it seems, this approach does not consider the usability aspect.


Design of the hardware
----------------------

The HaptiQ receives the tacton signal to execute. The tactile sensation is coming from a rubbery cap that is being vertically moved by a servomotor controlled by an Arduino electronic card. These components are placed inside a 3D printed case. This chapter will detail each part of this hardware.

Actuator element
^^^^^^^^^^^^^^^^

An actuator element is made of the following parts:

- a cap with a rubbery feeling
- a vertical plastic stick that supports the cap
- a servormotor that transmits a vertical motion to the plastic stick
- a 3D printed servo-holder which offers an appropriate casing for the servomotor

All these elements were brought up by the collaboration of Simone X. and Eve H. who have previously worked on a first version of the HaptiQ. The cap is made from a special material that can be used by a 3D printer and this gives a soft, yet elastic feeling. The shape can be described as a segment with a height on a top of a triangle. The vertical plastic stick enables to move this cap above the servomotor and is fixed to it by a small rubber. The vertical servomotor are one of the best ratio of small and inexpensive - they cost each 12€ and are about 2cm in height. The servo-holder is a design made by Eve.

The main issue with this assembly is the lack of tightness, this is why I have drilled screws for giving a resting position of the servomotor and attached it with an elastic band to maintain it. This solution is non destructive (apart from the hole) which was important in order to allow other solution.
Other alternatives have been explored such as a high usage of bluetack - but it has been depreciated as it could not maintain the same height when a hand is gently pressuring the actuators.

.. TODO figure of an actuator

In order to work, the servomotor needs to be powered and controlled by an electronic board.

Electronic components
^^^^^^^^^^^^^^^^^^^^^

Arduino is an electronic card that is backed by a huge opensource community. This makes the workflow of running programs on it fairly easy and highly documented. Because of its flexibility, many other electronic firms have built shield or extension components to enhance the possibilities or the card. This is the case of the Adafruit card that we are using on top of a Arduino Uno. This extra shield allows to easily map the circuits of the servomotors to the Arduino card which enables their control in the programme.

In order to make the device nomad, two batteries are needed one for the Arduino, one for the Adafruit. Yet, the commands could not be received, which has led us to add a bluetooth component and turn the HaptiQ into a fully wireless device.

.. TODO figue of the HatpiQ electronic boards

Case
^^^^

The case is also a design provided by Eve H as she has preivously worked on another version of the HaptiQ. Having it this massive did lead to some concerns, but it is actually more impressive than a problem. Ideally, 

Besides, even though 3D printing is widely spread - the actual process of going from zero knowledge to the printing of such pieces can be and was time costly. For instance a poorly configured printer took about 30 hours to print all the mention parts for this device.

Although a new promising design was delivered by Eve, the timing was too short for a risk free transfer.




This chapter has described the design of the software, the tactons and the hardware. Furthermore, it has detailed the reason of the iteration over some of them. We end up having a relatively inexpensive device - around 300€ and reproductible. The software is opensource and using the HaptiQ interactions is cross-platform; it is even designed to welcome new interaction techniques for the device or to ease comparison. The implementation of this design has lead to some rationale desicions as well which will be detail in the Implementation chapter.


