#!/usr/bin/env python

## 
 # ###################################################################
 #  FiPy - Python-based finite volume PDE solver
 # 
 #  FILE: "test.py"
 #                                    created: 11/26/03 {3:23:47 PM}
 #                                last update: 9/3/04 {10:33:19 PM} { 2:26:30 PM}
 #  Author: Jonathan Guyer <guyer@nist.gov>
 #  Author: Daniel Wheeler <daniel.wheeler@nist.gov>
 #  Author: James Warren   <jwarren@nist.gov>
 #    mail: NIST
 #     www: http://www.ctcms.nist.gov/fipy/
 #  
 # ========================================================================
 # This software was developed at the National Institute of Standards
 # and Technology by employees of the Federal Government in the course
 # of their official duties.  Pursuant to title 17 Section 105 of the
 # United States Code this software is not subject to copyright
 # protection and is in the public domain.  FiPy is an experimental
 # system.  NIST assumes no responsibility whatsoever for its use by
 # other parties, and makes no guarantees, expressed or implied, about
 # its quality, reliability, or any other characteristic.  We would
 # appreciate acknowledgement if the software is used.
 # 
 # This software can be redistributed and/or modified freely
 # provided that any derivative works bear some notice that they are
 # derived from it, and any modified versions bear some notice that
 # they have been modified.
 # ========================================================================
 #  
 #  Description: 
 # 
 #  History
 # 
 #  modified   by  rev reason
 #  ---------- --- --- -----------
 #  2003-11-10 JEG 1.0 original
 # ###################################################################
 ##

"""Run all the test cases in examples/
"""

import unittest

import fipy.tests.testProgram


import examples.convection.test
import examples.diffusion.test
import examples.elphf.test
import examples.phase.test
import examples.levelSet.test
import examples.cahnHilliard.test
import examples.chemotaxis.test

def suite():
    theSuite = unittest.TestSuite()
    
    theSuite.addTest(examples.convection.test.suite())
    theSuite.addTest(examples.diffusion.test.suite())
    theSuite.addTest(examples.phase.test.suite())
    theSuite.addTest(examples.elphf.test.suite())
    theSuite.addTest(examples.levelSet.test.suite())
    theSuite.addTest(examples.chemotaxis.test.suite())  
##    theSuite.addTest(examples.cahnHilliard.test.suite())  
    
    return theSuite

if __name__ == '__main__':
    fipy.tests.testProgram.main(defaultTest='suite')

