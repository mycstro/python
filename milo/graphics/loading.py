from ursina import *

class LoadingWheel(Entity):
    def __init__(self, **kwargs):
        super().__init__(
            parent=camera.ui,
        )
        self.point = Entity(
            parent=self,
            model=Circle(24, mode='point', thickness=3),
            color=color.blue,
            y=.75,
            scale=2
            )
        self.point2 = Entity(
            parent=self,
            model=Circle(12, mode='point', thickness=3),
            color=color.red,
            y=.75,
            scale=1
            )
        self.scale = .025
        self.text_entity = Text(
            world_parent = self,
            text = '  loading...',
            origin = (0,1.5),
            color = color.white,
            )
        self.y = -.25

        self.bg = Entity(parent=self, model='quad', scale_x=camera.aspect_ratio, color=color.black, z=1)
        self.bg.scale *= 400

        for key, value in kwargs.items():
            setattr(self, key ,value)


    def update(self):
        self.point.rotation_y += 5
        self.point2.rotation_y += 3

if __name__ == '__main__':
    app = Ursina()
    window.color = color.black
    def input(key):
        if key == 'space':
            LoadingWheel(enabled=True)

    app.run
