🌦️ Weather Data Analytics Mini Project
📌 Project Overview

This mini project performs exploratory data analysis (EDA) on a weather dataset using Python and Pandas.

The goal of this project is to practice data analysis techniques such as:

Inspecting datasets

Filtering data

Grouping data

Calculating statistics

Handling missing values

Renaming columns

Applying conditional queries

🛠️ Technologies Used

Python

Pandas Library

📂 Dataset

The project uses a CSV file named:

WeatherData.csv

The dataset contains weather-related information such as:

Weather condition

Wind speed (km/h)

Visibility (km)

Pressure (kPa)

Relative humidity (%)

Temperature

And more

🔍 Analysis Performed

The following analysis tasks were completed:

✔️ Basic Dataset Inspection

Display first 5 rows

Check dataset shape

View index and column names

Check data types

Count unique values

Detect null values

✔️ Specific Queries

Find unique values of Wind Speed

Count how many times weather was exactly Clear

Count how many times wind speed was exactly 4 km/h

Find all null values

Rename column "Weather" → "Weather Condition"

Find records where:

Weather is Clear

Wind speed is 4 km/h

Calculate mean of Visibility

Calculate standard deviation of Pressure

Calculate variance of Relative Humidity

Find all instances where Snow was recorded

Find records where:

Wind speed > 24 km/h

Visibility = 25 km

Show all records where weather is Fog

Find records where:

Weather is Clear

Visibility > 40

Find records where:

(Weather is Clear AND Humidity > 50)

OR Visibility > 40

📊 Skills Demonstrated

Data filtering using conditions

Boolean indexing

GroupBy operations

String matching using .str.contains()

Statistical calculations (mean, std, var)

Column renaming

Data exploration techniques

🚀 How to Run the Project

Install Python (3.x recommended)

Install Pandas:

pip install pandas

Update the file path inside the script:

pd.read_csv("path_to_your_file/WeatherData.csv")

Run the script:

python your_script_name.py
🎯 Purpose of This Project

This project was created to strengthen foundational skills in:

Data Analysis

Pandas operations

Exploratory Data Analysis (EDA)

It serves as a beginner-friendly analytics project for learning and practice.

📎 Future Improvements

Add data visualizations (Matplotlib / Seaborn)

Perform deeper statistical analysis

Convert into a Jupyter Notebook with markdown explanations

Create summary dashboards

👨‍💻 Author

Kechrida Med ali
Python Data Analytics Mini Project
