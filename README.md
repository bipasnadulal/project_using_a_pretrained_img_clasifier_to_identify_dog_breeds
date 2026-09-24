# Image Classification for a City Dog Show 🐕

A Python project that uses **pretrained image-classification models** to identify whether images contain dogs and, for images identified as dogs, determine the dog's breed.

This project focuses on applying Python programming skills to an existing image-classification tool rather than building a classifier from scratch.

## Project Overview

A citywide dog show requires every participant to submit an image of their pet during registration. Since some participants may submit images of pets that aren't actually dogs, the registration system needs a way to verify the submitted images.

This project uses three provided CNN-based image classification architectures:

- **ResNet**
- **AlexNet**
- **VGG**

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

- ResNet
- AlexNet
- VGG

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

#  Main Program

The primary program modified for this project is:

```text
check_images.py
```
## Dataset and Labels

The project uses a collection of pet images stored in the pet_images directory.

The expected labels are generated from the image filenames.

For example, an image filename containing a dog breed provides the expected breed label used to evaluate the classifier's prediction.

The project also uses:

dognames.txt

to determine whether a classifier's predicted label represents a dog breed.

This allows predictions to be categorized as:

Dog
Not Dog
