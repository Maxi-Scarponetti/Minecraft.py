from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()


 
class Voxel(Button):
    def __init__(self, position=(0, 0, 0),):
        super().__init__(
            parent=scene,
            model='cube',
            color=color.color(0,0,random.uniform(0.9,1)),
            highlight_color=color.lime,
            texture= 'brick',
            position=position,
            origin_y=0.5
        )

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                voxel = Voxel(position=self.position + mouse.normal)
            if key == 'right mouse down':
                destroy(self)






chunkSize = 16

for z in range (chunkSize):
    for x in range (chunkSize):
        voxel = Voxel (position=(z, 0, x))





player = FirstPersonController()
sky = Sky()



app.run()
