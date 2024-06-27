# game_classification
Goal: to create a program that can sort unordered gameplay clips into appropriately named folders for people with a lot of VODs on Windows.
Idea: train a model using python, export to ONNX, write the program in C++, running inference on the CPU.

# So far:
I trained a simple YoloV8 model to recognize 8 different games:
- Apex Legends
- Counter Strike 2 
- Diabotical
- The Finals
- KovaaKs
- Overwatch 2 
- Valheim
- Valorant

## Technical stuff
I trained the classification model on my Debian 12 system, using Python 3.8, Ultralytics 8.2, CUDA 11.8 and the 525.147.05 NVIDIA driver on a 3070 8GB card for 100 epochs, then exported it to ONNX so I can continue the development in C++ (this is my first time using C++, will probably do it on my Windows system cuz paths and testing might be easier if that's my target OS).

Dataset is just 140+30+30 pics per class (train, val, test) at 224x224x3 JPEGs. Got them by extracting keyframes using FFMPEG, ordered them with a bash script. Will do the same in the inference program but I'll load them into RAM.

I got 99.2% accuracy with it, it should probably be good enough because I'll be averaging results out from multiple frames. (Might need to try other videos as well but now I have something I can work with).

Model will also be loaded into RAM.
Program will probably look something like this:
    load model into RAM (it is 5.8MBs for the smallest yolov8 classification model I've trained on the 8 classes)
    get list of video paths
        use ffmpeg to get keyframes, up to 50 in 224x224x3 per clip, load them into RAM (~8MBs?)
            run inference on the frames
                average out results
                    use results to decide what folder to put the original video to
                        move the video to the folder
                        clean frames and other stuff that needs cleaning up and repeat until video list is empty, once it is done clear everything

Will try to use just the necessary parts from FFMPEG and ONNX Runtime, idk if I'll do any UI, might keep it CLI.

I've been thinking about making it accelerator agnostic (GPU, if doesn't exist, fall back onto GPU) but I want to make it at least run first. Theoretically the CPU inference is 12.9ms while the GPU inference is 0.31ms. The thing is (I haven't done the math on this) sending information between the hardware might not be optimal unless I do batch processing which probably requires more engineering I'm lazy to do, this should already be fast enough.
Other optimizations might come if they're necessary, will update this README.

Might train bigger models as well and/or train the same size (smallest) on more data. Might make it optional later on for people which one they want to use, dunno yet.

By the way I have no clue what I'm doing but I'm learning along the way. No clue about best practices, no clue about how to write documentation, I'm just rawdogging this shit.
