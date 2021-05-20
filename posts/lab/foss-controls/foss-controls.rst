.. _foss-controls:

FOSS Controls
=============

There are many layers of abstraction used in the interface of a computer
and peripherals (from now on just called devices) like process equipment
microcontrollers. One of the difficulties is that in the abstract
space of programming, the only thing that exists is the classification
because you can't see the thing which is being classified. But this
classification is not strict, and abstraction layers meld into each
other, especially as technology improves. This difficulty is compounded
by vernacular which comes from different field and communities and which
evolves over time. This post endeavors to explain some basics on serial
communication and controls with FOSS by giving the classification,
explaining the fundamentals so ambiguities in classification can be
resolved, and providing scripts and references which can be used as a
starting point.

LabVIEW is a commonly used commercial software provided by National
Instruments used (mostly) on Windows operating systems for controls. In
this post I present the case for the alternative of FOSS for controls on
Linux distributions.

Linux distributions are reputed to have a steep learning curve relative
to other operating systems. But their interfacing with devices is better
than Windows and in many cases there is plug-and-play result.

I divide the controls set-up into two steps:

#. Setting up communication between the primary device (computer) and
   secondary devices (computers and microcontrollers).
#. Developing and executing control scripts, which I discuss in :ref:`control-scripting`.

Setting up Communication to Devices
-----------------------------------

I quote here from the `Unix and Internet Fundamentals HOWTO`_:

    many Linux old-timers think the cleverness of Linux's boot-time
    probes (which made it relatively easy to install) was a major reason
    it broke out of the pack of free-Unix experiments to attract a
    critical mass of users.

.. _`Unix and Internet Fundamentals HOWTO`: https://tldp.org/HOWTO/Unix-and-Internet-Fundamentals-HOWTO/

The reason this is relevant is that within a computer there are devices
which send data using communication protocols, so an operating system
that is excellent at probing devices in the computer will also tend to
be excellent at interfacing with external devices.

If your process control equipment has a computer in it, by which I
mean desktop computer running an operating system as found in many
scientific instruments, then the communication is effectively network
communication. In that case many of the network protocols such as secure
shell (ssh) or Transmission Control Protocol (TCP) can be used, and it
is equivalent to communicating with a a server in a Local Area Network (LAN).

There are varying levels of complexity down from an operating system
(OS), which I categorize at four layers. At the bottom there are simple
electronic circuits, which might require bit banging if they were to
be connected to a computer directly. However, using a Data AcQuisition
(DAQ) board and associated Application Programming Interfaces (APIs)
like the one provided by LabJack avoids the need to do low-level
programming. So I will discuss only the first 3 of the 4. Note I am not
an expert in these standards and more expert people may disagree with
this classification, along with other points in this post--please
direct criticisms by consulting :ref:`the contact page <contact>`.

My rank of electronic complexity and corresponding communication protocols/hardware standards is:

#. Computers with network communications (IP/Ethernet)

#. Modern Universal Serial Bus (USB) serial devices (USB CDC/USB)

#. Serial devices (MODBUS/RS-232)

#. Simple electronic circuits (??/I2C)


The process of communication has the following steps which I will discuss in order:

-  Encoding: Sequence of Characters :math:`\to` Sequence of Raw Information Bits

-  Packing (Communication Protocol): Sequence of Raw Information Bits :math:`\to` Sequence of Packaged Information Bits

-  Sending: Sequence of Packaged Information Bits :math:`\to` Sequence of Electrical Pulses

There are also the inverse operations of receiving, unpacking, and
decoding. These inverse operations do not require new concepts to
understand and so are omitted.

An aside on naming: by convention some people, call RS-232 and other EIA
standards "serial communication", e.g. in the `pyserial`_ python package
and even by myself in this post. But serial communication is actually a
class of communication protocols meaning all the data is transmitted in
one line (allowing for hardware flow control in other ones). You can see
this in the naming of USB as a Universal *Serial* Bus, and also in the
different Advanced Technology Attachment (ATA) hardware, which was first
parallel before the development of the standard Serial ATA (SATA) and
renaming of the original to Parallel ATA (PATA). This might be because
RS-232 and other early standards were the first standards for serial
communication hardware and protocols. These standards were used for
`connecting teletypewriter (tty) terminals to early operating systems`_,
which is also the reason that ``tty`` is mentioned here, in the ``stty``
port configuration, even though serial communication is not specific to
that between computers and real or virtual/emulator tty terminals. 

.. _`connecting teletypewriter (tty) terminals to early operating systems`: https://en.wikipedia.org/wiki/Teleprinter

Encoding
--------

Computers work with sequences of ons and offs represented by 1 and 0
(electrically, by an electric charge or voltage and the absence of
an electric charge or voltage). To represent numbers, the numbers
have to be encoded in such a sequence. This can be done by a binary
representation of numbers, like the below table shows:

.. csv-table::
   :header: "base-10", "base-2", "8-bit representation"

    "0","0","00000000"
    "1","1","00000001"
    "2","10","00000010"
    "3","11","00000011"
    "4","100","00000100"
    "5","101","00000101"
    "6","110","00000110"
    "7","111","00000111"
    "8","1000","00001000"
    "9","1001","00001001"
    "10","1010","00001010"

While binary representation is required, the length of the number
(how many digits it must have, including leading zeros) can be
different. Above is an 8-bit representation. A number may be represented
with any bit representation provided that number is less than 2 to the
power of the number of bits. If it seems like you could just concatenate
several 8-bit representations, consider how a computer would interpret

