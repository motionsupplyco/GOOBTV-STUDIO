import bpy, math
from mathutils import Vector
bpy.ops.object.select_all(action='SELECT'); bpy.ops.object.delete(use_global=False)
s=bpy.context.scene
s.render.engine='BLENDER_EEVEE' if bpy.app.version < (4,2,0) else 'BLENDER_EEVEE_NEXT'
s.render.resolution_x=540;s.render.resolution_y=960;s.render.fps=24;s.frame_end=192
def material(name,color):
 m=bpy.data.materials.new(name);m.diffuse_color=(*color,1);return m
red=material('Baby red',(.9,.025,.04));orange=material('Dad orange',(1,.24,.01));white=material('White',(1,1,1));black=material('Black',(.015,.02,.025));purple=material('Purple',(.35,.1,.8));street=material('Road',(.22,.27,.34));blue=material('Sky blue',(.15,.6,.85))
def cube(name,loc,scale,mat):
 bpy.ops.mesh.primitive_cube_add(size=1,location=loc);o=bpy.context.object;o.name=name;o.dimensions=scale;bpy.ops.object.transform_apply(location=False,rotation=False,scale=True);o.data.materials.append(mat);return o
def ball(name,loc,scale,mat):
 bpy.ops.mesh.primitive_uv_sphere_add(segments=16,ring_count=8,location=loc);o=bpy.context.object;o.name=name;o.scale=scale;o.data.materials.append(mat);return o
def key(o,f,location=None,scale=None):
 if location is not None:o.location=location;o.keyframe_insert(data_path='location',frame=f)
 if scale is not None:o.scale=scale;o.keyframe_insert(data_path='scale',frame=f)
cube('Road',(0,0,-.2),(15,30,.2),street)
for x in [-5,5]:
 for y in [-8,0,8]:cube('Buildings',(x,y,2.5),(3,3,5),blue)
bpy.ops.mesh.primitive_cylinder_add(vertices=8,radius=.85,depth=.2,location=(0,0,1.9));baby=bpy.context.object;baby.name='Stop sign baby';baby.rotation_euler[0]=math.pi/2;baby.data.materials.append(red)
for x in [-.3,.3]:
 ball('Baby eye',(x,-.15,2.15),(.19,.08,.22),white);ball('Baby pupil',(x,-.23,2.14),(.07,.035,.1),black)
mouth=ball('Baby moving mouth',(0,-.16,1.64),(.24,.06,.1),black)
for x in [-1,1]:ball('Muscle arm',(x*.94,0,1.65),(.42,.3,.28),red)
seat=cube('Stroller',(0,.2,.9),(1.6,1,.3),purple)
for x in [-.7,.7]:
 for y in [-.2,.6]:ball('Wheel',(x,y,.48),(.2,.2,.2),black)
bpy.ops.mesh.primitive_cone_add(vertices=32,radius1=.65,radius2=.05,depth=1.9,location=(-2,1,1.8));dad=bpy.context.object;dad.name='Cone Dad';dad.data.materials.append(orange)
for x in [-.24,.24]:
 ball('Dad eye',(-2+x,.37,2.05),(.14,.1,.16),white);ball('Dad pupil',(-2+x,.27,2.05),(.06,.04,.07),black)
dadmouth=ball('Dad moving mouth',(-2,.37,1.68),(.19,.045,.09),black)
for x in [-.3,.3]:cube('Roller skate',(-2+x,.75,.55),(.3,.5,.2),purple)
for f,v in [(1,.3),(15,1.6),(32,.2),(70,.4),(90,1.8),(115,.2),(192,.2)]:key(mouth,f,scale=(.24,.06,.1*v))
for f,v in [(1,.3),(12,1.6),(30,.2),(145,.3),(160,1.8),(185,.2),(192,.2)]:key(dadmouth,f,scale=(.19,.045,.09*v))
for f,x in [(1,-2),(115,-2),(140,-1.6),(160,-.8),(192,1.3)]:key(dad,f,location=(x,1,1.8))
for f,y in [(1,.2),(110,.2),(140,-.3),(192,-2)]:key(seat,f,location=(0,y,.9))
for f,z in [(1,1.9),(65,1.9),(85,2.08),(105,1.9),(192,1.9)]:key(baby,f,location=(0,0,z))
bpy.ops.object.camera_add(location=(0,-12,4.5));cam=bpy.context.object;cam.rotation_euler=(Vector((0,0,1.6))-cam.location).to_track_quat('-Z','Y').to_euler();cam.data.type='ORTHO';cam.data.ortho_scale=7;s.camera=cam
for f,v in [(1,7),(60,5.5),(100,5.2),(150,6.8),(192,7)]:cam.data.ortho_scale=v;cam.data.keyframe_insert(data_path='ortho_scale',frame=f)
bpy.ops.object.light_add(type='AREA',location=(-4,-5,8));bpy.context.object.data.energy=2000;bpy.context.object.data.size=8
s.world.color=(.35,.4,.55);s.render.image_settings.file_format='PNG';bpy.ops.wm.save_as_mainfile(filepath='/tmp/goobtv.blend')
