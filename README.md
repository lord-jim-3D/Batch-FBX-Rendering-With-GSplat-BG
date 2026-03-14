This is a quick test for how I might trigger some kind of batch processing TOP net via python. 
It was also an excuse to look at the new gaussian splat compatibility in Houdini 21.

To run it you can open up the houdini terminal and then run the python script through hython.

v01 uses gaussian splats and comps them in with the fbx. However this requires some custom positioning of the shadow catcher and scene set up, designed to function with batches of fbxs.

v02 uses point clouds, not splats, therefore has no comp steps and is meant to be used with batches of plys and fbxs.

For the file to work you either need to download the guassian splat I made [here](https://lumalabs.ai/capture/ebdb74a9-8876-4559-9294-2f03e81e55b3) or modify the scene to use your own.

If you are going to modify the scene, do so in the lop net. You can basically do whatever you want, just make sure the shadow catcher is functioning correctly before sending it.
I.E. Make sure it covers the whole frame if you want to use the physical sky, and that it actually catches any notable shadows.

You could also use the point cloud (non gsplatified) as a shadow catcher if you want to do more complex light interactions.

The file will save all the images for every step, so if you want to intercept the system and do your own comp/encode you can just grab the images from the render folder.

Also if you are going to animate the camera you will need to modify the hscript in the frame range in the usd render rop and the samples in the karma render settings.