.. math:: 0000000100000001\,,

which could be either :math:`2^1+2^1 = 4`, or :math:`2^9 + 2^1 = 514`.
In practice, 8-, 16-, 32-, or even 64-bit representations of numbers
are taken, the bit value being specified for some file type or address
field (in a memory not managed by a file system). The reason to use
smaller bit representations is to save space in case all your numbers
are small. You might wonder if there were a set of numbers that meant
"interpret the next x set of 8-bits as one number". This is done in
many encodings and these are called escape sequences, and if done
correctly it saves space, since the extra space required to encode
escape sequences and put in extra checks for data integrity in case
those important sequences get corrupted is less than the space you
save by having mixed bit representations. But this compression is not
further discussed as it isn't part of any of the communication protocols
explicitly discussed or necessary to understand them in general.

The binary representation is all that is needed if only numbers are in
a message. But characters, like the 26 letters in the alphabet, require
an encoding. There has to be a standard for sequence of 1 and 0 which
means A, another sequence of 1 and 0 which means B, and so on for every
letter of the alphabet. ASCII is a standard for 8-bit encoding (it
was first 7-bit but later extended to 8-bit to allow more characters,
though some people call the various encodings which extended ASCII
Latin-1 and keep ASCII to mean the original 7-bit encoding). With
only 256 possible things it can encode, it communicates large numbers
by their concatenation in some base. For example, 213 would be sent
as 3 8-bit representations of 2, 1, and 3 in sequence, or maybe in
hexadecimal as the 2 8-bit representations of d and 5 in sequence.  It
has encodings for not only the 26 letters of the alphabet, but some
more, since 7-bit (and the later 8-bit) allows for 128 characters
(or 256 characters), more than the 26 + 10 needed for letters of the
English alphabet and numbers in base-10. These other characters are
punctuation such as comma (,) and quotation ('), control characters
such as forward slash (/) and backslash (\), as well as non-printable
characters. Non-printable characters include the bell character, for
communicating "make a sound", the line feed for communicating "put
the next characters on a new line" or is commonly interpreted as "end
of command", and the carriage return which has a similar purpose as
the line feed. Of special importance here are the four device control
characters, which don't have definitions specified by the ASCII standard
but have come to be used in particular ways for program signals (see
later discussion in :ref:`port-config-signals`).

The below script shows the text "hello world" in 8-bit ASCII, though
for these characters, 7-bit ASCII would suffice. The ASCII encoding is
simple and requires only looking up entries in a table (in Linux systems
the Command Line Interface (CLI) ``ascii`` displays the 128 original
7-bit ASCII encodings in a table). Encryption, encoding which can only
be undone by having secret information, is a much more interesting
field, but is only necessary for security purposes and the communication
protocols explicitly discussed here don't support it.

.. literalinclude:: ord.py

Communication Protocols
-----------------------

Communication protocols do the packing (and unpacking) of the raw
information, now encoded into bits, so they can be transmitted. This is
analogous to packing an item for shipment by the postal service. Like a
shipping box, there is information in the packaging used for information
being sent, such as sender, receiver, and function (you might write
Merry Christmas on the outside of the packaging). Complicated
communication protocols, like the internet protocol, have several
layers, each with its own packaging. Since packaging is within
packaging, this is called encapsulation. In analogy, you may wrap and
seal a fragile item for long transport inside a shipping box. Even
the simplest protocol for serial devices discussed here has two
communication protocols, RS-232 for the outer one and MODBUS RTU
for the inner one. Higher level protocols (example MODBUS RTU) are
encapsulated in the lower level ones (example RS-232), which doesn't
exactly agree with the analogy here where a shipping box encapsulates
foam-wrapped items. The reason for this is that each part of the data
from a higher level protocol is encapsulated in a frame of the lower
level protocol. This would be like if you were to wrap letter blocks in
foam which spell out the address and send them one at a time to the post
office, then send them the foam-wrapped items you want to deliver. Still
the analogy in other ways is informative and kept here.

Communication protocols have hardware standards along with them. That's
why you hear things like "serial cable" and "serial port". These
hardware are also discussed in this section. Note a hardware standard
for a given communication protocol often allows for more than one piece
of hardware for a given function, e.g., the connector (DB-25 vs. DE-9
among others for the RS-232 and other serial standards). The same is
true for settings of the communication protocol--standards rarely
specify single values and instead give sets or ranges of allowed values.

Network Communication
~~~~~~~~~~~~~~~~~~~~~

For network communications, at least one of the computers must be set
up as a server to receive network requests from another one. This
communication can still be two-way, since the server can write to files
it has based on write requests and return data from read requests made
by the non-server computer.

Network communication is at the highest place more complicated than the
others. Network communications are also (at least for the purpose of
controlling lab equipment) plug-and-play. At the time of publication
in 1989, RFC1112 1.2.4 stated there are no self-configuring host
implementations of the IP protocol. But developments in the early 2000s
led to the Dynamic Host Configuration Protocol (DHCP).

Because of these things, I will skip this and instead give a simple
control script using network communication, the Secure Shell (SSH), in
the second part.

Modern (USB) Serial Devices
~~~~~~~~~~~~~~~~~~~~~~~~~~~

As a brief aside, USB does support network communication (there is the
`usbnet driver`_ for Linux). And commonly ethernet and TCP are used
for non-network serial communication, like master-slave communication
between a computer and a LabJack DAQ boards. However, USB is more often
supported and at lower costs. The only advantage of ethernet for most
laboratory applications is longer cable range, which can anyways be
dealt with by USB cable boosters. So I limit discussion of modern serial
hardware and protocols to USB.

.. _`usbnet driver`: http://www.linux-usb.org/usbnet/

In the intermediate device complexity, the device that plugs in is
recognized by the kernel, logged in the kernel ring buffer (view by
``dmesg``) among other places, and assigned a port in ``/dev``. These
can either use the Universal Serial Bus (USB) protocol directly, or use
a Communication Device Class (CDC) specified in the USB standard, one of
them being the Abstract Control Module (ACM) (see `this blog post`_ for
more information on the differences between USB and USB CDC).

.. _`this blog post`: https://rfc1149.net/blog/2013/03/05/what-is-the-difference-between-devttyusbx-and-devttyacmx/

As the blog post says, USB has a specification for analog modulation
to a phone line using a USB device, which would convert rectangular
sequences of 1s and 0s to some analog waveform like for dial-up
connections. Exactly how this is done can be complicated, since 
modulation protocol has been optimized for maximum bit rate, but in any case it isn't
relevant for digital serial communication (which is what you need for
a modern lab). The ACM device pretends to be a modem in the case it is
used for digital serial communication, but never uses a modem to convert
the instructions given to it in the ACM CDC protocol. A USB device
doesn't pretend to be a modem.

The communication between the device and the USB port on the computer
is digital in all cases, USB and USB CDC ADM (even when actually used
as a modem). The communication isn't simply "null modem" (which you
can think of like extension cord). That's why the USB hub inside the
computer is assigned a separate device label than whatever device you
connect to it. The USB hub inside the computer has a card and PCI
connection to the motherboard. Usually privileges come with that PCI
connection (PCI is one type of the class of IO connections internal to a
computer), such as an Interrupt ReQuest number to signal to the CPU that
the buffer has filled up or emptied and it needs to receive or transmit
data. But unlike the older serial protocol, USB is designed to have
up to 127 devices using the same interrupt signal. This allows you to
daisy chain USB hubs, so peripheral USB devices have access to the CPU,
though they must make the request through the USB host to which they are
connected. Of course, the USB hub supports communication with terminal
USB devices, like a mouse and keyboard, which is another reason why the
port needs a card.

