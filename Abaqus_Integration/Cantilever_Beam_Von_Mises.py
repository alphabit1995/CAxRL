from abaqus import *
from abaqusConstants import *
import mesh
from odbAccess import openOdb
import step
import numpy
import shutil

import time
import os.path
import sys

def CreateBeam(length ,breadth):
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=STANDALONE)
    s1.rectangle(point1=(0.0, 0.0), point2=(length, breadth))
    p = mdb.models['Model-1'].Part(name='Beam', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Beam']
    p.BaseSolidExtrude(sketch=s1, depth=3.0)
    s1.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Beam']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']

def BeamSection():
    mdb.models['Model-1'].Material(name='Concrete')
    mdb.models['Model-1'].materials['Concrete'].Elastic(table=((30000000000.0, 
        0.3), ))
    mdb.models['Model-1'].HomogeneousSolidSection(name='BeamSection', 
        material='Concrete', thickness=None)
    p = mdb.models['Model-1'].parts['Beam']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    region = p.Set(cells=cells, name='BeamSet')
    p = mdb.models['Model-1'].parts['Beam']
    p.SectionAssignment(region=region, sectionName='BeamSection', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)

def MeshCreation(mesh_size):
    p = mdb.models['Model-1'].parts['Beam']
    p.seedPart(size=mesh_size, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['Beam']
    p.generateMesh()
    session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)

def ElementTypeSelection():
    elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD, 
        kinematicSplit=AVERAGE_STRAIN, secondOrderAccuracy=OFF, 
        hourglassControl=DEFAULT, distortionControl=DEFAULT)
    elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
    elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
    p = mdb.models['Model-1'].parts['Beam']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    pickedRegions =(cells, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
        elemType3))

def InstanceCreation():
    a = mdb.models['Model-1'].rootAssembly
    a = mdb.models['Model-1'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['Model-1'].parts['Beam']
    a.Instance(name='Beam-1', part=p, dependent=ON)

def LoadCreation():
    a = mdb.models['Model-1'].rootAssembly
    mdb.models['Model-1'].StaticStep(name='Load', previous='Initial')
    a = mdb.models['Model-1'].rootAssembly
    f1 = a.instances['Beam-1'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#1 ]', ), )
    region = a.Set(faces=faces1, name='Support-Set')
    mdb.models['Model-1'].EncastreBC(name='Fixed-Support', 
        createStepName='Initial', region=region, localCsys=None)
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['Beam-1'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#2 ]', ), )
    region = a.Surface(side1Faces=side1Faces1, name='Load-Surface')
    mdb.models['Model-1'].Pressure(name='UDL', createStepName='Load', 
        region=region, distributionType=UNIFORM, field='', magnitude=30000.0, 
        amplitude=UNSET)
    mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=(
        'S', 'MISES', 'MISESMAX', 'PE', 'PEEQ', 'PEMAG', 'LE', 'U', 'RF', 'CF', 
        'CSTRESS', 'CDISP'))

def JobCreation():
    mdb.Job(name='BeamJob', model='Model-1', description='', type=ANALYSIS, 
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
        scratch='', resultsFormat=ODB)
    mdb.jobs['BeamJob'].submit(consistencyChecking=OFF)

def Visualize():
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    o3 = session.openOdb(name='C:/temp/BeamJob.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=o3)
    session.viewports['Viewport: 1'].makeCurrent()
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.mdbData.summary()
    session.viewports['Viewport: 1'].setValues(
        displayedObject=session.odbs['C:/temp/BeamJob.odb'])
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        CONTOURS_ON_DEF, ))


def calculate_stress(cantilever_beam_length, cantilever_beam_breadth):

    #print >> sys.__stdout__,"----------------------------------------------------------"

    CreateBeam(cantilever_beam_length, cantilever_beam_breadth)

    BeamSection()

    MeshCreation(1)

    ElementTypeSelection()

    InstanceCreation()

    LoadCreation()

    JobCreation()

    #print >> sys.__stdout__,"----------------------------------------------------------"
    #print >> sys.__stdout__,"Job submitted."
    #print >> sys.__stdout__,"----------------------------------------------------------"
    while not os.path.exists("BeamJob.odb"):
        #print >> sys.__stdout__, "Waiting for the analysis results..."
        time.sleep(1)

    if os.path.isfile("BeamJob.odb"):
        #shutil.move('BeamJob.odb', 'Odb_Files/BeamJob.odb')
        #print >> sys.__stdout__, "Job finished. Reading the results..."
        #print >> sys.__stdout__,"----------------------------------------------------------"
        odb=openOdb("BeamJob.odb")
        allIPs = odb.steps['Load'].historyRegions.keys()
        stressTensor = odb.steps['Load'].frames[-1].fieldOutputs['S'].getSubset(position=CENTROID)
        mStress = stressTensor.getScalarField(invariant=MISES,)
        dat = mStress.bulkDataBlocks[0]
        maxMies = numpy.max(dat.data)
        #print >> sys.__stdout__,"Job finished. Returning the results.."
        odb.close()
        os.remove("BeamJob.odb")
    else:
        raise ValueError("%s isn't a file!" % "BeamJob.odb")
    
    return maxMies


start_time = time.time()

cantilever_beam_length = sys.argv[-1]
cantilever_beam_breadth = sys.argv[-3]
print("From Abaqus: " + str(cantilever_beam_length) + str(cantilever_beam_breadth))
print >> sys.__stdout__, "From Abaqus: " + str(cantilever_beam_length) + str(cantilever_beam_breadth)
cantilever_beam_length = float(cantilever_beam_length)
cantilever_beam_breadth = float(cantilever_beam_breadth)
stress = calculate_stress(cantilever_beam_length, cantilever_beam_breadth)

print >> sys.__stdout__, str(stress)
#print >> sys.__stdout__, "Max von Mises Stress: " + str(stress) + " Pa"
#print >> sys.__stdout__, ("Elapsed time: " + str(time.time() - start_time)) + " seconds"
