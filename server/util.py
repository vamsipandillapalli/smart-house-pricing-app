import json
import pickle
import numpy as np
__model = None
__data_columns = []
__locations = []
import numpy as np

def get_estimated_price(location, sqft, bhk, bath):
    location = location.strip().lower()
    try:
        loc_index = __data_columns.index(location)
    except ValueError:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    # Set 1 in the one-hot encoded location column
    if loc_index >= 0:
        x[loc_index] = 1

    # Predict and return rounded price
    predicted_price = __model.predict([x])[0]
    return round(predicted_price, 2)
def get_location_names():
      return __data_columns
def load_saved_artifacts():
    print("loading saved artifacts ...... start")
    global __data_columns
    global __locations
    global __model
    with open("./artifacts/columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
    with open("./artifacts/banglore_home_model.pickle",'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts ....done")



if __name__ =='__main__':
    load_saved_artifacts()
    #print(get_location_names())
    #print(get_estimated_price('1st Phase JP Nagar',1000,2,2),"lakhs")