According to the `LDP Modem HOWTO`_, RS-232 and USB both support modem
devices.  Both USB nor RS232 standards are for digital communication,
But they are are used to connect to a modem because they have serial
communication protocols. There are two functions you need for
transmitting and receiving from a digital computer through an analog
medium: one, to transmit and receive signals continuously through time
by reading from buffers and sending interrupts to the CPU, which is
the serial function of taking data possibly from parallel sources and
encoding/compressing/packaging it to a single stream. Two, to change the
signal to an analog one and use something like frequency multiplexing
and data compression which is specific to analog signals. You can use
a modem which has only the second function if you have a port and
communication protocol which accepts serial communication and acts
between the computer and a modem which does only the first function. The
author provides `a schematic of this`_ for the data buffers in the
HOWTO. The UART with 16 byte FIFO buffer is the serial device between
computer memory and CPU and the modem:

.. _`LDP Modem HOWTO`: https://tldp.org/HOWTO/Modem-HOWTO.html
.. _`a schematic of this`: https://tldp.org/HOWTO/Modem-HOWTO-4.html#ss4.10

Network cards using the LAN Ethernet hardware standard and IP
communication protocol are "digital modems" that do the first function
only and don't require the second function, since the hardware layer
they communicate over is for digital signals. So-called "digital modems"
might be better called "serial cards", though they may do more than a
UART and are properly called "terminal adapters" according to the Modem
HOWTO. There are also "soft modems" which rely on the CPU and RAM to do
the first function (or most of it), and only (or mostly) do the second
function of converting the digital stream to an analog waveform. Modern
network cards like those for gigabit ethernet use the term Serial
Deserializers (SerDes), which follows the same naming convention as the
modem and show they only do the first function.

Modern serial USB devices are hot-pluggable, meaning the device can be
put in while the computer is on rather than before start and the kernel
will recognize it. The device will respond to queries by the kernel
about its make, model, sub-model or ID number, along with communication
protocol settings, in a process called handshaking. The kernel will
assign a devince name, which one can see in the output simply by
``diff``'ing the dev directory before and after plugging the device
in. I've found ``dmesg`` won't show the DEVNAME, probably because the
device name is assigned after the kernel discovers the device up by the
``udevadm`` daemon, but one can look this up by reading the product
ID from ``dmesg``, then searching for it in the output of ``udev`` by
``udevadm -e | less``.

This assumes the port you are connecting to (the card with an IO
connection to the motherboard) is already assigned an IO address, IRQ
number, and device name. You should be able to see the port details in
``lsdev`` (in this case also ``lsusb``) and more detailed information
in ``udevadm -e``. The Linux HOWTOs tell you how to do low level
programming in the unlikely case the port isn't recognized.

