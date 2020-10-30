from . import panda
import argparse

def cli():
    parser = argparse.ArgumentParser(prog = "walking_panda")

    parser.add_argument("--no-rotate", help = "Suppress Rotation",
                        action = "store_true")

    parser.add_argument("--scale", type=int, help = "Scale the panda",
                        default='1')

    parser.add_argument("--sound-on", help = "Turn sound off",
                        action = "store_true")

    parser.add_argument("--flip", help = "Flip Panda",
                        action = "store_true")

    parser.add_argument("--panda-rotate", help = "Rotate Panda",
                        action = "store_true")

    args = parser.parse_args()
    walking = panda.WalkingPanda(**vars(args))
    walking.run()

