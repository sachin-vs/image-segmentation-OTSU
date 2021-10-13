# Foreground object extraction
There are multiple objects in the image captured.Image segmentation is necessary for extracting objects from background.For extracting objects from background we use thresholding using Otsu’s method and Grab cut.Both are functions available in OpenCV library.Otsu’s thresholding method convert input image to its binary.
Application- To use this method together with a classifier on assembly lines for inspecting availablity of each child parts for assembling a part.
# input
![input](https://user-images.githubusercontent.com/85213549/137192814-df095f8a-d815-4287-9a8d-c15a09e41038.jpg)
# OTSU output
![index](https://user-images.githubusercontent.com/85213549/137192858-1adff88b-b901-45fd-a51a-ad81c97404ce.png)
# Extracted objects in bounding box
![index4](https://user-images.githubusercontent.com/85213549/137192959-1fc959f7-db30-42f0-8a37-548c71001edd.png)
