#!/usr/bin/env python

## 
 # -*-Pyth-*-
 # ###################################################################
 #  FiPy - Python-based finite volume PDE solver
 # 
 #  FILE: "mesh.py"
 #                                    created: 11/10/03 {2:44:42 PM} 
 #                                last update: 10/19/04 {11:33:34 AM} 
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
 # ###################################################################
 ##

"""
Generic mesh class defining implementation-agnostic behavior.

Make changes to mesh here first, then implement specific implementations in
`pyMesh` and `numMesh`.

Meshes contain cells, faces, and vertices.
"""

##import sets

import Numeric
import MA

from fipy.tools.dimensions.physicalField import PhysicalField

class Mesh:
    def __init__(self):
	self.scale = {
	    'length': 1.,
	    'area': 1.,
	    'volume': 1.
	}
	
	self.calcTopology()
	self.calcGeometry()
    
    """topology methods"""
    
    def calcTopology(self):
	self.calcInteriorAndExteriorFaceIDs()
	self.calcInteriorAndExteriorCellIDs()
	self.calcCellToFaceOrientations()
	self.calcAdjacentCellIDs()
	self.calcCellToCellIDs()
        self.calcCellToCellIDsFilled()
       
    """calc topology methods"""
	
    def calcInteriorAndExteriorFaceIDs(self):
	pass

    def calcExteriorCellIDs(self):
	pass
	
    def calcInteriorCellIDs(self):
        pass
