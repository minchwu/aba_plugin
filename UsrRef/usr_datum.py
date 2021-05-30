# -*- coding: mbcs -*-
# author: Mingchun Wu
# create: 2021/05/30
# version: 0.1

from abaqus import *
from abaqusConstants import *


def datumPlaneCoord(locModel, locPart):

    if mdb.models.has_key(locModel):
        usrModel = mdb.models[locModel]
        usrModel.Part(locPart)
        usrPart = usrModel.parts[locPart]
    else:
        mdb.Model(locModel)
        usrModel = mdb.models[locModel]
        usrModel.Part(locPart)
        usrPart = usrModel.parts[locPart]
    usrPart.DatumPointByCoordinate(coords=(0.0, 0.0, 0.0))
    usrPart.DatumAxisByPrincipalAxis(principalAxis=XAXIS)
    usrPart.DatumAxisByPrincipalAxis(principalAxis=YAXIS)
    usrPart.DatumAxisByPrincipalAxis(principalAxis=ZAXIS)
    usrPart.DatumPlaneByPrincipalPlane(principalPlane=XYPLANE, offset=0.0)
    usrPart.DatumPlaneByPrincipalPlane(principalPlane=YZPLANE, offset=0.0)
    usrPart.DatumPlaneByPrincipalPlane(principalPlane=XZPLANE, offset=0.0)

    vpName = session.currentViewportName
    session.viewports[vpName].setValues(displayedObject=usrPart)
    session.viewports[vpName].view.setValues(session.views['Iso'])
    session.viewports[vpName].view.setProjection(projection=PARALLEL)
