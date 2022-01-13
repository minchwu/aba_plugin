# -*- coding: mbcs -*-
# author: Mingchun Wu
# create: 2021/05/30
# version: 0.1

from abaqus import *
from abaqusConstants import *

MODIMCONST = {'3D': THREE_D, '2D': TWO_D_PLANAR, 'AX': AXISYMMETRIC}
MODTYPECON = {'DF': DEFORMABLE_BODY, 'DS': DISCRETE_RIGID_SURFACE,
              'AS': ANALYTIC_RIGID_SURFACE, 'EU': EULERIAN}


def UserCoolMain(usrModel, usrPart, usrDim, usrTyp):

    if mdb.models.has_key(usrModel):
        usrModel = mdb.models[usrModel]
        usrModel.Part(name=usrPart,
                      dimensionality=MODIMCONST[usrDim],
                      type=MODTYPECON[usrTyp])
        locPart = usrModel.parts[usrPart]
    else:
        mdb.Model(usrModel)
        usrModel = mdb.models[usrModel]
        usrModel.Part(name=usrPart,
                      dimensionality=MODIMCONST[usrDim],
                      type=MODTYPECON[usrTyp])
        locPart = usrModel.parts[usrPart]
    # locPart.DatumPointByCoordinate(coords=(0.0, 0.0, 0.0))
    locPart.DatumAxisByPrincipalAxis(principalAxis=XAXIS)
    locPart.DatumAxisByPrincipalAxis(principalAxis=YAXIS)
    locPart.DatumAxisByPrincipalAxis(principalAxis=ZAXIS)
    locPart.DatumPlaneByPrincipalPlane(principalPlane=XYPLANE, offset=0.0)
    locPart.DatumPlaneByPrincipalPlane(principalPlane=YZPLANE, offset=0.0)
    locPart.DatumPlaneByPrincipalPlane(principalPlane=XZPLANE, offset=0.0)

    vpName = session.currentViewportName
    session.viewports[vpName].setValues(displayedObject=locPart)
    session.viewports[vpName].view.setValues(session.views['Iso'])
    session.viewports[vpName].view.setProjection(projection=PARALLEL)
