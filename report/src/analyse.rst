.. 7p: 2110 words

Analyse
=======

The following chapter presents a background research on the technologies that can be used for graphs exploration without sight and a description of the contributions from previous work of the HaptiQ. It will first start with a task analysis on graph exploration.
This chapter aims at giving a wilder outlook on the alternatives and giving some understanding on what characteristics should be considered for graph exploration.

Task analysis
-------------

Finding visually impaired people for collaboration with is not an easy task. The partnership between IJA and ELIPSE tries to overcome this issue, yet many different projects are running at the same time and each one of them needs this precious collaboration. In order to avoid constant requests of their presence in the laboratories, ELIPSE has the undergoing policy to restrict these requests to the evaluation phase.

This makes the user centered development process not ideal. Nevertheless, I have managed to find other ways in order to seize the usability issues and being surrounded by sources focusing on the users.

- A direct contact with Bernard Orniola - one of the permanent member of ELIPSE who happens to be visually impaired, has provided me with some very key knowledge and understanding of this handicap in a day-to-day perspective
- My tutor Christophe Jouffrais has a long experience in working with visually impaired people and was able to emphasize on some aspects he could feel I was missing
- My participation in general meetings on larger project such as AccessiMap has given me insightful information on how to adapt a development process for blind people
- A direct contact with X. who was doing his master internship in the cognitive science field has been indicating me the limits of my design when exposed and showed to him
- Colleagues who have tried a previous version of the HaptiQ uncompleted have warned me about the major issues that they have experienced has users

By these proxies, I was able to come up wit the following task analysis.

Giving a blind exploration using only a haptic device and a trained user on the interaction techniques, the task would be decomposed into the following steps:

1. Feeling the device
2. Moving (depending on a strategy if one) and waiting a feedback
3. If there is no tactile feedback, continue moving
4. If there is a tactile feedback, processing to understand what is the information encoded this way
5. Given the new piece of information acquired, adapt the strategy of exploration
6. while exploration is not completed go back to step 2

These steps may seem fairly simple, it actually gives us some clues on the importance of having a very recognisable tactile signal as it plays immensely during the explroation phase.

Another interesting aspect is the fact that an exploration is the result of a sum of strategies. We can consider that finding the network is the first goal then it is to explore all the nodes, which can mean sticking as much as possible to the network. In order to help with these strategies, a solution could be to build tactile signal that would naturally guide for these strategies and confort the users in their choice.


Related research
----------------

Making an exhaustive taxonomy would be illusionnary as research related to haptics devices has been diversified and significally growing for the last twenty five years [ref needed]. Yet, this chapter will present the different technologies usable for blind people that could be used as a way to acquire data through graphs and maps exploration.

This background research is based on the doctoral thesis of Thomas_Pietrzak__ on "Dissemination of haptics information in a multimodal environnement" and on the master thesis of Simone__ on "The HaptiQ: A Haptic Device for Graph Exploration by People with Visual Disabilities".


.. ref needed
Braille
^^^^^^^

The braille is a tactile writing system that has been spreaded over the world since 1824. Although it could potentially represents some form of graphs with series of dots, arrows, bullets it is intended for text reading. The main issue remains the fact that it is difficult to learn and thinking that all blind people would know it is a common misinformation.


.. ref needed
ScreenReaders 
^^^^^^^^^^^^^

