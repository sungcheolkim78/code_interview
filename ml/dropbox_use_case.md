# Creating a Modern OCR Pipeline Using Computer Vision and Deep Learning

- [link](https://dropbox.tech/machine-learning/creating-a-modern-ocr-pipeline-using-computer-vision-and-deep-learning)

- Optical Character Recognition (OCF) pipeline
- using bi-directional LSTMs, connectionist temporal classification (CTC), convolutional neural nets(CNNs)
- mobile document scanner -> only image -> OCR -> text
- integrating the commercial system into our scanning pipeline
- build our own in-house OCR system for several reasons
    - cost consideration
    - commercial system was tuned for the images from flat bed scanners
    - more control over own destiny

Steps:

1. Research and prototyping to see if something is possible
1. Productionization of the model for actual end users
1. Refinement of the system in the real world

## Research and prototyping

- collectiong a representative set of donated document images that match what users might upload, such as receipts, invoices, letters, etc.
- safety precautions on user-donated data - never keeping on local machines in permanent storage, maintaining extensive auditing, requiring strong authentication to access
- Amazon's Mechanical Turk (MTurk) - don't want to expose user-donated data in the wild
- created own platform for data annotation "DropTurk"
    - Transcribing the actual text in an image
    - Marking whether the word is orineted incorrectly
    - Marking whether it's a non-English script
    - marking whether it's unreadable or contains no text
- Word Detector, Word Deep Net

## Word Deep Net

- CNN -> Bidirectional LSTM -> CTC -> Batch Normalization
- In most computer vision problems it's currently too difficult to generate realistic-enough images for training algorithms

Synthetic data pipeline

1. A corpus with words to use
1. A collection of fonts for drawing the words
1. A set of geometric and photometric transformations meant to simulate real world distortions

- million synthetic words -> 79% accuracy
- receipts -> adding Uniform Product Code (UPC) database
- disconnected segments -> adding a new font with representative ancient thermal printer
- hand-selecting 2,000 fonts -> font frequency system
- negative training examples -> adding textured backgrounds like wood, marble, conutertops
- adding visual transformations, such as warping, fake shadows, fake creases

>> Data is as important as the machine learning model used, so we spent a great deal of time refining this data generation pipeline.

- Train: Amazon EC2 G2 GPU instances, spinning up many experiments in parallel

- precision: true positives / total positives, recall: true positives / total numbers

## Word Detector

- primary candidates: object detection systems, like RCNN
- most documents have hundreds or even thousnads of them
- final model: a classical computer vision approach named "Maximally Stable Extremal Regions (MSERs)"
- 1) add infomation about contious regions of the word 2) white text on black background

## Combined End-to-End System

- document-level images
- primary issues: spacing and spurious garbage text from noise in the image
- modify CTC layer -> give us a confidence score in addition to the predicted text
    - high confidence -> accpet the prediction
    - low confidence -> reject the prediction
    - middle confidence -> apply different transformations, attempt to combine words or split them in various ways

## Productionization

- we needed to create a distributed pipeline suitable for use by millions of users and a system replacing our prototype scripts.

![overall productionized OCR pipeline](https://dropbox.tech/cms/content/dam/dropbox/tech-blog/en-us/2020/01/12-s_a5d57ee03480ad99adf37089497274a382beafcaac54e1a98f6d51e323e2fc30_1491598157110_ocr_system_diagram.png)

- abstraction for different OCR engines
- image upload -> Remote Procedure Call (RPC) to a cluster of servers -> isolated the actuaal OCR engine -> OCRed text

## Performance tuning

- actual engineering pipeline (with unit tests and continual integration)
- however, using GPUs at inference time is a harder call to make currently
- we decided that we could hit our performance targets on just CPUs at similar or lower costs than with GPU machiens
- BLAS libraries for the Word Deep Net, rewriting OpenCV's C++ MSER implementation

## Refinement

- user-image donation flow
- orientation predictor - only a small percentage of images are actually rotated
- thie entire processes took about 8 months to complete

[link](https://dropbox.tech/machine-learning)
