# Hikki
Object Tracking for Physics Apparatuses 

Hikki operates using pixel color determination to find objects in a given set of frames. Hikki can read in a video (recommended in mp4) format,
find all pixels in the video that correspond to a user-defined color and a user-defined threshold, and determine the median pixel for each frame, thus finding a good approximation of the object's position.

The purpose of Hikki is to track an object's position with only the use of a camera, reducing the need for other equipment. Hikki has been tested and is shown to work decently well in suboptimal light conditions, and with imperfect objects as well.
