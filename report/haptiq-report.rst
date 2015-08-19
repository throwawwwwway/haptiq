******************************************************************************
HaptiQ: a haptic tracking device with vectorial guidance for graph exploration
******************************************************************************

.. 150 words

Abstract
========

Graph - as a vector of information, is widely used; it is cross-cultural and does not require specific knowledge to easily learn from. Even though it is easily digitizable, accessibility for graphs is not the trend in today's research and technology progress. Meanwhile, the technology gap with visually impaired people is increasing and they are more and more likely to require assitance to benefit from this progress. There are 285 million visually impaired people worldwide: 39 million of them are blind, and 246 million have remaining visual capacities. Standard printed drawings and diagrams are not accessible to visually impaired people, which may have a general impact on spatial cognition and space representation. The HaptiQ is a haptic device providing mutliple tactile feedbacks in forms of segments. Such guidance would allow a more natural approach in graph exploration and therefore would contribute to blind accessibility with an easily repoducable and affordable device.


Keywords
========


.. 2p

Introduction
============

Graphs can be found in the undergrounds to help travellers find their way, in maps where paths connects various point of interests, in school books to help pupils understand abstract notions. They are a synthesized way to represent information and its usage is widely spread across countries and fields of study. We are so used to them, that our day-to-day life is filled by them without us noticing. This vector of information is not limited by the language, does not require perticular knowledge; it can be used for various context, for various data and can be easily digitilize and thus, transportable or modifyable. Yet its representation is graphical and therefore relies on sight. Finding alternatives in order to access these graphical information is a major issue for the visually impaired population to overcome. 

The digital gap is there, and while technology assist everyone's tasks better and faster, people with disabilities are more and more dependent on other's help to benefit from this progress.
Braille - which is considered to be the most used form of tactile graphics, is being depreciated for tablets. Although the latter allows enriched interactions and a comforting object to hold on to; they do not combine with the former. The need for a new vector of information is real.
More and more data is being produced, this comes with dedicated jobs like Data Analysts and dedicated research like Information visualisation. The increase of research activity in this field has been substential over the last 20 years. We are in the age of Big Data with challenges for a better understanding, visualisation, sharing; yet, accessibility tends to be neglicted.

In the laboratory of the SACHI team in St Andrews - Scotland, a small haptic device has been developed: the Haptic Tabletop Puck (HTP). By moving this special mouse, the user receives haptic feedbacks which can be used for exploration. Although this device allows multiple interactions, the main issue is that there is a single actuator for mapping the height of what is under. The way to explore would be to *bump* onto the limits.
If we were to build another device that would allow multiple feedbacks, we would have a more efficient exploration; users would feel where to go. If we were to have longer segment instead of single point under the palms, the users could follow directions. Such a device could be a first window in the accessibility of graphs exploration for visually impaired people as the interaction techniques would be purely tactile. Furtheremore, the audio channel is heavily used for accessibility and developing other interaction contributes in the global autonomy of visually impaired people.

The HaptiQ project aims to design and evaluate an inexpensive haptic device that allows blind users to acquire the representation of graphs and therefore, the key to the understanding of spatial information - like maps, or abstract concepts - like organigrams. The project is framed by Dr Nacenta (St Andrews, UK) and Dr Jouffrais (Toulouse, FR).

I will present in this report the main steps that has led to the creation of this device. I will explain the starting context of the project and the analysing phase; then the design decisions made for this project followed by the way I have implemented them. Finally, I will explain the methods used for the evaluation and an ending discussion about the results and a personal feedback on the skills in human-computer interactions that has been employed for this project.


Glossary
========

TODO

.. 3p

Context
=======

About accessibility
-------------------

Given the 10th International Statistical Classification of Diseases and Related Health Problems, there are four categories for vision:

	- normal vision
	- moderate visual impairment
	- severe visual impairment
	- blindness

Visual impairment includes the last two and from the World Health Organization, it concerns nearly 285 million people worldwide: 39 million of them are blind and 246 million have remaining visual capacities.

