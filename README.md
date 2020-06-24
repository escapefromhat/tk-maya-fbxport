# tk-multi-fbxport

This is a development app intended to provide a method of exporting FBX files and their JSON transforms. It will likely eventually be implemented in publish hooks, but during pipeline development it will be a standalone app so as to leave the publish process undisturbed.

## What's it do?

This app implements our cheap-a$$ based-on-a-true-USD framework to export two files out of Maya for importing into Unreal. It does this outside of the publish process, so the files do not automatically become integrated into the pipeline. However, they can be published using the standalone publisher, and more publish integration is *on* **its** ***way*** <super>(eventually)</super>.

## *Two* Files??

Yup. This exports an FBX file, containing the geometry of each mesh in the scene hierarchy, along with a JSON file that describes the transform tree that, when reapplied, brings these geometries back to where they go in the scene. The FBX file contains the meshes not in their original locations in the scene, but each moved so that the pivot is located at the origin. The rotation and scale are unchanged.

## ...why would you do that
Unreal brings in FBX assets with a pivot point at the origin, regardless of where they are when exported. That means, frozen or unfrozen transforms, bringing in a complex scene from a single FBX sets all the mesh pivots to the origin. Translation is unaffected, but scaling and rotation are both made effectively useless by this process, as they then happen relative to the origin, not to the object's center, or bottom, or whatever the pivot is. This process maintains pivots *and* transforms, and allows the scene to be "reset" to its Maya-export-time transforms, the first in a series of Unreal manipulation tools that will be developed.

## How's it work?

This app adds a single menu item to the Shotgun menu in Maya. This triggers the export process, which goes as follows:
 - save the Maya scene
 - export a JSON file containing transform info
 - move components by pivot to origin & freeze
 - export zeroed, frozen fbx
 - reset scene to saved point

The files will be exported to locations set in the shotgun configuration.
