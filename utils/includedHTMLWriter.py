## -*-Pyth-*-
 # ###################################################################
 #  FiPy - a finite volume PDE solver in Python
 # 
 #  FILE: "includedHTMLWriter.py"
 #                                    created: 9/29/04 {11:41:20 AM} 
 #                                last update: 9/29/04 {11:47:46 AM} 
 #  Author: Jonathan Guyer <guyer@nist.gov>
 #  Author: Daniel Wheeler <daniel.wheeler@nist.gov>
 #  Author: James Warren   <jwarren@nist.gov>
 #  Author: James Warren <jwarren@nist.gov>
 #    mail: NIST
 #     www: http://www.ctcms.nist.gov/fipy/
 #  
 # ========================================================================
 # This document was prepared at the National Institute of Standards
 # and Technology by employees of the Federal Government in the course
 # of their official duties.  Pursuant to title 17 Section 105 of the
 # United States Code this document is not subject to copyright
 # protection and is in the public domain.  includedHTMLWriter.py
 # is an experimental work.  NIST assumes no responsibility whatsoever
 # for its use by other parties, and makes no guarantees, expressed
 # or implied, about its quality, reliability, or any other characteristic.
 # We would appreciate acknowledgement if the document is used.
 # 
 # This document can be redistributed and/or modified freely
 # provided that any derivative works bear some notice that they are
 # derived from it, and any modified versions bear some notice that
 # they have been modified.
 # ========================================================================
 #  See the file "license.terms" for information on usage and  redistribution of this file, and for a DISCLAIMER OF ALL WARRANTIES.
 #  
 #  Description: 
 # 
 #  History
 # 
 #  modified   by  rev reason
 #  ---------- --- --- -----------
 #  2004-09-29 JEG 1.0 original
 # ###################################################################
 ##

import os

from docutils.writers.html4css1 import HTMLTranslator, Writer as HTMLWriter
from docutils import languages

class IncludedHTMLTranslator(HTMLTranslator):
    def __init__(self, document):
	HTMLTranslator.__init__(self, document)
	
	self.head_prefix.insert(0, r"""<!--
This file was automatically generated by invoking

    python setup.py build_docs <dash><dash>webpage
    
Any changes to the contents should be made in the file '""" + document.attributes['source'] + r"""'
-->
""")
	
	dir = os.path.join('documentation', 'www')

	headObj = open(os.path.join(dir, 'head.html'))
	head = headObj.read()
	
	self.body_prefix.append(head)
	
	tailObj = open(os.path.join(dir, 'tail.html'))
	tail = tailObj.read()
	
	self.body_suffix.insert(0, "</div>")
	
	self.body_suffix.insert(0, r"""<div id="validation">
<p>
  <a class="right" href="http://jigsaw.w3.org/css-validator">
  <img style="border:0;width:88px;height:31px" src="http://jigsaw.w3.org/css-validator/images/vcss" 
  alt="Valid CSS!" /></a>  
  <a href="http://validator.w3.org/check?uri=referer"><img
      src="http://www.w3.org/Icons/valid-xhtml10"
      alt="Valid XHTML 1.0!" height="31" width="88" /></a>
</p>
</div>
""")
	
	import time
	mtime = time.gmtime(os.stat(document.attributes['source']).st_mtime)
	format = "<div id=\"update\">\nLast updated: %a, %d %b %Y %H:%M:%S +0000\n</div>\n"
	self.body_suffix.insert(0, time.strftime(format, mtime))
	
	self.body_suffix.insert(0, "<div id=\"subfooter\">\n")
	    
	self.body_suffix.insert(0, tail)

class IncludedHTMLWriter(HTMLWriter):
    def __init__(self):
	HTMLWriter.__init__(self)
	self.translator_class = IncludedHTMLTranslator