90% are in low income settings and 82% are above 50 years old. Being visually impaired is more often something we become and having to learn how to live without sight can be extremely demanding. Only 15% of the visually impaired people know braille. Designing and building software or devices that take into account this need of autonomy, is the real challenge.

In order to build and design for visual impairment, user studies and in-field usage are required. Since visually impaired people are difficult to reach, a partnership with 

.. figure:: cherchonspourvoir.jpg
   :scale: 50 %

   This organisation operates as a plateform of research for better autonomy of visually impaired people


Work environments
-----------------

The majority of the placement has taken place in the laboratory of IRIT in Toulouse - France. It has been the starting point where I have been immersed in a team fully dedicated towards improving accessibility for visual impairment through various project. 

A second 


Challenges
----------

Collaboration between two research teams
Adapt to multiple skills

Produce something adapted to visual impaired people
Produce something that could be easily rebuild
Produce something that is cheap


.. 8p: 

Analyse
=======

The following chapter presents a state of the art focused on the technologies that could enable exploration of graphs without sight. On a second part it will try to synthesise some knowledge gathered on the way mathematical concepts are taught or shared.
Making an exhaustive taxonomy would be illusionnary as research related to haptics devices has been diversified since ?? (01__). Yet, this chapter will present the different solutions available for blind people in order to explore through data.

This background research is based on the doctoral thesis of Thomas_Pietrzak__ on "Dissemination of haptics information in a multimodal environnement" and on the master thesis of Simone__ on "The HaptiQ: A Haptic Device for Graph Exploration by People with Visual Disabilities".

As for in-field observations, I have based my work on the following references: ...


.. 6p -> 3000 words

Related work
------------

In order 


Braille (ref needed)
+++++++

The braille is a tactile writing system that has been spreaded over the world since since 1824. Although it could potentially represents some form of graphs with series of dots, arrows, bullets it is intended for reading text. The main issue remains the fact that it is difficult to learn and thinking that all blind people would know it is a common misinformation.

ScreenReaders (ref needed)
+++++++++++++

