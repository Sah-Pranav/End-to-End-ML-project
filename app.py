from flask import Flask, request, render_template
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Predict route
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            # Validate and fetch each input
            date = request.form.get('date')
            if not date:
                return "Error: 'date' field is required.", 400

            bedrooms = request.form.get('bedrooms')
            if not bedrooms:
                return "Error: 'bedrooms' field is required.", 400
            bedrooms = int(bedrooms)

            bathrooms = request.form.get('bathrooms')
            if not bathrooms:
                return "Error: 'bathrooms' field is required.", 400
            bathrooms = float(bathrooms)

            sqft_living = request.form.get('sqft_living')
            if not sqft_living:
                return "Error: 'sqft_living' field is required.", 400
            sqft_living = int(sqft_living)

            sqft_lot = request.form.get('sqft_lot')
            if not sqft_lot:
                return "Error: 'sqft_lot' field is required.", 400
            sqft_lot = int(sqft_lot)

            floors = request.form.get('floors')
            if not floors:
                return "Error: 'floors' field is required.", 400
            floors = float(floors)

            waterfront = request.form.get('waterfront')
            if not waterfront:
                return "Error: 'waterfront' field is required.", 400
            waterfront = int(waterfront)

            view = request.form.get('view')
            if not view:
                return "Error: 'view' field is required.", 400
            view = int(view)

            condition = request.form.get('condition')
            if not condition:
                return "Error: 'condition' field is required.", 400
            condition = int(condition)

            grade = request.form.get('grade')
            if not grade:
                return "Error: 'grade' field is required.", 400
            grade = int(grade)

            sqft_above = request.form.get('sqft_above')
            if not sqft_above:
                return "Error: 'sqft_above' field is required.", 400
            sqft_above = int(sqft_above)

            sqft_basement = request.form.get('sqft_basement')
            if not sqft_basement:
                return "Error: 'sqft_basement' field is required.", 400
            sqft_basement = int(sqft_basement)

            yr_built = request.form.get('yr_built')
            if not yr_built:
                return "Error: 'yr_built' field is required.", 400
            yr_built = int(yr_built)

            yr_renovated = request.form.get('yr_renovated')
            if not yr_renovated:
                return "Error: 'yr_renovated' field is required.", 400
            yr_renovated = int(yr_renovated)

            lat = request.form.get('lat')
            if not lat:
                return "Error: 'lat' field is required.", 400
            lat = float(lat)

            long = request.form.get('long')
            if not long:
                return "Error: 'long' field is required.", 400
            long = float(long)

            sqft_living15 = request.form.get('sqft_living15')
            if not sqft_living15:
                return "Error: 'sqft_living15' field is required.", 400
            sqft_living15 = int(sqft_living15)

            sqft_lot15 = request.form.get('sqft_lot15')
            if not sqft_lot15:
                return "Error: 'sqft_lot15' field is required.", 400
            sqft_lot15 = int(sqft_lot15)

            # Create CustomData instance (without zipcode)
            data = CustomData(
                date=date,
                bedrooms=bedrooms,
                bathrooms=bathrooms,
                sqft_living=sqft_living,
                sqft_lot=sqft_lot,
                floors=floors,
                waterfront=waterfront,
                view=view,
                condition=condition,
                grade=grade,
                sqft_above=sqft_above,
                sqft_basement=sqft_basement,
                yr_built=yr_built,
                yr_renovated=yr_renovated,
                lat=lat,
                long=long,
                sqft_living15=sqft_living15,
                sqft_lot15=sqft_lot15
            )

            pred_df = data.get_data_as_data_frame()
            print(pred_df)

            
            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(pred_df)
            print(f"After Prediction result is: {results}")

            return render_template('home.html', results=round(results[0], 2))

        except Exception as e:
            return f"An error occurred: {str(e)}", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
