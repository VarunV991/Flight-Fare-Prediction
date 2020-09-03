from flask import Flask, request, render_template
import sklearn
import pandas as pd
import numpy as np
import joblib

app = Flask(__name__)
model = joblib.load('model/flight_fare.pkl')

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route('/predict', methods = ["GET", "POST"])
def predict():
    if request.method == "POST":
        # Date_of_Journey
        date_dep = request.form["Dep_Time"]
        Journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)

         # Departure
        Dep_hour = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
        Dep_min = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)

        # Arrival
        date_arr = request.form["Arrival_Time"]
        Arrival_hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
        Arrival_min = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)

        # Duration
        dur_hour = abs(Arrival_hour - Dep_hour)
        dur_min = abs(Arrival_min - Dep_min)

         # Total Stops
        Total_stops = int(request.form["stops"])

        # Airline
        airline_arr = list()
        airline=request.form['airline']
        if(airline=='Air India'):
            airline_arr = airline_arr + [1,0,0,0,0,0,0,0,0,0,0]
        elif (airline=='GoAir'):
            airline_arr = airline_arr + [0,1,0,0,0,0,0,0,0,0,0]
        elif (airline=='IndiGo'):
            airline_arr = airline_arr + [0,0,1,0,0,0,0,0,0,0,0]
        elif (airline=='Jet Airways'):
            airline_arr = airline_arr + [0,0,0,1,0,0,0,0,0,0,0]
        elif (airline=='Jet Airways Business'):
            airline_arr = airline_arr + [0,0,0,0,1,0,0,0,0,0,0]
        elif (airline=='Multiple carriers'):
            airline_arr = airline_arr + [0,0,0,0,0,1,0,0,0,0,0]
        elif (airline=='Multiple carriers Premium economy'):
            airline_arr = airline_arr + [0,0,0,0,0,0,1,0,0,0,0]
        elif (airline=='SpiceJet'):
            airline_arr = airline_arr + [0,0,0,0,0,0,0,1,0,0,0]
        elif (airline=='Trujet'):
            airline_arr = airline_arr + [0,0,0,0,0,0,0,0,1,0,0]
        elif (airline=='Vistara'):
            airline_arr = airline_arr + [0,0,0,0,0,0,0,0,0,1,0]
        elif (airline=='Vistara_Premium_economy'):
            airline_arr = airline_arr + [0,0,0,0,0,0,0,0,0,0,1]
        ## Air Asia
        else:
            airline_arr = airline_arr + [0,0,0,0,0,0,0,0,0,0,0]

        #Source
        source_arr = list()
        source=request.form['source']
        if(source=='Chennai'):
            source_arr = source_arr + [1,0,0,0]
        elif (source=='Delhi'):
            source_arr = source_arr + [0,1,0,0]
        elif (source=='Kolkata'):
            source_arr = source_arr + [0,0,1,0]
        elif (source=='Mumbai'):
            source_arr = source_arr + [0,0,0,1]
        ## Bengaluru
        else:
            source_arr = source_arr + [0,0,0,0]

        #Destination
        dest_arr = list()
        dest=request.form['dest']
        if(dest=='Cochin'):
            dest_arr = dest_arr + [1,0,0,0,0]
        elif (dest=='Delhi'):
            dest_arr = dest_arr + [0,1,0,0,0]
        elif (dest=='Hydrerabad'):
            dest_arr = dest_arr + [0,0,1,0,0]
        elif (dest=='Kolkata'):
            dest_arr = dest_arr + [0,0,0,1,0]
        elif (dest=='New Delhi'):
            dest_arr = dest_arr + [0,0,0,0,1]
        ## Bengaluru
        else:
            dest_arr = dest_arr + [0,0,0,0,0]

        if(dur_hour<0 or dur_min<0 or (source==dest)):
            return render_template('result.html',prediction_text="Sorry, Invalid Input")

        final_arr = [Total_stops, Journey_day, Journey_month, Dep_hour, Dep_min, Arrival_hour, Arrival_min,dur_hour, dur_min] + airline_arr + source_arr + dest_arr
        data = np.array(final_arr)
        data = data.reshape(1, -1)
        #Prediction
        prediction=model.predict(data)
        output=round(prediction[0],2)
        
        #Output
        if(output<0):
            return render_template('result.html',prediction_text="Sorry, Invalid Fare Price")
        else:
            return render_template('result.html',prediction_text="Your Flight Fare is Rs. {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)