How this was made 
=================

This website is made by the following process, using only FOSS:

#. Posts are written in LaTex for mathematical typesetting and ease of compiling
#. The pandoc library is used to convert LaTex to ReStructuredText--this is only possible if the LaTex document uses a limited set of LaTex packages which ReStructuredText supports, but the most important ones from ams are supported 
#. The python package Sphinx is used to compile HTML from ReStructuredText with styling specified by template in a required ``conf.py`` file
#. The http server is ran by Apache 2 (in addition to http, Apache 2 sets up PHP and MySQL servers, though the latter two are not used for this website).
   
The advantage of Sphinx is that it creates navigation bars with the same structure as the generating directory, and requires only a small number of table of content specifications.

Images are made either with Sphinx supported programs like GraphViz or included as raster images.

Other details
-------------
First a discount HP Compaq DC5800 computer was made into a server by installing the Lubuntu 18.04 LTS operating system and the Apache 2 HTTP web server software. A domain name was purchased from a company so that network directing routers (not only those in a house, but also those that direct network traffic between countries, cities, et cetera) would point to this server.

I then opted to use a web hosting service since the firewall would close port 80 for reasons I couldn't diagnose, and also to make the website available 24/7 (robust to power outages, moves, and other disturbances on a home server).

Images
------

From docutils docs I found the following:

    Scalable vector graphics (SVG) images are the only standards-compliable way
    to include vector graphics in HTML documents. However, they are not
    supported by all backends/output formats. (E.g., LaTeX supports the
    PDF or Postscript formats for vector graphics instead.)

But there is the ``pdf2svg`` program for converting pdf to svg
format. Therefore, for pdf output graphics, svg could be made, which can
be included as an image or directly in a raw directive as HTML to allow
svg object features.
