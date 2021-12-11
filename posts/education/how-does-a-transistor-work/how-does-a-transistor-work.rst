.. _how-does-a-transistor-work:

How does a transistor work?
===========================

The transistor is the basic unit which all logic gates and therefore all
digital circuits, including those used for computing, are made of. Its function
is simple, a switch, but to achieve that at a microscopic level with the
ability to cheaply manufacture many such switches required significant advances
in physics. Here I wish to give a simple model for the function of a transistor
using only classical physics arguments of the asymmetry of matter and motion of
electric charges.

History of Science of Electricity
---------------------------------

History of Science of Electrical Charge Carriers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before the discoveries of physics in the later part of the 19th century,
the assignment of sign to charges was arbitrary. Benjamin Franklin chose the
sign of charge when he studied static electricity on different materials in the
mid 18th century. He ended up assigning positive potential to what was really a
deficiency of electrons on materials rubbed with glass, which he thought had an
excess of some electrical fluid, and negative potential to what was really an
excess of electrons on materials rubbed with resin, which he thought had a
deficiency of some electrical fluid.  The sign is arbitrary because though the
pith ball experiments indicated that a material could be charged to either
opposite signs, they did not indicate which sign of the charge carrier, or even
that there was only one charge carrier with one sign.

For 150 years in the study of heat transport there was the caloric fluid theory
which hypothesized a calorific fluid which contained heat (from late 18th
century to mid 19th century). Heat flowed from regions with an excess of
calorific fluid to regions with a deficiency of calorific fluid. The caloric
fluid theory failed when experiments verified the mechanical theory of heat,
that is, heat is transported by the collisions of particles transferring
energy. It was around the same time that calorific fluid was introduced that
the basics of electricity were being discovered (Franklin's pith ball
experiments occured in the mid 18th century slightly before this). When
electric current was discovered by scientists working on batteries (Volta
invented the battery in 1800), it was thought to be the flow of the
hypothesized electrical fluid from regions with an excess of it to regions with
a deficiency of it. And unlike heat, it turned out to be correct that there is
an electrical fluid, of a sort.

..
    Invisible fluids were very common in physics at that time, and it would
    take the same time needed to find the sign of the charge carrier to also
    prove that the luminiferous ether in which light supposedly traveled didn't
    exist. 


J. J. Thomson's work on cathode rays in 1897 showed that charge is
transported by carriers of one charge, one that flowed opposite the
direction of current as defined by convention, and so it was assigned
to be negative. The charge carriers were found to be particles, not an
indivisible fluid. It was called the electron because it is the particle
of electricity.

Part of J. J. Thomson's work found the charge-to-mass ratio [#]_ of electrons,
from which the mass of an electron could be calculated. That mass was far too
small to account for the mass of matter, and so whatever was positively charged
had to have a much smaller charge-to-mass ratio. There are the following
balances: :math:`c_+ + c_- = 0`, for the charge neutrality of an atom, and
:math:`m = m_+ + m_-`, for the mass of an atom. By substitution, these
equations give :math:`\frac{m}{2c} = \frac 12 (\frac{m_+}{c} + \vert
\frac{m_-}{c} \vert)`, where :math:`c = c_+ = -c_-`. The atom's mass-to-charge
ratio, which is counting both negative and positive charges, is the average of
the absolute values of mass-to-charge ratio of the positive and negative parts.
Since :math:`m_-/c \ll m/(2c)`, it follows that :math:`m_+ \approx m`.

