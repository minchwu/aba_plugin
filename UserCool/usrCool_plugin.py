from abaqusGui import *
from abaqusConstants import *
import os
thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)

toolset = getAFXApp().getAFXMainWindow().getPluginToolset()
toolset.registerGuiMenuButton(
    buttonText='Usr Cool',
    object=Activator(os.path.join(thisDir, 'usrCoolDB.py')),
    kernelInitString='import usrCool',
    messageId=AFXMode.ID_ACTIVATE,
    applicableModules=ALL,
    version='0.1',
    author='Mingchun Wu',
)
