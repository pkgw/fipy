#!/usr/bin/env python

## -*-Pyth-*-
 # ###################################################################
 #  FiPy - Python-based finite volume PDE solver
 # 
 #  FILE: "phaseDiffusionVariable.py"
 #                                    created: 11/12/03 {10:39:23 AM} 
 #                                last update: 9/3/04 {10:38:53 PM} 
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
 #  2003-11-12 JEG 1.0 original
 # ###################################################################
 ##

import Numeric

from fipy.variables.faceVariable import FaceVariable

class PhaseDiffusionVariable(FaceVariable):
    def __init__(self, parameters = None, halfAngle = None):
        FaceVariable.__init__(self, halfAngle.getMesh())
	self.parameters = parameters
	self.halfAngle = self.requires(halfAngle)

    def _calcValue(self):
	alpha = self.parameters['alpha']
	c2 = self.parameters['anisotropy']

        zsq = self.halfAngle[:] * self.halfAngle[:]
	b = (1. - zsq) / (1. + zsq)
	z = (1.+ c2 * b)
        
        self.value = alpha**2 * z * z