Before communicating with the device instructions and data, you may
need to configure the port for the particular communication protocol
(this is an encapsulated communication protocol, not the RS-232 or USB
one). For the USB device, handshakes communicate to the kernel what
the settings are (or at least the different settings can be tested by
the kernel until a response is received) so that programs, such as the
terminal emulator ``screen`` called by ``screen /dev/devname``, often
don't require the port to be configured by the user (see the `section
on tty window types in the screen manual`_ for more detail). If that
is the case it is only required to start the terminal emulator and
enter strings which are valid for the encapsulated communication
protocol, since the encoding of the characters in these strings
and the outer communication protocol is managed by the terminal
emulator. Because of this a discussion of these settings are deferred to
the :ref:`serial-devices` section where such handshaking with the external device isn't supported.

.. _`section on tty window types in the screen manual`: https://www.gnu.org/software/screen/manual/screen.html#Window-Types

.. _serial-devices:

Serial Devices (UART/USART)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The device type Universal (Synchronous) Asynchronous Receiver
Transmitters (UART/USART) accept what is compliant with RS-232, the
later RS-485, or other EIA standards for serial communication. Devices
with UART can be identified by having the serial connectors, like
the DE-9. It may seem contradictory that serial communication, which
is communication over one line as opposed to parallel
communication over many lines, should use 9-pin, 15-pin, 25-pin, 37-pin, or even
50-pin connectors. But only 2 pins are used for data, transmission
and receiving, in these standards. The rest of the pins are used only
to communicate information controlling the data transmission, like
if a device is ready to transmit or receive. These control pins are
said to be used for hardware flow control. These standards are over
50 years old and are designed for old technology which didn't have as
cheap or reliable computing power for software flow control. USB 2.0
type A uses software flow control and so limits the number of pins
to just power, ground, transmit, and receive. The standard reverted
somewhat to hardware flow control with USB type C connectors which has
two "configuration channels", but this is mostly because of the large
diversity of devices and protocols USB supports, and the configuration
channel can anyways be also used as an additional power line.

To plug serial devices into a computer which doesn't have serial
ports, you can use a serial-USB converter. For serial devices you
take a null modem cable between the internal serial port (or the
external hub connected by USB) and the port on the device you are
connecting to. Unlike the modern serial USB, the device shouldn't be
recognized--you input to the serial port which will transmit and receive
to a device unknown to the kernel. There are no RS-232 to RS-232 hubs
because the serial port can only use one IRQ.

Generally you have to configure the serial port to transmit correctly
to the device of interest since the kernel is unaware of the external
device. That is discussed in :ref:`configuring-serial-ports`. But there
are values which are used as default from being so commonly used for
serial devices, for example, 9600 baud, 1 stop bit, 8-bit byte size,
and no parity bit. A parity bit is a checksum for the outer level
communication protocol, in this case RS-232, but you often don't need a
parity bit because you have a checksum in the encapsulated protocol like
discussed in :ref:`modbus-rtu-protocol`. So you can at least try ``cat <
/dev/devname`` and then something like ``echo -ne "\x54\x45\x53\x54\r" > /dev/devname`` 
(substitute a message that follows the encapsulated
communication protocol like discussed below). As a note on naming,
for serial communications handshaking is limited to the hardware flow
control and does not include communication of device attributes and
communication protocol settings.

RS-232 specifies the hardware, hardware specifications and limits
to the signals (like what their voltages are and how fast they can
change), and the hardware flow control pins. It also specifies how
each bit needs to be sent through the transmit and receive lines, like
just given above.  But it doesn't specify how the data is turned into
a stream of bits. That data follows an encapsulated communication
protocol. Serial devices often have encapsulated communication protocols
where you directly address memory in the microcontroller, to either
read it or write on it. This is different from the case which is usual
for modern serial USB communication where the receiving device can
interpret string commands with variable names by looking up a table
in its non-volatile memory. The DASNET protocol at mod-spec-controls_
is an example of the second case where commands encoded in ASCII are
sent down an RS-232 serial cable. The control scripts for the Legato
syringe pump and CM-400 Mass Flow Controller (MFC) at mod-spec-controls_
are also exampes of the second case. They use the pyserial_ module,
in particular, the ``serial.Serial`` object takes the device name and
input parameters which specify the settings for the outer communication
protocol, RS-232. The strings which correspond to the encapsulated
communication protocol are encoded in ASCII and input by the write
method on the ``Serial`` object.

For completeness, the first case using the MODBUS RTU protocol is now
discussed.

.. _mod-spec-controls: https://github.com/dollodart/mod-spec-controls
.. _pyserial: https://pyserial.readthedocs.io/en/latest/pyserial_api.html

.. _modbus-rtu-protocol:

MODBUS RTU Protocol
~~~~~~~~~~~~~~~~~~~

The simplest thing to do with MODBUS RTU (note there is a TCP protocol
for MODBUS over ethernet, and alternative ASCII over serial lines) is to
read the first coil in the memory of a microcontroller. The message in
RTU protocol for doing so is as follows:

#. silence:1111111111111111111111111111
#. station address:00000001
#. function code:0000000000000001
#. data field:0000000000000001
#. checksum:1000100111000000
#. silence:1111111111111111111111111111

The order of the given fields is the order in which they are sent. How
they arrive (e.g., the allowed time interval between the fields and
separate messages) can be looked up in the standards (both the RS-232
standard and the MODBUS serial line specification).

The kind of data you have to enter into the data field depends on the
function code, e.g., if you want to pull a contiguous range of coils
(read holding registers) as opposed to a single one. All functions
have the purpose of reading or writing to different types, sizes, and
access privileges of memory, as expected for a low-level protocol. The
`wikipedia article on MODBUS`_ is an exhaustive reference for types
of memory (bit or byte/integer), their access privileges (read or
read-write), and the function codes (single or contiguous array of
memory access).

.. _`wikipedia article on MODBUS`: https://en.wikipedia.org/wiki/Modbusg

See the end of this post for a discussion of the checksum evaluation
and a python script which evaluates a Cyclic Redundancy Check (CRC)
and shows the work. The shown version is not for the MODBUS RTU CRC,
though an annotated form of the MODBUS RTU CRC given by the `pymodbus3`_
package is also given.

Following the analogy of packing for shipment by the postal service,
a checksum might be something like specifying the total weight of a
package to let the receiver know if they received everything they were
supposed to. Like checksums, it is possible though unlikely weight is
lost and added to the package so the contents change but the weight
remains the same.

.. _configuring-serial-ports:

Configuring Serial Ports
~~~~~~~~~~~~~~~~~~~~~~~~

Within port configuration, there are several types of settings. In ``man
stty.1`` the settings are grouped as "special characters", "special
settings", "control settings", and "input settings". The "output
settings", "local settings", and "combination settings" are irrelevant
here. The info page for ``termios`` shows 142 parameters in total (``termios``
is the C program for configuring both of these levels, while ``stty`` is
a CLI that does the same).

The simplest type of special characters is character escaping, in which
literal character text input is changed to a non-literal meaning. For
example, '\n' literally means backslash and n, but the backslash is
interpreted as an escape character so that '\n' is understood to be
a line feed (also called newline) character. In (extended) ASCII
encoding, this example would be changing the sequence 0101110001101110
to 00001010. One setting of this simplest type in ``stty`` is ``icnrl``
to convert line feed (00001010) to carriage return (00001101).

The second type of special characters are literal character to
program signal encoding. This is included in the appendix (see
ref:`port-config-signals`) because it has more to do with how the kernel
does interprocess communication with the port than how the port does
serial communication with the external device it is transmitting to
and from. Note some port configuration settings are for how terminal
(emulator) input or input from a script (generally called application
input) is changed by the kernel before being piped to the port, rather
than how the port communicates to the external device.

Most of the input settings, the control settings, and the special
settings are either for some abstraction layers between the application
and the port (see :ref:`port-config-signals`), or for the case of
interest here logical and physical settings of the communication
protocol: hardware or software flow control, baud rate, byte size,
parity bit. Flow control is first discussed in :ref:`serial-devices` and
baud rate is discussed in :ref:`sending-packed-encoded`, while parity
bits can be understood as a "simple checksum" modulo 2 as elaborated on in
:ref:`cyclic-redundancy-check`.

You can set up permanent configuration settings using ``udev``. For
example, you can assign a device a descriptive symlink in ``/dev`` which is activated
when the device is plugged in. Putting the following line in
``/etc/udev/rules.d/10-local.rules`` accomplishes this:::

    SUBSYSTEM=="tty", ATTRS{idVendor}=="FFFF", ATTRS{idProduct}=="FFFF", SYMLINK+="main-pump"

Where you substitute the actual hexadecimal ids of the vendor and product here given FFFF value. 

In addition to the man and info pages there are many forum posts on
these programs and so they aren't discussed here further.

.. _sending-packed-encoded:

Sending: How are Packed, Encoded Characters Sent?
-------------------------------------------------

So far I have discussed the encoding and packing.  There remains the
problem of sending the sequence of bits as electrical pulses. Especially
interesting is how the transmitter and receiver time their output
and input. Two strategies, synchronous and asynchronous, exist for
this. In synchronous, the transmitter uses a separate channel to tell
the receiver when data is coming. In asynchronous, every data frame is
packaged to indicate a start and stop, and the transmitter relies on the
receiver's internal clock to measure the bits once they agree upon how
fast the bits are communicated (a nominal baud rate).  I refer to the
excellent `commercial website for CAMI Research`_ for more details.

.. _`commercial website for CAMI Research`: https://www.camiresearch.com/Data_Com_Basics/data_com_tutorial.html


Baud rates are similar to bit rate and in some cases equal it. One
way to define them is how often there is a discrete change in voltage
levels. There is also a distinction between raw bit rate, which is what
you would see on a display for the voltage on a line, and the data
bit rate, which is how often the bits corresponding to your data are
sent. There are several reasons baud rates can differ from bit rates
(and bit rates from each other):

#. People define baud rate as a raw bit rate, which includes communication
   protocol characters (like start and stop in asynchronous) in addition to the
   data being sent, so the baud rate is larger than the data bit rate. 

#. People define a baud rate with compression, so that the actual number
   of bits transmitted is smaller than the number of data bits it encodes, so the
   data bit rate is the compression ratio larger than the raw bit rate.

#. People define baud rate as a data character rate for a given encoding, like 8-bit
   ASCII, so there are actually 8 bits per baud and the bit rate is 8 times
   larger than the baud rate.

#. The baud rate is given over an analog channel with more than two levels.
   When there are more than two levels, like in the analog output of a modem,
   the bit rate (both raw and data) can be much faster than the baud rate. The
   simplest case of more than two levels which is symmetrical is four levels,
   with which you can communicate twice as fast since two bits at a time can be
   communicated: level 1 is 00, level 2 is 01, level 3 is 10, level 4 is 11. 

Commonly used baud rates for serial devices range between 9600 and
115200 per second. If you equate one baud with one bit, which is the
case for digital serial communication with two levels signifying 0 and
1, then the time interval between bits being sent is in the range of
104.2 to 8.7 microseconds. Since an ASCII character is 8 bits it takes
at most a millescond to send a letter like A or a digit like 0. This
is very slow (100 times or more slower) compared to the Gigabit rates
for ethernet and USB SuperSpeed, but for many lab applications this is
irrelevant.

For more on the "most misused terms in computing and
telecommunications" see the `Modem HOWTO`_.

.. _`Modem HOWTO`: https://tldp.org/HOWTO/Modem-HOWTO-23.html

Some hardware layers of communication protocols work better over long
distances. Modern serial USB devices are convenient because of their
automatic configuration, common use, low cost, and support of up to
127 devices in chains and hubs. But USB cable can only be used to
around 5 meters before transmission is lossy. There are boosters for
USB cables, some of which use ethernet cable (rated for 100 meters)
between USB ports. For serial devices the RS-232 standard gives a
maximum length of 15 meters for the cable, which should be enough for
most laboratories. The ethernet protocol has such longer range because
of wire design, in particular larger cross-section (24 AWG Ethernet
compared to 28 AWG USB and 24 AWG RS-232, the ratio of cross-sections
for 24 AWG:28 AWG is just over 5:2) and twisted cable (twisted data
cable USB and untwisted data cable RS-232).

The inverse operations of receiving electrical bits and decoding the
signal to characters are not using different concepts than the forward
operations. I refer to the `HOWTO on serial communication`_ for more
details on this subject and how the kernel manages and receives signals
from ports, and now turn to the second part of this post, scripting for
FOSS controls.

.. _`HOWTO on serial communication`: https://tldp.org/HOWTO/Serial-HOWTO-1.html

.. _control-scripting:

Control Scripting with Python
-----------------------------

Python is taken just as one FOSS available for control scripting because of the author's familiarity.

In a (lexical only) irony, control scripting using serial communications
generally requires parallel processes.  In LabVIEW this is difficult to
achieve because the data flow programming paradigm, in which flows must
complete, requires relatively complicated program design to be used for
parallel processes. Controls often requires independent processes which
can pass messages between each other and spawn other processes.

Programming parallel processes with Python on Linux is comparitavely
easy because the problem of simultaneous processes is already a solved
on. For example, you can open up a web browser at the same time as you
run a spreadsheet program. To control many devices, you can just write
a script for each device having in it nested loops for updating their
respective device outputs, and then run those scripts in parallel. The
kernel handles these just like other parallel processes. Efficient and
time exact parallel process management is not easy , but for the lab
use where you only need time exactness on the order of milliseconds
or higher and the fractional CPU resource use is small, its not
relevant. Those cases where time exactness and reliability is needed
which use dedicated hardware, rather than a desktop program which just
uses whatever allocation the resources the kernel gives it, are outside
the present scope.

If the inputs for some devices depend on the outputs of other devices,
then file reading and writing can be used in each script which is
independently controlling its respective device. The problem of access
by several programs to the same file, to read, append, or write is also
solved. For the interested reader see the dining philosophers problem as
an introductory problem to read access between several processes for one
file, and generally concurrent programming (since there is one resource
being shared, the solution has to be concurrent meaning only one process
reads it at a time, rather than parallel in which several processes
would read copies of the file at the same time).

Compare these two scripts in python, to be executed at the
same time, which pass data between them:

.. code:: python

    """read.py"""
    from time import sleep
    sleep(1)
    with open('common_file.txt', 'r') as _:
        print(_.read())
    sleep(1.5)
    with open('common_file.txt', 'r') as _:
        print(_.read())

and

.. code:: python

    """write.py"""
    from time import sleep
    with open('common_file.txt', 'w') as _:
        _.write('hello world')
    sleep(1)

    with open('common_file.txt', 'w') as _:
        #sleep(2)
        _.write(' hello again')


At the command line, call the interpreter in parallel on the read and write scripts:

.. code:: bash

    python read.py & python write.py


In the above two scripts, the second print is ``hello world``, but if
you include the sleep statement commented out it is nothing. This is
because the file has been entered (and with writing, that clears all
the data in it) but not exited at the time of the second read. For more
details, see `PEP 343 -- The "with" Statement`_. This is in contrast
to opening a file handle, writing to it, and then closing it at the
end. Other programs will not see changes made to a file handle until
the file handle is closed with the ``close`` method and the file is written to.

.. _`PEP 343 -- The "with" Statement`: https://www.python.org/dev/peps/pep-0343/

The below two scripts illustrate the difference between the with
statement and a file handle. The first writes to the file in each loop
using the with statement while the second will not write to the file
until the loop ends. The second script will close the file handle and
write the file if interrupted, e.g. by the user typing ``ctrl+c``
in the terminal. However if you open ``common_file.txt`` like ``cat
common_file.txt`` while ``write-no-update.py`` is executing, you will
see it is empty, since the file handle buffer is still accumulating
input before the close method is called on the file handle. The
``flush`` method, if uncommented, will make the ``write-no-update.py``
script behave the same as ``write-update.py``. For reading, file
handles can be used equivalently to the with statement by calling
``file.seek(0)`` to reset the stream position before calling each read
method.


.. code:: python

    """write-update.py"""
    from time import sleep, time
    t0 = time()
    while time() - t0 < 5:
        with open('common_file.txt','a') as log:
            log.write('hello world\n')
        sleep(1)


.. code:: python

    """write-no-update.py"""
    from time import sleep, time
    t0 = time()
    log = open('common_file.txt','a')
    while time() - t0 < 5:
        log.write('hello world\n')
        #log.flush()
        sleep(1)
    log.close()

The ``subprocess`` module allows you to run subshells and so do process
spawning. The below script will execute without sleeping, and in
addition all the subprocesses opened will execute without waiting on
the completion of other subprocesses. The spawned processes are said to
be "forked" from the parent process. Of course, in this application one
would be opening subshells which execute other python scripts.

.. code:: python

    import subprocess
    subprocess.Popen('sleep 5', shell=True)
    subprocess.Popen('echo "a" > a.txt', shell=True)

For applications with high computational loads and those that need more
efficient and scalable message passing and process spawning, there is
mpi4py_.

You can save python objects as compressed binary rather than (ASCII
or other encoded) text files, using the ``shelve`` and its subsidiary
``pickle`` modules. Other non-text encodings can be used, or compression
on text encodings like ``gzip`` (which is part of the python standard
library). There are at least two reasons to use non-native binary
encodings (including compression): one, it makes the data easily read
by programs other than python, two, it's more secure since pickle files
allow execution of arbitrary code when loaded.

See how I used parallel python scripts with reading and writing
shared text and pickle files to control process equipment at
mod-spec-controls_.

.. _mod-spec-controls: https://github.com/dollodart/mod-spec-controls
.. _mpi4py: https://mpi4py.readthedocs.io/en/stable/overview.html#parallel-input-output

Control Scripting Over Remote Networks
--------------------------------------

An example of network communication is to an OpenSSH server. Below is
a shell script which uses the same file read and write as described
in :ref:`control-scripting` but over network with the ssh communication
protocol. The executables ``process_output`` and ``process_input``
could be aliases for something like ``python process_script.py`` on
the server and on the local machine (which would usually be different
scripts):

.. code:: bash

    #!/bin/bash
    while [ 1 ]; do # until the user breaks
    scp input.txt user@server:/path/to/dir/input.txt # copy input to the server
    ssh user@server:/path/to/dir 'process_input input.txt' # run program on server
    sleep 5 # wait some time before starting next loop
    scp user@server:/path/to/dir/output.txt output.txt # read what the server processed
    process_output output.txt > input.txt # change the input file based on what the server processed
    done


This communication appears simple to the end-user because of the high
level interfaces for networking between a computer and a server, here
the ``ssh`` and ``scp`` CLI for the OpenSSH protocol.

FOSS compatible hardware and firmware
-------------------------------------

Devices which support industry standard protocols like MODBUS can be
interfaced on a Linux system. If it is proprietary but the manufacturer
gives the standard for it, like is the case for, e.g., DASNET at
mod-spec-controls_, a program can be written for the protocol. Only if
the device has a proprietary communication protocols which is given
in a binary file distributed with it, e.g., on a disk, will there be
a problem. Products which have such binary programs for proprietary
communication protocols, and sometimes even charge extra for them,
usually have direct alternatives or can be constructed out of some
alternatives. An example is the WATLOW EZ-Zone PM6R1FC-1RFAAA which
charges extra for MODBUS RTU and otherwise offers a "Standard Bus"
proprietary protocol. This can be replaced with an outlet power
relay for systems with high thermal mass, or a triac "dimmer" for
systems with low thermal mass (but still high enough that the waveform
is irrelevant), in a computer and DAQ board system. The computer
calculates the power from temperature feedback and does all the other
calculation functions (like interlock), while the DAQ board supplies
control voltage and reads temperature.

LabJack makes stand-alone microcontroller hardware which is FOSS
compatible, meaning its drivers are free and openly available. LabJack
does not only have open communication protocols but also provides
high-level APIs in programming languages like Python. In addition, it
has excellent documentation. It may take less than 30 minutes to have
a device like the U3-HV configured for the simplest controls, such as
sending out digital or analog outputs based on analog input reading. The
LabJack application notes are extensive and I recommend consulting them
directly.

Appendix
--------

.. _port-config-signals:

Port Configuration for Program Signals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Changing characters to program signals is different from character
escaping because the program signals can go over different channels:
whereas character escaping just replaces one sequence with another
in a stream of data, program signals can bypass the serial stream to
control the data transmission process. The Linux kernel treats its ports
like files, meaning it pipes input and output from them like files,
and assigns them a file descriptor (see ``man socket.7``). Signals
(see ``man signal.7``) have general meaning like "interrupt this
process". When signals are piped to and from a process at a port for
transmitting or receiving, the signals are converted to actions specific
to the communication protocol. For serial protocol like RS-232 that
can be hardware flow control through dedicated pins like Clear to Send
and Ready to Send (``crtscts`` setting in ``stty``), or software flow
control with special characters in Transmit and Receive pins (``ixon``
setting). In the latter case the process signal encoding happens to be
literal, and in ASCII encoding XOFF is (usually taken to be) Device
Control 3 00010011 and XON is (usually taken to be) Device Control 1
00010001, though the user won't include flow control in their input so
it is not character escaping.

As an aside sockets are also used for network communication, but here
mean interprocess communication on the computer. The two are highly
analogous and in fact distributed systems with "microkernels" use
interprocess communication sockets over networks.

For a more nuanced discussion of the abstraction layers between the
application, in particular user input at a terminal (emulator), and the
port see `this blog post on tty (teletype terminal)`_.

.. _`this blog post on tty (teletype terminal)`: http://www.linusakesson.net/programming/tty/

.. _cyclic-redundancy-check:

Cyclic Redundancy Check (CRC)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The CRC calculation may appear relatively mathematically complicated
to the novice, but it is just long division without carrying. It only
requires two basic operations which can be done bitwise, meaning the
value at each bit position depends only on the value of a bit in a
corresponding position. The two operations are bit shifting, like moving
1s and 0s through a register, and XOR, or comparing bits at the same
positions of two registers and resulting in 0 if they are the same and
1 if they are different. In fact the XOR operation is addition modulo
2: the remainder of 0 + 0 with 2 is 0, the remainder of 0 + 1 with 2
is 1 and likewise for 1 + 0, and the remainder of 1 + 1 with 2 is 0. A
CRC is called a checksum, which in its simplest form is a sum of all
the bits in a message (and this is called a "simple checksum" from
here on out). A parity check, like that used in the RS-232 protocol,
is a simple checksum modulo 2, by which I mean it takes the remainder
of the checksum with 2. The modulo 2 is equivalent to evenness (if 0)
and oddness (if 1) of the simple checksum, hence the name parity. The
parity check isn't any better at detecting or correcting errors than the
simple checksum--it just saves memory, since instead of having to send
a bit sequence equal to the sum of bits, you just have to send 1 bit
which makes the sum including it have a particular parity. For example,
if ``101011`` is a 7-bit message that is supposed to have even parity
with the addition of a bit at the end, the parity bit ``0`` is added to
make ``1010110`` rather than ``100`` which would be used for the simple
checksum.

A modular addition like that used in the CRC is still an addition, so
when people call the CRC a checksum it is in this way valid. One of the
reasons calculing CRCs may appear complicated is because of the many
design choices available for the CRC calculation algorithm:

#. How many different polynomials there are. (hundreds)
#. Whether the CRC applies to the message as a whole, or to bytes of the
   message in registers separately, or nibbles or otherwise. (2 factors or more)
#. Whether the CRC is initialized to a non-zero value. (2 factors or more)
#. Little-endian or big-endian bit order and byte order. (2 factors or more)
#. Some nice mathematical properties of addition modulo 2 that allow
   you to change bit order and use a reciprocal polynomial for equivalent
   result. (2 factors)

There are at least, by counting the above, 16 variants of CRC
calculation using the same polynomial, some equivalent and some not
equivalent.

CRCs have other advantages than bitwise calculation over simple
checksums and parity checks: one, the probability a corrupted packet
goes undetected is even smaller than that of the simple checksum.  Two,
the CRC checksum can be used not only to detect if the message is
wrong, but reconstruct the correct message instead of requesting it be
resent, which can be important for transmission lines which are highly
unreliable. Unlike a simple checksum which can be incremented with an
error at any 0 or decremented with an error at any 1, and which can't
detect an error where a 1 bit is changed to 0 and a 0 bit is changed to
1, any error in the message will likely change the evaluated CRC to be
both detectable (different from the correct) and distinct (different
from any other error), at least for a given polynomial size and message
size. The test of the CRC for MODBUS serial lines at the end of this
section shows all 48 possible 1-bit errors on randomly generated 6 byte
messages have distinct CRCs, and of 1128 possible 2-bit errors 853 of
them are distinct. There is a theory of error correcting codes but it is
beyond the scope of this post.

The below script calculates the CRC for any string and any polynomial,
assuming it applies to the whole message and an initial value of the
remainder of 0. Most of the code is for visualizing the work. The
polynomial is specified as a bit sequence corresponding to whether or
not the power of the binary position exists (coefficient of 0 or
1). That is, the polynomial of ``11000000000000101`` is :math:`x^{16} +
x^{15} + x^2 + 1` (note that polynomial bit sequences are usually reported
as hexadecimal with an implicit leading 1). This is because of the
perfect correspondence between arithmetic long division and polynomial
long division, provided the coefficients can be either 0 or 1. In
that case the coefficients on polynomial powers correspond exactly
to the numbers at equivalent numeral positions. I've also included a
`bitstring2polynomial` converter. Everywhere here the binary numbers
are assumed to be little-endian. This is taken and modified from the
`Wikipedia article on the CRC remainder`_.

.. literalinclude:: crc_remainder.py
.. _`Wikipedia article on the CRC remainder`: "https://en.wikipedia.org/wiki/Cyclic_redundancy_check"

In the above, you can switch between the paper-and-pencil long division
procedure, when the divisor is shifted relative to the fixed dividend,
to a hardware level implementation of calculating a checksum in a
register, in which the divisor is fixed and the dividend is shifted
through a register, using the ``shifting`` keyword argument.

An annotated form of the CRC for MODBUS serial lines, from `pymodbus3`_,
is given below. Note the use of the register analogy is made here but is
not perfect because the python 3 integer type can be arbitrarily long
(the parts are allocated across different memory registers):

.. literalinclude:: modbus.py
.. _`pymodbus3`: https://pypi.org/project/pymodbus3/

Here is a test of the uniqueness of the CRC to single bit errors in a 6
byte message (uses ``numpy`` python library). It is both time and space
inefficient but straightforward for the purpose of instruction:

.. literalinclude:: crc-test.py


As reference, see "A PAINLESS GUIDE TO CRC ERROR DETECTION ALGORITHMS"
for an excellent summary. As the comments in the script indicate, the
modbus serial line specification gives all the details needed to program
the CRC for MODBUS serial lines calculation.

Downloads
---------

- :download:`crc_remainder.py`
- :download:`modbus.py`
- :download:`crc-test.py`

Versions
--------

First posted on 2021-01-24.
