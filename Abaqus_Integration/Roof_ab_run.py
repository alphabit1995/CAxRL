# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__
import section
import regionToolset
import displayGroupMdbToolset as dgm
import part
import material
import assembly
import step
import interaction
import load
import mesh
import optimization
import job
import sketch
import visualization
import xyPlot
import displayGroupOdbToolset as dgo
import connectorBehavior

import time
import os
import sys

from odbAccess import openOdb

def Create_Model():
    mdb.Model(name='GUI_Model', modelType=STANDARD_EXPLICIT)
    a = mdb.models['GUI_Model'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)


def CreateRoof(positions, breadth):
    s = mdb.models['GUI_Model'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.Arc3Points(point1=(-35.0, 0.0), point2=(35.0, 0.0), point3=(0.0, 5.0))
    for i in positions:
        if i == 1:
            s.Line(point1=(-30.0, 1.34661099511595), point2=(-30.0, 0.0))
            continue
        if i == 2:
            s.Line(point1=(-25.0, 2.47448713915901), point2=(-25.0, 0.0))
            continue
        if i == 3:
            s.Line(point1=(-20.0, 3.38962679253063), point2=(-20.0, 0.0))
            continue
        if i == 4:
            s.Line(point1=(-15.0, 4.09673645990847), point2=(-15.0, 0.0))
            continue
        if i == 5:
            s.Line(point1=(-10.0, 4.59935794377111), point2=(-10.0, 0.0))
            continue
        if i == 6:
            s.Line(point1=(-5.0, 4.89995996796802), point2=(-5.0, 0.0))
            continue
        if i == 7:
            s.Line(point1=(0.0, 5.0), point2=(0.0, 0.0))
            continue
        if i == 8:
            s.Line(point1=(5.0, 4.89995996796802), point2=(5.0, -0.00631403923034668))
            continue
        if i == 9:
            s.Line(point1=(10.0, 0.0), point2=(10.0, 4.59935794374906))
            continue
        if i == 10:
            s.Line(point1=(15.0, 0.0), point2=(15.0, 4.09673645999283))
            continue
        if i == 11:
            s.Line(point1=(20.0, 0.0), point2=(20.0, 3.38962679263204))
            continue
        if i == 12:
            s.Line(point1=(25.0, 2.47448713915901), point2=(25.0, 0.0))
            continue
        if i == 13:
            s.Line(point1=(30.0, 1.34661099511595), point2=(30.0, 0.0))
            continue
    
    p = mdb.models['GUI_Model'].Part(name='Roof', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['GUI_Model'].parts['Roof']
    p.BaseShellExtrude(sketch=s, depth=breadth)
    s.unsetPrimaryObject()
    p = mdb.models['GUI_Model'].parts['Roof']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['GUI_Model'].sketches['__profile__']


def Create_Steel_Material():
    mdb.models['GUI_Model'].Material(name='Steel')
    mdb.models['GUI_Model'].materials['Steel'].Elastic(table=((210000.0, 0.3), ))


def Create_Sections():
    mdb.models['GUI_Model'].HomogeneousShellSection(name='Roof_Section', 
        preIntegrate=OFF, material='Steel', thicknessType=UNIFORM, 
        thickness=1.0, thicknessField='', nodalThicknessField='', 
        idealization=NO_IDEALIZATION, poissonDefinition=DEFAULT, 
        thicknessModulus=None, temperature=GRADIENT, useDensity=OFF, 
        integrationRule=SIMPSON, numIntPts=5)


def Create_Support_Set(positions, coordinates, breadth):
    p = mdb.models['GUI_Model'].parts['Roof']
    f = p.faces
    faces = []
    for i in positions:
        tuple_coordinates = (coordinates[i],)
        face = f.findAt( tuple_coordinates )
        fi = face[0].index
        faces.append( f[fi:fi+1])
    
    e = p.edges
    edges = []
    edge_1 = e.getByBoundingBox(-35.0, 0.0, 0.0, 35.0, 5.0, 0.0)
    edge_2 = e.getByBoundingBox(-35.0, 0.0, breadth, 35.0, 5.0, breadth)
    edge_3 = e.findAt(((-35.0, 0.0, breadth/2), ), ((35.0, 0.0, breadth/2), ))
    edges.append(edge_1)
    edges.append(edge_2)
    edges.append(edge_3)
    p.Set(edges = edges, faces = faces, name = 'Support_Set')


def Create_Pressure_Set(positions, coordinates):
    p = mdb.models['GUI_Model'].parts['Roof']
    f = p.faces
    faces = []
    for i in positions:
        tuple_coordinates = (coordinates[i],)
        face = f.findAt( tuple_coordinates )
        fi = face[0].index
        faces.append( f[fi:fi+1])
    temp_set = p.Set(faces = faces, name = 'Temp_Support_Set')
    all_faces = p.Set(faces = p.faces, name = 'All_Faces_Set')
    pressure_set = p.SetByBoolean(name = 'Pressure_Set', sets = (all_faces, temp_set), operation = DIFFERENCE)
    del mdb.models['GUI_Model'].parts['Roof'].sets['Temp_Support_Set']


def Assign_Sections():
    p = mdb.models['GUI_Model'].parts['Roof']
    f = p.faces
    region = regionToolset.Region(faces=f[0:])
    p.SectionAssignment(region=region, sectionName='Roof_Section', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)


def Create_Assembly():
    a = mdb.models['GUI_Model'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    a = mdb.models['GUI_Model'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['GUI_Model'].parts['Roof']
    a.Instance(name='Roof-1', part=p, dependent=ON)


def Create_Step():
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=ON)
    mdb.models['GUI_Model'].StaticStep(name='Step-1', previous='Initial', 
        timeIncrementationMethod=FIXED, initialInc=0.1, noStop=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')


def Create_Boundary_Conditions():
    a = mdb.models['GUI_Model'].rootAssembly
    region = a.instances['Roof-1'].sets['Support_Set']
    mdb.models['GUI_Model'].EncastreBC(name='BC-1', createStepName='Step-1', 
        region=region, localCsys=None)


def Create_Pressure_Conditions():
    a = mdb.models['GUI_Model'].rootAssembly
    s1 = a.instances['Roof-1'].sets['Pressure_Set']
    region = regionToolset.Region(side2Faces=s1.faces[0:])
    mdb.models['GUI_Model'].Pressure(name='Load-1', createStepName='Step-1', 
            region=region, distributionType=UNIFORM, field='', magnitude=200.0, 
            amplitude=UNSET)


def Create_Mesh():
    p = mdb.models['GUI_Model'].parts['Roof']
    p = mdb.models['GUI_Model'].parts['Roof']
    p.seedPart(size=4.0, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['GUI_Model'].parts['Roof']
    p.generateMesh()


def Create_Job():
    a1 = mdb.models['GUI_Model'].rootAssembly
    a1.regenerate()
    mdb.Job(name='GUI', model='GUI_Model', description='', type=ANALYSIS, 
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
        scratch='', resultsFormat=ODB)


def Start_Job():
    a = mdb.models['GUI_Model'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=OFF)
    a = mdb.models['GUI_Model'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    mdb.jobs['GUI'].submit(consistencyChecking=OFF)
    time.sleep(15)


def View_Results():
    a = mdb.models['GUI_Model'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    o3 = session.openOdb(
        name='GUI.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=o3)
    session.viewports['Viewport: 1'].makeCurrent()
    a = mdb.models['GUI_Model'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.mdbData.summary()
    session.viewports['Viewport: 1'].setValues(
        displayedObject=session.odbs['GUI.odb'])
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        CONTOURS_ON_DEF, ))
    session.viewports['Viewport: 1'].animationController.setValues(
        animationType=TIME_HISTORY)
    session.viewports['Viewport: 1'].animationController.play(
        duration=UNLIMITED)


breadth = float(sys.argv[-3])
#breadth = 55.0
print >> sys.__stdout__, breadth

position_1_point_1 = (-30.0, 1.34661099511595, 0.0)
position_1_point_2 = (-30.0, 0.0, 0.0)
position_1_coordinates = (-30.0, 1.34661099511595/2, breadth/2)

position_2_point_1 = (-25.0, 2.47448713915901)
position_2_point_2 = (-25.0, 0.0)
position_2_coordinates = (-25.0, 2.47448713915901/2, breadth/2)

position_3_point_1 = (-20.0, 3.38962679253063)
position_3_point_2 = (-20.0, 0.0)
position_3_coordinates = (-20.0, 3.38962679253063/2, breadth/2)

position_4_point_1 = (-15.0, 4.09673645990847, 0.0)
position_4_point_2 = (-15.0, 0.0, 0.0)
position_4_coordinates = (-15.0, 4.09673645990847/2, breadth/2)

position_5_point_1 = (-10.0, 4.59935794377111, 0.0)
position_5_point_2 = (-10.0, 0.0, 0.0)
position_5_coordinates = (-10.0, 4.59935794377111/2, breadth/2)

position_6_point_1 = (-5.0, 4.89995996796802, 0.0)
position_6_point_2 = (-5.0, 0.0, 0.0)
position_6_coordinates = (-5.0, 4.89995996796802/2, breadth/2)

position_7_point_1 = (0.0, 5.0, 0.0)
position_7_point_2 = (0.0, 0.0, 0.0)
position_7_coordinates = (0.0, 5.0/2, breadth/2)

position_8_point_1 = (5.0, 4.89995996796802, 0.0)
position_8_point_2 = (5.0, 0.0, 0.0)
position_8_coordinates = (5.0, 4.89995996796802/2, breadth/2)

position_9_point_1 = (10.0, 4.59935794377111, 0.0)
position_9_point_2 = (10.0, 0.0, 0.0)
position_9_coordinates = (10.0, 4.59935794377111/2, breadth/2)

position_10_point_1 = (15.0, 4.09673645990847, 0.0)
position_10_point_2 = (15.0, 0.0, 0.0)
position_10_coordinates = (15.0, 4.09673645990847/2, breadth/2)

position_11_point_1 = (20.0, 3.38962679253063, 0.0)
position_11_point_2 = (20.0, 0.0, 0.0)
position_11_coordinates = (20.0, 3.38962679253063/2, breadth/2)

position_12_point_1 = (25.0, 2.47448713915901, 0.0)
position_12_point_2 = (25.0, 0.0, 0.0)
position_12_coordinates = (25.0, 2.47448713915901/2, breadth/2)

position_13_point_1 = (30.0, 1.34661099511595, 0.0)
position_13_point_2 = (30.0, 0.0, 0.0)
position_13_coordinates = (30.0, 1.34661099511595/2, breadth/2)

coordinates = {1: position_1_coordinates, 2: position_2_coordinates, 3: position_3_coordinates, 4: position_4_coordinates, 5: position_5_coordinates, \
               6: position_6_coordinates, 7: position_7_coordinates, 8: position_8_coordinates, 9: position_9_coordinates, 10: position_10_coordinates, \
                11: position_11_coordinates, 12: position_12_coordinates, 13: position_13_coordinates}


positions = sys.argv[-1]
#positions = [1,3,5,11,13]
positions = map(int, positions.strip('[]').split(','))
print >> sys.__stdout__, positions

Create_Model()
CreateRoof(positions, breadth)
Create_Steel_Material()
Create_Sections()
Assign_Sections()
Create_Assembly()
Create_Step()
Create_Support_Set(positions, coordinates, breadth)
Create_Pressure_Set(positions, coordinates)
Create_Boundary_Conditions()
Create_Pressure_Conditions()
Create_Mesh()
Create_Job()
Start_Job()
View_Results()

#sys.exit()
