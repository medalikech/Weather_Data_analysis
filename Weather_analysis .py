import pandas as pd

data = pd.read_csv(r"C:\Users\moham\Documents\WeatherData.csv")
print(data.head())
print(data.shape)
print(data.index)
print(data.columns)
print(data.dtypes)

print(data["Weather"].unique())
print(data.nunique())
data.count()
data["Weather"].value_counts()
print(data.info())
#Q1:find the "wind speed" unique values
print(data["Wind Speed_km/h"].nunique())
print("Q1 is :",data["Wind Speed_km/h"].unique())
#Q2:find the number of times when the weather is exactly Clear
print(data[data["Weather"] == "Clear"])
print("Q2 is :",data.groupby("Weather").get_group("Clear").count())
#Q3:find the number of times when the wind speed was exactly 4 km/h
print(data[data["Wind Speed_km/h"] == 4])
print("Q3 is :",data.groupby("Wind Speed_km/h").get_group(4).count())
#Q4:find out all the null values in the dataset
print(data.isnull().sum())
#Q5:rename the column name "Weather" to "Weather Condition"
data.rename(columns={"Weather": "Weather Condition"}, inplace=True)
print("Q5 is :",data.columns)
#Q6:find the number of times when the weather is exactly Clear and wind speed is 4 km/h
print(data[(data["Weather Condition"] == "Clear") & (data["Wind Speed_km/h"] == 4)])
print("Q6 is :",data[(data["Weather Condition"] == "Clear") & (data["Wind Speed_km/h"] == 4)].count())
#Q7:find the mean "Visibility" 
print("Q7 is :",data["Visibility_km"].mean())
#Q8:find the standard deviation of "Pressure"
print("Q8 is :",data["Press_kPa"].std())
#Q9:find the variance of relative humidity
print("Q9 is :",data["Rel Hum_%"].var())
#Q10:find all instance when snow was recorded
print(data[data["Weather Condition"].str.contains("Snow")])
print("Q10 is :",data[data["Weather Condition"].str.contains("Snow")].count())
#Q11:find all instance when the wind speed is above 24 and visibility is 25
print(data[(data["Wind Speed_km/h"] > 24) & (data["Visibility_km"] == 25)])
print("Q11 is :",data[(data["Wind Speed_km/h"] > 24) & (data["Visibility_km"] == 25)].count())
#Q12: show all the records where weather is fog
print(data[data["Weather Condition"].str.contains("Fog")])
print("Q12 is :",data[data["Weather Condition"].str.contains("Fog")].count())
 #Q13: find all the instance when the weather is clear and visibility is above 40
print(data[(data["Weather Condition"] == "Clear") & (data["Visibility_km"] > 40)])
print("Q13 is :",data[(data["Weather Condition"] == "Clear") & (data["Visibility_km"] > 40)].count())
#Q14: find all the instance where A. weather is clear and relative humidity is above 50 or B. visibility greater than 40 
print(data[((data["Weather Condition"] == "Clear") & (data["Rel Hum_%"] > 50)) | (data["Visibility_km"] > 40)])
print("Q14 is :",data[((data["Weather Condition"] == "Clear") & (data["Rel Hum_%"] > 50)) | (data["Visibility_km"] > 40)].count())