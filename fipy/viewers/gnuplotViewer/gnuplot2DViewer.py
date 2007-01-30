#!/usr/bin/env python

## -*-Pyth-*-
 # ###################################################################
 #  FiPy - Python-based finite volume PDE solver
 # 
 #  FILE: "gnuplot1DViewer.py"
 #                                    created: 9/14/04 {2:48:25 PM} 
 #                                last update: 7/6/05 {4:31:38 PM} { 2:45:36 PM}
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
 #  See the file "license.terms" for information on usage and  redistribution
 #  of this file, and for a DISCLAIMER OF ALL WARRANTIES.
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

__docformat__ = 'restructuredtext'

from fipy.tools import numerix

from gnuplotViewer import GnuplotViewer
from fipy.meshes.grid2D import Grid2D

class Gnuplot2DViewer(GnuplotViewer):
    """
    Displays a contour plot of a 2D `CellVariable` object.    
       
    The `Gnuplot2DViewer` plots a 2D `CellVariable` using a front end
    python wrapper available to download (Gnuplot.py_).

    .. _Gnuplot.py: http://gnuplot-py.sourceforge.net/

    Different style script demos_ are available at the Gnuplot_ site.

    .. _Gnuplot: http://gnuplot.sourceforge.net/
    .. _demos: http://gnuplot.sourceforge.net/demo/

    .. note::
    
        `GnuplotViewer` requires Gnuplot_ version 4.0.

    """
    def __init__(self, vars, limits = None, title = None):
        """
        Creates a `Gnuplot2DViewer`.
        
        :Parameters:
          - `vars`: A `CellVariable` object.
          - `limits`: A dictionary with possible keys `'xmin'`, `'xmax'`, 
            `'ymin'`, `'ymax'`, `'datamin'`, `'datamax'`. Any limit set to 
            a (default) value of `None` will autoscale.
          - `title`: displayed at the top of the Viewer window

        """
        GnuplotViewer.__init__(self, vars = vars, limits = limits, title = title)
        
        if len(self.vars) != 1:
            raise IndexError, "A 2D Gnuplot viewer can only display one Variable"
            
    def _plot(self):

        self.g('set cbrange [' + self._getLimit('zmin')  + ':' + self._getLimit('zmax') + ']')
        self.g('set view map')
        self.g('set style data pm3d')
        self.g('set pm3d at st solid')
        mesh = self.vars[0].getMesh()

        if isinstance(mesh, Grid2D.__class__):
            nx, ny = mesh.getShape()
        else:
            N = int(numerix.sqrt(mesh.getNumberOfCells()))
            nx, ny = N, N
            
        self.g('set dgrid3d %i, %i, 2' % (ny, nx))

        import Gnuplot
        data = Gnuplot.Data(numerix.array(mesh.getCellCenters()[:,0]),
                            numerix.array(mesh.getCellCenters()[:,1]),
                            self.vars[0][:])

        self.g.splot(data)
