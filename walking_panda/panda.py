from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor

class WalkingPanda(ShowBase):

    def __init__(self, no_rotate = False, scale = 1, sound_on = True, flip = False, panda_rotate = False):
        ShowBase.__init__(self)

        # Disable mouse controlling camera
        self.disableMouse()

        # Load the environment model
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)
        # Set default position for camera
        self.camera.setPos(0, -20, 3)

        # Add the spinCameraTask procedure to the task manager.
        if (no_rotate == False):
            self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

        # Load and transform the panda actor.
        self.pandaActor = Actor("models/panda-model", {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.005 * scale, 0.005 * scale, 0.005 * scale)
        self.pandaActor.reparentTo(self.render)

        # Check if panda should rotate
        if (panda_rotate == True):
            self.taskMgr.add(self.rotatePandaTask, "rotatePandaTask")

        # Check if panda should be flipped
        if (flip == True):
            self.pandaActor.setHpr(0, 0, 180)
            self.pandaActor.setPos(0, 0, 3)

        # Check for sound and play
        if (sound_on == True):
            ambience = self.loader.loadSfx("ambience.mp3")
            ambience.setVolume(0.5)
            ambience.setLoop(True)
            ambience.play()

        # Loop its animation.
        self.pandaActor.loop("walk")

    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont

    # Define a procedure to rotate the panda
    def rotatePandaTask(self, task):
        angleDegrees = task.time * 12.0
        self.pandaActor.setHpr(angleDegrees, 0, 0)
        return Task.cont

