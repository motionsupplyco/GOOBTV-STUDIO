import bpy
scene=bpy.context.scene
scene.render.engine='BLENDER_WORKBENCH'
scene.display.shading.light='STUDIO'
scene.display.shading.color_type='MATERIAL'
scene.display.shading.show_shadows=True
scene.display.shading.show_cavity=True
scene.display.shading.cavity_type='BOTH'
scene.render.resolution_x=640
scene.render.resolution_y=360
scene.render.resolution_percentage=100
scene.render.fps=12
scene.frame_end=120
# Preserve original keyframe timing by using frame step 2 at render time.
scene.render.image_settings.file_format='PNG'
print('GOOBTV fast Workbench preview configured')
