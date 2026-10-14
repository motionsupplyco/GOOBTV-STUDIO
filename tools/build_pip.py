"""WRONGSIDE Pip: original procedural Blender character asset.
Usage: blender -b -t 2 --python tools/build_pip.py
Exports assets/characters/pip.glb. No paid assets.
"""
import bpy, math, os
from mathutils import Vector
bpy.ops.object.select_all(action='SELECT'); bpy.ops.object.delete(use_global=False)
def mat(name,c,rough=.82):
 m=bpy.data.materials.new(name);m.diffuse_color=(*c,1);m.use_nodes=True
 bs=m.node_tree.nodes.get('Principled BSDF');bs.inputs['Base Color'].default_value=(*c,1);bs.inputs['Roughness'].default_value=rough
 return m
fur=mat('Pip turquoise fur',(0.025,.52,.53)); belly=mat('Cream muzzle',(.95,.77,.52)); vest=mat('Sunny yellow vest',(1,.64,.055)); orange=mat('Orange belt',(.96,.23,.055)); dark=mat('Deep navy',(0.025,.045,.09));white=mat('Eye whites',(1,.96,.86));iris=mat('Iris jade',(.12,.45,.31));pink=mat('Ear pink',(.85,.35,.4))
def uv(name,loc,scale,material,parent=None):
 bpy.ops.mesh.primitive_uv_sphere_add(segments=32,ring_count=20,location=loc);o=bpy.context.object;o.name=name;o.scale=scale;o.data.materials.append(material)
 bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
 for p in o.data.polygons:p.use_smooth=True
 if parent:o.parent=parent
 return o
def cube(name,loc,scale,material,bevel=.09,parent=None):
 bpy.ops.mesh.primitive_cube_add(size=1,location=loc);o=bpy.context.object;o.name=name;o.dimensions=scale;bpy.ops.object.transform_apply(location=False,rotation=False,scale=True);o.data.materials.append(material)
 if bevel:mod=o.modifiers.new('soft rounded corners','BEVEL');mod.width=bevel;mod.segments=3;o.modifiers.new('weighted normals','WEIGHTED_NORMAL')
 if parent:o.parent=parent
 return o
root=bpy.data.objects.new('PIP_ROOT',None);bpy.context.collection.objects.link(root)
uv('Body', (0,0,1.14),(.44,.31,.62),fur,root)
uv('Vest front',(0,-.22,1.14),(.4,.13,.48),vest,root)
cube('Belt',(0,-.24,.79),(.82,.19,.15),orange,.04,root)
cube('Belt buckle',(0,-.35,.79),(.18,.06,.13),belly,.03,root)
uv('Head',(0,-.015,2.08),(.57,.42,.5),fur,root)
for s in [-1,1]:
 uv('Ear outer '+str(s),(s*.42,-.02,2.48),(.22,.13,.28),fur,root)
 uv('Ear inside '+str(s),(s*.42,-.14,2.5),(.12,.035,.16),pink,root)
 uv('Mask '+str(s),(s*.245,-.348,2.15),(.25,.105,.205),dark,root)
 uv('Eye '+str(s),(s*.245,-.445,2.17),(.125,.07,.14),white,root)
 uv('Iris '+str(s),(s*.22,-.51,2.17),(.063,.035,.09),iris,root)
 uv('Pupil '+str(s),(s*.22,-.54,2.17),(.032,.019,.07),dark,root)
 uv('Eye glint '+str(s),(s*.2,-.558,2.22),(.018,.01,.022),white,root)
 uv('Cheek '+str(s),(s*.29,-.35,1.93),(.23,.14,.15),belly,root)
 uv('Arm '+str(s),(s*.53,0,1.26),(.18,.19,.41),fur,root)
 uv('Hand '+str(s),(s*.55,-.035,.94),(.18,.19,.19),fur,root)
 uv('Leg '+str(s),(s*.23,0,.48),(.2,.22,.42),fur,root)
 uv('Shoe '+str(s),(s*.23,-.14,.16),(.26,.4,.16),dark,root)
uv('Snout',(0,-.43,1.94),(.27,.22,.16),belly,root)
uv('Nose',(0,-.64,2.02),(.105,.08,.07),dark,root)
cube('Smile',(0,-.615,1.865),(.23,.022,.026),dark,.01,root)
for i in range(5):
 o=uv('Tail segment '+str(i),(.38+i*.13,.18+i*.09,.77+i*.07),(.26-i*.025,.23-i*.018,.18-i*.008),dark if i%2 else fur,root)
# One pivot animation for now; body-part rigging and walk cycles remain future gates.
bpy.context.view_layer.objects.active=root;root.select_set(True)
for frame,rot in [(1,0),(12,-.05),(24,0),(36,.05),(48,0)]:
 root.rotation_euler[2]=rot;root.keyframe_insert(data_path='rotation_euler',frame=frame)
# The pivot keyframes export as a simple idle animation.
scene=bpy.context.scene;scene.frame_start=1;scene.frame_end=48;scene.render.fps=24
os.makedirs('assets/characters',exist_ok=True)
bpy.ops.object.select_all(action='SELECT')
bpy.ops.export_scene.gltf(filepath=os.path.abspath('assets/characters/pip.glb'),export_format='GLB',export_animations=True)
print('WROTE assets/characters/pip.glb')
