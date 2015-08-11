# inriawrapper

A python library to make maximum use of Sanskrit related tools available at http://sanskrit.inria.fr/

# Usage

See [Documentation](https://github.com/drdhaval2785/inriawrapper/blob/master/documentation.html) for usage of various functions.

# Requirements

1. [python2.7](https://www.python.org/)

2. [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/)

3. Libraries used - codecs, urllib2, datetime, time, re

4. [Transcoder](https://github.com/funderburkjim/sanskrit-transcoding) module by Jim Funderburk.

# Todo

The library is still under development.

The expected output of the project is-

1. To derive a python functionality for declention of *noun* forms based on http://sanskrit.inria.fr/DICO/grammar.en.html - *Done*

2. To derive a python functionality for declention of *verb* forms based on http://sanskrit.inria.fr/DICO/grammar.en.html - *Done*

3. To derive a python functionality for declention of *kridanta* forms based on http://sanskrit.inria.fr/DICO/grammar.en.html

4. To develop [SanskritMark](https://github.com/drdhaval2785/inriawrapper/blob/master/SanskritMark.md) (a specification like markdown for writing Sanskrit stuff) which can be benifited by the present scripts. - *Done Primary Draft*

5. To derive a python functionality for dictionary lookup of a Sanskrit word based on http://www.sanskrit-lexicon.uni-koeln.de/ data.

6. To derive a python functionality for getting the possible details of the root noun / verb from inflected words (based on http://sanskrit.inria.fr/DICO/index.en.html#stemmer). - *Done*

7. Write a parser for texts written in the specification mentioned in point 4.- *Done*

8. Write a converter from txt to SanskritMark - *Done*

9. Write a converter from SanskritMark to txt - *Done*

10. Write a converter from html to SanskritMark and vice versa.

11. To derive a python functionality for sandhi generation given in http://sanskrit.inria.fr/DICO/sandhi.en.html


# Duration

The project has just started. It would take quite some time to complete all the functionalities.

# Limitations

The project depends on the availability of internet for its usage, because it fetches data from external websites.

Source code for sanskrit.inria.fr is made public, but yet it is not friendly to install. If it gets installed easily, we may get 100 % standalone system for local environment.
