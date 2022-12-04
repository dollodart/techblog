.. _file-systems:

File Systems Theory
===================

Introduction
------------

The structure of file systems is the structure of a rooted and oriented tree,
which is a particular class of graphs. There is a root which is the ancestor of
all other files, meaning you can find a path pointing from it to every other
file. The root is a directory. Each directory [#]_ is a subtree (or internal
node); even an empty directory can be thought of as subtree pointing to nil.
Every non-directory file is an external node (or leaf). Symlinks are
quasi-directories that let you violate the tree structure of a filesystem. You
can point a symlink anywhere, and that symlink may be considered a directory of
at least one file, and possibly many depending on if it points to a directory.
Symlinks should generally be avoided, but can't always, especially for
backwards compatibility, and are quite abundant in practical systems.

Some file systems have more than one 'root', though there can only be one root
as defined above. For example, on Linux the system root is ``/`` and
corresponds to the root as defined above, but the user root is given the alias
``~`` and appears therefore to have no ancestors, as one expects for a root. The
user root can be understood as a subtree, since a tree consists of subtrees,
that is, any internal node of a tree is with its lower nodes also a tree. The
user directory is a tree within a tree which contains all the files that a
non-administrative user wants to modify, and so that subtree (usually
``/home/username``) is given the alias ``~``. In the Windows operating system,
several different user directories are given as root, at least as displayed in
the Windows File Explorer: Documents, Downloads, and Pictures are examples. 

The first thing to do in a filesystem is visualize the tree structure. Use 
``ls -R``, or for a more aesthetically pleasing presentation, the CLI ``tree``
to visualize the directory structure. Doing so on an example filesystem gives

::

        example/
        ├── a
        │   ├── a.txt
        │   ├── b
        │   │   ├── b.txt
        │   │   ├── link2a -> ../
        │   │   └── link2a.txt -> ../a.txt
        │   └── link2b.txt -> b/b.txt
        ├── c
        │   └── alphabet.txt
        └── d
            └── link2b -> ../a/b/

Here symbolic links point to other places in the filesystem, but the output of
tree only shows the directory structure defined by the children of directories.
This tree has depth indicated by left-to-right distance and breadth indicated
by top-to-bottom distance. For thorough introductions to what trees are, the
reader is referred to section 2.3 of Knuth's The Art of Computer Programming,
Second Edition (TAOCP).

.. rubric::