Rutherford's gold foil experiment in 1908 proved that the positive charged
material wasn't distributed continuously in matter, but concentrated in small
nuclei. Now not only was the charge-to-mass ratio significantly different, but
so too was the mass-to-volume ratio. Matter was found to be mostly empty [#]_
with a small nucleus of positive charge surrounded by electrons. Rutherford
discovered the volume of the nuclei, approximately, through an analysis of the
scattering of the alpha particles using the same gold foil experiment.
Rutherford later found that the nuclei of all elements is made of the same
nucleus as that of hydrogen, and he called that unit a proton. The proton has
the same charge as an electron, but is 1835 times more massive. 

Though electrons don't have a radius, if one uses the "classical electron
radius" which is based off some other parameters, the electron volume is 37
times greater than the proton (the mass-to-volume ratio of an electron is
therefore 67,895 times less than that of a proton). If one were to take the
electron cloud volume, which is the atom volume, the electron volume is 3
thousand trillion times greater than the proton volume. Matter was discovered
to be made of very asymmetric parts. This fact had eluded all investigators in
previous experiments where such asymmetry couldn't be observed, and would
subsequently be exploited both in vacuum and later solid-state devices.

The below table summarizes the differences between the proton and
electron, where the smaller quantity is assigned a value of 1 and the
other is given as multiples of that smaller quantity:

+----------+----------+----------+
| quantity | proton   | electron | 
+----------+----------+----------+
| mass     | 1835     | 1        |
+----------+----------+----------+
| charge   | 1        | 1        |
+----------+----------+----------+
| volume   | 1        | 37       |
+----------+----------+----------+

History of the Science of Electric Motion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The science of electric motion was developed after Ben Franklin's studies of
static electricity. Alessandro Volta discovered electric current resulted from
chemical reactions in dissimilar metals arranged in a voltaic pile; Hans
Christian Ørsted found a relation between electric current and magnetic
deflection in compass needles; Michael Faraday discovered also a relation
between electric current and deflection (in the rotation of a rod suspended in
mercury), developed much of electrochemical science, and created the theory of
electric fields; André-Marie Ampère, Jean-Baptiste Biot, and Félix Savart
discovered various laws for the electric and magnetic forces on charges in
motion; and James Clerk Maxwell formalized the existing experimental results in
the theory of electromagnetism. This list isn't exhaustive, of either the work
of those named or of the scientists who contributed to the development of
electricity and magnetism. These scientists, among others, were working from
the late 18th century to the mid 19th century. The science of electric motion
developed before the sign of the charge carrier was discovered, which was
possible because the observed phenomena were independent of the sign of a
charge carrier.

For the current purposes of explaining the transistor, it suffices to
discuss not the quantitative laws but the qualitative theory of electric
fields. Magnetic fields and forces are unnecessary to consider, as
well [#]_. Charges spontaneously generate electric fields from themselves
and to other charges. But for the current purposes, it suffices to think
of the electric field as static and charges running through them---this
situation is quite often realized, since the charge which is being moved
can be much smaller than the charges which are static and generating the
field.

In the theory of electric fields, regions have an associated potential.
Differences in potential cause lines of force to generate between them. The
potential can be thought of as a quantity of electric fluid, like in the
hydraulic theory. The cause for that differing potential can generally be
complicated (it can be electrochemical, or purely physical in the accumulation
of charges), but one need not consider that for these purposes. The lines of
force act on charges and cause them to move from regions of higher potential to
regions of lower potential. The lines of force don't need a medium and can
stretch through vacuum. For negatively charged particles, the direction of the
line of force is from regions of lower potential to regions of higher
potential, because the potential is defined for a positive charge; and when you
make a higher value negative, it is lower than the originally lower value made
negative. That is, if :math:`x > y`, then :math:`-x < -y`. But none of the
experiments could tell whether negative charge carriers were flowing from low
potential to high potential, or positive charge cariers were flowing from high
potential to low potential. They could just tell that there were lines of force
which caused transport of some charge in either direction. I will draw the
lines with arrows pointing in the direction that a positive charge carrier
would be caused to go, in agreement with the convention of positive current.
But electrons travel the other direction.

Very often the qualitative lines of force are not relevant, and one just needs
to know that there is a potential difference which tends to move charge in a
direction. In that case, instead of specifying an electric field and lines of
force, one simply species the voltage, defined as the difference in
potential between two regions.

Analogy to Motion of Gases
~~~~~~~~~~~~~~~~~~~~~~~~~~

The transport of charge by electrons should be contrasted to the
transport of mass by gas molecules, which are uncharged. Passive
one-way valves controlling gas flow exist by using a spring attached to
a stop. The stop is commonly ball-shaped in devices and in that case
the valve is called a ball check valve. But there is no way to prevent
gas flow from descending down a decrease in pressure in the absence of
anything else (inside an otherwise empty volume).

The electric field allows you to move charges from one place to
another, like a pressure difference lets you move gas from one place
to another. But there is no such thing as a spring and stop which can
be used to block charge carriers inside a material [#]_. So
the question is, how can a one-way valve be constructed for charge
transport?

The answer lies in the asymmetry of the charge particles. In
matter, there are the heavy and therefore unmoving nuclei containing the
positively charged protons, and the light negatively charged electrons
which conduct charge. The opposite of this, antimatter, has been
observed in microscopic amounts but is not encountered naturally. 

The exploitation of the parity is not trivial. One material will
conduct electricity in any direction (be a conductor) or not at all
(be an insulator), like in the classical experiments by the battery
scientists. But the fact that electrons are what conducts charge and
have a negative charge can be exploited by making solid state devices
out of several materials (or more precisely, several differently doped
regions of a material). The transistor is the fundamental device for
computation which is based on this exploit. But first, I will explain
a simpler system which preceded the transistor and accomplished the
function of a one way valve for charge.

.. rubric:: Footnotes

.. [#]
  The author prefers the term mass specific charge, since ratios are for
  like-dimensioned quantities, but this is the convention. Notably, Euclid
  defined a ratio in Book V Definition 3 as "a sort of relation in respect of
  size between two magnitudes of the same kind", a high, if ancient, authority
  on definition.

.. [#]
  Actually the electron doesn't have a definite position, but a probability
  distribution making up a "cloud". The fact that the alpha particles in
  Rutherford's gold experiment weren't stopped is more to do with the fact that
  the electron is so much less massive than the alpha particle and proton than
  that the atom is empty space (the proton could be "hitting" electrons, their
  wave function may be collapsing when the proton impinges, though I don't know
  enough about dynamics in quantum systems to answer such a question---it
  doesn't matter for current purposes, because even if electrons were
  ricocheting like billiard balls, they're so much less massive than an alpha
  particle it would be like baseballs hitting a light car, when the light car
  is going faster than astronomical speeds). 
  
  Since the proton is 1835 times more massive than the electron, it's wave
  character is negligible. While quantum mechanics is quite often thought of
  the "science of small", here the dependence on mass through the momentum in
  the Heisenberg uncertainty principle, :math:`\sigma_x \sigma_p = \hbar/2`, is
  clear. The uncertainty in the proton's position is small because the mass
  and therefore uncertainty in its momentum is large. Generally, this is
  expressed in terms of the Compton wavelength, though this is the wavelength
  that an equivalent photon would have and not a property of the particle
  (since photons are massless, it is the energy that the photon would have to
  equal the mass of the particle by Einstein's mass-energy equivalence).

.. [#] 
  Magnetic phenomena are important for long-term memory which use quantum magnetic spin states.

.. [#]
  If you tried to use a check valve for electrons, the problem is they are so
  less massive than atoms in a gas that there's difficulty in build a spring
  and stop which are sensitive enough and small enough in mass to work. As
  already discussed, the electron is 1835 times less massive than the proton.
  And because the particles are charged, you would either have charge
  accumulation, if the stop were made of insulating material, which would repel
  the electrons, or you would absorb a large amount of the electrons which were
  impacting the stop if it were made of a conductive material attached to
  ground.

Vacuum Devices
--------------

.. _vacuum-diode:

Vacuum Diode
~~~~~~~~~~~~

A vacuum does not equalize electric potential throughout it like a
conductor nor impede transport like an insulator. An electric field can
be imposed in a vacuum as Faraday postulated. That field can accelerate
or retard electrons traveling with or against its direction. Electrons
can be emitted into a negative potential end (cathode) of a tube, and
the lines of force from that end to the positive potential end (anode)
will move the electrons to the anode. This is the vacuum diode and is shown below in an on-state.

.. figure:: figs/vacuum-diode.svg
   :alt: schematic of vacuum diode in vacuum tube with qualitative lines of force

   The lines of force are qualitatively given, using Bezier curves. The
   denser the lines of force shown, the greater the electric field. The
   electric field strength is greatest at the cathode and anode,
   and grows weaker nearer the middle of the tube and the tube
   boundary. Electrons travel oppositely the lines of force shown for
   positive charge carriers, that is, they travel from cathode to anode.

How are electrons emitted into a vacuum? Under strong electric fields
electrons will spontaneously emit from a metal. The threshold for the
required field strength is given by the work function. Electrons are
attracted to the matter that they are a part of, and the work function
is amount of energy needed to remove an electron from the matter. The
rate of emission is not fast enough for electric fields that can be
practically applied at room temperature, so metals have to be heated
until a significant fraction of the electrons have enough kinetic energy
to leave the metal. This is called thermionic emission when the cathode
is hot enough that the electrons would be emitting without the electric
field and it is called Schottky emission (or field enhanced thermionic
emission) when the electric field is significant in lowering the work
function to allow electrons to be emitted. 

..
    The vacuum diode is easily modified to make a vacuum triode which is
    analogous to the transistor. 

.. _vacuum-triode:

Vacuum Triode
~~~~~~~~~~~~~

In the vacuum triode the flow of electrons is controlled by an added electrode
in the middle, whose potential when more negative than the cathode will repel
the electrons away from it that otherwise would flow from cathode to anode.
Because of its function to block current this electrode is called a gate. The
gate is not heated and so it does not emit electrons even when the voltage to
the anode is greater in magnitude than the voltage of the cathode to the anode.
The gate does not need to be in the way between the anode and cathode because
the field it produces will extend beyond it into the vacuum, though it often
is. The gate is often a mesh in devices so it can be situated between the anode
and cathode and when its potential is neutral relative to the cathode,
electrons can go through the mesh holes to the anode. Common device designs are
radially symmetric, where the cathode is an inner cylinder, a gate is an
intermediate cylinder, and an anode is an outer cylinder. Below is shown a
vacuum triode in the off state.

.. figure:: figs/vacuum-triode.svg
   :alt: schematic of vacuum triode with concentric cylinder geometry

   The lines of force are easy to draw for concentric cylinders. By radial
   symmetry, inside a cylinder there is no electric field. Outside the
   cylinder, the lines of force emanate radially outward. When the gate voltage
   to cathode is zero, the lines of force from the cathode are undisturbed when
   going to the anode (recall that the grid is not a solid cylindrical surface,
   but a mesh). When the gate voltage to the cathode is positive, the effect
   can be to reverse the lines of force between the gate and the anode, as
   shown. By the symmetry, the electric field lines can be offset by any angle;
   it is only their angular spacing that shows the electric field strength
   which decays as one goes further from the cylinder.

Solid State Devices
-------------------

In order to explain how a transistor works, some particular properties
of semiconductors, the material for solid state devices, must be explained. In particular, there must
be an introduction of the concept of a hole. Like a conventional hole
is the absence of dirt, a hole in semiconductors is the absence of an
electron. It is in everyway analogous and opposite to an electron:
holes have a negative wave vector, a negative energy, and a negative
mass, which results in them acting like a positive charge carrier
[#]_. It may then be asked, how can the fact that charge carriers are
negatively charged, as opposed to gas particles, be exploited if there
is a symmetric counterpart, the positively charged hole? Some points bear
mentioning:

#. The case of uncharged particles is distinct to that of two oppositely
   charged particles. In particular, there can be materials which are mostly
   having excess positively charged mobile particles (holes), and materials
   which are mostly having excess negatively charged mobile particles
   (electrons). However, the asymmetry of protons and electrons is necessary
   not only for the function of vacuum devices but also solid state ones, so
   this point doesn't answer the question.

#. The hole is an absence of an electron is not a true particle. Every piece of
   experimental evidence is in support of the hypothesis that charge is
   transported by electrons everywhere [#]_. The case of a charged particle and
   a fictitious particle which is its absence is distinct from the case of two
   charged particles, each of which would have its respective fictitious
   particle by its absence. While a positron is an electron with positive
   charge, a hole is an electron with negative wave vector, negative energy,
   and negative mass. While the hole has an equation of motion identical to a
   positron, in the more sophisticated theory than that is presented here, it
   lives in a valence band as a result of being an absence of a hole, and so
   isn't in any way physically like a positron (which would exist in a high
   energy state in a conduction band in order to transport).

In fact, as it turns out, transistors require the existence of holes. [#]_

The materials with excess holes are called :math:`p`-type (for positive), those with 
excess electrons :math:`n`-type (for negative). When these materials are
arranged the transistor can be made. Again, a :math:`p`-type
material will conduct electricity in either direction, as will an
:math:`n`-type material---it is only their arrangement that can control
the direction of flow.

Where do the excess charge carriers in :math:`p`- and :math:`n`-type materials
come from? The excess charge carriers are a result of an absence or
abundance of protons from a process called doping [#]_. Doping introduces atoms
with nuclei whose proton number is more (:math:`n`-type) or less
(:math:`p`-type) than the nuclei of the host material. These atoms ionize
because the neighboring host atoms have too few or too many electrons to
satisfy their chemical valence, and the result of that ionization are charge
carriers.  This ionization conserves electroneutrality---an :math:`n`-type
material is not negatively charged nor is a :math:`p`-type material positively
charged. The doping atoms release or trap electrons and generate charge
carriers while remaining immobile, again showing the asymmetry of matter is
necessary for the function of solid state devices.

.. rubric:: Footnotes

.. [#]
  Kittel, Solid State Physics, 8th Edition, Chapter 8. An actual positive
  charge carrier, like the positron, has positive mass---it is only the
  behavior with respect to electric current that is identical.

.. [#]
  See nanoHUB-U: Thermoelectricity: From Atoms to Systems: Unit 1: Bottom Up Approach by Supriyo Datta.

.. [#]
  See also Kittel, Solid State Physics, 8th Edition, Chapter 8.

.. [#]
  Doping is a process which usually involves shooting beams of high energy
  ionized impurities at a semiconductor host material, which embed some
  distance into the material, then increasing the temperature until the nuclei
  move to spread them more uniformly out and repair the damage to the host
  material (both impurities and native nuclei will move, the latter repairing
  the damage from the high energy impact). The characteristic temperatures at
  which nuclei move may be around 1000 degrees Celsius, but even then they move
  much more slowly than electrons, and the process may take several hours. 

.. _semiconductor-diode:

The Semiconductor Diode
-----------------------

Many people explain semiconductor function with basic solid state
physics derived from quantum mechanics, which includes transitions
between electron bands and forces induced on conduction band electrons
from band bending. However, for the current purposes, a classical
view of electrons as charges being moved by lines of forces in an
electric field is sufficient [#]_. First I explain the function of a
:math:`p`-:math:`n` junction, which is the working principle of
a semiconductor diode and is one step before the transistor, a
semiconductor triode.

A :math:`p`-:math:`n` junction results from the (hypothetical) joining of
:math:`p`- and :math:`n`-type regions (in practice the regions are made by
differently doping regions of the same host material). The nominal junction is
the hypothetical plane abruptly separating the :math:`p`- and :math:`n`-type
regions. If charge carriers are free to move, how can :math:`p`- and
:math:`n`-type regions which are brought together not annihilate the electrons
and holes [#]_? And if charge carriers are not free to move, how can charge
transport happen?  The charge carriers are free to move, but a :math:`p`-type
and :math:`n`-type material brought together will remain :math:`p`-type and
:math:`n`-type because the nuclei won't move [#]_ and the charge carriers will
remain attracted to them (:ref:`depletion-layer` explains what happens at the
interface). This is why the charge parity of electrons and protons, and mass
disparity, is necessary for the controlled flow of charge. The protons in the
nuclei, again the positive charges which make up matter, stay fixed.

.. _depletion-layer:

Depletion Layer at Zero Bias
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

What happens when the :math:`p`- and :math:`n`-type regions are hypothetically
brought together? Ideally no current flows [#]_. You can
think of the :math:`p`-type region as a lattice of negatively charged dopants
with mobile holes (the lattice is superimposed on the crystal structure of the
semiconductor, but it is much larger, since dopant densities are 1 million
times less than the atom density).  Similarly, the :math:`n`-type region is a
lattice of positively charged dopants and mobile electrons. When a :math:`p`-type
region and an :math:`n`-type region are brought together, the holes and
electrons near the interface annihilate each other, and what is left are the
dopant lattices in something called the depletion layer. So the depletion layer
in the :math:`p`-type region is negatively charged, and the depletion layer in
the :math:`n`-type region is positively charged. Away from the interface, the
electrons in the :math:`n`-type region far from the interface are attracted to
the positive lattice, and the holes in the :math:`p`-type region far from the
interface are attracted to the negative lattice, but because of
electroneutrality and the fact that carriers in the regions far from the
interface are also attracted to their own regions, the resulting profile of
charge carrier density is depleted (zero) in a layer around the
:math:`p`-:math:`n` junction.

.. figure:: figs/depletion-layer-1.svg
   :alt: qualitative schematic of p-n junction made from hypothetically joined p- and n-type regions prior to depletion

   A qualitative schematic showing the formation of a depletion layer. The
   squares are the dopants. The circles are charge carriers. The charge
   carriers annihilate with each other to form the depletion region (in this
   hypothetical path). The size of the carriers and dopants are greatly
   exaggerated to be visible.
   
   Note that dopants, unlike crystal atoms, have no lattice structure and will
   not be arranged in such a symmetric way, but randomly distributed on the
   length scale. Here the length scale is 50 nanometers. On average a cube with
   edge length 50 nanometers will have 2 dopants, 1 at the center, and 1/8 of
   one at each corner. This gives :math:`2/(50 {\rm nm})^3 = 1.6e+16 {\rm cm}^{-3}` dopant density,
   which is a representative dopant (and therefore carrier) density in old
   devices where the depletion layer is relatively thick.  What is shown isn't
   the zero bias depletion layer width for silicon or any other material, but
   is representative.

.. figure:: figs/depletion-layer-2.svg
   :alt: qualitative schematic of p-n junction made from hypothetically joined p- and n-type regions after depletion with electric field

If charges attract each other the closer they are, the depletion region which
has bare positive charges near an :math:`n`-type region and bare negative
charges near a :math:`p`-type region may be contradictory. In fact, the actual
explanation is in equality of chemical potential across the junction and a
solution of the Poisson equation, and while there is a depletion region, the
true result is smoothly (if steeply) varying [#]_.  But there is a valuable
infinite plane of charge approximation that allows the simple model presented
here to explain the result. This states that when charge is in a plane, then
for distances from that plane which are much smaller than the width and height,
the electric field strength is pointed normal to the plane (away if it is
positive) and is constant in magnitude within that distance. This mathematical
result has the intuitive reasoning that the distance from the point and the
large majority of the charge in the plane for such small distances is
effectively constant.

By considering the :math:`p`- and :math:`n`-type dopants to be in planes of
charge, the electric field they exert is zero outside the depletion region (the
negative planes attract electrons just as much as the positive planes repel
them everywhere outside the depletion region). The lines of force here are
multiplying in density everytime a new plane of charge in the depletion layer
is passed until a maximum is reached in the middle of the depletion region.
Note the electric field points from the :math:`n`-type region to the
:math:`p`-type region. This means that there is a barrier for electrons to
cross over the depletion layer, while at the same time the depletion layer is
stable (exerting no electric field outside it and so attracting no charge
carriers to it). Do note this model can't say, though, what makes the depletion
layer a given thickness under a given applied voltage---it is simply assumed to
result from some factors including the applied voltage, being thinner with
increasing forward bias and thicker with increasing reverse bias.

.. _forward-reverse-operation:

Forward and Reverse Bias
~~~~~~~~~~~~~~~~~~~~~~~~

When a voltage is applied that moves electrons against the depletion layer it
is called a forward bias. Equivalently, this is when the "negative" potential
is on the :math:`n`-type side and the "positive" potential is on the
:math:`p`-type side. This makes the depletion layer thinner and therefore the
barrier smaller. As a result, carriers cross over the barrier more frequently
leading to an electric current. It's common to define a "built-in" voltage for
a :math:`p`-:math:`n` junction needed to move an electron across it and a
representative value is 1 volt, though note that "built-in" voltage is geometry
specific, because what is important is the electric field strength.  [#]_

It isn't necessary that the two regions be equally doped (the depletion layer
is symmetric about the nominal junction when they are, but will extend deeper
into the less doped region when they are not, by the proportion of the
densities). In the below, a diode is shown in the forward bias which has the
:math:`n`-type region more heavily doped than the :math:`p`-type region. 

.. figure:: figs/diode.svg
   :alt: qualitative schematic of semiconductor diode under forward bias

   A qualitative schematic showing, at a length scale significantly greater
   than the depletion layer, that the :math:`n`- and :math:`p`-type regions can
   differ in their concentration of dopants and therefore charge carriers,
   leading to different currents of minority carriers when the diode is on.
   Because the doping density is a factor of 2 different (the lattice spacing
   is :math:`2^{1/3}` greater for the :math:`p`-type region than the
   :math:`n`-type region), the depletion layer widths on either side of the
   nominal junction are a factor of 2 different, and the minority charge
   carrier currents also are a factor of 2 different.

   The forward bias causes a depletion layer thickness to decrease, so this
   figure may be compared to the previous for which the depletion layer on
   the :math:`n`-type side is larger. The net electric field inverts near the
   nominal junction (where the electric field due to the depletion layer is
   strongest) and opposes the charge carrier motion. The arrows only show a net
   direction of movement. 

   In a cross-section parallel to the flow the two-dimensional current would
   mathematically be zero. But if one takes the width of the depicted region as
   the distance into the plane of the paper, one can quantify the number of
   charge carriers given a current density. But because choosing any time
   interval allows one to show any number of charge carriers, and then this
   would be related to the device figures only under some further assumptions,
   the number is arbitrarily chosen in this semiquantitative figure. By one
   calculation at an applied voltage of 0.1 V there is 20 electrons per second
   flowing through this cross-section, and due to the exponential dependence,
   there is 1 electron per microsecond at 0.4 V. As a final note, the
   equilibrium minority carrier concentration is not zero, but I haven't shown
   it, it being so small relative to the equilibrium majority carrier
   concentration that it doesn't appear on this length scale.
   
When the forward bias equals or exceeds the built-in voltage, the forward bias
applied causes the electric field to invert from the direction due to the
depletion layer, so electrons would be moved along by the electric field (the
depletion layer vanishes at this same point, too). In such a case, the
:math:`p`-:math:`n` junction has no resistance, and the only resistance the
diode has is due to the resistivity of the bulk semiconductor material making
up the device. However, long before that mode of operation is achieved and when
there is still a barrier, a diode will still conduct current, and in fact this
is the usual mode of operation and what is depicted in the above figure. In
this mode of operation, if the charge carrier is outside the depletion layer,
its motion is directed along (or against) the electric field, but inside the
depletion layer, in particular near the junction, its motion is due to
diffusion and randomly oriented. Each charge carrier has spontaneous motion
that causes it to move around randomly, and this diffusion effect is independent of the
motion caused by the electric field [#]_. Because it is independent and random,
this diffusion can oppose the electric field, causing electrons (holes) to
travel with (against) the electric field in the depletion layer. The spillover
rate gets faster the greater the concentration of particles and the shorter the
distance, because there are more particles and the shorter distance leads to
random walk more often extending across the depletion layer leading to
spillover. Once on the other side of the depletion layer, the charge carriers
are moved by the electric field into the bulk, where they might recombine with
a majority carrier or even reach an electrode.

The effect of the biases for this mode of operation is to decrease the
equilibrium depletion layer thickness (and the barrier) for the diffusion of
charge carriers. A reverse bias increases the depletion layer thickness and
barrier, leading to no current and in fact preventing leakage current.

The semiconductor diode is the semiconductor analogy to a one-way valve. It's
not a switch but a passive valve. That is, whether it lets current through or
not depends only on the sign of the voltage from the :math:`p`-type region to
the :math:`n`-type region. A transistor is an active valve, like the vacuum
triode, and can be opened or closed by applying a voltage.

.. rubric:: Footnotes

.. [#]
  You may wonder why a classical model works. The drift-diffusion
  model which is used for quantative solution to semiconductor device
  transport relies only on Boltzmann statistics and classical transport
  equations of motion. This happens because the fermion properties of
  electrons (and correspondingly holes) limit to Boltzmann behavior for
  the mobile carriers. Because the charge carrier concentration depends on
  the quasi-Fermi level, which in turn depends on the applied voltage,
  it turns out to be correct to think of the charge carriers as if
  they had been attracted or repelled by an electric field toward or
  away from a depletion layer. 


.. [#]
  Classically opposite charges, if they were to come together, would create an
  infinite amount of force and energy, because they are points and the attractive
  force between them varies as the inverse square distance and an infinite density of lines
  of force would exist between them as they approached each zero. Here, I will simply
  take the view that the carriers can collide, like balls with finite width, and
  when they do, they annihilate to nothing. 

.. [#]
  Nuclei move at elevated temperatures, which is how :math:`n`- and
  :math:`p`-type materials are made in a doping process (see explanation in
  :ref:`semiconductor-diode` and footnotes). But after quenching to room
  temperature they stay fixed.

.. [#]
  There is a small current even under zero potential, often called leakage
  current, as you would expect from the fact that charge carriers are mobile
  (see :ref:`forward-reverse-operation` for explanation of diffusion). To
  design a semiconductor diode for some currents at some applied voltages and
  nearly zero current at no applied voltage requires calculating the optimal
  carrier densities in the two regions, among other non-idealities.  Design
  gets more difficult for non-ideal geometries in real devices where they are
  minituarized (see section 8.1 of Lundstrom's Carrier Transport).  For the
  current discussion, though, I am considering only the ideal semi-infinite
  geometry, for which the numerical solutions can be obtained relatively easily
  and under the right assumptions there are even analytical solutions (see,
  e.g., Marder, Solid State Physics Chapter 19).


.. [#]
  See, e.g., Marder, Solid State Physics Section 19.4.2 for the ideal
  (discontinuous) equilibrium carrier concentration profile at a
  :math:`p`-:math:`n` junction. Numerical solutions of the Poisson equation are
  presented in `Section 4.3 of Van Zeghbroeck's Principles of Semiconductor
  Devices <https://ecee.colorado.edu/~bart/book/book/chapter4/ch4_3.htm>`_. In
  the model given here, while the depletion layer is stable, it isn't explained why
  it has the width it does and how it would vary with the bias.

.. [#]
  That may surprise you since the vacuum diode required high temperatures in
  order to excite electrons to move into the vacuum. But the electric field
  goes as voltage divided by distance, and the distance here is small, the
  depletion layer width being around 500 nm thick in the figure. In vacuum
  devices the voltage has to be a lot higher than that because the device
  geometry isn't nanometers but centimeters and greater. In vacuum devices with
  significant field-enhanced thermionic emission, voltages in kilovolts are not uncommon.
  It is the geometry which distinguishes vacuum and semiconductor devices, not
  differences in energies between metal and vacuum interfaces and :math:`p`-
  and :math:`n`-type interfaces (though there is also a significantly greater
  energy penalty of going across a surface to vacuum than across a junction, it
  is small in effect relative to the geometry).
  
  To elaborate, a metal-vacuum interface has a work function like 5
  electron-volts, but a 5 volt difference can't be used to draw out an electron
  in a vacuum diode. Light which hits a metal surface is enough to
  spontaneously emit electrons (called the photoelectric effect) because 5
  electron-volts is a small amount of energy. But again it is geometry making
  the potential difference lead to very small electric field strength. The
  relevant factor is the electric field strength above the surface of the
  metal, not the potential at some macroscopic distance away. In analogy, the
  potential energy required to remove you from the face of the earth is like
  the potential, but the force of gravity acting on you at the earth is like
  the electric field.  If you were to travel along a line between you and the
  sun, at some point in your travel the attraction to the sun from its
  gravitational potential would have done enough energy to "bring you from the
  surface of the earth". But of course the sun doesn't pull you off the surface
  of the earth, because its gravitational field at the surface of the earth is
  weak compared to the Earth's. That is, the potential to do work over a very
  long distance doesn't mean anything about where you will be moved. The
  analogous photoelectric effect is if you were rocketed off the face of the
  earth by an incoming rocket.

  If electrons have a distribution of energies, why doesn't the photoelectric
  effect give off any electrons until the energy is equal to the work function?
  You might expect something like "electron evaporation". But since the room
  temperature thermal energy is around 25 millielectronvolts, and the Fermi
  level may be something like 5 eV or higher in a metal, whether or not the
  electrons are relatively excited, the photoelectric effect would appear only
  at the work function energy; the spread in energies is so much smaller than
  the mean energy that it wouldn't be seen in experiment (careful experiments do
  show a "thermally assisted photoemission" consistent with a distribution of
  energies). Analogously, even if you are on top of a tall building the energy
  required to rocket you off the face of the earth remains effectively the
  same.
  
  Cold electron emission, called Fowler-Nordheim field emission, requires
  electric field strengths on the order of 5 V/nm. The physical intuition is
  that the electron must be subjected to a force sufficient to work on it to
  exceed its work function on a length scale similar to the electron's
  (classical) size or the lattice constant. One may derive the tunneling
  transmission coefficient as a function of surface electric field strength
  (see `Richard Fitzpatrick, Quantum Mechanics`_).  Using the equation provided
  in that source, one can calculate that the required electric field strength
  for a transmission probability at 50\% is 10 V/nm (the equation is for an
  electron in a 1-D well). 

.. [#]
  This spontaneous and random motion can be observed even for macroscopic
  particles (as caused by the random motion of molecules). It was observed by
  microscope for pollen grains by Robert Brown and then called Brownian motion.
  Classically, each particle can be thought of as having a kinetic energy equal
  to 25 millielectronvolts at room temperature, which for a ballistic electron
  would be a velocity of 95 kilometers per second. In solid state systems, the
  Fermi velocity is used, which is based on the Fermi energy and even higher,
  around hundres of kilometers per second for semiconductors. Though these
  speeds are so fast, depletion layers are less than micrometers, which means
  such an electron (traveling 1000 km/s) would traverse the perpendicular
  distance if uninterrupted in less than a picosecond. One must, though,
  account for the very frequent scattering events, of which there are many
  types, to obtain a mean free path of hundreds of nanometers or less (in this
  model, scattering is due to ballistic collisions between charge carriers and
  between charge carriers and the lattice atoms, just like in a gas). The
  diffusion coefficient is the product of thermal velocity and mean free path,
  thus coming to a moderate value to predict the transport rates of charge
  carriers by diffusion in the depletion layer. One can also formulate the
  diffusion coefficient in terms of length and time scales, the latter of which
  represents relaxation times from scattering events. The interested reader is
  referred to Lundstrom's Carrier Transport for a full and quantitative account
  of drift and diffusion transport (which are generally not independent due to
  cross effects, though the random walk orientation of diffusive transport is
  never changed). 

.. _Richard Fitzpatrick, Quantum Mechanics: http://farside.ph.utexas.edu/teaching/qmech/Quantum/node50.html

The Transistor
--------------

The asymmetry of matter is the key to the function of the transistor, but the
:math:`n`-:math:`p`-:math:`n` transistor is just the negative of the
:math:`p`-:math:`n`-:math:`p` transistor, by which I mean its behavior is the
same when all signs are inverted. So it suffices to talk only about the
:math:`n`-:math:`p`-:math:`n` transistor. A vacuum triode can be used for
switching or amplifying. There are two main types of transistors which
have the same functions, the metal oxide semiconductor field-effect transistor
(MOSFET) and the bipolar junction transistor (BJT). Here I am talking about the
MOSFET as a switch used for computation, the transistor's most famous role
today [#]_. The BJT is the more straightforward generalization of
the diode, but the MOSFET (with some device arrangements (CMOS) and geometry
changes (FINFET)) is what is used for computer chips today. Also, the
three-letter designation is usually used for BJT, and for FETs it is convention
to use nMOS for :math:`n`-:math:`p`-:math:`n` and pMOS for
:math:`p`-:math:`n`-:math:`p`.

The nMOS can be thought of as two diodes, or two :math:`p`-:math:`n` junctions,
opposing each other with a thin shared :math:`p`-type region. Under no bias,
these junctions will form depletion layers like in the diode. The gate controls
the electric field in the :math:`p`-type region (and extend through the
junctions and into the :math:`n`-type regions). The gate is a metal and
conductor, and it is electrically isolated from the doped semiconductor regions
by an oxide. The electrodes are on the opposite :math:`n`-type regions.  The
:math:`n`-type region at a higher potential is called the drain, and the
:math:`n`-type region at a lower potential is called the source, because
electrons flow from lower to higher potential. By the symmetry of the device,
it doesn't matter which direction the voltage is in and therefore which
terminal is source or drain. The gate in an on-state changes the electric field
as in the below schematic to point into the device, and therefore draw
electrons to it. 

.. figure:: figs/mosfet.svg
   :alt: schematic of mosfet showing electric field at high gate to source voltage and nearly zero drain to source voltage

   A qualitative schematic showing the electric field by lines of force
   generated by high gate to source voltage.  The arrows point away from the
   gate because positive charge is repelled. The electrons in the
   :math:`n`-type region are attracted to the two :math:`p`-:math:`n`
   junctions, but more strongly closer to the gate, and likewise for the holes
   in the p-type region. This eventually leads to a depletion layer and then
   inversion layer forming near the oxide-:math:`p` junction. This symmetric
   drawing is showing the field from the gate is the same towards the drain and
   the source.  But in order for the device to be on the drain to source
   voltage must be greater than zero. At low drain to source voltages the field
   from the gate would dominate and the electric field would be approximately
   symmetric like shown.
   
   No length scale is provided because the depletion layer thickness depends on
   the doping, which would be tuned to make a transistor of a given dimension.

Depletion Layer at Zero Bias
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For transistors bias refers to the gate to source voltage (and not the drain to
source voltage, as one might guess by analogy to diodes). The oxide-:math:`p`
junction forms a depletion layer in the :math:`p`-type region similar to that
of a :math:`p`-:math:`n` junction. The oxide can't annihilate any of the
carriers, but the hypothetical path of carriers from two regions annihilating
at an interface is just one of many hypothetical paths a system can take to
reach equilibrium. Here one can imagine the holes leave the oxide-:math:`p`
junction and annihilate at the :math:`p`-:math:`n` junctions [#]_. While the
oxide has no charge accumulation, the metal behind it, which is held at high
potential, has charge depletion, and the depletion layer in the
:math:`p`-type region compensates for this. At low gate to source voltages, a
depletion layer forms at the oxide-:math:`p` junction, but this is too wide for
diffusion to cause current. Therefore the gate to source voltage has to be
increased to form the inversion layer, where electrons are drawn into the
region and are driven by the field.

In the below schematic, the electric field strength is constant through the
oxide because the oxide has no mobile charges by which to form a depletion
layer. It decays step-wise by the planes of charge from dopant atoms just as
before, under the same approximation as before that dopants are uniformly
distributed in a cubic grid. In device design the oxide thickness is taken to
be as small as possible while preventing current from the :math:`p`-type region
to the gate because it requires a higher potential at the gate to obtain the
same electric field strength at the oxide-:math:`p`-type junction.

.. figure:: figs/oxide-p-1.svg
    :alt: schematic of depletion layer formation at an oxide-p junction in an nMOS

    The before and after equilibrium, using a hypothetical path of joining an
    oxide gate device element and a :math:`p`-type region. The gate
    spontaneously gains a surface charge and a depletion layer is formed in the
    :math:`p`-type region. A hypothetical process for this would be that the
    mobile holes move away from the junction, which then causes the charges in
    the metal to move to compensate the exposed dopants. The simple model
    offered here again only shows how the depletion layer could be stable, not
    how it would come to be or what would make it a particular width (see
    :ref:`depletion-layer`). By the arguments in the footnotes of this section
    the system when at zero bias is as if it were at positive bias, because of
    a negative flatband voltage, which would explain why holes are moved away
    and the depletion layer is stable, but this requires explanation beyond the
    simple model given here.

.. figure:: figs/oxide-p-2.svg
    :alt: the oxide-p junction after the depletion region forms from hypothetical annihilation with resulting electric field

On State at High Bias
~~~~~~~~~~~~~~~~~~~~~

When the gate voltage to the source is positive, electrons from the source are
attracted to the :math:`p`-:math:`n` interface, especially nearer the gate. The
electric field imposed has to offset the repulsive electric field from the ions
in the depletion layer at the :math:`p`-:math:`n` junctions like in the diode.
But more importantly it has to attract electrons to channel through the
depletion layer formed at the oxide-:math:`p` junction where there are
negatively charged ions.  In fact, because the :math:`p`-type region is so much
wider than depletion layers at :math:`p`-:math:`n` junctions, the quantitative
analysis of an nMOS doesn't even consider the :math:`p`-:math:`n` junctions
[#]_.  Rather, the conduction is modeled by a surface charge at the
oxide-:math:`p` junction. When the gate voltage to the source exceeds a
threshold voltage, an inversion layer at the oxide-:math:`p` junction forms in
which the electrons become a majority carrier in a :math:`p`-type region with
negative ions. The electrons then flow from source to drain through the
inversion layer.  

.. figure:: figs/inversion.svg
    :alt: qualitative schematic of the formation of an inversion layer

    In this model, the inversion layer is a surface charge in which the
    electrons hug the oxide-:math:`p` junction. 
    
    The depletion layer extends farther into the bulk than before because of a
    greater bias. Note, however, that the depletion layer will not grow wider
    after the depletion to inversion transition. The previous figure was
    somewhere in the middle of depletion as a function of bias before
    inversion. The current model can only explain this if the surface charge
    would be added to compensate any additional potential, but again, the
    current model only explains stability, not cause, of the layer forming. The
    concentration of electrons at the surface can again be depicted assuming
    the in-page depth is the same as the width in the shown cross-section, but
    it is arbitrary like in the diode because it depends on how much greater
    the bias is to the threshold voltage. Under one quantification, if the bias
    is 1 V above the threshold voltage, the number of electrons to be shown
    here would be 540. While this seems like a lot, note what is depicted is a
    fictitious dopant lattice, and the semiconductor crystal is about a million
    times as dense.

What is shown in the figure is the bias, but whether or not the electrons
travel along the oxide-:math:`p` junction depends on the drain to source
voltage. Because the gate to source voltage controls the switch, even for a
near-zero drain to source voltage, like depicted in the earlier figure, there
will be current.

The threshold voltage (or more precisely minimum electric field strength)
increases with doping concentration of the :math:`p`-type region, opposite to
the case of the diode. The :math:`p`-type region in the nMOS is a thin region
between the two :math:`n`-type regions, different from :math:`p`-type region in
the case of the diode where the volumes of the :math:`p`-type and
:math:`n`-type regions were similar. It isn't a source of hole current, and
electrons are here the only charge carriers making a current as they travel
from the :math:`n`-type source to drain throught the inversion layer [#]_.

.. rubric:: Footnotes

.. [#]
  The MOSFET can act both as a switch (on/off valve) and an amplifier,
  depending on circuit and which region of operation is active (linear or
  saturation, though linear can also amplify depending on the gain
  coefficient).  For an exhaustive treatment of these cases, see Agarwal and
  Lang's Foundations of Digital and Analog Electronics Chapter 7 (switching)
  and Chapter 8 (amplifying).  The vacuum triode started out and continued to
  be most often used as an amplifier, sometimes even today in some audio
  equipment, but historically was also used in early computers as switches like
  the MOSFET.

.. [#]
  Why would holes be moved away at zero bias? In general, electrons are more
  attracted to semiconductor materials than to metals (at least, at the doping
  concentrations used). This kind of chemical/quantum physical attraction can't
  be accounted for in this model, but it ends up just shifting the effect of bias
  (so that at zero bias, it is as if you have a positive bias pushing away the holes).

.. [#]
  The :math:`p`-:math:`n` junction still plays a role by preventing the
  majority carrier, holes, from being conductors when the bias is near or below
  zero (more precisely, when it is below the flat band voltage).  That is, the
  junction has a device function of preventing leakage current, not merely an
  artifact of the :math:`n`-type region used as a source of electrons (though
  it would not be possible to create a MOSFET using only one carrier type
  region and metal electrodes anyway since metal electrodes can source holes or
  electrons).

.. [#]
  This is how the MOSFET differs most significantly from the BJT which has current
  into or out of each region and is the more straightforward generalization of
  the diode. The :math:`p`-type region in the MOSFET isn't attached to an
  electrode to which it could send electrons after generating hole-electron
  pairs in order to make a hole current.  The only way it would generate
  carriers is by generating electron-hole pairs and pushing electrons into the
  neighboring :math:`n`-type regions which would cancel the effect of hole
  current.

Conclusion
----------

In the transistor the gate is the handle of an active valve---by putting it at
a high voltage to source, current will flow between the drain and source, and
by putting it at a low voltage to source, current will be closed between the
drain and source. This switching is fundamental to how computers work. Computer
chips have a small number of inputs and outputs relative to the number of
transistors inside them, which is different from, e.g., a switchboard. But by
alternatively switching transistors on and off through the limited number of
inputs, calculations can be done and their results stored in registers, a
process that iterates over time in clock cycles. The subject of how this is
exactly done is computer architecture and is beyond the scope of this post. It
suffices here to state that, once one has an active valve and a few other
things like register storage, one has the parts needed to store and retrieve
results and do logical operations on them, and therefrom to do calculations
most everyone is familiar with, such as addition, subtraction, multiplication,
and division.

The explanation of the transistor here was elementary and based on concepts in
classical physics, namely, the asymmetry of matter and the motion of electric
charges. The inventors and contemporary workers of the transistor were pioneers
in solid state physics, which is founded in quantum mechanics. The level of
explanation presented here is, of course, not sufficient to fully understand a
transistor, and even moreso a modern one which has non-local effects and
mesoscale transport.  But what is of value is that such an elementary model can
consistently explain the mechanisms of solid state devices as analogous in
operation to vacuum ones---in fact, that was what informed people of the
possibility of transistors more than 2 decades before they were succesfully
made [#]_.

.. rubric:: Footnotes

.. [#] 
  See Marder, Solid State Physics Section 19.4.5.

Appendix
--------

Tables of Symmetry for Antimatter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The design of vacuum tubes and transistors depends on the asymmetry of matter:
heavy protons making up immobile nuclei and light electrons which conduct
charge. It is only appropriate to discuss the opposite case, antimatter, which
is a sign-reciprocal of matter in which everything would be reversed. The
columns are carrier charge, the rows are mass, the entries are particles. The
particles are arranged in the below table. The NW-SE diagonal, by convention
called the diagonal, has the particles which make up matter. The SW-NE
diagonal, by convention called the anti-diagonal, has the particles which make
up antimatter [#]_. 

+-------+-------+-------+
|       |  \+   |  \-   |
+-------+-------+-------+
|   h   |   p   |   e*  |
+-------+-------+-------+
|   l   |   p*  |   e   |
+-------+-------+-------+

What if antimatter were to be used in a vacuum tube? In the below table, the
row is the "sign" of the gate potential (actually the sign of the voltage
to anode), the column the sign of a hypothetical charge carrier, and the
entries the result of conduction or no conduction under the assumption of a
constant direction of bias of the cathode and anode. Only the top right entry
is possible---the bottom left entry is not since there is no stable and mobile
positive charge carrier in vacuum like the electron [#]_.

+-------+-------+-------+
|       |   \+  |   \-  |
+-------+-------+-------+
|   \+  |   N   |   C   |
+-------+-------+-------+
|   \-  |   C*  |   N   |
+-------+-------+-------+

.. rubric:: Footnotes

.. [#]
  I am unsure why anti-diagonal is given with a hyphen, whereas antimatter (or
  anticlockwise) are not. The orthography of hyphenation in English appears to
  be effectively ruleless, or having so many exceptions to rules as to confound
  many or even most predictions.

.. [#]
  Positively charged ions can be made in vacuum, but it requires higher energy
  processes since they are so massive relative to electrons. The conditions are
  extreme enough that effectively it not possible to use positive charge
  carriers for vacuum devices. Scientific instruments which use positively
  charged ions make them by high temperature and field-enhanced emission, and
  those require special set-ups to get rid of the electrons which come with the
  ions. 

The n-node
~~~~~~~~~~

The :math:`n`-node, where here :math:`n` stands for an integer rather than
negative, is a sequence of :math:`n`-type and :math:`p`-type regions in row.
Semiconductor :math:`n`-nodes were developed after vacuum :math:`n`-nodes which
are defined as having :math:`n` electrodes, and continued beyond the vacuum
triode and transistor. The arrangement of :math:`n` and :math:`p`-type regions
for higher :math:`n` are not blocks in sequence like the semiconductor diode
and MOSFET/BJT transistors. A list of vacuum :math:`n`-nodes and semiconductor
device analogs is given below.

- pn, np: diode 
- pnp, npn: triode (transistor) 
- pnpn, npnp: tetrode (thyristor) 
- pnpnp, npnpn: pentode (if you count the number of regions, an insulated gate bipolar transistor has 5)
- pnpnpn, npnpnp: hexode (bidirectional triode thyristor)

Beginning at thyristors, not each region has its own electrode.

Calculation File
~~~~~~~~~~~~~~~~

The figures provided are only semiquantitative, but calculations were made with
the equations provided by the models of the sources above cited to inform the
depicted quantities. The calculation file is included below (download:
:download:`calcs.py`).

.. literalinclude:: calcs.py
