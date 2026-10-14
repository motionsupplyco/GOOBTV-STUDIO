import bpy, math, os
from mathutils import Vector
bpy.ops.object.select_all(action='SELECT'); bpy.ops.object.delete(use_global=False)
sc=bpy.context.scene
sc.render.engine='CYCLES';sc.cycles.device='CPU';sc.cycles.samples=6;sc.cycles.use_denoising=False
sc.view_layers[0].cycles.use_denoising=False
sc.render.resolution_x=640;sc.render.resolution_y=360;sc.render.resolution_percentage=100
sc.render.fps=24;sc.frame_end=240
def mat(n,c):
 m=bpy.data.materials.new(n);m.diffuse_color=(*c,1);m.use_nodes=True;m.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(*c,1);return m
teal=mat('Pip turquoise fur',(.035,.63,.68));cream=mat('Muzzle cream',(.95,.79,.55));dark=mat('Face dark',(.024,.045,.065));white=mat('Eye white',(.98,.96,.91));vest=mat('Safety vest yellow',(.99,.72,.055));orange=mat('Tool belt orange',(.92,.29,.03));pavement=mat('Living sidewalk',(.53,.58,.62));road=mat('Asphalt',(.19,.23,.29));grass=mat('Grass',(.16,.55,.26));brick=mat('Coral house',(.95,.37,.35));blue=mat('Blue roof',(.09,.35,.74));brown=mat('Trash bin green',(.1,.4,.31))
def cube(n,loc,dim,m,bev=0):
 bpy.ops.mesh.primitive_cube_add(size=1,location=loc);o=bpy.context.object;o.name=n;o.dimensions=dim;bpy.ops.object.transform_apply(location=False,rotation=False,scale=True);o.data.materials.append(m)
 if bev:mod=o.modifiers.new('Soft edges','BEVEL');mod.width=bev;mod.segments=2;o.modifiers.new('Weighted normals','WEIGHTED_NORMAL')
 return o
def ball(n,loc,scale,m):
 bpy.ops.mesh.primitive_uv_sphere_add(segments=16,ring_count=8,location=loc);o=bpy.context.object;o.name=n;o.scale=scale;o.data.materials.append(m);return o
def group(n,loc):
 o=bpy.data.objects.new(n,None);bpy.context.collection.objects.link(o);o.location=loc;return o
def attach(o,p):o.parent=p;o.matrix_parent_inverse=p.matrix_world.inverted()
def animate(o,frame,location=None,rotation=None,scale=None):
 if location is not None:o.location=location;o.keyframe_insert(data_path='location',frame=frame)
 if rotation is not None:o.rotation_euler=rotation;o.keyframe_insert(data_path='rotation_euler',frame=frame)
 if scale is not None:o.scale=scale;o.keyframe_insert(data_path='scale',frame=frame)
cube('Lawn',(0,0,-.2),(28,24,.3),grass)
cube('Road',(0,-4,-.03),(28,6,.09),road)
slab=group('SENTIENT SIDEWALK',(0,-1.15,.07))
p=cube('Sidewalk slab',(0,0,0),(9,2,.18),pavement,.07);attach(p,slab)
for x in [-2,0,2]:
 crack=cube('Joint',(x,0,.11),(.045,1.8,.015),road);attach(crack,slab)
# crooked house with door, windows, roof
cube('House',(0,5,2.0),(5.3,3.3,4),brick,.2)
roof=cube('Crooked roof',(.2,5,4.2),(6.2,4,.6),blue,.08);roof.rotation_euler[1]=.12
cube('Door',(-.9,3.32,.98),(1.1,.1,1.95),dark,.06)
for x in [1.05,2.0]:cube('Window',(x,3.3,2.35),(.65,.09,.85),white,.05)
# animated raccoon inventor Pip, coordinates relative to root
pip=group('PIP RIG',(-3,0,0))
def part(o):attach(o,pip);return o
part(ball('Pip body',(0,0,1.05),(.52,.36,.68),teal))
part(ball('Pip head',(0,-.04,2.05),(.61,.46,.55),teal))
part(ball('Cream muzzle',(0,-.46,1.91),(.36,.12,.21),cream))
part(ball('Nose',(0,-.58,2.02),(.11,.08,.08),dark))
for side in [-1,1]:
 part(ball('Raccoon ear',(.47*side,0,2.47),(.25,.18,.31),teal))
 part(ball('Ear inner',(.48*side,-.15,2.48),(.14,.055,.18),cream))
 part(ball('Dark eye patch',(.25*side,-.39,2.17),(.22,.075,.22),dark))
 part(ball('White eye',(.25*side,-.465,2.19),(.115,.045,.14),white))
 part(ball('Pupil',(.25*side,-.51,2.18),(.05,.03,.07),dark))
 part(ball('Arm',(.57*side,-.02,1.18),(.18,.22,.48),teal))
 part(ball('Foot',(.28*side,-.19,.25),(.23,.35,.17),dark))
part(cube('Yellow vest',(0,-.25,1.12),(.84,.23,.85),vest,.08))
part(cube('Orange tool belt',(0,-.42,.72),(.91,.12,.18),orange,.04))
tail=part(ball('Raccoon tail',(.65,.32,.68),(.46,.24,.26),teal))
# trash can and bush, fixed objects
can=cube('Talking trash can',(4,-.15,.63),(1.05,.95,1.24),brown,.12)
cube('Trash lid',(4,-.15,1.29),(1.25,1.12,.13),dark,.06)
for x in [3.78,4.22]:ball('Trash eye',(x,-.64,.86),(.1,.035,.13),white)
for x in [1.6,2.05,2.5]:ball('Landing bush',(x,.5,.55),(.68,.62,.52),grass)
# walk -> sidewalk dodges -> tumble
for f,loc,rot in [(1,(-3,0,0),(0,0,0)),(30,(-2.1,0,0),(0,0,0)),(55,(-1.15,0,0),(0,0,0)),(68,(-.65,0,0),(0,0,-.25)),(82,(.1,0,.45),(0,-.3,-.95)),(105,(1.2,.2,.25),(0,-.5,-1.7)),(128,(1.85,.2,0),(0,0,-1.5)),(165,(1.85,.2,0),(0,0,-1.5)),(190,(2,.2,.1),(0,0,-.5)),(240,(2,.2,0),(0,0,0))]:
 animate(pip,f,location=loc,rotation=rot)
for f,x in [(1,0),(48,0),(63,1.15),(88,1.15),(128,.4),(240,.4)]:
 animate(slab,f,location=(x,-1.15,.07))
# lighting, orthographic framing
bpy.ops.object.camera_add(location=(0,-13,6))
camera=bpy.context.object;camera.rotation_euler=(Vector((.5,1,1.5))-camera.location).to_track_quat('-Z','Y').to_euler()
camera.data.type='ORTHO';camera.data.ortho_scale=10.5;sc.camera=camera
bpy.ops.object.light_add(type='AREA',location=(-4,-5,9));bpy.context.object.data.energy=1800;bpy.context.object.data.size=7
sc.world.color=(.42,.55,.72)
bpy.ops.wm.save_as_mainfile(filepath='/tmp/wrongside_shot.blend')
