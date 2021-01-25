.. _linux-for-lab-notes:

Linux For Lab Notes
===================

Linux supports text searching and other command line interfaces (CLI)
which are either poorly implemented or not implemented (natively) at all
in Windows. Of course unix based systems such as MacOS and OpenBSD also
support these--I am using the convention of referring to GNU/Linux by
its kernel, linux, and citing this because it is the most popular and
robustly developed family of free operating system.

In this post I give a few examples of using CLI and terminal text
editors for digital lab notes in a simple directory structure. This
tutorial is supposed to assist people generally but is motivated for
those using the laboratory management program I develop at lab-notes_.

.. _lab-notes: https://github.com/dollodart/lab-notes

Using a terminal editor may have some disadvantages over a full-featured
text editor. However, most people are very acquainted with text editors,
so I demonstrate the use of a terminal editor here. Vim, an improved
form of the text editor vi, is only one terminal editor available on
linux systems. Only some of what is presented, like the different
editing modes, is particular to Vim over other terminal text editors.

Searching by Patterns
---------------------

Let us assume that there is already a system in place which stores data
in text files. How can we search those text files? Below I give the
means of doing that in a linux based system.

The command line utilities which allow the below discussions to be
applied to all text files in a directory, are below. These would be
input on the command line and so have the necessary escape characters
(backslash on semicolon, literals quotes on file stand-in curly
brackets) for a bash shell.

- search: ``find . -type f -name "*.txt" -exec grep --perl-regexp "<pattern>" "{}" \;``
- replace: ``find . -type f -name "*.txt" -exec sed --in-place=bckup '<replacementcommand>` "{}" \;``

I am using perl compatible regular expressions. The vim expressions show
how to do the grep-like find and the sed-like replace in the vim command
line.

grep, sed, awk, and all that 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
These are venerable tools. Their functionalities are 

- grep: find pattern 
- sed: find and replace pattern basic (sed is a core utility including in /bin) 
- awk: find and replace pattern advanced

Here I only cover the basics of grep and sed. There are excellent books
on these programs, in fact the O'Reilly series started with Sed and
Awk, and has since extended to many others (including other programs
considered here like vi and vim).


The problem these programs solve, to find instances of a general
pattern, and acting on it, is a problem for which there is a lot of
theory in computer science (for the interested, the key term is finite
automaton). The non-trivial nature of this problem can be shown by the
limitations of the following naive algorithm for matching a literal
string, a sequence of characters, in a text file:

Given a string (of the file contents) and the literal, begin an
iteration of the string index. If the substring given by the interval of
the index through the length of the literal to be matched matches the
literal, return a match and continue. Otherwise return nothing and
continue. If no more characters exist to make the substring, quit.

This naïve algorithm is efficient for matching a literal (it might be
made better by comparing each character in the string first to the first
character of the literal, and only then comparing the next character
in the string to the second character of the literal, and so on, but
that is a constant factor). But it is very inefficient for a general
pattern, like 3 digits. If you were to use this for a general pattern,
you would have to enumerate all of them (000, 001, 002, ...) and check
against them all. This gives a number of computations as the product of the
search text length and the number of literal patterns belonging to that
general pattern, in this case 9^3 = 729. Because many literals exist for
a general pattern (without further qualification, a pattern is assumed
to be general), using the naïve algorithm leads to combinatoric
explosion in the general case.

In fact, a finite automaton does a character by character match, with
two catches: it matches the character to one in a provided set, and
it changes the set it compares the character to based on the current
character value (for a given pattern, the sequence of characters
determine the state at each character in a match at each point
only based on the current character value).

Finding with Regular Expressions
--------------------------------

Regular expressions are ways of specifying a pattern.

As a motivating case, suppose one is interested in temperatures (and
maybe angles) and so one wants to find a number with or without a space
next to a degree symbol °. How to use regular expressions?

