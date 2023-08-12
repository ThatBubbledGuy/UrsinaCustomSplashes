from ursina import *

if __name__ == '__main__':
    app = Ursina()
class CustomSplash:
    def __init__(self,overlay_color,logo_texture,delay_time,audio,audio_volume):
        camera.overlay.color = overlay_color
        
        audio_intro = Audio(sound_file_name=audio,auto_destroy=True)
        audio_intro.volume = audio_volume
        audio_intro.loop = False
        audio_intro.play()
        logo = Sprite(parent=camera.ui, texture=logo_texture, world_z=camera.overlay.z-1, scale=.1, color=color.clear)
        logo.animate_color(color.white, duration=2, delay=1, curve=curve.out_quint_boomerang)

        camera.overlay.animate_color(color.clear, duration=1, delay=int(delay_time))
        destroy(logo, delay=5)

        def splash_input(key):
            destroy(logo)
            camera.overlay.animate_color(color.clear, duration=.25)

        logo.input = splash_input



if __name__ == '__main__':
    app.run()