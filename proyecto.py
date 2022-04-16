#importo librerias
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
#inicio la app
app = Ursina()


#creo la clase del cubo
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
#defino la funcion de romper
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                voxel = Voxel(position=self.position + mouse.normal)
            if key == 'right mouse down':
                destroy(self)





#cargo el chunk
chunkSize = 16

for z in range (chunkSize):
    for x in range (chunkSize):
        voxel = Voxel (position=(z, 0, x))




#lo pongo en 1 persona 
player = FirstPersonController()

#creo el cielo
sky = Sky()


#corro el programa
app.run()