Note: in the below I am using the regular expressions with the
nterpretation of the characters as, by default, control characters
and not literals if they are non-alphanumeric. That is, if the
character ``x`` (non-alphanumeric) is ever used for control, then in
order for it to be interpreted as a literal, it needs to be escaped as
``\x``. Alternatively, if the character ``x`` is alphanumeric, then in
order for it to be interpreted as a control character it needs to be
escaped.  I show how Vim is used, where the default interpretation may
be literal or non-literal (Vim also has some other rules like how many
of the delimiters need to be escaped). My convention is Perl compatible,
at least for the strings given.

Enumerating some cases, there are ``12 °`` and ``1.5°``. But to
enumerate all these patterns would be large: there can either be a
space or no space, so even for numbers in the range 0.0 to 9.9 with a
degree symbol either separated by one space or with no space, there are
:math:`9\times 2 \times 9 \times 2 = 324` possible matches. This is where
regular expressions come in.

A pattern which matches all the same as the above two patterns is
``\d+\.?\d*\s?°`` (vim:``/\d\+\.\?\d*\s\?°``). Here \d stands
for any digit in 0 to 9, and + is a modifier saying 1 or more of
those digits. The ``\.?`` matches one literal dot if it exists, or
nothing. The ``\s?`` matches a space, if it exists. Note you do not have
to specify ``\d*`` after the ``\.?`` to match, due to how regex works in
extending preceding pattern matches in the case of 0 matches. But it is
retained here for ease of interpretation.

Regular expressions can match patterns with number of possible
combinations being millions, billions, or more (this is a property
of the regular expression language, that it can match an arbitrary
pattern, which is a result found in theoretical computer science). So
you can ask general questions, like what about the case of finding
any temperature quantity, with different white spaces? The below text
shows some but not all the ways a temperature in degrees celsius might be written:

12.4 °C 136.7° C 28 ° C

The regular expression to match any of these is ``\d+\.?\d\s?°\s?C``
(vim: ``/\d\+\.\?\d\s\?°\s\?C``). To match a temperature of
degrees Fahrenheit or Kelvin like 23.2 ° F or 235 °K, use
``\d+\.?\d\s?°\s?[CFK]`` (vim:``/\d\+\.\?\d\s\?°\s\?[CFK]``). The
square brackets indicate choose any one character from the set. For
example, ``\d`` is equivalent to ``[0123456789]``. Usually kelvin
are not reported with degree symbols, so to match cases like
121K or 235 K, add a zero or more ``\d+\.?\d\s?°*\s?[CFK]``
(vim:``/\d\+\.\?\d\s\?°*\s\?[CFK]``). This may be disagreeable,
since it will also match units of coulombs or farad. Instead,
there should only be a match with the omission of a degree
symbol in the case of K. In that case we need to use
groups like so: ``\d+\.?\d\s?(°\s?[CF]|°\s?K)`` (vim:
``/\d\+\.\?\d\s\?\(°\s\?[CF]\|°\s\?K\)``). The bar character separates
two possibilities. These rounded brackets were necessary, rather than
square brackets, because the options were to choose among a set of
possibilities more than one character long.

This use of rounded brackets to denote matching groups segues into the
next discussion: replacing with regular expressions.

Finding and Replacing with Regular Expressions
----------------------------------------------

The sed syntax for replacing, using regular expressions to find, is given here. The general sed syntax is

``s/<regex_patterns>/<replacement>/<globalsetting>``

Here ``/`` is just one example of a delimiter, for example, one could
use ``s^a^b^g`` (vim:``:%s^a^b^g``) to replace all a characters with
b characters. The ``g`` stands for global, and an empty character
like ``s^a^b^`` (vim:``:%s^a^b^``) will only replace the first a
character found with b. Of course one could do a regex search, like
``s^[a-z]^b^g`` (vim:``:%s^[a-z]^b^g``) to replace all lowercase letters
with b.

Quite often you desire to replace a regex pattern with something
derived from that match. For example, you want to replace any word
of a given length with the first 3 letter abbreviation. To match
words of a 15 character length or greater, you can do ``[a-z]{15,}``
(vim:``[a-z]\{15,}``). However, in order to substitute, the first
three letters have to be grouped, like ``([a-z]{3})[a-z]{12,}``
(vim:``\([a-z]\{3}\)[a-z]\{12,}``). Unlike the use of rounded
brackets in finding for matching between possibilities greater
than one character in length, the use in replacing is to define a
group to be used in the replacement, though it can serve the first
purpose, too. Escaped numbers in the replace field refer to a group
matched in the search pattern. For the entire expression, it is
``\0``, and for numbers greater than zero, it is the left-to-right
groups, including nesting (numbered by appearance of left rounded
bracket). In this case there is only one matching group, so
the replacement command is ``s/([a-z]{3})[a-z]{12,}/\1./g``
(vim:``:%s/\([a-z]\{3}\)[a-z]\{12,}/\1./g``).

