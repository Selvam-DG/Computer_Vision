# Computer_Vision
## Video Data
## Image Features
## Object Detection
## Object Tracking

### Matlab Onramp commnds
- v = VideoReader(filename)
- fr = readFrame(v); => read frame from the video file
- prop = obj.PropertyName
- read function extracts a specific frame from a video file.
  - fr = read(v,n);
- skip to the last frame by specifying Inf as the second input to read.
  - fr = read(v,Inf);
 - reset video time by using the below command
   - filename.CurrentTime = 2

- mcrop function allows you to crop an image by specifying the rectangle you want to keep.
  - imCropped = imcrop(im,rect);
  - Specify the rectangle as a four-element vector, [xmin ymin width height].
- To detect the blob-like features in an image, you can use the detectSIFTFeatures function.
  -pts = detectSIFTFeatures(im)
- use the extractFeatures function for any type of feature.
  - [feat,ftPts] = extractFeatures(im,pts)

- match the features using the matchFeatures function.
  - indexedPairs = matchFeatures(feat1,feat2)
 
-  draw bounding boxes on an image by using the insertObjectAnnotation function.
  - imNew = insertObjectAnnotation(im, ...    shape,pos,label);
- create training images from a video file using the objectDetectorTrainingData function.
  - [ims,labs] = objectDetectorTrainingData( ...     gTruth,SamplingFactor=n);

- combine the images and labels with the combine function.
  - imsWithLabels = combine(ims,labs);
- Aggregate channel features (ACF) object detectors use features from color channels and other 2D representations of an image to detect objects.
  - create an ACF detector trained with your ground truth images using the trainACFObjectDetector function.
  - d = trainACFObjectDetector(imsWithLabels)
- apply a detector to an image by using the detect function.
  - [b,s] = detect(detector,im)
-  draw bounding boxes on an image by using the insertObjectAnnotation function.
  - imNew = insertObjectAnnotation(im, ...     shape,pos,label);


