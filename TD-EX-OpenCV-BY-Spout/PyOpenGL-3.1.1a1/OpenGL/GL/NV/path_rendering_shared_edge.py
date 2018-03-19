'''OpenGL extension NV.path_rendering_shared_edge

This module customises the behaviour of the 
OpenGL.raw.GL.NV.path_rendering_shared_edge to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/path_rendering_shared_edge.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.NV.path_rendering_shared_edge import *
from OpenGL.raw.GL.NV.path_rendering_shared_edge import _EXTENSION_NAME

def glInitPathRenderingSharedEdgeNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION