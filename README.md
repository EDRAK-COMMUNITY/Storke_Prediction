# Stroke Prediction Using Machine Learning
This repository is the official implementation of our Stroke Prediction project.

In this project, we used two different models, Logistic Regression and XGBoost, to predict the occurrence of stroke based on various health parameters. The XGBoost model achieved higher accuracy.

## Data
The data used for training the models was obtained from two different datasets available on Kaggle. 

- The first one is [_The Stroke Prediction_](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)
- And the second one is [_The Synthetic Stroke Prediction_](https://www.kaggle.com/competitions/playground-series-s3e2/data)

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

[Demo on HuggingFace](https://huggingface.co/spaces/3zoozzn/Stroke_Prediction)

## Pre-trained Models
You can download our pre-trained models here:

- [Our Logistic model trained on the Kaggle datasets.](https://huggingface.co/3zoozzn/Stroke-Prediction/blob/main/logistic_model.pkl)
- [Our XGBoost model trained on the Kaggle datasets.](https://huggingface.co/3zoozzn/Stroke-Prediction/blob/main/xgb_model.pkl)

## Results
Our XGBoost model achieved higher accuracy in predicting stroke occurrence in Kaggle competetion:

| Model name | Accuracy |
|------------|----------|
| Logistic Regression | (0.88975) |
| XGBoost | (0.89516) |


## Contributing
### Authors
- [Abdulaziz Alzendani]()
- [Yazan Abualneaj]()
- [Aman Allah Alrawel]()

### Licen
[MIT]()
