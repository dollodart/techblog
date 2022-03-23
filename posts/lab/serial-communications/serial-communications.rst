.. _serial-communications:

Serial Communications
=====================

This post is a continuation of :doc:`../foss-controls/foss-controls` and
influenced by `Linux Serial HOWTO`_ [#]_. `Linux Serial HOWTO`_ is an excellent
combination of exposition and instruction needed to understand and practically
implement serial communications on Linux, being a Linux HOWTO. This post is
more theoretical and expository than instructive, and discusses serial
communication protocols and hardware used for serial communications and how
they relate to other communication protocols and hardware.

.. _`Linux Serial HOWTO`: https://tldp.org/HOWTO/Serial-HOWTO-1.html

Serial communications may be defined as communication in which all information
is put into a sequence to be read in order. Serial communication is in contrast
to parallel communication where some information is passed, often
simultaneously, in separate channels. Serial communication is used much more
because it can transmit general information, unlike parallel communication, but
it requires a nontrivial procedure of serializing the information to do that.
Even in modern networks like the internet which use packets to allow parallel
communication, there is a serialization done on the information, before it is
segmented for parallel communication (see :ref:`aside-on-network-comms`).  Hence serialization
is a more general concept than serial communication, and in fact is used even
in storing data on a computer, since memory is a serial register. This post
discusses serialization in the context of original serial communications.

Serial communication is a property of the communication method, not the data it
transmits (communication protocols are said to be transparent to the data which
they communicate). Some data doens't mean anything until you have more of it,
like an incomplete sentence, whereas other data such as streaming media has all
the information you need at the time it is made. Serial communication can be
used for communicating both of these kinds of data, though it is more often
used for the first kind.

.. rubric:: Footnotes

.. [#]

  Full references for material not linked are at the end of the post.

Serial Communication for Streaming Media like Music
---------------------------------------------------

A favorite application of serial communications is in recording and playing
music. Time clearly defines the sequence in a piece of music. In a musical
piece, some number of instruments make sound at the same time. The instruments
operate in parallel, but the effect on your ear or the microphone is serial;
every sound is superimposed on another, which leads to the musical effects such
as harmony where two or more instruments play notes with a given relationship
between the pitches at the same time.

The reproduction of music in electronics works on the same principle of
superposition. When a microphone records music, the superposition of presure
waves that is the sound one hears is the same one which deflects a diaphragm in
the microphone. The deflections are transduced to an electrical signal which
is stored in memory digitally. When a speaker plays music, the same signal is
read from memory, put into an analog signal, and transduced to deflections of a
diaphragm.

The simplest speaker has only two wires, one to put the signal in and the other
to take the signal out. The signal carries both the information and the power
to make the sound at the diaphragm [#]_. Headphone cables that have more than 2
connections have an electrical ground and some number of connections for
combined function devices, such as a microphone wire.  You can count the number
of connections by the spaces separating metal on standard cylindrical
connectors.

How can music transmission be so simple? It's because the ear is a remarkable
sensor and the human brain a remarkable computer.  The ear can resolve all the
frequencies (notes or pitches), at different volumes, present in the sound, and
the brain can then deconvolute the sound into the set of contributions from
instruments and voices. It is an active area of research to just identify a
singing voice in music, determine the pitches played in so-called polyphonic
audio signals, and identify percussive events from drums playing [#]_. Speech
is another remarkable thing we understand effortlessly given our tendency to
slur and mumble, and it is only recently (around 2017) that computer
scientists developed machine learning models that allow computers to recognize
human speech accurately to the level of humans without ever having heard a
particular person speak before, a task which is done effortlessly by most every
person. This technology is now applied in automatic closed captioning.

Computers transmit and receive sound data in separate, parallel channels. For
example, studio music is recorded on different channels which can then be
independently amplified. While some transforms of a music signal depend on its
properties, like upping or downing the bass or treble does on the frequency
band, if you want to make the drums louder, the only way to do that is to have
a separate channel, because the separation of music contributions from
instruments is still an active area of research and would anyway be
computationally expensive. The superposition principle of sounds allows a sound
signal to be put in one line, and it also allows parallel communication to be
done between devices which may want to manipulate independent channels and then
superpose the results. This superposition principle, however, doesn't apply
when communicating information.

.. rubric:: Footnotes

.. [#] 

  A speaker cannot necessarily act as a microphone, even though it is just a
  reverse operation. This is because the sound intensity at the microphone
  diaphragm is usually much smaller than the sound intensity at the speaker
  diaphragm.  This is the difference between a sound source and sound sink, where
  the sink hears an intensity which is the inverse square of its distance smaller
  than that at the edges of the source. A microphone diaphragm is thinner than a
  speaker diaphragm. 

.. [#]

  See Machine Learning Applied to Music/Audio Signal Processing.

.. _serial-comm-for-info:

Serial communications for information: Serialization
----------------------------------------------------

Unlike music, information cannot be serialized just by using
superposition of analog signals to another analog signal, at least not
efficiently [#]_. Instead, information must be transmitted
digitally. Digital serialization cannot be done by summing
superposition. For example, both

.. math:: 101+010\,,110+001

have the same sum :math:`111`. Instead, they must be serialized. One way of
serializing is to concatenate, like

.. math:: 101+010\to 101010\,,110+001\to 110001\,.

As just presented serial communications might seem trivial: given some data to
be communicated, just concatenate the data in some alphabetical or other agreed
upon order. If you need to specify where something is coming from or where it
is going to, you may put a receiving and sending address at the beginning
of the data stream (this is so-called protocol control information), like you
may put a receiving and sending address on the envelope containing a letter.

But there are many optimizations to be done when considering practical
implementations which makes serialization nontrivial.  Making an analogy of
communication protocols to transportation of goods, and this naive approach to
serial protocols is tantamount to saying "just stick everything in a bag and
put it on a truck". Here, networking protocols are not considered at depth,
which is analogous to the choice of which truck or whether a truck, train, or
ship. Instead, the serial communication protocol, in particular the
serialization, will be considered at depth, while taking it as given the
message data (not protocol control information) is already effeciently coded.
This might be analogous to how you arrange tightly packed goods in containers
for shipment.

As an example of non-trivial optimization, the data you want to transmit may
not be fixed size, so some identifying information has to be put between these
pieces of information. This is like how you might put a subject line or P.S. at
particular lines in the letter.

Serializing requires you to order and delimit the information. An analog signal
for music or television is naturally ordered because it is a streaming media,
that is, everything comes in order of the time that it is played. Information
doesn't have a natural order: if you ask someone about the weather, they
could tell you that there's a chance of wind and rain, or a chance of rain and
wind, and it means the same thing. So some order has to be imposed. In order
for that order to be recognized, the information has to be cut and delimited.
The information content of a music signal is instantaneous: whatever the wave
form is at an instant is what is played out the speaker (actually, if it's a
digital signal, it has a given time scale from its sampling rate which tells
the computer how fast to play it). But the information which is serialized can
span lengths and moreover varying lengths. While rain and wind are both
4-letter words, someone might tell you it will be cloudy, which is a 6-letter
word. In addition, they could tell you only that it's going to rain, or they
could tell you it's going to be cloudy and rain.

.. rubric:: Footnotes

.. [#] Modems, which make the curious sequence of noises people may recognize
  from the days of the early internet, do communicate analog signals. But they
  first serialize the data and then only did parallel transport of segments of it
  (this serializiation and segmentation may be the subject of careful
  optimizations for maximum bit rate, but is not the subject discussed here). In
  principle, given a sufficiently large discretization of an analog band, say a
  given amplitude can be divided into 1000 values, you could do some limited
  superposition of information signals. But this is not practical. Note that
  analog and parallel, to be discussed later, go hand-in-hand, because any analog
  signal has more than 2 states, so it necessarily can communicate more than one
  bit of information at a time, a fact which is important for modem optimization.


Example Serial Protocols
~~~~~~~~~~~~~~~~~~~~~~~~

What you are reading now is an output of a serial protocol, the (written)
English language. Natural language is so complicated that theories of grammar
are still being developed to explain them and computer programs to parse
natural language into grammatical structure are still imperfect (an example of
such a program is the `Stanford Parser`_). But there are many simpler serial
protocols in use for computers which one can understand with little study [#]_.

.. _`Stanford Parser`: https://nlp.stanford.edu/software/lex-parser.shtml

I'll take as example the XMPP for instant messaging (among other
messaging services). This is a high level protocol, but that makes it easier to
illustrate the concepts, and I already discussed the low level MODBUS protocol
:doc:`../foss-controls/foss-controls`, in particular,
:ref:`modbus-rtu-protocol`. In XMPP the data are sent in structured XML
snippets which include not just message data but among other things "presence
information", that is, whether a contact has their chat open or not.  XML is a
structured data language that allows any data type to be used (formally, it is
known as a matched tag coding of data [#]_). The delimitation is given by the
opening and closing tags which allow any data, including other data, to be
placed under a given data tag.

To illustrate this, I will take a natural language sentence and put it into XML
format. In writing we delimit words with blank spaces, sentences by periods,
paragraphs by newlines and indents, and sections by headings, among many other
delimitations in our grammar which aren't obvious like our orthography (such as
prefixes and suffixes usually requiring a consanant between them and a root
word). This example doesn't contain grammatical structure, but just the
information that a human reader or computer sees before doing any "real"
processing (this is called tokenization, incidentally).  Communication
protocols are simpler than our orthography and require only one delimiter. Even
tags in a high-level encoding like XML are really only one pair of delimiters,
<> or </>.


:: 

  <chapter title="Romeo and Juliet">
    <paragraph>
      <sentence type=question>
        <word>Art</word><word>thou</word><word>not</word>
        <word>Romeo</word><punctuation type=comma><word>and</word>
        <word></word>a<word>Montague</word><punctuation type=questionmark>
      </sentence>
    </paragraph>
  </chapter>

In XML, the white space is meaningless, and is just used here to imply the
structure that results from data being nested in other data.  Data is nested in
tags, and the tags are themselves having key-value pairs which are data. One
can see from the verbosity of this why we choose the indent for paragraph, the
period for sentence, and especially the space for word delimitations in our
writing. That verbosity in serial protocols corresponds to information bit rate, which is
meaningful. But XML has an advantage in being very flexible, and will shortly
be contrasted to more space efficient protocols which operate at a level that
doesn't require this flexibility.

Now consider the XMPP (this example message is taken from RFC 6121):

::

   <message
       from='juliet@example.com/balcony"
       id='ktx72v49"
       to='romeo@example.net"
       type='chat"
       xml:lang='en'>
     <body>Art thou not Romeo, and a Montague?</body>
   </message>

Serial communication protocols encapsulating this protocol (higher level
communication protocols are encapsulated within lower level ones) are more
limited in how they can transport information. For a given (or static) set of
information to be transported, however, the differences appear only in the
characters chosen and the possible omission of the tags, instead relying on
order of delimitation. Lower level protocols would use some characters,
possibly nonprintable ASCII control characters, to delimit variable length
fields in message and body, or fix the length of each field so no delimiter
would be needed, or it would have a field for how long the field that follows
it is. For example, the DASNET protocol at mod-spec-controls_ does the latter
for the message type field.

.. _mod-spec-controls: https://github.com/dollodart/mod-spec-controls

These lower-level protocols don't allow for dynamic data: that is, every
message would have to have the same data types in it (which may be called
fields, or other things). XMPP does allow for dynamic data, but it isn't
arbitrarily structured: it is tree structured, so that some data can be
contained in some other data and can itself contain any data, but cannot be
linked to, e.g., other data which is contained outside it but within its parent
[#]_. In formal words the abstract syntax allowed by lower level protocols is
less than that of higher level protocols [#]_. 

Formally, the XMPP has what is called type-length-value coding [#]_.
You can have length-value, like in DASNET, and type-value coding, as will be
shown below. A type-value or type-length-value coding appears to violate the
ordering requirement given in :ref:`serial-comm-for-info` because it allows you
to specify any number (or omit any number) of data fields and to switch them
around. But there is still an ordering in the ordering of key and value within
a key-value pair (which is typically key then value), and even when the
ordering of key-value pairs is arbitrary, one can impose an order which may
have some practical benefits.  The information content is now not only what the
particular information for a known type of message is (the value), but what
even the kind of information is being given (the key or type).  The type-value
protocols are approximately double as expensive because the to communicate a
given value you also have to specify the key which would be otherwise implicit
by the value position.

Now to enumerate the possibilities for delimiting fields (and omitting their
types), as would be done by a lower level communication protocol. Suppose all
messages were to have the above fields from the XMPP example. For demonstration
purposes I will consider encoding the message in a low level communication
protocol rather than consider a low level protocol would encapsulate the XMPP
message, though in practice the latter would be done. How lower level protocols
serialize the information when they encapsulate higher level protocols is a
good question, however, the process of multiple serializations for encapsulated
protocols is not treated here to any extent it can be considered different from
segmenting (which is discussed in :ref:`aside-on-network-comms`) . The message
using a fixed field length to 8 or 16 characters and 0-padding is: 

::

   juliet00example.com00000balcony0ktx72v49romeo000example.net0000000000000chat0000en000000Art thou not Rom^M
   juliet00example.com00000balcony0ktx72v49romeo000example.net0000000000000chat0000en000000eo, and a Montag^M
   juliet00example.com00000balcony0ktx72v49romeo000example.net0000000000000chat0000en000000ue?0000000000000^M

Here ``^M`` would be the ASCII code for a carriage return, not the literal
carat and character. Alternatively, ``^M`` could be used to delimit the
message, which is just substituting the XML tags with a single character
delimiter:

::

   juliet^Mexample.com^Mbalcony^ktx72v49^Mromeo^Mexample.net^M^Mchat^Men^MArt thou not Romeo, and a Montague?^M

If a user wants to place a ``^M`` in the text body, there must be so-called
character stuffing, or a special escape character which precedes that and says
this is not a delimiter.

Another possibility, giving more flexibility, is the number of characters could
precede each field, here in hexadecimal

::

   6julietAexample.com7balcony8ktx72v495romeoAexample.net04chat2en23Art thou not Romeo, and a Montague?1^M

This puts limits on how long each field can be, though, since to interpret the
correct hexadecimal number a specified number of hex-igits must be given. The
first fields in the above are allocated only a length between 0 and 15, or one
hex-igit. The message field is allocated value between 0 and 255, or two
hex-igits. 

One can also do a type-length-value serialization which almost as general as
XML in XMPP but it doesn't contain the structure information, for example, the body is
not contained in the message:

::

   fromuser6julietfromdomainAexamplefromsubdomain7balconyid8ktx72v49touser5romeotodomainAexample.nettosubdomain0type4chatlang2enbody23Art thou not Romeo, and a Montague?^M

Note the above is dynamic like XMPP so long as some convention is followed,
e.g., characters 0-9 and A-F represent numbers and so effectively delimit
fields. There are considerations to make for how robust these message protocols
are to errors, but that isn't discussed here (see
:doc:`../foss-controls/foss-controls`, in particular
:ref:`cyclic-redundancy-check`, for a short discussion on error checking using
checksums).

To summarize, the different communication protocols are [#]_ [#]_:

- Fixed-length or positional: static ordered set of constrained values
- Delimited: static ordered set of unconstrained values
- Length-value: same as delimited, up to some maximum length which can be specified
- Type-value: dynamic set of constrained values
- Type-length-value: dynamic set of unconstrained values
- Matched tag coding: recursive dynamic set (tree structure) of unconstrained values

.. rubric:: Footnotes

.. [#] 
  It raises a valid question why, given how hard natural language is compared
  to any communication protocol, we should require any learning to understand
  communication protocols. The answer is that we all have built-in brain organs
  that allow us to understand natural language without understanding at an
  explicit and conscience level its rules. It's one of the most remarkable
  things about the human brain: see, among many other resources, the popular
  science book The Language Instinct.

.. [#]
  See section 8.4 Matched Tag Coding in Hercog.


.. [#]
  See section 8.3 TLV Coding in Hercog.

.. [#] 
  Of course, one can define links in XML data structures using ids which allow
  for arbitrary graph data to be communicated. This is the highest complexity of
  data structure possible.

.. [#]
  See section 2.2 Protocol as Language in Hercog.

.. [#] Hercog would consider what I've presented here as only different types
  of encodings, the protocol being defined more by the fields present and how
  protocol entities exchange information. From a theory viewpoint the most
  interesting parts of a protocol are (1) its message encoding, (2) its
  "handshaking" or connection making process, and (3) error checking and
  correction. I have presented the message encoding as effectively different
  types of protocols without considering the latter two because I've already
  discussed error checking in a previous post and connection making for serial
  devices is, while theoretically interesting, too low of a level for me to have
  any knowledge on at this time. The majority of the Linux kernel is device drivers which probe
  devices to make connection. Log messages for these probes can be seen with the
  ``dmesg`` command.

.. [#] There is another classification of types of protocols (or their
  encodings) in the Encyclopedia of Computer Science. The types of protocols are
  bit-oriented protocols, character-oriented protocols, and byte count-oriented
  protocols. These are whether you consider 1 bit, 7-bits or another byte size
  for some character set encoding, or 8-bits at a time when receiving
  information. In the above I implemented everything as character-oriented
  protocols for ease of reading, but for simpler protocols such as positional and
  delimited a bit-oriented protocol is superior.  The receiving device can keep a
  table relating numerical inputs (as communicated by bits) to some meaning, so
  the choice between bit-oriented and character-oriented protocol depends on the
  hardware of the receiving device, the complexity of the message, and the
  bandwidth of the channel (since a byte-size character encoding needs 8 bits to
  send one symbol, whereas any number of smaller may be used by a bit-oriented
  protocol, provided you have a delimiter bit sequence). Lower level protocols
  tend to be bit-oriented as a result. 

Serial Hardware
---------------

The following D-sub connectors used for serial communications have a large
number of pins, indicated by the number following the hyphen: DE-9, DA-15,
DB-25, DC-37, DD-50. Given that serial communication is over a single line, the
most apparent question is why do serial cables have so many wires and serial
connectors have so many pins/holes? This question was briefly addressed in
:doc:`../foss-controls/foss-controls` (in particular :ref:`serial-devices`),
but is elaborated here to explain serial hardware (see also sections 4.1, 21.9
in `Linux Serial HOWTO`_ addressing this question).

Some connectors with large numbers of pins do use more than one pin in parallel
communication applications. For example, the DE-15 (more commonly known as VGA)
and DVI (which has 24 + 5 pins) have specifications which use 5 or more pins.
The principal reason for this is simply bandwidth, which increases by a factor
of the number of wires you are using (see :ref:`aside-on-parallel-comms`).
So one justification for why serial communication cables have so many pins is
that they are also used for parallel communications. But even in serial
communication protocols, the pins have many functions for which they were
designed. For example, in a DE-9, pins 8, 6, 1, 4, and 9 have functions other
than data transmission, while 3 and 2 are for transmitted and received data.

In principle serial cables could be like a headphone cable, having just two
wires, in and out, and for fault tolerance a ground [#]_ [#]_.  Serial cables
and their connectors were designed for equipment which needed to be controlled
independently of the data signals they were exchanging. This was for safety,
override, and interlock reasons. You didn't want just one channel over which
everything communicated, because any fault in that system would interrupt the
entire communications. The general engineering principle of independent and
loosely connected components for failure control was applied and different
circuits were used for the information stream(s) and any controls or signals.
Hardware flow control, which gives a specified set of pins exclusively some
functions, was more reliable at a time when the operating system was limited in
how well it could handle with the general hardware of the serial port
interrupts and other control functions [#]_. Now it is possible to have the
serial stream contain all of the information for the communication protocol,
including control information such as start and stop. This is part of the
general trend in computing where functions which were achieved by hardware are
virtualized into software. Modern serial hardware, such as USB, use far fewer
pins, as little as 4 for USB-B which has no hardware control.

.. _information-versus-power:

Information Versus Power Flow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The question as to why so few wires are used might be motivated by contrasting
to power applications, where you have thick wires to supply high currents even
at voltages much higher than used in computers (120 or 240 V versus 5 V). It
would seem a waste if in a power connector you only used one wire for power
when there were many others, and it would. But the currents in data transfer
are very small, and this is what allows data transfer to be so fast. The
semiconductor devices used for communication tend to grow smaller to improve
performance in many metrics, and one metric that changes is their capacitance
(amount of charge they hold or do not hold) decreases in the same proportion as
the transistor dimensions. An analogy might be how thin a glass capillary is
that you fill and empty with water to signal an off or on state. The time
required for that glass capillary for a given current is reduced by the same
amount as the water. But people want faster communications, so the rate at
which that glass capillary is emptied and filled is increased such that you
have the same flow of water into and out of the capillary. This rate of glass
capillary filling is for the semiconductor device an operating frequency.

The quantitative values for these trends are known as Dennard's scaling laws
(which have become obsolete since around mid 2000 but were accurate for around
30 years, but the basic physics principles for proportionalities are still
valid). Note these facts about transistors which are cited as scaling for
computing power in CPUs apply to every digital chip---even memory chips need
transistors to operate. In serial communications, voltage specifications remain
fixed at something like +/- 5V or +/- 12V because you have to have a strong
enough signal relative to the noise and resistance losses in the transmission
medium over fairly large distances of centimeters, meters, or longer. A
heuristic derivation of the current in a communication channel is then as
follows. In this model, I consider the communication as a thin wire channel
between two MOSFET transistors. The transmitter MOSFET has a signal attached to
its gate which permit current to flow out from one +5V terminal out of the
other terminal to the communication channel.  The receiver has the
communication signal enter at its gate and has a +5V voltage across its
terminals to reproduce the signal (but this is technically not a necessary part
of the model, as the transmitter alone defines the communication here).

1. :math:`CV^2f = P`. This is the definition of active power in a transistor. 
2. :math:`V = IR`. This is Ohm's law as applied to the transmission medium,
   where :math:`R` = line resistance.
3. :math:`I_{act} = CVf` is an approximate "active" current. The switching is
   approximately an alternating current (bits of zeros and ones don't tend to
   be mixed). Here :math:`f` = frequency of communication, :math:`C` =
   capacitance of transmitter/receiver, :math:`V` = transmission voltage. Note
   transmission voltage is fixed in serial communications, like +/- 5V, unlike
   over transistors. Ideally, transistors would operate as capacitors, as I
   just stated above, and those don't dissipate any power. But the above active
   power is the power which is dissipated on switching, and I am assuming the
   current which is dissipated in switching in the semiconductor devices is
   equal to the current through the communication channel, according to my
   simple model. In any case, it should be proportional, which is all that is
   needed for scaling laws (one can consider :math:`I = cI_{act}` for some
   constant :math:`c`).
4. Dennard's scaling laws would say :math:`I_{act}`, as long as this quantity
   is well defined, would remain almost constant, since capacitance decreases
   by the same amount as frequency increases.
5. Since :math:`I_{act}` (= current in the line) remains constant and the
   transmission voltage is fixed, the line resistance :math:`R` can also remain
   constant.

That is, as data transmission rate increases, the current remains constant, so
wire size can remain fixed. That doesn't mean the wire size would be small, but
that is the case since transistors used for communications started out
sufficiently small (and therefore with sufficiently small capacitance) and with
sufficiently low frequencies to be supported by their current wire sizes. In
fact, the first transatlantic communications were enabled by the hypersensitive
mirror galvanometer (and its automated successor, the syphon recorder)
developed by the scientist William Thomson (later Lord Kelvin). 

Quantitatively, information currents are milliamperes, as opposed to power
which can be amperes for household electronics. If power is like flowing water
through a 6 inch pipe at 10 cubic feet per second, then information flow is
like a flow of 0.017 cubic inches per second, which would only need a diameter
of less than 1 percent of 1 thousandth of an inch to have the same flow
velocity [#]_.

.. rubric:: Footnotes

.. [#]

  From `Linux Serial HOWTO`_, 4.1:  Besides the two wires used for transmitting and
  receiving data, another pin (wire) is signal ground. The voltage on any wire
  is measured with respect to this ground. Thus the minimum number of wires to
  use for 2-way transmission of data is 3. Except that it has been known to
  work with no signal ground wire but with degraded performance and sometimes
  with errors.

.. [#]

  It is possible to have only one wire, for example, the Dallas one-wire
  protocol. It is unusual to have serial communications over one wire because
  the electronic devices which transmit signals are different than those which
  receive them. You can make a switch so that it would go over one pin---you
  can also build a device which can do both transceiving and receiving, which
  is a transceiver (but the extent to which this is "the same device" versus
  something that switches between two independent units could depend
  significantly on application---in the simplest case, the only difference
  between receiving and transmitting is where the source is, but even here you
  need differences, because output power has to be much higher than input power
  from the square law of intensity, as was given for the case of sound in a
  microphone and a speaker. Wikipedia says transcievers are implemented usually
  as half-duplex, which in practice means some elements of the circuits for
  transceiving and receiving are shared and some are not. The Dallas one-wire
  protocol is used to send and receive on one wire between master and slave
  devices using a single transceiver. Each device has to have a ground in order
  for current to flow, otherwise there would be charge accumulation, but there
  doesn't need to be a ground wire between the master and slave. Dallas
  one-wire is generally used for simple slave devices like sensors.  Non-wired
  communication protocols also are effectively one wire, like antennas on cell
  phones, and in fact transceiver without qualification tends to mean circuits
  used for radio communications. 

.. [#]

  The original serial port buffer was only 1 byte, when today it is 16.
  Communicating control information over separate channels would have a
  significant advantage because the operating system has to be alerted
  everytime a buffer is filled.

.. [#]

  This dimension is microscopic and at microscopic dimensions, the conventional
  laws of fluid mechanics don't apply due to capillary effects. This is an
  example of the general difference between electrical and mechanical physics,
  namely that electrical physics have quantities that vary over many more orders
  of magnitude than do mechanical systems, at least those mechanical systems that
  we experience and can effectively construct and design (astrophysics has
  mechanical phenomena that span many orders of magnitude in mass and space).

.. _aside-on-parallel-comms:

Aside on Parallel Communications
--------------------------------

Already an example application of music with independently adjustable channels
was given for parallel communications. Any time a device needs real-time
updates of several data points it is better for them to be supplied
independentlyone so it doesn't have to deserialize mixed data from one line.
Another example is RGB video, which sends the red, green, and blue inputs down
separate cables. Since TV displays have separate "subpixels" for red, green,
blue (and in some cases also white) light, the TV can just forward the data
streams directly to the respective subpixels. Note that there is not parallel
cables for, for example, different quadrants of the screen.  The
synchronization and the spatial intensity are serialized within one color
stream because those instructions aren't parallel.  Just as in the case of
music, the parallel communication here is due to superposition: just like music
is a superposition of sounds from different instruments, a T.V. display is a
superposition of light from 3 different colors (note that superposition isn't a
requirement for parallel communications, though lack of superposition is a
requirement for serial communication, as given above). Printers are similar in
that they take multiple color data at the same time to give a point on a paper
a particular color. 

There are two more reasons why communication might be made parallel, in
addition to the fact the information to be communicated is fundamentally
parallel (like the different subpixels in a TV being almost like separate
devices):

#. Large amounts of data need to be communicated in short amounts of time. What
   defines large amounts of data and short amounts of time is the current
   technology. Modern network cards for personal computers can
   support 10s to 100s of gigabits per second. To give an idea, most people
   blink in about 0.1 seconds. At 1 gigabit per second, in the blink of an eye,
   there is 100 million bits communicated. With (extended) ASCII 8-bit encoding, this is
   12.5 million characters, which is using an average of 5 characters per word
   2.5 million words, or 81 copies of Shakespeare's *Hamlet*, the longest
   Shakespeare play. For this reason, as time goes on, communication tends to
   become digital and serial over analog and parallel.

#. The communication is one-way. A control computer only needs to know that a
   printer or display is working, which can be provided by one separate pin as
   part of hardware control, and otherwise requires no feedback. Because there
   are no interrupts other than "failure" or "error" from the slave device,
   there isn't any need to know what has been communicated to start, stop, or
   otherwise change what is being communicated.

As noted, there may be a natural ordering (usually time) and superposition of
the media which allows for parallel communication which would be superior to
serial communication. The serial accumulation would have to acquire a stack of
some memory before simultaneously displaying it to the screen. For example, if
you serialize color film you could at most display at a frame rate 3 times less
than the transmission rate, rather than equal to the transmission rate for
parallel communication. In modern technology, however, transmission rate is
rarely a bottle neck, again leading to the trend where communication tends
to become serial.

.. _aside-on-network-comms:

Aside on Network Communications
-------------------------------

Another question that may occur to you when looking at cables is how information
from the internet is transmitted by an 8-pin connector which is hubbed to other
8-pin connectors. The internet has billions of users and even the data transfer
rate for a single user is very high. It is common that one can download thousands 
of books in seconds.

First to discuss the hardware. The category 6 cable now in use for internet
connections, and generally network connections including local area networks,
has 4 pairs of twisted wire for 8 pins, a fairly small number. These do operate
in parallel and nowadays allow for hundreds of gigabits per second data
transmission.  In light of the above discussion
(:ref:`aside-on-parallel-comms`) it may seem remarkable that network and
internet connections, which are serial by nature of the connection between
either two peers or a client and a server (but not a master and a slave), would
be parallel over 8 pins. More remarkable is that these connectors are hubbed
and all computers in a network can talk among each other. The straightforward
send, wait, receive, wait cycle from master to slave doesn't suffice. The
technological development which allows for this remarkable communication is the
ethernet protocol (and its associated device technology).  Ethernet is a kind
of serial/parallel communication protocol over networks (I will call it a
network protocol rather than serial/parallel, because in fact there are
network-specific properties of communication protocols over networks). It was
accomplished in the 1980s, more than 20 years after the introduction of the
RS-232 protocol for serial communications in 1960. [#]_

Internet communication protocols serialize data but they do de facto
parallel communication through a network with many routers (and even the
parallel wires on the same cable) by a process called segmenting. After you
serialize information into a single data stream, you cut up that data stream
into segments and ship the segments with information on how to reassemble them
once they all arrive [#]_. In an analogy to shipping, this is like sending
several reams of paper for books each in separate packages with cover sheets
indicating the order to assemble them for book binding. The order in which the
packages arrive doesn't matter so long as they are marked with the order to
reassemble them. In fact, the analogy to shipping is so strong that when data
segments are put into their final communication protocol "package", they are
called packets. Just like postal packets, packets have information of sender,
receiver, and subject (in TCP header, these are source port, destination port,
and sequence number, where sequence number which indicates where in the order
the packet is in like the cover sheet in the analogy).

By segmenting the serial data stream and sending packets some delays or losses
in the packets, which may be frequent in such a massive network system as the
internet, can be tolerated.  Provided you have established what it is your
expecting, you can always know what's missing, and request it again.
Communication protocols can agree that when a router inspects what it is
shipping and it is so old it should throw it out, and this guides their
expectation for when they send a request for a missing for a missing packet. [#]_

You may question how the scale of internet communication could possibly be
managed. The answer is in the logarithmic growth of hierarchical systems in
terms of levels. Imagine if for every pair of computers (for a total of
:math:`n` computers) there was a router, and that each pair of routers
communicated up to one top router. In such a case, there would be required
:math:`n/2 + n/4 + n/8 + \ldots = n` routers to connect the whole internet. The
top most router would be at a level relative to computers at level 0 so that
:math:`n/2^h \leq 1`, or :math:`h >= \lg(n)`. For 10 billion devices, this is 34
layers of 10 billion routers, the router at a level :math:`i` routing
:math:`2^{i - j}` more traffic than a router at level :math:`j` [#]_. But it is
feasible to define gateway protocols for 34 layers, that is, protocols that
change communication between different hardwares optimized for different
traffic, for example, changes in the maximum packet size.

In fact, the analogy to the postal office here continues, because our postal
system is hierarchical in design and enormous in scale (in 2021, it delivered
128.8 billion pieces of mail, though this pales in comparison to the 2017
internet protocol traffic of 122,000 petabytes per month, which assuming 1 byte
per character, 4.7 characters per word, and 10000 characters per mail piece,
would give around 31 thousand-trillion equivalent digital mail pieces per
year). Post offices collect mail from residential areas (or at their office
location), and send it to distribution centers, which then send to distribution
senders, which then send to post offices, which send to residences (or hold at
their office location for pickup). Though this two level hierarchy appears much
simpler than the 34 level hierarchy above, within distribution centers there
may be several sets of collections that correspond to different levels. And in
fact using a branching factor of 2 is just for simplicity and 
unrealistic. If the branching factor for routing in the ISPs, meaning the
number of users or routers served by a higher level router, were 10 instead of
2, then only around 11 levels of routers would be needed (the bottom level
being the clients and servers). There are three tiers of ISPs above internet
users, though within each tier of ISP how many different router hardwares there
are is another question.

The other assumption of a simple hierarchy, in which a single router stands
between one and the other half of the world's devices, is false. The networks
are designed to be robust, with many redundant channels, and to optimize
traffic between servers which are often centrally located in special facilities
and user computers which are distributed across space, since user computers
rarely directly communicate. But the general mathematical result, of
logarithmic growth of network levels, is correct.

.. rubric:: Footnotes

.. [#]

  Like before, I neglect for the most part here the connection making, or in
  network protocols, the routing process.  This is the thing of greatest
  theoretical interest in network protocols, but not for the purpose of comparing to
  serial protocols.

.. [#]

  See chapter 9 Segmentation and Reassembly of Protocol Data Units of Hercog.

.. [#]

  The time-to-live and timestamping strategy for discarding messages is used in
  sliding window methods, in which there is a specified range (window) of
  packets the transmitter may transmit before it receives an acknowledgement of
  receipt from a receiver (section 12.6.2 of Hercog), though this strategy is
  implemented by routers and independent of the protocols in use by transmitter
  and receiver. The UDP protocol for sending datagrams without an established
  connection has a simpler strategy than this: the client just dumps everything
  if they don't get all the packets by a certain time, see section 9.2 and 9.3
  of Hercog.  However, at lower layers of the protocol stack there are
  implementations of Automatic Repeat Request Protocols (ARQ) in which "the
  receiving protocol entity detects corrupted and lost messages and informs the
  transmitting protocol entity about the success or failure of transfer; the
  transmitter retransmits the messages that have been corrupted or lost"
  (section 12.3 Hercog). 

.. [#]

  Fundamentally the question is what the average distance between a leaf and
  any other leaf is in a binary tree (in particular, the ideal "2-Cayley" tree
  considered here). The sum distances from a leaf to all other leaves is
  :math:`\sum_{i=1}^h \frac{1}{2^i} \frac{n+1}{2} 2(h+1-i)`, understanding that
  1/2 of all node are a distance :math:`2h` away, 1/4 of all nodes are a
  distance :math:`2h-2` away, and so forth. This can be simplified to
  :math:`\frac{n+1}{2^{h+1}} \sum_{j=1}^h j2^j` where :math:`h = \lg(n+1) - 1`
  is the height of the tree. The series :math:`\sum_k^n k2^k` can be solved by
  standard methods. Asymptotically, I find the sum distance from any leaf to
  all others goes as :math:`n \lg n`, which means the average distance goes as
  :math:`\lg n`, which is a very slowly growing number.

How do communications improve?
------------------------------

The ideal communication is 

- instantaneous, meaning it takes no time over any distance
- zero error, meaning the receiver receives all and only what the sender sends
- zero power, meaning the sender and receiver operate without consuming energy
- infinite volume, meaning there is no limit to the amount of data which can be sent

This ideal limit is impossible to achieve but as technology improves
communication moves toward it. One can track the history of technological
limits quantified in single measures such as

- Number of transistors per centimeter, Moore's famous law saying the
  transistor density in a microprocessor doubles every 18 to 24 months. When
  transistors become smaller the communications can become faster by Dennard's
  scaling laws, in particular, because of the switching frequency increase (see section
  :ref:`information-versus-power`).
- Modem speed, the rate at which information is sent along a modem line (the
  thing of interest here), which is called Edholm's law and is also an
  exponential growth at least from the years 1960 to 2000. After this time
  digital communication became just as good as analog communication over long
  distances, so the "serdes" hardware took over [#]_. A plot of the increase
  in bit rates for modems and computer peripherals is shown below. Digital network
  communications would be a better contrast but the data is split out nicely
  this way since all peripherals are digital. Download the processing script here: :download:`exp-growth-modem-bitrate.py`.

.. image:: exponential-growth.png

These measures increased because of developments of the transmitting and
receiving hardware, but there is one case in which the transmission medium was
developed with the invention of fiber optics cables. The internet travels along
the same medium of metal as power electricity for home lighting for most people
because in terms of cost and performance metal, in fact elemental metal such as
copper, is optimum. Transatlantic cables which carry the world's international
internet traffic over distances of thousands of miles do benefit from hardware
optimization, and in fact fiber optic cables have been used there for decades.

The other route of improvement is in the protocols and their implementations in
software. The theory of serialization is complete [#]_, like the theory of
parsing is complete for any programming language (considering all programming
languages to be specified with deterministic context-free grammar). There is,
though, engineering work to be done with complete theory, and in fact many
network communication protocols have been developed for different application
needs because the scale of internet communications makes careful optimization
worth it. The Internet Protocol suite has a long list of communication
protocols as evidence.  Because communication protocol in the Internet Protocol
suite are network protocls and so have serial and parallel components (parallel
resulting from the network transport of serial stream segments), the still
active research area of distributed algorithms may be applied to their
development as regards the parallel (and network or distributed) component, and
optimizations for different application needs may be done by the complete
theory of serialization as regards the serial component.

.. rubric:: Footnotes

.. [#]
  See "The World's Technological Capacity to Store, Communicate, and Compute Information" for a summary.

.. [#]
  Theory of serialization isn't a standard term, but I don't know of one. As
  presented here, it's a simple kind of source coding when you know every
  possible input to your source encoder.  Coding theory then applies here,
  which has standardized research areas, though they concern more difficult
  problems. For example, the best serialization achieves maximum data
  compression and minimum undetected error, and source coding and channel
  coding are the studies of these optimizations more generally. That is, source
  coding theory only assumes little about the input, such as if its image or
  video data, whereas in serialization you know every field and every possible
  value of that field. Channel coding is optimized to particular failure types
  which depend on the physical characteristics of the channel medium and its
  disturbances, but this amounts to probability distribution information and so
  is still quite general.

Conclusion
----------

Serial communication was defined, giving an example of streaming media (music)
and then a general or theoretical description. Types of serial communication
protocols were enumerated, or more precisely, serial encodings. A brief
discussion of serial hardware was given which explained why serial hardware has
so many pins/wires and why serial cables have remained unchanged even as serial
transmission rates have increased. For the purpose of comparison to serial
communication, brief asides on parallel and network communications were given.
Finally, a discussion of how communications improve based on the history of
communication hardware and protocol development was presented.

References
----------

- Hercog, Drago. Communication Protocols: Principles, Methods and Specifications. Springer Nature, 2020.
- Pinker, Steven. The language instinct: The new science of language and mind. Vol. 7529. Penguin UK, 1995.
- Ralston, Anthony, Edwin D. Reilly, and David Hemmendinger. Encyclopedia of computer science. Grove's Dictionaries Inc., 2000.
- Hilbert, Martin, and Priscila López. "The world's technological capacity to store, communicate, and compute information." Science 332.6025 (2011): 60-65.
- Lerch, A.; Knees, P. Machine Learning Applied to Music/Audio Signal Processing. Electronics 2021, 10, 3077. https://doi.org/10.3390/electronics10243077

Version
-------

First posted on 2022-03-22.
