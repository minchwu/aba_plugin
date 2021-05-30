from abaqusGui import getAFXApp, Activator, AFXMode
from abaqusConstants import ALL
import os
thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)

toolset = getAFXApp().getAFXMainWindow().getPluginToolset()
toolset.registerGuiMenuButton(
    buttonText='Usr Reference',
    object=Activator(os.path.join(thisDir, 'usrRefDB.py')),
    kernelInitString='import usr_datum',
    messageId=AFXMode.ID_ACTIVATE,
    icon=None,
    applicableModules=ALL,
    version='0.1',
    author='Mingchun Wu',
    description='N/A',
    helpUrl='N/A'
)