VIP rely heavily on their audio sens in order to compensate their handicap. This heavy usage would even trigger an "obstacle perception" [95]. ScreenReaders provides an efficient alternative to access text. Several screen readers alternatives are available [#]_.
If only a few would enable navigation tasks as well like JAWS or VoiceOver from Apple, the main issue remains the usage of audio as a channel for spatial guidance. VIP are not necessarily inclined to use cardinal points neither up, down, right and left as a way of orientation and map exploration through a Screen Reader would require a constant audio feedback. These aspects disqualify this medium as the most suited.
Besides, it is preferable to interfer with the audio channel as little as possible in order to facilitate the debit of textual information expressed this way.

.. [#] http://alternativeto.net/tag/screen-reader/ (accessed the 19/08/15)


Tactile Maps
++++++++++++



3D printing
+++++++++++

Dynamic Braille Display
+++++++++++++++++++++++










.. 2p -> 1000 words

General observations
--------------------


Conclusion
----------

Many alternatives exist, yet the issue remains that we are too focus on the way to represent data more than giving the underlying meaning of them. It might be more relevant to focus on the general trends more than the exact measurment. Let us remember that it is really hard to learn for VIP, the simple knowledge of a squared angle is not easily acquired.
(ref: 01__)

The following list states the properties to be taken into account. It is a result of these background researchs and gives the direction towards what we want to go.


.. 8p

Design
======

Global design
-------------

Design of the software
----------------------

Design of the device
--------------------

Design of the interactions
--------------------------


.. 8p

Implementation
==============

Iterations of the software
--------------------------

Iterations of the interaction techniques
----------------------------------------

Final state
-----------


.. 7p

Evaluation
==========

Hypothesis
----------

Protocols desgin
----------------

Results
-------


.. 3p

Discussion
==========

About the project
-----------------

Acquired skills
---------------

Remarks
-------

This report has been generated with RsT, which in my opinion is a technology to keep a close eye on. It is the official technology for Python which is considered to be one of the most developer friendly language because of their philosophy, and this has extended to the way they would create documentation.
Another thing is that it is open-source and does not require a very complicated setup.



.. 1p

Conclusion
==========

UX designer has increased in the UK, the US... it's becoming interesting for european countries. Yet, France industrials do not consider as seriously as these other countries. How we, ENAC student of the Master IHM can stand for more usability in the software development in France? Besides software development has starting to be outsourced for cheaper wages. Lived in romania... IT students should be concerned about this, as they will not be able to compete very long. I see two possibilities to maintain (interest), being an expert in a particular technology or starting to 
This is the kind of things I think would be beneficial for students to hear from our teachers. 

Justifying is key to ux, and reporting is key for justification. My placement has lacked of reporting as it was difficult to understand what needed to be retracable and what not. Started with a board journal, but it's actually killing the information. Better is to focus on main steps like brainstorming, informal evaluation, 

This report may take some strong position that better experts than me could easily critcise, and I would be happy to see them. I have just started to grasp to idea of a good UX design and this report can be seen as an effort to summarize my understanding.

This report has also been emphasizing the development side of the internship on purpose. UX designers are the interpret between users and developers. They should have a global understanding of computing as well as human behaviors. From my point of view, a good UX designer should be able to easily switch between platforms and limit his preferences, he should have also invested enough time to understand the tricks and ways of upcoming development process and that requires to deal with less user friendly tools. Yet, it's necessary to take this path. I am convinced that quality code and efforts made towards best practices lead to better design in the end by time saving, easy iteration and codeveloper friendly.



The work becomes research once the last sentence of the report written. Like, problem we allow people using results, but how about the device itself? Research can also consider the fact of making your project redoable.


yeah sure!

Bibliography
============

[95] Vincent LE ́VESQUE : Blindness, technology and haptics. Rapport technique, McGill University, Montre ́al, Que ́bec, Canada, 2005.


.. .. 8 pages
.. Analyse
.. =======
.. (key concepts: having a clear understanding of what is going on with visually impaired people)

.. State of the art
.. understanding the usage (constant talking with VI supervisor Bernard, exploring documentation made about VI)
.. scenarios
.. tasks modeling
.. brainstorming


.. + interviews, personas


.. .. 10 pages
.. Adapt
.. =====
.. code engineering (evolutive structure, identifying what is key)
.. testing and coverage (how to make sure the whole is still functional if we add change one thing?)
.. python (developer friendly)
.. versioning (tag previous versions, can come back easily, facilitate open source)
.. documenting (why? -> , how?, small remark about comments)
.. refactoring (helps understanding the code and the logic better)
.. iterative ( )
.. polyvalent (3D printing, TUIO, )
.. communication skills (two labs, two different views of the final build, different ways: latex, )
.. proactive intelligence (explaining why, how: twitter, feedly, reddit)
.. planning?


.. .. 8 pages
.. Justify
.. =======
.. (key ideas: HCI can be easily countered, tests are ok but eaisly falsiable, but how about we - UX designer create a clear way of justification our work, requires a lot of honesty, but it could be very beneficial and we can have an immediate feeling of how suitable for users the product is, this why I would like to suggest this recap)

.. - why not using dream -> unhappy with software and think it misses the point, yet, it's a good effort towards design justification
.. why not purely citing papers -> my opinion is that papers should be referenced for critical stuff, also citing a paper can be misleading. The academics field knows that there is a variety of quality in papers and scholars know how to evaluate it, but how about others? If your work is to be kept in this field, no problem, but if we were to think UX design with an open-source perspective, we will be able to benefit from it only if we make the justifications readable. Citing a paper does not make it readable, it just adds a step of complexity for an idea that could be summarize in one sentence. 


.. .. 8 pages
.. Evaluate
.. ========
.. (key idea is that this evaluation phase is for users only)
.. user study (iterative, approuved, self testing, real testing, logging)
.. informal testing (iterative, various persons, enrich the development, quick enough to be done on the spot -> force you to always have something to show)
.. personal critic (okay that one is far fetched, but there is a reason to continue to have a critic eye on one's work, you need )
.. statistics

.. + more users? more VI?