##	self.interiorCellIDs = list(sets.Set(range(self.numberOfCells)) - sets.Set(self.exteriorCellIDs))
##        onesWhereInterior = Numeric.zeros(self.numberOfCells)
##        Numeric.put(onesWhereInterior, self.exteriorCells, Numeric.zeros((len(self.exteriorCellIDs))))
##        self.interiorCellIDs = Numeric.nonzero(onesWhereInterior)
##        self.interiorCellIDs = (0,0)
        
    def calcInteriorAndExteriorCellIDs(self):
	self.calcExteriorCellIDs()
	self.calcInteriorCellIDs()

    def calcCellToFaceOrientations(self):
	pass

    def calcAdjacentCellIDs(self):
	pass

    def calcCellToCellIDs(self):
	pass

    def calcCellToCellIDsFilled(self):
        N = self.getNumberOfCells()
        M = self.getMaxFacesPerCell()
        cellIDs = Numeric.reshape(Numeric.repeat(Numeric.arange(N), M), (N, M))
        cellToCellIDs = self.getCellToCellIDs()
        self.cellToCellIDsFilled = MA.where(cellToCellIDs.mask(), cellIDs, cellToCellIDs)

    
    """get topology methods"""

    def getCellFaceIDs(self):
        return self.cellFaceIDs

    def getExteriorFaceIDs(self):
	return self.exteriorFaceIDs
	
    def getExteriorFaces(self):
	pass

    def getInteriorFaceIDs(self):
	return self.interiorFaceIDs
	    
    def getInteriorFaces(self):
	pass
	
    def getExteriorCellIDs(self):
	return self.exteriorCellIDs

    def getInteriorCellIDs(self):
	return self.interiorCellIDs

    def getCellFaceOrientations(self):
        return self.cellToFaceOrientations

    def getNumberOfCells(self):
	return self.numberOfCells
	
    def getAdjacentCellIDs(self):
        return self.adjacentCellIDs

    def getDim(self):
        return self.dim

    def getCellsByID(self, ids = None):
	pass
	    
    def getCells(self, filter = None, ids = None, **args):
	"""Return `Cell` objects of `Mesh`."""
	cells = self.getCellsByID(ids)
	
        if filter is None:
            return cells
        else:        
	    return [cell for cell in cells if filter(cell, **args)]

    def getFaces(self):
        pass
    
    def getFacesWithFilter(self, filter, **args):
	"""Return `Face` objects of `Mesh`."""
	faces = self.getFaces()
	
        if filter is None:
            return faces
        else:        
	    return [face for face in faces if filter(face, **args)]

    def getMaxFacesPerCell(self):
	pass

    def getNumberOfFaces(self):
	return self.numberOfFaces

    def getCellToCellIDs(self):
        return self.cellToCellIDs

    def getCellToCellIDsFilled(self):
        return self.cellToCellIDsFilled
	
    """geometry methods"""
    
    def calcGeometry(self):
	self.calcFaceAreas()
	self.calcFaceNormals()
	self.calcOrientedFaceNormals()
	self.calcCellVolumes()
	self.calcCellCenters()
	self.calcFaceToCellDistances()
	self.calcCellDistances()        
	self.calcFaceTangents()
	self.calcCellToCellDistances()
	self.calcScaledGeometry()
        self.calcCellAreas()
       
    """calc geometry methods"""
    
    def calcFaceAreas(self):
	pass
	
    def calcFaceNormals(self):
	pass
	
    def calcOrientedFaceNormals(self):
	pass
	
    def calcCellVolumes(self):
	pass
	
    def calcCellCenters(self):
	pass
	
    def calcFaceToCellDistances(self):
	pass

    def calcCellDistances(self):
	pass
        
    def calcAreaProjections(self):
	pass

    def calcOrientedAreaProjections(self):
	pass

    def calcFaceTangents(self):
	pass

    def calcFaceToCellDistanceRatio(self):
	pass

    def calcFaceAspectRatios(self):
	self.faceAspectRatios = self.getFaceAreas() / self.getCellDistances()

    def calcCellToCellDistances(self):
	pass

    def calcCellAreas(self):
        from fipy.meshes.numMesh.mesh import MAtake
        self.cellAreas =  MAtake(self.getFaceAreas(), self.cellFaceIDs)
    
    """get geometry methods"""
        
    def getFaceAreas(self):
        return self.scaledFaceAreas

    def getFaceNormals(self):
        return self.faceNormals
	
    def getCellVolumes(self):
	return self.scaledCellVolumes

    def getCellCenters(self):
	return self.scaledCellCenters

    def getFaceToCellDistances(self):
        return self.scaledFaceToCellDistances

    def getCellDistances(self):
        return self.scaledCellDistances

    def getFaceToCellDistanceRatio(self):
        return self.faceToCellDistanceRatio

    def getOrientedAreaProjections(self):
        return self.orientedAreaProjections

    def getAreaProjections(self):
        return self.areaProjections

    def getOrientedFaceNormals(self):
        return self.orientedFaceNormals

    def getFaceTangents1(self):
        return self.faceTangents1

    def getFaceTangents2(self):
        return self.faceTangents2
	
    def getFaceAspectRatios(self):
	return self.faceAspectRatios
    
    def getCellToCellDistances(self):
	return self.scaledCellToCellDistances

    def getCellNormals(self):
        return self.cellNormals

    def getCellAreas(self):
        return self.cellAreas

    def getCellAreaProjections(self):
        return self.cellNormals * self.getCellAreas()[:, :, Numeric.NewAxis]
	    
    """scaling"""

    def setScale(self, value = 1.):
        self.scale['length'] = PhysicalField(value = value)
	self.calcHigherOrderScalings()
	self.calcScaledGeometry()

    def calcHigherOrderScalings(self):
	self.scale['area'] = self.scale['length']**2
	self.scale['volume'] = self.scale['length']**3

    def calcScaledGeometry(self):
	self.scaledFaceAreas = self.scale['area'] * self.faceAreas
	self.scaledCellVolumes = self.scale['volume'] * self.cellVolumes
	self.scaledCellCenters = self.scale['length'] * self.cellCenters
	
	self.scaledFaceToCellDistances = self.scale['length'] * self.faceToCellDistances
	self.scaledCellDistances = self.scale['length'] * self.cellDistances
	self.scaledCellToCellDistances = self.scale['length'] * self.cellToCellDistances
	
	self.calcAreaProjections()
	self.calcOrientedAreaProjections()
	self.calcFaceToCellDistanceRatio()
	self.calcFaceAspectRatios()
	
    """point to cell distances"""
    
    def getPointToCellDistances(self, point):
	tmp = self.getCellCenters() - PhysicalField(point)
	import fipy.tools.array
	return fipy.tools.array.sqrtDot(tmp, tmp)

    def getNearestCell(self, point):
        try:
            tmp = self.getCellCenters() - point
        except TypeError:
            tmp = self.getCellCenters() - PhysicalField(point)
        i = Numeric.argmin(Numeric.add.reduce((tmp * tmp), axis = 1))
	return self.getCellsByID([i])[0]

    def getNearestCellID(self, point):
        try:
            tmp = self.getCellCenters() - point
        except TypeError:
            tmp = self.getCellCenters() - PhysicalField(point)
        i = Numeric.argmin(Numeric.add.reduce((tmp * tmp), axis = 1))
	return i    

## pickling

##    self.__getinitargs__(self):
##        return (self.vertexCoords, self.faceVertexIDs, self.cellFaceIDs)
    

## ##     def __getstate__(self):
## ##         dict = {
## ##             'vertexCoords' : self.vertexCoords,            
## ##             'faceVertexIDs' : self.faceVertexIDs,
## ##             'cellFaceIDs' : self.cellFaceIDs }
## ##         return dict
## ## 
## ##     def __setstate__(self, dict):
## ##         self.__init__(dict['vertexCoords'], dict['faceVertexIDs'], dict['cellFaceIDs'])
        
                      
    
