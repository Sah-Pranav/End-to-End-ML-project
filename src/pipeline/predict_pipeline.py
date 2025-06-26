import os
import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')

            print("Before Loading")
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            print("After Loading")

            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)

            return preds

        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(self,
                 date: str,
                 bedrooms: int,
                 bathrooms: float,
                 sqft_living: int,
                 sqft_lot: int,
                 floors: float,
                 waterfront: int,
                 view: int,
                 condition: int,
                 grade: int,
                 sqft_above: int,
                 sqft_basement: int,
                 yr_built: int,
                 yr_renovated: int,
                 lat: float,
                 long: float,
                 sqft_living15: int,
                 sqft_lot15: int):
        
        self.date = date
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.sqft_living = sqft_living
        self.sqft_lot = sqft_lot
        self.floors = floors
        self.waterfront = waterfront
        self.view = view
        self.condition = condition
        self.grade = grade
        self.sqft_above = sqft_above
        self.sqft_basement = sqft_basement
        self.yr_built = yr_built
        self.yr_renovated = yr_renovated
        self.lat = lat
        self.long = long
        self.sqft_living15 = sqft_living15
        self.sqft_lot15 = sqft_lot15

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "date": [self.date],
                "bedrooms": [self.bedrooms],
                "bathrooms": [self.bathrooms],
                "sqft_living": [self.sqft_living],
                "sqft_lot": [self.sqft_lot],
                "floors": [self.floors],
                "waterfront": [self.waterfront],
                "view": [self.view],
                "condition": [self.condition],
                "grade": [self.grade],
                "sqft_above": [self.sqft_above],
                "sqft_basement": [self.sqft_basement],
                "yr_built": [self.yr_built],
                "yr_renovated": [self.yr_renovated],
                "lat": [self.lat],
                "long": [self.long],
                "sqft_living15": [self.sqft_living15],
                "sqft_lot15": [self.sqft_lot15]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