.. [#]
  A directory is usually defined as an address conversion table in computing,
  not a structure generating object. But in hierarchical directory system, it
  also defines structure by making address conversion to nested directories.
  Here a directory is consistent with this definition and should be understood
  as a node in a filesystem tree that is an internal node, because such details
  such as address conversion from user-defined names to internal system names
  is not relevant for the abstract discussion here. See, e.g., "Operating
  Systems: General Principles" in Ralston, Reilly, Hemmendinger, Encyclopedia
  of Computer Science, 4th Ed.. For such definitions, see, e.g., Hercog
  Communication Protocols section 10.3. 

Filesystem Structure (Tree) Properties
--------------------------------------

A filesystem with no symlinks is structured as a tree and one can measure its
tree properties. A filesystem with symlinks can be considered a tree with some
number of non-tree edges which can be ignored for the purpose of quantifying
tree properties, which I shall do here. See my package `osfs`_ for a Python
program doing this quantification.

There are different types of tree properties. The simplest property which
makes a distribution is a node property.  This would be, e.g., the node depth.
Some might object that this is a structure property, not a node property like
color or size or something unrelated to the tree in which it is placed, but
since it is defined relative to the root which is a single reference, I don't
make such a distinction. Other properties are statistics applied to some
subtrees, and so one forms a distribution of statistics. For example, the
maximum or minimum distance to a descendent from a given subtree root is an order
statistic on that subtree, and when one evaluates that for all subtrees in a
tree, one obtains a distribution of the statistic.

In addition to averages of properties, the standard deviations of these
properties is valuable to measure how consistent the file system design is
across different subtrees. Note, though, that certain properties, such as
balance defined by a difference in subtree heights, are already defined as
kinds of measures of consistency or constancy, thus the variance or standard
deviation has some additional interpretation as a measure of the consistency of
inconsistency. A tree could be consistently imbalanced in the sense that all
subtrees tend to have branches whose depth differ by a given amount. Higher
moments, such as skew, can be taken, and these may be insightful, because
designed systems aren't subject to any laws like convergence to a normal
distribution for which the skew would be zero.

For properties that are defined for every subtree in a tree, nodes lower in the
tree are 'overweighted' in how they contribute to an average for the
distribution of statistics. That is, lower nodes appear more often in the
calculation of averages. This relative weighting of nodes depending on depth
must be considered, and can be corrected for by grouping statistics by depth,
i.e., averaging the structure properties for all subtree roots at a given
depth.

Depth Properties
~~~~~~~~~~~~~~~~

The tree depth is the maximum number of edges between the root and the file
which in a simple path (a simple path doesn't have coinciding edges, that is,
it doesn't go back the same way it came. For trees that means descent-only). If
one makes a statistical definition of the tree depth which is based on
recursively defined subtree depth, then it becomes more similar to the average
depth of a node. The depth of a node is simply the number of edges from the
root and is a distribution for which statistics may be made.

A perfectly balanced [#]_ binary tree has as sum depths going as

.. math::

   1*0 + 2*1 + 4*2 + ... + 2^l*l

where there are :math:`l` levels and :math:`l = \lg(n+1)-1`. One can obtain a
closed form for :math:`\sum_{k=0}^l 2^k k` by standard methods, which asymptotically goes as
:math:`n\lg(n)`, giving :math:`\lg(n)` average depth for a node.

In summary, there are the following properties of depth:

- :math:`max(depth(st.l), depth(st.r))` (order statistic)
- :math:`\{max(depth(st.l), depth(st.r))\}_{st \in subtree\ roots}` (distribution of order statistics)
- :math:`\{depth(n)\}_{n \in nodes}` (distribution of node depths)

One measure of a filesystem depth is that the average number of directories
you have to descend to reach a file. The distribution of this would be
:math:`\{depth(l)\}_{l \in tree\ leaves}`.

Balance Properties
~~~~~~~~~~~~~~~~~~

The tree balance is the difference in heights of the right and left subtree.
The overall tree balance can be quantified as an average of the tree balance of
every subtree in the tree, including the root of the tree.  When taking an
average or (any other statistic) the absolute value should be used, otherwise
one has a 'left-biased' or 'right-biased' which would just be negatives of each
other, but when averaged could cause spurious measures depending on which
branches are left or right. If one takes a left-to-right ordering where, e.g.,
all subtrees have left-to-right order of subtrees by their depth, the answer
would come out different for balance than if alternatingly the largest, second
largest, and so forth are assigned left and right [#]_. This problem emerges
since (sub)trees can have any number of branches. A simpler measure of balance
is in the distribution of the directory depths, that is, the subtree roots and
not leaves. This simpler measure may, though, overweigh the lower directories
which are generally exponentially growing in number from the root.

Alternatively to depth, one can use the distribution of the size of subtrees
(number of nodes) to be the measure of balance. It makes the most sense to
group by the depth of the directories. If two subtrees are unbalanced, it isn't
necessarily the case that the tree to which they are attached are unbalanced by
some of the proposed measures of balance here. For example, the balance defined
by :math:`|depth(st.l) - depth(st.r)|` could be zero for a tree even when its
two subtrees are highly unbalanced.

For a perfectly balanced binary tree, the average balance is, of course, 0,
when defined as a difference between the depth of left and right subtree. The
number of nodes that are in subtrees for a tree with :math:`n` nodes goes
asymptotically as :math:`n\lg(n)`. Given that there are :math:`n` asymptotic
subtrees, the average subtree size is only logarithmic with the number of
nodes.

In summary, there are the following properties of balance:

- :math:`|depth(st.l) - depth(st.r)|` (for binary trees)
- :math:`|depth(st.subtree) - average(depth(st.subtreee), st)|` (generalized from the result for binary trees for any trees)
- :math:`\{depth(st)\}_{st \in subtree\ roots}` (the same as depth properties)
- :math:`\{nnodes(st)\}_{st \in subtree\ roots}` (this should be split out or grouped by depth)

Branching Factor
~~~~~~~~~~~~~~~~ 

The branching factor for an internal node is the number of direct children it
has. The overall tree branching factor can be quantified as the average of the
branching factor for every internal node. The branching factor can be seen as a
simpler, and less insightful form, of the balance. It has only one expression
as the distribution :math:`\{\sum_{st.children} 1\}_{st in subtree roots}`.

For a perfectly balanced binary tree, the average branching factor is, of course, 2.

.. rubric::

.. [#] 
    Perfectly balanced here means a kind of symmetric tree. A balanced binary
    tree, as given in section 6.2.3 of TAOCP, has a height between :math:`lg(n+1)` and
    :math:`1.4404\lg(n+2) - 0.3277`. An optimum balanced tree has all external nodes on
    two adjacent levels. Perhaps the word here is power-tree, or dense tree, or
    something similar? The standard is a weight-balanced tree, which has the
    size of the subtrees as constant. The reason for power-tree is that the
    number of nodes is :math:`2^m-1`. Knuth also gives a "complete
    binary tree" in section 2.3.4.5, and the perfectly balanced tree may be
    thought of as a complete binary tree for which the number of nodes is such
    a power as given before. It may also be called a Cayley tree, which is defined as
    a 'symmetric regular tree in which each node is connected to the same
    number k of others' (Newman, Networks 2nd Ed., 338). In particular, it is
    a 2-Cayley tree.

.. [#]
    See TAOCP, section 2.3.4.2 for a distinction between oriented and directed trees.

Symlinks and Directed Graph Structure
-------------------------------------

Symlinks, also known as soft links, are places in the filesystem which point to
other places. When you have a graph that is otherwise an oriented tree but its
tree structure is violated by some number of edges, you classify those non-tree
edges as either "forward", "back(ward)", or "cross". 

- Forward edges point from a place higher in the tree to a place lower in the
  tree where there is still an ancestor-descendent relationship. A
  quasi-forward edge occurs when a symlink is child to a directory which is an
  ancestor of what it points to. This isn't very useful since search paths for
  programs are specified to search everywhere in a subtree. Having a
  quasi-forward symlink point to a descendent only results in a depth-first
  search finding it faster, provided a search first explores that symlink
  rather than the directory (in a DFS, you can choose to to explore all
  non-directories before descending into some directory to make sure this
  happens), or a breadth first search finding it faster in all cases. Note that
  there are no forward edges in filesystems because a symlink cannot also be a
  directory.

- Back(ward) edges point from a place lower in a tree to a place higher in the
  tree where there is an ancestor-descendent relationship. Backward symlinks,
  for which the link is located in a directory which is a descendent of some
  directory it points to, are rarely used too. They are only useful if a search
  path begins at a point deeper in a tree than where the resource is, so that a
  backward symlink will be point the program to a place above where it started
  its search (also, backward symlinks must have a directory target, and it is
  more common for regular files to be targets). One can also define
  *quasi-backward* symlinks if the link points to a file which is in a
  directory ancestor of the link. 

- Those edges which are cross but not quasi-forward or quasi-backward are
  termed *very cross*.

- Sometimes symlinks point to a file which is in the same directory as them. In
  such a case, the symlink has no topological effect on the graph of the
  filesystem. One may call this an *alias*.

The degree of separation of any two files in a filesystem, including between a
symlink source and target, is the length of the (unique) path in the tree (that
is, excluding symlinks) between them. With symlinks, which are necessarily
directed, one can also define a degree of separation for directed paths which
takes into account symlinks. To evaluate the average degree of separation
without considering symlinks is simple to do by tree traversal (and is the same
thing as an average depth). To evaluate the degree of separation in the case of
symlinks (relative to the root) requires a single-source shortest-paths
algorithm from the root. To evaluate statistics on the degree of separation in
the case of symlinks requires an all-sources shortest-paths algorithm, for
which there are many efficient implementations.

Symlinks also introduce the possibility for cycles when searching leading to an
infinite loop. For example, suppose you have a directory A with a symlink B to
another directory C which has a symlink D to your original directory A. Then
your search path could start in A, descend until it finds B, go to C, then
descend until it goes to D, then go to A, and loop infinitely. The question is
then how to avoid this problem. One way is to keep memory of all directories
which have been visited, and only follow a symlink if it points to a directory
which hasn't yet been visited. During a search this is done by keeping
the object state of all files as visited or not visited. [#]_

Parent-child relationships for directories and files are often understood to be
bidirectional because trees by definition only have one path between any two
nodes, though here they have been considered oriented from the root. This
bidirectionality is evident in the parent alias ``..`` in Unix file systems for
something like the ``cd`` command and the ability to list all children
(files/subdirectories) of a directory with a command like ``ls``.  However,
symlinks are fundamentally directed: they point from a source to a target. If
you think of the filesystem as an oriented tree where each upper directory
points to lower directories, then it is often the case that symlinks make
directed acyclic graphs, though sometimes they make general directed graphs in
the case of cycles like above discussed.

The example directory has 4 symlinks, which are classified below:

::

        example/
        ├── a
        │   ├── a.txt
        │   ├── b
        │   │   ├── b.txt
        │   │   ├── link2a -> ../ (back)
        │   │   └── link2a.txt -> ../a.txt (quasi-back)
        │   └── link2b.txt -> b/b.txt (quasi-forward)
        ├── c
        │   └── alphabet.txt
        └── d
            └── link2b -> ../a/b/ (very cross)

.. rubric::

.. [#] 
  The example directory used in the introduction can't be put in the build path
  for the Sphinx project here because of infinite looping from the filesystem
  traversal (called walking, as in the python ``os`` module's ``walk``
  function). However, it can be analyzed with the `osfs`_ package because
  anyways symlinks are not followed. All files in a filesystem are assumed to
  be reachable from the specified root.

.. _`osfs`: https://github.com/dollodart/osfs

Conclusion
----------

Quantifications of the tree properties of depth, balance, and branching factor
were given, and their asymptotic expression or exact value for a perfectly
balanced was given. Classifications of non-tree edges in practical filesystems
containing symlinks was given, as well as the means of evaluating properties of
directed acyclic graphs and general graphs by the shortest-paths method.

References
----------

All theory used in this post is derived from Introduction to Algorithms (CLRS)
and The Art of Computer Programming (TAOCP).

See `Janakiev's Python Filesystem Analysis`_ for a tutorial and a link to a
GitHub repo that analyzes filesystems using a pandas based python package. The
idea of using pandas in python to analyze filesystems is at least as old as
2012: see the Usenix ;login: article Data Processing with Pandas (link
available at https://www.dabeaz.com/usenix.html). Of course, the idea of analyzing
filesystems is as old as filesystems. 

.. _`Janakiev's Python Filesystem Analysis`: https://janakiev.com/blog/python-filesystem-analysis/

Version
-------

First posted on 2022-12-02.
