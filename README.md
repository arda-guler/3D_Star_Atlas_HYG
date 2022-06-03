# HYG Database 3D Star Atlas

![ss](https://user-images.githubusercontent.com/80536083/171954477-c34d8218-fade-4a8f-820a-989fa354f538.PNG)

A 3D map of local and bright stars in OpenGL, data from HYG database. 

The database can be found at https://github.com/astronexus/HYG-Database and is not my work. It is licensed by a Creative Commons Attribution-ShareAlike license. For more details, read the Creative Commons page (https://creativecommons.org/licenses/by-sa/2.5/).

This Python repository simply takes the position, luminosity and spectral type data of stars and visualizes it.

## Assumptions and Approximations

 - Only the main spectral class of a star is used for the RGB color (O, B, A, F, G, K, M). Non-main-sequence stars and all other sorts of stellar objects are just painted white.
 - Lumniosity is capped between 10 Solar luminosity (max pixel brightness) and 0.1 Solar luminosity (min pixel brightness). The reason is that a pixel can only go so bright, and if I didn't cap the value, some stars would be so dim in comparison to others that they simply wouldn't be visible on the screen. (So a simple normalization doesn't work.)
 - Stars don't appear brighter if you get closer to them. Luminosity value is used for brightness, and not apparent magnitude relative to camera. (It makes more sense for a map.)
 - Stars are just pixels and are not modeled as spheres. No matter how close you get to a star with the camera, a star will always paint the same number of pixels on your screen.

## Controls
Controls can be modified in main.py if needed.

- WASDQE for camera rotation.
- IJKLUO for camera translation.
- T to double max star render distance (from Sol), G to halve. If you press T too much, expect the script to run like a potato.
