# CUSTOM URSINA SPLASH SCREENS!

The custom ursina splash screen is a way to add your own splash screens with **custom and customizable** splash screens!


## HOW TO INSTALL
   To install this tool, you should clone this repository into your project folder. Then, remove the __README__.md file and then follow the tutorial. You can tweak things as you want.


### HOW TO USE IT
How to use it:
 ```python
  from customsplash import CustomSplash #import the library
from ursina import * #import ursina as usual
app = Ursina() #initalize ursina

'''basic usage'''
CustomSplash(overlay_color=color.black,logo_texture='image.png',delay_time=4,audio='audio.mp3',audio_volume=1)  #Copy until here
```
__overlay_color__ is what color will the background and the fade out animation will be. You can only use ursina's pre-built colors or hsv's. There is no official support for other ways.

__logo_texture__ is the image that will be displayed as the photo. Currently, gifs only display as a single image. Type in the *RELATIVE* path to the image in strings.

__delay_time__ is how long will the screen will be in seconds. Please use integers.

__audio__ is the sound that will be played immediately in the splash screen. You type the *RELATIVE* path to the audio.

__audio_volume__ is the volume of the audio. It is between 1 to 0 in floats.

_AUDIO HAS TO BE SEPERATE, GIFS DONT WORK FOR NOW, ALSO VIDEOS DONT WORK_

*You can tweak the values of it,
When there is no texture or sound, it will skip*

Now add, app.run() at the end.

```python
app.run()#run ursina 
```
