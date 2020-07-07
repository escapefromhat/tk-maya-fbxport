# Jason Angell
# Parallux
# Execution logic for tk-maya-fbxport

import sgtk
import os
import time

# standard toolkit logger
logger = sgtk.platform.get_logger(__name__)
SDFramework = sgtk.platform.get_framework('tk-framework-scene-description_v0.1.1')
MTW = SDFramework.import_module('utils.MayaTransformWriter')

def xport(app_instance):
	# grab the maya exporter from the scene description framework
	mtw = MTW.MayaTransformWriter('C:\\fake\\ass\\path')
	mtw.publish_collapsed(app_instance)


def center_pivots(app_instance):
	MTW.center_pivots()