In the vim command line, it is required to specify the range of
text. Here I chose the whole file (buffer), which is ``%``. To replace
on the current line, use ``.`` before ``s``. For a range of lines,
``3,5``. You can use relative ranges, like ``.,+15`` for 15 lines from
the current line.

Special characters in Vim
-------------------------

In insert mode, any unicode character can be put in by ``Ctrl+v`` and
the four digits of the unicode encoding. To get a degree symbol, for
example, in the insert mode press ``Ctrl+v`` and then ``u,0,0,b,0``. The
unicode encoding for the degree symbol, °, is the 4-digit hexadecimal
00b0. This is prefaced with u because ``Ctrl+v`` allows interpretation
of many non-literal things. For example, ``Ctrl+v`` and then enter will
make a carriage return, rather than the newline.

Unicode encodings are freely available online to find the 4-digit
hexadecimal for "non-keyboard" symbols.

One can map commonly used characters in the .vimrc user root directory,
``~/.vimrc`` (make this if it doesn’t exist). Here imap is used, for mapping
in the insert mode.

``:imap deg. °``

Now when deg. is typed in insert mode, the cursor will pause on the
sequence and then return the degree symbol if all four characters are
typed, or expand after some time (less than 1 second) to. Using standard
american english abbreviations, with period endings, lets these
abbreviations be used without interfering with typing the full words.

Greek letters are often used, and it is possible to use mappings for
these. For 4 digit unicode charactesr, use ``Ctrl+v``, u in insert mode, and
insert the 4 digits. For 5 digit unicode characters, for example for
italic mathematical symbols, use ``Ctrl+v,Shift+u`` in insert mode, then
enter the 5 digits.

I have used imap for all the greek letters, using three character
abbreviation such as alp. for alpha. But too many imaps can make
spotting typos more difficult because the cursor is jumping from the
recognition of many starting sequences. An escape character can be used,
such as the backslash, which omits the need for a period to indicate an
escape code:

``:imap \alpha 𝛼``

Unicode characters can be used in some programming languages, so
that one can program scripts with greek characters or any other
symbols. However, if you want to avoid these escape sequences in all
but laboratory note text files, you can put these mappings not in the
~/.vimrc but in a file

``~/.vim/ftplugin/text.vim``

with the following line in ``~/.vimrc``: ``filetype plugin indent on``. Then
only files with the file suffix ``.txt`` will have these mappings.

Using Vim for Long Form Text
----------------------------

Many suggest that vim is inadequate for long form text writing, but I 
find this is not the case. With little experience it is better for
navigating a document than a WYSIWYG editor. The most cited
disadvantage is that there is not point and click support of cursor
movement. But cursor navigation commands are many, in fact the majority,
of vim commands

- G: end of file 
- gg: beginning of file 
- (: beginning of sentence 
- ): end of sentence 
- {: beginning of paragraph 
- }: end of paragraph 
- L: screen bottom
- M: screen middle 
- H: screen top 
- $: line end 
- ^: line beginning (soft) 
- 0: line beginning (hard) 
- e: end word 
- b: prev word 
- t: 'till

It is a fair complaint that there are many commands for navigating the
cursor and acquaintence may be hard to learn.

The minimum understanding required to make vim faster than WYSIWYG is
(1) knowing there is an insert mode and a normal mode and how to go
between the two (from command mode to insert mode, press ``i``, from
insert mode to command mode, press ``Esc``) (2) knowing that ``/`` in
normal mode lets you find. To go to the position in text where there
is the place bohemia type ``/bohemia`` in the normal mode. In long
documents there is the potential for matching several words. It is
always possible to type out more, as in ``/the place bohemia``. In
normal mode ``n`` for find next and ``N`` for find previous lets one go
between cases to avoid retyping search criteria.

