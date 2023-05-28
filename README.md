# Stroke Prediction Using Machine Learning
This repository is the official implementation of our Stroke Prediction project.

In this project, we used two different models, Logistic Regression and XGBoost, to predict the occurrence of stroke based on various health parameters. The XGBoost model achieved higher accuracy.

## Data
The data used for training the models was obtained from two different datasets available on Kaggle. 

(Provide links or instructions on how to access the datasets)

## Requirements

This project requires Python 3.6 or later. The dependencies for the project are listed in the `requirements.txt` file.

### Using pip

You can install the requirements via pip using the following command:

``` pip install -r requirements.txt ```

### Using Conda
If you are using Conda, you can create a new environment for this project and install the requirements using the following commands:
``` 
conda create -n stroke_prediction python=3.8
conda activate stroke_prediction
pip install -r requirements.txt
```

This will create a new Conda environment called "stroke_prediction" and install the necessary packages within that environment.


## Project Structure
The entire project is contained within a single Jupyter notebook: `main.ipynb`. This notebook includes all the steps from data loading, preprocessing, model training, evaluation, and results visualization.

## Demo
We have a live demo of the model hosted on Hugging Face using Gradio. You can interact with the model and make predictions in real-time.

(Provide the link to the demo and any necessary instructions on how to use it)

## Pre-trained Models
You can download pretrained models here:

Our XGBoost model trained on the Kaggle datasets.

(Give a link to where/how the pretrained models can be downloaded and how they were trained.)

## Results
Our XGBoost model achieved higher accuracy in predicting stroke occurrence:

| Model name | Accuracy |
|------------|----------|
| Logistic Regression | (insert accuracy) |
| XGBoost | (insert accuracy) |

(Include a table of results from your project, and link back to the leaderboard for clarity and context. If your main result is a figure, include that figure and link to the command or notebook to reproduce it.)

## Contributing
(Pick a license and describe how to contribute to your code repository.)

Footer
© 2023 My Name, Inc.
****
