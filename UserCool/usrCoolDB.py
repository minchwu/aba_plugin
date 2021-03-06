# Do not edit this file or it may not load correctly
# if you try to open it with the RSG Dialog Builder.

# Note: thisDir is defined by the Activator class when
#       this file gets executed

from rsg.rsgGui import *
from abaqusConstants import *

execDir = os.path.split(thisDir)[1]
dialogBox = RsgDialog(title='User Cool', kernelModule='usrCool', kernelFunction='UserCoolMain',
                      includeApplyBtn=True, includeSeparator=True, okBtnText='OK', applyBtnText='Apply', execDir=execDir)
RsgHorizontalFrame(name='HFrame_1', p='DialogBox',
                   layout='0', pl=0, pr=0, pt=0, pb=0)
RsgTextField(p='HFrame_1', fieldType='String', ncols=12,
             labelText='Model:\tThe Model You want to Use or Create',
             keyword='usrModel', default='Model-1')
RsgTextField(p='HFrame_1', fieldType='String', ncols=12,
             labelText='Part:\tThe Part You want to Use or Create',
             keyword='usrPart', default='Part-1')
RsgHorizontalFrame(name='HFrame_2', p='DialogBox',
                   layout='0', pl=0, pr=0, pt=0, pb=0)
RsgTextField(p='HFrame_2', fieldType='String', ncols=12,
             labelText='Dimen:\tInput the Part Dimension{3D,2D,AX}',
             keyword='usrDim', default='3D')
RsgTextField(p='HFrame_2', fieldType='String', ncols=12,
             labelText='Type:\tDeformable or Rigid{DF,DS,AS,EU}',
             keyword='usrTyp', default='DF')
dialogBox.show()
