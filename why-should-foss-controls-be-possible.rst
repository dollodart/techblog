Why Should FOSS Controls be Possible?
=====================================

From Process Dynamics and Controls, Seborg, Edgar, Mellichamp, Doyle:

::
    Because of their high performance, low cost, and ease of use, personal computers (PCs) are a popular platform for process control. When configured to perform scan, control, alarm, and data acquisition (SCADA) functions, and when combined with a spreadsheet or database management application, the PC controller can be a low-cost, basic alternative to the DCS [Distributed Control Systems].

Industrial hardware and software, and embedded processors, are highly specialized and lag behind consumer PCs for just about every metric except for reliability, because they are designed for a specific purpose. They don't have economy of scale and their cost to functionality ratio is therefore much higher than consumer PCs. In a laboratory, the use of a main server and thin clients can further reduce costs.

The linux kernel works well on machines of many types (including old and inexpensive ones) and at communicating with many peripherals. Over 50% of the linux kernel is drivers and one reason it managed to succeed as a free operating system is because it could run on the most hardware of any alternatives (citation: ESR, The Unix and Internet Fundamentals HOWTO).

Customized peripherals for controls have been enabled by a consumer revolution not only in computation but also in robotics and what might be called recreational electronics, and also the Internet of Things. Several DAQ boards are out of the box functional and easily programmed with Python such as LabJack and Raspberry Pi (the latter of which is integrated with an onboard Linux distro).

Finally, the development of Python and the many packages related to both hardware interfacing and scientific computing and visualization provide an abstraction layer which novice programmers can use in application with a much smaller barrier to entry than, e.g., writing full applications in C. Modern computational challenges are in two domains: scaling of approximation solution methods for ill-defined problems, and solving mathematically well-defined yet still computationally expensive problems. The problems needed to be solved in an experimental university laboratory are always small scale and most often computationally inexpensive, and so can be done by (high-level) FOSS software with generic FOSS compatible hardware.

This truth is acknowledged by, e.g., the efforts of implementing Python controls in CERN. This is most remarkable as CERN is the largest experimental apparatus, and indeed the situation isn't like for a university laboratory where high level languages and generic hardware can be used everywhere. Python and other FOSS libraries are only used peripherally at CERN for their analysis and settings, with proprietary software and custom hardware for directly controlling the accelerator. 

The two functions of a lab linux server or a set of distributed PCs are:

#. Provide terminals and GUI sessions to use spreadsheet applications, laboratory notetaking software, and for procedure display and check lists
#. Execute controls scripts and display real-time plots using Python and the many scientific computing, numerical computing, and visualization packages available for it

Many physical and life science laboratories are not outfitted with the latest technology, but this is not due to prohibitive cost but lack of knowledge. It could cost less than 10,000 dollars in hardware costs, and zero in software costs, to implement these solutions, which is less than 6 months of a graduate student's stipend. I illustrate this below:

#. Cost of an old linux server which can handle modest computational costs of experimental laboraties (mostly spreadsheet applications): 1500 $, alternatively 3 old/inexpensive PCs at 500 $ each
#. Thin clients for connecting to the linux server: 3 at 100$ = 300 $ (this cost could be avoided by a suitable peripheral and software to allow connection of all UIs to the server with different terminal instances)
#. Monitors, keyboards, and mice for user interface: 3 at 400 $ = 1200 $
#. High performance DAQ boards: 6 at 350 $ each = 2100 $
#. Power regulators, semiconductor temperature sensors, humidity sensors, thermocouples (K-type, W-type, others), instrumentation amplifiers: costs to balance (4900 $)
