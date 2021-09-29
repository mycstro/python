from os import path
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.health_bar import HealthBar

app = Ursina()

window.title = 'Milo'
window.color = color.black
window.exit_button.visible = False
window.fps_counter.visible = False
window.fullscreen = True
window.show_ursina_splash = False

bg = Entity(model='quad', scale_x=window.aspect_ratio, texture='')
bg.scale *= 2.0
bg.aspect_ratio = bg.scale_x / bg.scale_y

fg = duplicate(bg)
fg.texture = ''
fg.z = -2


class Load_Assets:
    def __init__(self):
        print("Starting Asset Loader")

    def load_textures(self, texs):
        textures_to_load = texs
        for i, t in enumerate(textures_to_load):
            w = path.split(t)
            w1 = w[1].split('.')
            _info = Text(text="{} Loading texture, '{}'".format(i, w1))
            printvar(_info)
            load_texture(w1[0], t)
            print(i, 'Loaded texture....', t)

    def load_audio(self, auds, loop=False, autoplay=False):
        audio_to_load = auds
        for i, a in enumerate(audio_to_load):
            w = path.split(a)
            w1 = w[1].split('.')
            _info = Text(text="{} Loading audio, '{}'".format(i, w1))
            printvar(_info)
            Audio(a, loop=loop, autoplay=autoplay)


def update():
    print("Global Updating!")
    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()


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


for z in range(20):
    for x in range(20):
        voxel = Voxel(position=(x, 0, z))

player = FirstPersonController()
sky = Sky()
hand = Hand()

app.run()