The navigation commands, like in the ones listed above or the hjkl
cursor movement, are not necessary for better performance (typos are
unique, or if not one finds multiple typos, so that if a tpyo is made,
/tpyo and insert mode with the conventional arrow, delete, and backspace
keys can be used). Only the following are needed:

- Esc: insert mode to normal mode 
- i: insert mode 
- /: find in normal mode 
- n: find next in normal mode 
- N: find previous in normal mode (note: ?bohemia is equivalent to /bohemia,enter,N) 

In any case, there are GUI forms of almost all terminal editors, e.g., xvim.

Information Control
-------------------

One can see the last date the file was modified with ``ls -l``. Using
file permissions, the ability to read, write, and execute files of
different types can be managed to ensure data security. For example

``chmod a=r FILE; chmod u+wx FILE; chmod g+x FILE``

Will set the file to read only mode for all users, then allow the file
owner to additionally write and execute, and those belonging to the file
group (automatically the group to which the user who created the file
belongs) to also execute. A more succinct command uses the numeric mode:
``chmod 754 FILE``.

As an example application, the electronic medical records mandate as
part of the affordable care act is now being fulfilled by difficult
to use GUIs which many doctors find frustrating.  Though using Linux
servers may be an overlarge technical challenge for adoption by doctors,
nurses, and other medical professionals, data entry by power users would
be much faster than is currently done with GUIs.  Scribes, which are
already in use by some corporate and private practices, could be trained
on these tools. There are some difficulties with HIPAA compliance and
authorization/encryption which are not covered here. In addition to
file access control, file encryption/decryption utilities like OpenPGP
encryption and signing tool can be used.

Templated Record Keeping
------------------------

For standard operating protocols or commonly repeated experiments,
proprietary data file types can be made which will allow for easy data
analysis and regression. These data file types may be as simple as
sets of key-value pairs. With libraries that read any of the xml based
data file formats, also spreadsheets can be used for storing data and
retrieving the results in a systematic way.

For the experimental sciences, a record of equipment performance and
maintenance which is easily searchable could reduce time spent
troubleshooting systems significantly. In the health professions,
keeping searchable records of patient documents may assist healthcare
providers in aiding patients and developing epidemiological analysis.
Humanities can do quantitative analysis of word occurance, often done in
sentiment analysis.

See how to do template based record keeping at lab-notes_.

.. _lab-notes: https://github.com/dollodart/lab-notes

Compiling to Formatted Documents
--------------------------------

In linux using the many programs (from GNU and other open source software
developers), it is possible to convert a set of laboratory notes in
a directory into a compiled document with search function, table of
contents, image display, and other helpful features of reference for
the person making the lab notebook and for their colleagues. The
laboratory worker is often too busy to make detailed summaries of their
practical knowledge, especially those outside of the scope of a Standard
Operating Protocol such as design, troubleshooting, and maintenance of
equipment, and analysis and interpretation of data. This is acknowledged
in textbooks, for example, Exercise 1.13 in "Modeling and Analysis
Principles for Chemical and Biological Engineers" has a problem
premise in which a graduated student does not respond by e-mail to
requests for the source of software used for analyzing data and so one
must treat it as a black box. While the problem of laboratory workers
not recording their findings cannot be fixed by any software, having
notes in a server allows for them to be searched.

One of the advantages of using digital lab notebooks is that the quality
of printed documents can be higher than handwritten notes--legibility is
ensured, page enumeration and timestamping is automatic, and tables of
contents and indices for commonly repeated words can be automatically
generated giving structure to the document which is either absent or
done manually by students. 

It is straightforward to make templates for compiling to print documents
and web documents. This report generation is greatly facilitated by
templates which can accommodate variable sized information (do things
like execute for loops on variable sized arrays), which many templating
libraries support as in-template compile-time code.

See how compilation based on on Markdown text using the Cheetah template library for python is done at lab-notes_.

.. _lab-notes: https://github.com/dollodart/lab-notes

Versions
--------
First posted on 2020-12-29.
