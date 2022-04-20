from moviepy.editor import *


def create_gif(path, gif_name):
    clip = (VideoFileClip(path)
            .subclip(2.0, 4.0)
            .speedx(0.5)
            .resize(.4))
    clip.write_gif(f"{gif_name}.gif", fps=5)
