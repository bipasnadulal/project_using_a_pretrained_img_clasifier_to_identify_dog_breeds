# Image Classification for a City Dog Show 🐕

A Python project that uses **pretrained image-classification models** to identify whether images contain dogs and, for images identified as dogs, determine the dog's breed.

This project focuses on applying Python programming skills to an existing image-classification tool rather than building a classifier from scratch.

## Project Overview

A citywide dog show requires every participant to submit an image of their pet during registration. Since some participants may submit images of pets that aren't actually dogs, the registration system needs a way to verify the submitted images.

This project uses three provided CNN-based image classification architectures:

* **ResNet**
* **AlexNet**
* **VGG**

The classifiers are applied to the same collection of pet images, and their results are analyzed based on:

1. How accurately they distinguish **dogs from non-dogs**.
2. How accurately they identify the **breed of dogs**.
3. How long each model takes to process the images.

The project therefore explores the trade-off between **classification accuracy and computational runtime**.

---

## Project Objectives

The project has four main objectives:

### 1. Identify Dogs vs. Non-Dogs

Determine whether each submitted pet image contains a dog.

A prediction is considered successful for this objective even when the classifier incorrectly identifies the dog's breed, as long as it correctly determines that the image contains a dog.

### 2. Identify Dog Breeds

For images that contain dogs, determine whether the classifier correctly identifies the dog's breed.

### 3. Compare CNN Architectures

Compare the performance of:

* ResNet
* AlexNet
* VGG

The models are evaluated based on their ability to achieve the first two objectives.

### 4. Consider Runtime

Measure how long each classification algorithm takes to process the images.

The project considers the practical trade-off between:

> **Accuracy ↔ Runtime ↔ Computational Resources**

A model that provides slightly lower accuracy may still be a reasonable alternative if it requires significantly less time and computational resources.

---

## How the Project Works

The project uses an existing Python image classifier. The classifier takes an image as input and returns a prediction describing what the image contains.

The implementation builds a pipeline around this classifier:

```text
Pet Images
    │
    ▼
Create Expected Image Labels
    │
    ▼
Run Pretrained CNN Classifier
    │
    ▼
Create Classifier Labels
    │
    ▼
Compare Expected vs. Predicted Labels
    │
    ▼
Determine Dog / Not-Dog
    │
    ▼
Evaluate Dog Breed Classification
    │
    ▼
Calculate Accuracy + Runtime
    │
    ▼
Compare ResNet / AlexNet / VGG
```

---

## Main Program

The primary program modified for this project is:

```text
check_images.py
```

The `check_images.py` program contains the main workflow and functions required to perform the classification analysis.

The project involves implementing the undefined functions marked with `TODO` comments.


## Dataset and Labels

The project uses a collection of pet images stored in the `pet_images` directory.

The expected labels are generated from the **image filenames**.

For example, an image filename containing a dog breed provides the expected breed label used to evaluate the classifier's prediction.

The project also uses:

```text
dognames.txt
```

to determine whether a classifier's predicted label represents a dog breed.

This allows predictions to be categorized as:

```text
Dog
Not Dog
```

---

## Classification Process

### Step 1 — Measure Runtime

The Python `time` module is used to measure how long the classification process takes.

The runtime is recorded so that the three CNN architectures can be compared not only by accuracy but also by computational cost.

### Step 2 — Get Program Inputs

Command-line arguments are used to provide inputs to the program.

This allows the classifier and image directory to be specified when running the program.

### Step 3 — Create Pet Image Labels

The filenames in the pet image directory are processed to create the expected labels.

These labels are stored in a data structure such as a dictionary.

### Step 4 — Run the Image Classifier

The provided classifier function is used to classify each image.

The classifier's predictions are stored alongside the expected labels.

### Step 5 — Compare Labels

The expected pet-image label and classifier label are compared.

This makes it possible to determine whether the classifier correctly identified the image.

### Step 6 — Determine Dog / Not-Dog

The classifier labels are compared against the list of dog breeds contained in `dognames.txt`.

This allows every image to be classified as either:

* Dog
* Not Dog

### Step 7 — Calculate Results

The collected labels and classifications are used to calculate the performance of the image-classification algorithm.

The analysis considers:

* Number of correctly classified dogs
* Number of incorrectly classified dogs
* Number of correctly classified non-dogs
* Number of incorrectly classified non-dogs
* Correct dog-breed classifications
* Overall classification performance
* Program runtime

### Step 8 — Print Results

The calculated results are printed so that the performance of each CNN architecture can be analyzed.

The process is repeated for:

```text
ResNet
AlexNet
VGG
```

---

## Models Compared

### ResNet

ResNet is one of the CNN architectures provided for the project. Its predictions are evaluated for both dog detection and breed classification, along with its runtime.

### AlexNet

AlexNet is another provided CNN architecture used to classify the same images and evaluate accuracy and runtime.

### VGG

VGG is the third CNN architecture used in the comparison.

The same evaluation process is applied to VGG as to ResNet and AlexNet.

---

## Evaluation

The project evaluates each architecture using two primary classification tasks.

### Dog Identification

The classifier should correctly identify:

```text
Dog → Dog
Not Dog → Not Dog
```

A dog image can still count as correctly identified as a dog even if the predicted breed is incorrect.

### Breed Identification

For images that are actually dogs, the predicted breed is compared with the expected breed.

```text
Expected Breed
       │
       ▼
Classifier Prediction
       │
       ▼
Correct / Incorrect
```

### Runtime

The execution time of each classifier is measured to understand the computational cost of the approach.

---

## Accuracy vs. Runtime

One of the important aspects of this project is that classification performance isn't considered independently from runtime.

For example:

```text
Model A
Higher accuracy
+
Longer runtime

Model B
Lower accuracy
+
Shorter runtime
```

Depending on the requirements of the application, Model B could potentially provide a sufficiently accurate result while requiring fewer computational resources.

The project therefore compares both **classification performance and execution time** when analyzing the three architectures.

---

## Running the Project

The project uses command-line arguments to provide the required inputs.

A typical execution follows the structure:

```bash
python check_images.py --dir <image_directory> --arch <architecture>
```

For example:

```bash
python check_images.py --dir pet_images --arch resnet
```

The architecture can then be changed to evaluate the other provided models.

```bash
python check_images.py --dir pet_images --arch alexnet
```

```bash
python check_images.py --dir pet_images --arch vgg
```

> Use the exact argument names and values supported by the version of `check_images.py` in the project workspace.

---

## What I Learned

This project provided practical experience with:

* Python functions
* Command-line arguments
* Dictionaries and complex data structures
* File and directory processing
* String manipulation
* Working with existing Python modules
* Using an existing machine-learning classifier
* Comparing expected and predicted labels
* Classification evaluation
* Measuring program runtime
* Analyzing accuracy vs. computational cost
* Working with CNN-based image classifiers

Most importantly, the project demonstrates that machine-learning systems can be used effectively by building the **Python application logic around an existing trained model**, without necessarily creating and training the model itself.

---

## Possible Improvements

The project could be extended by:

* Creating a simple web interface for image uploads.
* Returning the predicted breed and confidence score.
* Adding visualizations for model comparison.
* Recording results in CSV or JSON format.
* Building an API around the classifier.
* Deploying the classifier as a small computer-vision application.
* Testing the models on additional dog breeds and non-dog images.

---


## Project Documentation

The original project specification is included in the repository as:

```text
Image Classification for a City Dog Show.docx
```

It describes the project scenario, objectives, required tasks, and implementation workflow.
