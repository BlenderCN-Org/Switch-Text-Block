# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Switch Text Block",
    "description": "Switch the active text blocks with shortcuts",
    "author": "Ray Mairlot",
    "version": (1, 0),
    "blender": (2, 71, 0),
    "location": "Text Editor > Shift+Tab or Ctrl+Shift+Tab",
    "category": "Development"}
    
import bpy    
        

class NextTextBlockOperator(bpy.types.Operator):
    """ Switch to the next text block in the list """
    bl_idname = "text.text_block_next"
    bl_label = "Next text block"


    def execute(self, context):
        main(context,"Next")
        return {'FINISHED'}
    
    
class PreviousTextBlockOperator(bpy.types.Operator):
    """ Switch to the previous text block in the list """
    bl_idname = "text.text_block_previous"
    bl_label = "Prevous text block"


    def execute(self, context):
        main(context, "Previous")
        return {'FINISHED'}    


def main(context, direction=""):
    
    if direction=="Next":
        offset = 1
    else:
        offset = -1
    
    texts = []
    
    for text in bpy.data.texts:
        texts.append(text.name)
        
    textIndex = texts.index(context.edit_text.name)
        
    space = context.area.spaces[0]
    
    
    if textIndex<len(bpy.data.texts)-1 and direction=="Next":    #Not at end, going forward                             
        space.text = bpy.data.texts[textIndex+offset]
    elif textIndex==len(bpy.data.texts)-1 and direction=="Next": #At end, going forward
        space.text = bpy.data.texts[0]
    elif textIndex==0 and direction=="Previous":                 #At beginning, going backwards
        space.text = bpy.data.texts[len(bpy.data.texts)-1]
    elif textIndex>0 and direction=="Previous":                  #Not at beginning, going backwards
        space.text = bpy.data.texts[textIndex+offset]


def register():
    bpy.utils.register_class(NextTextBlockOperator)
    bpy.utils.register_class(PreviousTextBlockOperator)
    
    kc = bpy.context.window_manager.keyconfigs.addon

    km = kc.keymaps.new(name='Text', space_type='TEXT_EDITOR')
    km.keymap_items.new("text.text_block_next", 'TAB', 'PRESS', ctrl=True)
    
    km = kc.keymaps.new(name='Text', space_type='TEXT_EDITOR')
    km.keymap_items.new("text.text_block_previous", 'TAB', 'PRESS', ctrl=True, shift=True)


def unregister():
    bpy.utils.unregister_class(NextTextBlockOperator)
    bpy.utils.unregister_class(PreviousTextBlockOperator)
    
    kc = bpy.context.window_manager.keyconfigs.addon
    kc.keymaps.remove(kc.keymaps['Text'])    


if __name__ == "__main__":
    register()