VIP rely heavily on their audio sens in order to compensate their handicap. This heavy usage would even trigger an "obstacle perception" [95]. ScreenReaders provides an efficient alternative to access text and many are available [#]_.
If only a few would enable navigation tasks as well like JAWS or VoiceOver, the main issue remains the usage of audio as a channel for spatial guidance. VIP are not necessarily inclined to use cardinal points neither up, down, right and left as a way of orientation and map exploration through a Screen Reader would require a constant audio feedback. Surely, this interaction may provide a useful help for graph exploration, yet it cannot be qualified as the most suited. Besides, it is preferable to interfer with the audio channel as little as possible in order to facilitate the debit of textual information expressed this way. In other ways, it would be beneficial to leave this interaction for more other type of information that work well with it.

.. [#] http://alternativeto.net/tag/screen-reader/ (accessed the 19/08/15)


Tactile Maps
^^^^^^^^^^^^

Tactile maps are paper heated to form bumps and relief in order to create shapes, lines and dots. They are popular among visually impaired people as a way to learn geometry or to explore a map. Even though they offer lots of tactile freedom - it is easier to grasp a general idea of the shapes by using the ten fingers, they do not provide further interaction unless they are combined with a tabletop such as the Multimodal Interactive Maps (MIMs) project [6]. MIMs is an input / output system mixing different technolgies. Such a system manages to keep the possibility of a ten fingers exploration, but require a new printing for each visualisation.
The main issue of tactile maps remains the fact that the scanning and printing process would require the help of another person and thus, do not contribute in the autonomy of VIP.


Machanical actuators 
^^^^^^^^^^^^^^^^^^^^

Presented as the technologic equivalency of braille, they can dynamically change a matrix of actuators in order to provide an information which can be a Braille symbol or simple shapes. This matrix can be placed on the finger zone of a mouse like the VTPlayer [ref needed] or the Tactiball [ref needed] which implies that the moving hand is also receiving the tactile information or it can be separated like the Tactos device [ref needed] but with a smaller matrix. The lack of success could be a result of poor quality in the software applications as suggested by Thomas Pietrzak. Given Jansson [84] mouses are not compatible with navigation tasks for visually impaired people.

Other displays like the Brailliant from Humanware [link needed] offers a full range of actuators forming braille letters, but remains fairly expensive.

A perticular case has to be made for the HTP - a precursor of the HaptiQ. One of my tutor - Miguel Nacenta, has been involved in the design of this input output device with a single actuator in the center [ref needed]. The purpose of the HTP is to explore other possible interactions with tabletops like their further work has suggested [ref needed]. It plays with unconventional outputs like friction and softness which can be integrated in various application. Although innovative, its usage is supported with visual elements and has not been though for visually impaired people.

Vibrations
^^^^^^^^^^

Some devices use vibrations in oder to provide feedbacks. Small vibro-motors can be attached to a glove which makes the device adapted to a hand like the Cybertouch [ref needed]. Or they could be integrated on a small surface imiting a matrix of actuators like the Optacon [ref needed].

Vibrations can be used in a matrix of thin vertical panels trigerring a feeling of cavity or bumps when sitting the hand to it as in STReSS [ref needed].

Electrovibration is used in the TeslaTouch and Revel systems [ref needed, ref needed]; it is imitating the sensation of friction and is therefore only perceptable when the fingers are in motion.


Forcefeedback
^^^^^^^^^^^^^

Forcefeedback has known a famous entry in the gaming field with Joystick and Wheels - but their application is far beyond that. One of the most recurrent name is the PHANToM [ref needed] that forces the point in certain directions. 
Forcefeedback comes in a variety of techniques in order to push a single point into a certain direction (articulated arm, pantographes, or pneumatics).

Having a single point of contact does not allow users to follow easily lines or understand shapes [ref needed] which make Forcefeedback not suitable for our project. 

Air
^^^

Feedbacks can be perceived via air motion. It triggers the same signals than with tactile thanks to the variety of sensitivy receptors [88, 101]. AIREAL [19] makes this approach possible and uses a motion detector camera as their input. Using highly pressured air wave allows long distance interaction (10m); it is besides scalable and affordable. Even though they offer a wide range of angle from which the air is pushed, the lack of resolution highly limits its usage. Besides, AIREAL is presented more as an interaction in order to enhance user experience than an input output system.

No hands involved
^^^^^^^^^^^^^^^^

(FIGURE: Homonculus sensoriel)

If we were to represent the human body by its touch sensitivy, we would end up with a weak figurine with enormous hands, lips and tongue.
This is maybe why bolder interaction are exploiting the latter with the Tongue Display Unit [9]. This display places a seven by seven grid filled with electrodes on the tongue and could be used in scenarios when both of the hands are taken: as for instance a working surgeon. And others would use the brow with the Forhead Retina System [ref needed].

Although intriguing both of these displays allow limited interaction and are suited for very perticular scenarios.


Previous versions
-----------------

FIGURE haptiQ evolution, tactons

In 2014, Simone I.C. has worked on a first version of the HaptiQ in the University of St Andrews. His development process was focused on the engineering of a device handling multiple actuators. These actuators could therefore have their own language in order to transmit information. He has designed multiple cases for embarking the HaptiQ and maintaining all the servomotors.

His work on a background research narrowed the disadvantages of other haptics solutions. He has also implied that a vector based mechanical actuator such as the HaptiQ is unique. His ideas on possible applications in order to help math signal representation (like in Figure ?) are highly valuable.

Even though, his design on the caps does not appear in his report, we are to give him credit for it. Although his work on tactons seemed promising, they could not be backed by any user study which forces to reconsider them.

He has also managed to extend this first version with button and has started to work on different possible interaction with pressure which still seems a valid option.

Finally he has pointed briefly the issue of having multiple wires running in order to control the servomotors which has led me to prefer solutions allowing the device to be as nomad as possible.


Conclusion
----------

Haptics devices demand material and often electronic circuits to be build. This result in a general expensive cost and is often dedicated to a specific usage. If our goal is to provide a solution for VIP around the world, then we were to take into account other aspects such as making it easily replicable and easing applications to be build on top of the key interactions like the Haptic Puck Tabletop and the Phantom. But this goal requires various skills and a carefull design.

Many alternatives exist, yet the issue remains that we are too focus on the way to represent data more than giving the underlying meaning of them. It might be more relevant to focus on the general trends more than the exact measurements. Let us remember that it is really hard to learn the simple knowledge of a squared angle for VIP. The challenge is there: trying to give a natural interaction for the strategies involved in an exploration. A way of solving it is to take a step back in the representation of information: we are not interested in the value of a perticular pixel but its meaning, its purpose. Is it a part of an edge? Is it filling a cue point? Or is it just random noise? These problems can be solved by giving meaning; this is why we are focusing only on graphs as they are a scalable and precise representation of the key information. Understanding graphs is mastering a way to easily acquire conceptual and spatial information.
(ref: 01__)
