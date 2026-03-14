import hou
import argparse
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

parser = argparse.ArgumentParser(description='Cook FBX files and render to MP4 using Houdini.')
parser.add_argument('--hip', default = os.path.join(dir_path, 'houdini_files', 'autosplatscene_v02.hipnc'), type=str, help='Path to the Houdini .hip file')
parser.add_argument('--files', type=str, help='Path to the directory containing the FBX files')
parser.add_argument('--render', default = '$HIP/renders', type=str, help='Path to the directory where the rendered MP4 files will be saved')
parser.add_argument('--splat', type=str, help='Path to directory containing gaussian splat files')

args = parser.parse_args()
hip_file = args.hip
fbx_files = args.files
render_path = args.render
splat_file = args.splat

hou.hipFile.load(hip_file)

splattop = hou.node('/obj/topnet1/splat_files')
splattop.parm('pattern').set(splat_file + '/*.ply')

filetop = hou.node('/obj/topnet1/fbx_files')
filetop.parm('pattern').set(fbx_files + '/*.fbx')

encodetop = hou.node('/obj/topnet1/ffmpegencodevideo1')
encodetop.parm('outputfilepath').set(render_path + '/' + '`@splatname`_`@filename`.mp4')

encodetop.dirtyAllWorkItems(True)
encodetop.cookWorkItems(block=True)
