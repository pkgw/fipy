#!/usr/bin/env python

## 
 # ###################################################################
 #  FiPy - Python-based finite volume PDE solver
 # 
 #  FILE: "input.py"
 #                                    created: 12/29/03 {3:23:47 PM}
 #                                last update: 10/6/04 {2:16:30 PM} 
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

"""

This is a simple test case for the `NthOrderDiffusionEquation` for the
case of ordinary diffusion when `N=2`.

    >>> it.timestep()
    >>> Lx = nx * dx
    >>> x = mesh.getCellCenters()[:,0]
    >>> import Numeric
    >>> value = valueLeft + (valueRight - valueLeft) * x / Lx
    >>> Numeric.allclose(var, value, rtol = 1e-10, atol = 1e-10)
    1

"""
__docformat__ = 'restructuredtext'

##from fipy.tools.profiler.profiler import Profiler
##from fipy.tools.profiler.profiler import calibrate_profiler
 
from fipy.meshes.grid2D import Grid2D
from fipy.equations.nthOrderDiffusionEquation import NthOrderDiffusionEquation
from fipy.solvers.linearPCGSolver import LinearPCGSolver
from fipy.boundaryConditions.fixedValue import FixedValue
from fipy.boundaryConditions.fixedFlux import FixedFlux
from fipy.iterators.iterator import Iterator
from fipy.variables.cellVariable import CellVariable
from fipy.viewers.grid2DGistViewer import Grid2DGistViewer

nx = 10
ny = 1

dx = 1.
dy = 1.

valueLeft = 0.
valueRight = 1.

mesh = Grid2D(dx = dx, dy = dy, nx = nx, ny = ny)

var = CellVariable(name = "concentration",
                   mesh = mesh,
                   value = valueLeft)

eq = NthOrderDiffusionEquation(var,
                       transientCoeff = 0., 
                       diffusionCoeff = (1.,),
                       solver = LinearPCGSolver(tolerance = 1.e-15, 
                                                steps = 1000
                                                ),
                       boundaryConditions = (FixedValue(mesh.getFacesLeft(),valueLeft),
                                             FixedValue(mesh.getFacesRight(),valueRight),
                                             FixedFlux(mesh.getFacesTop(),0.),
                                             FixedFlux(mesh.getFacesBottom(),0.)
                                             )
                       )

it = Iterator((eq,))

if __name__ == '__main__':

    viewer = Grid2DGistViewer(var, minVal =0., maxVal = 1.)
    it.timestep()
##     print var
    viewer.plot()

    raw_input("finished")
