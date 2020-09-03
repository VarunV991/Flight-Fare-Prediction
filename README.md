# Flight Fare Prediction

![Python 3.7](https://img.shields.io/badge/Pyhton-3.7-blue) ![Flask](https://img.shields.io/badge/Flask-1.1-orange) ![Heroku](https://img.shields.io/badge/Heroku-Deployment-brightgreen)

## Objective

The objective of this project is to calculate the <strong>fare of a flight journey</strong> based on various parameters such as source,destination,no. of stops, etc.

## Live Demo

<a href="https://flight-fareprediction.herokuapp.com/">Flight Fare Predicition</a>

  ### Glimpse of the Web App
  <br>

  ![GIF](flightfarepred.gif)

## Installation
The Code is written in Python 3.7. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```

## Directory Tree 
```
├── data
├── static 
│   ├── style.css
├── templates
│   ├── index.html
│   ├── result.html
├── Flight_Fare_Prediction.ipynb
├── Procfile
├── README.md
├── app.py
├── flightfarepred.gif
├── requirements.txt
```

## Dataset

The dataset is taken from kaggle. This dataset is given by MachineHack and contains various attributes which descibe a flight journey. The dataset link is given <a href="https://www.kaggle.com/nikhilmittal/flight-fare-prediction-mh">here</a>.

## Code

The code for the model, algorithms used and accuracy of the model can be found <a href="https://github.com/VarunV991/Flight-Fare-Prediction/blob/master/Flight_Fare_Prediction.ipynb">here</a>.
The trained model is available <a href="https://drive.google.com/file/d/1rF5g8wPw-V2kbFKcTRdSFIbv18DWC8i-/view?usp=sharing">here</a>.

## Web App and Deployment

This project uses Flask for the web app and its deployment is done on Heroku.

#### Other Info
This project is a modified version of an older project on the same topic.The original project is available <a href="https://github.com/Mandal-21/Flight-Price-Prediction">here</a>.
