from __future__ import print_function

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from tqdm.auto import tqdm

import os
import sys
import struct
from panda3d.core import Vec3, load_prc_file_data, Texture, GeomEnums
from panda3d.core import OmniBoundingVolume
from direct.showbase.ShowBase import ShowBase

# Change to the current directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Insert the pipeline path to the system path, this is required to be
# able to import the pipeline classes
pipeline_path = "../miloSystems/"

# Just a special case for my development setup, so I don't accidentally
# commit a wrong path. You can remove this in your own programs.
# if not os.path.isfile(os.path.join(pipeline_path, "../RenderPipeline/setup.py")):
#     pipeline_path = "/"
#
# sys.path.insert(0, pipeline_path)

# Import the render pipeline class
from milo.RenderPipeline.rpcore import RenderPipeline

# This is a helper class for better camera movement - see below.
from milo.RenderPipeline.rpcore.util.movement_controller import MovementController
from milo.graphics.loading import LoadingWheel

app = Ursina()

grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture = load_texture('assets/dirt_block.png')
bedrock_texture = load_texture('assets/bedrock.png')
oak_log_texture = load_texture('assets/oak_log.png')
obsidian_texture = load_texture('assets/obsidian.png')
wood_texture = load_texture('assets/wood.png')
wool_texture = load_texture('assets/wool_block.png')

sky_texture = load_texture('assets/skybox.png')
water_texture = load_texture('assets/water.jpg')
arm_texture = load_texture('assets/arm_texture.png')

punch_sound = Audio('assets/punch_sound', loop=False, autoplay=False)

block_pick = 1

window.title = 'Milo'
window.color = color.black
window.fps_counter.enabled = False
window.exit_button.visible = True


def update():
    global block_pick

    if player.y <= -10:
        player.x = 0
        player.z = 0
        player.y = 0

    #voxelUpdate()

    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()

    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4
    if held_keys['1']: block_pick = 5
    if held_keys['2']: block_pick = 6
    if held_keys['3']: block_pick = 7
    if held_keys['4']: block_pick = 8

class Inventory(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'quad',
            scale = (.9, .1),
            origin = (-.5, .5),
            position = (-0.45,-0.4),
            texture = 'widgets',
            texture_scale = (9,1),
            color = color.dark_gray
            )


class Items(Entity):
    def __init__(self,texture,position):
        super().__init__(
            parent=camera.ui,
            model='quad',
            scale=(.1, .1),
            origin=(-.5, .5),
            position=(-position, -0.4),
            texture=texture,
            texture_scale=(1, 1),
            color= color.white
        )


class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture=grass_texture):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1)),
            scale=0.5)

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                punch_sound.play()
                if block_pick == 1: voxel = Voxel(position=self.position + mouse.normal, texture=grass_texture)
                if block_pick == 2: voxel = Voxel(position=self.position + mouse.normal, texture=stone_texture)
                if block_pick == 3: voxel = Voxel(position=self.position + mouse.normal, texture=brick_texture)
                if block_pick == 4: voxel = Voxel(position=self.position + mouse.normal, texture=dirt_texture)

            if key == 'right mouse down':
                punch_sound.play()
                destroy(self)


class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='sphere',
            texture=sky_texture,
            scale=150,
            double_sided=True)


class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='assets/arm',
            texture=arm_texture,
            scale=0.2,
            rotation=Vec3(150, -10, 0),
            position=Vec2(0.4, -0.6))

    def active(self):
        self.position = Vec2(0.3, -0.5)

    def passive(self):
        self.position = Vec2(0.4, -0.6)


def gridLines():
    r = 8
    for i in range(1, r):
        t = i / r
        s = 4 * i
        print(s)
        grid = Entity(model=Grid(s, s), scale=s, color=color.color(0, 0, .8, lerp(.8, 0, t)), rotation_x=90, y=i / 1000)
        subgrid = duplicate(grid)
        subgrid.model = Grid(s * 4, s * 4)
        subgrid.color = color.color(0, 0, .4, lerp(.8, 0, t))
        EditorCamera()
gridLines()

voxels = []
def voxelGround():
    for z in tqdm(range(20)):
        for x in range(20):
            voxel = Voxel(position=(x, 0, z))
            voxels.append(voxel)
voxelGround()

def myFirstPersonController():
    controller = MovementController()
    controller.set_initial_position_hpr(
        Vec3(-23.2, -32.5, 5.3),
        Vec3(-33.8, -8.3, 0.0))
    controller.setup()

player = myFirstPersonController()

def voxelUpdate():
    for z in range(int(player.z - 5), int(player.z + 5)):
        for x in range(int(player.x - 5), int(player.x + 5)):
            # optimizing by not making any voxels where there are already voxels
            if (x, z) not in [(voxel.x, voxel.z) for voxel in voxels if len(voxels) != 0]:
                voxel = Voxel((x, 0, z))
                voxels.append(voxel)


sky = Sky()
hand = Hand()

app.run()
