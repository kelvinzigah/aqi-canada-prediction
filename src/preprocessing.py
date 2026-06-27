import pandas as pd
import matplotlib.pyplot as plt

from statsmodels.graphics.tsaplots import (
    plot_acf,
    plot_pacf
)

#---------------------------------------------------------------
#Part A : Data Understanding
#----------------------------------------------------------------

# Load the datasets
df2019 = pd.read_csv("data/raw/Montreal - Trudeau Airport/2019/data_2019.csv")
df2020 = pd.read_csv("data/raw/Montreal - Trudeau Airport/2020/data_2020.csv")
df2021 = pd.read_csv("data/raw/Montreal - Trudeau Airport/2021/data_2021.csv")
df2022 = pd.read_csv("data/raw/Montreal - Trudeau Airport/2022/data_2022.csv")
df2023 = pd.read_csv("data/raw/Montreal - Trudeau Airport/2023/data_2023.csv")
df2024 = pd.read_csv("data/raw/Montreal - Trudeau Airport/2024/data_2024.csv")

# Combine them

df = pd.concat(

    [df2019, df2020, df2021, df2022, df2023, df2024],
    ignore_index=True
)

# Standardize inconsistent pollutant naming for 2019 dataset

df["Pollutant"] = df["Pollutant"].replace("PM2.5", "PM25")

# Display first rows of the combined dataset

print(df.head())

# Display dataset shape

print("Dataset shape:", df.shape)

# Display general information about the dataset
print(df.info())

# Display descriptive statistics of the dataset

print(df.describe())

#Check missing values in each column

print("Missing values:")

print(df.isnull().sum())

# Display the pollutants in the dataset

print("Pollutants:")

print(df["Pollutant"].unique())

# Count how many rows each pollutant has

print("Rows per pollutant:")

print(df["Pollutant"].value_counts())

# Missing Concentration values per pollutant

print("Missing Concentration values per pollutant:")

pollutants = df["Pollutant"].unique()

for pollutant in pollutants:

    pollutant_data = df[df["Pollutant"] == pollutant]

    missing_values = pollutant_data["Concentration"].isnull().sum()

    print(pollutant, ":", missing_values)

# Missing Concentration percentage per pollutant

print("Missing Concentration percentage per pollutant:")

for pollutant in pollutants:

    pollutant_data = df[df["Pollutant"] == pollutant]

    total_values = len(pollutant_data)

    missing_values = pollutant_data["Concentration"].isnull().sum()

    missing_percentage = (missing_values / total_values) * 100

    print(pollutant, ":", round(missing_percentage, 2), "%")
    
    #--------------------------------------------------------------
    #Part B : Data cleaning
    #--------------------------------------------------------------
    # Keep only pollutants used in AQHI calculation

df = df[
    (df["Pollutant"] == "NO2") |
    (df["Pollutant"] == "O3") |
    (df["Pollutant"] == "PM25") |
    (df["Pollutant"] == "CO")
]

print("Dataset shape after keeping AQHI pollutants:")

print(df.shape)

# Remove rows with missing concentration values

df = df.dropna(subset=["Concentration"])

print("Dataset shape after removing missing concentrations:")

print(df.shape)

# Check remaining missing values

print("Remaining missing values:")

print(df.isnull().sum())
# Remove Method_Code column

df = df.drop(columns=["Method_Code"])

print("Dataset shape after removing Method_Code:")

print(df.shape)

    #--------------------------------------------------------------
    #Part C : Data Transformation
    #--------------------------------------------------------------
 # Create DateTime attribute

df["DateTime"] = pd.to_datetime(

    df["Date_yyyy_mm_dd"] + " " + df["Start_Time_Local_Standard"]

)

# Sort data from oldest to newest

df = df.sort_values("DateTime")

print(df[["Date_yyyy_mm_dd",

          "Start_Time_Local_Standard",

          "DateTime"]].head())

# Convert from long format to wide format

df_pivot = df.pivot(

    index="DateTime",

    columns="Pollutant",

    values="Concentration"

)

# Convert index back into a normal column

df_pivot = df_pivot.reset_index()

# Sort from oldest to newest

df_pivot = df_pivot.sort_values("DateTime")

print(df_pivot.head())

print("Pivoted dataset shape:", df_pivot.shape)

    #--------------------------------------------------------------
    #Part D:feature Engineering
    #--------------------------------------------------------------
    
    #Unit check
print("Units by pollutant:")

print(
    df.groupby("Pollutant")["Units"].unique()
)

# Calculate AQHI
import numpy as np
# Create Date column

df_pivot["Date"] = df_pivot["DateTime"].dt.date

# Create Day column

df_pivot["Day"] = df_pivot["DateTime"].dt.day

# Create Month column

df_pivot["Month"] = df_pivot["DateTime"].dt.month

# Create Hour column

df_pivot["Hour"] = df_pivot["DateTime"].dt.hour

print(df_pivot[["DateTime", "Date", "Day", "Month", "Hour"]].head())

# Create 3-hour block

df_pivot["ThreeHourBlock"] = df_pivot["Hour"] // 3

# Calculate 3-hour averages for the pollutants

df_3hour = df_pivot.groupby(

    ["Date", "Day", "Month", "ThreeHourBlock"]

)[["CO","NO2", "O3", "PM25"]].mean()

df_3hour = df_3hour.reset_index()

print(df_3hour.head())

print("3-hour dataset shape:", df_3hour.shape)

# Calculate AQHI using 3-hour averages

df_3hour["AQHI"] = (

    (10 / 10.4)

    * 100

    * (

        (np.exp(0.000871 * df_3hour["NO2"]) - 1)

        + (np.exp(0.000537 * df_3hour["O3"]) - 1)

        + (np.exp(0.000487 * df_3hour["PM25"]) - 1)

    )

)

print(df_3hour[["Date", "ThreeHourBlock", "NO2", "O3", "PM25", "AQHI"]].head())

# Create daily dataset

df_daily = df_3hour.groupby(

    ["Date", "Day", "Month"]

)[["CO","NO2", "O3", "PM25", "AQHI"]].mean()

df_daily = df_daily.reset_index()

#create previous day's AQHI as a feature
df_daily["AQHI_PreviousDay"] = df_daily["AQHI"].shift(1)

# Create next day's AQHI (target variable)

df_daily["AQHI_NextDay"] = df_daily["AQHI"].shift(-1)


print(

    df_daily[

        [

            "Date",

            "AQHI",
            "AQHI_PreviousDay",

            "AQHI_NextDay"

        ]

    ].head(10)

)





# Create Season feature

df_daily["Season"] = ""

# Winter
df_daily.loc[df_daily["Month"] == 12, "Season"] = "Winter"
df_daily.loc[df_daily["Month"] == 1, "Season"] = "Winter"
df_daily.loc[df_daily["Month"] == 2, "Season"] = "Winter"

# Spring
df_daily.loc[df_daily["Month"] == 3, "Season"] = "Spring"
df_daily.loc[df_daily["Month"] == 4, "Season"] = "Spring"
df_daily.loc[df_daily["Month"] == 5, "Season"] = "Spring"

# Summer
df_daily.loc[df_daily["Month"] == 6, "Season"] = "Summer"
df_daily.loc[df_daily["Month"] == 7, "Season"] = "Summer"
df_daily.loc[df_daily["Month"] == 8, "Season"] = "Summer"

# Fall
df_daily.loc[df_daily["Month"] == 9, "Season"] = "Fall"
df_daily.loc[df_daily["Month"] == 10, "Season"] = "Fall"
df_daily.loc[df_daily["Month"] == 11, "Season"] = "Fall"

print(df_daily[["Date", "Month", "Season"]].head(15))

# Convert Season to numeric values

df_daily["Season_Code"] = -1

df_daily.loc[df_daily["Season"] == "Winter", "Season_Code"] = 0
df_daily.loc[df_daily["Season"] == "Spring", "Season_Code"] = 1
df_daily.loc[df_daily["Season"] == "Summer", "Season_Code"] = 2
df_daily.loc[df_daily["Season"] == "Fall", "Season_Code"] = 3

df_daily["Season_Code"] = df_daily["Season_Code"].astype(int)

print(df_daily[["Month", "Season", "Season_Code"]].head())

print(df_daily.head())

print("Daily dataset shape:", df_daily.shape)



  #--------------------------------------------------------------
# Part E: Data Preparation for Modeling
#--------------------------------------------------------------

# Check missing values before removing rows
print("Missing values before removing rows:")
print(df_daily.isnull().sum())

# Show dates with missing AQHI

print("Dates with missing AQHI:")

print(

    df_daily[df_daily["AQHI"].isnull()][

        ["Date", "NO2", "O3", "PM25", "AQHI"]

    ]

)

print("Dates with missing NO2:")

print(
    df_daily[df_daily["NO2"].isnull()][
        ["Date", "NO2", "O3", "PM25", "AQHI"]
    ]
)

print("Dates with missing PM25:")

print(
    df_daily[df_daily["PM25"].isnull()][
        ["Date", "NO2", "O3", "PM25", "AQHI"]
    ]
)

# Remove rows where AQHI could not be calculated

df_daily = df_daily[df_daily["AQHI"].notna()]

print("Dataset shape after removing rows with missing AQHI:")
print(df_daily.shape)


# Remove only rows where the target variable is missing
df_daily = df_daily[df_daily["AQHI_NextDay"].notna()]

# Remove rows with missing preious day's AQHI values
df_daily = df_daily[df_daily["AQHI_PreviousDay"].notna()]

ordered_columns = (
    [
        "Date",
        "Day",
        "Month",
        "CO",
        "NO2",
        "O3",
        "PM25",
        "Season",
        "Season_Code"
    ]
    
    + [
        "AQHI_PreviousDay",
        "AQHI",
        
        "AQHI_NextDay"
    ]
)

df_daily = df_daily[ordered_columns]

# Fill missing CO values with the median CO value
df_daily["CO"] = df_daily["CO"].fillna(df_daily["CO"].median())

# Check missing values after removing missing target
print("Missing values after removing missing target:")
print(df_daily.isnull().sum())



print(df_daily.head())

# Features and target variable
X = df_daily[

    [

        "Day",

        "Month",

        "CO",

        "Season_Code",

        "NO2",

        "O3",

        "PM25",

    
    "AQHI_PreviousDay",

    "AQHI"

]
]
y = df_daily["AQHI_NextDay"]

print("Feature matrix shape:", X.shape)
print("Label vector shape:", y.shape)

# Save processed dataset

df_daily.to_csv(
    "data/processed/air_quality_project_dataset.csv",
    index=False
)

print("CSV saved successfully!")

#AQHI over time plot
plt.figure(figsize=(12,5))
plt.plot(df_daily["Date"], df_daily["AQHI"])
plt.title("AQHI Over Time")
plt.xlabel("Year")
plt.ylabel("AQHI")
plt.show()

#NO2 over time plot
plt.figure(figsize=(12,5))
plt.plot(df_daily["Date"], df_daily["NO2"])
plt.title("NO2 Over Time")
plt.xlabel("Year")
plt.ylabel("NO2")
plt.show()

#PM25 over time plot
plt.figure(figsize=(12,5))
plt.plot(df_daily["Date"], df_daily["PM25"])
plt.title("PM25 Over Time")
plt.xlabel("Year")
plt.ylabel("PM25")
plt.show()

#O3 over time plot
plt.figure(figsize=(12,5))
plt.plot(df_daily["Date"], df_daily["O3"])
plt.title("O3 Over Time")
plt.xlabel("Year")
plt.ylabel("O3")
plt.show()

#AHI Histogram
plt.hist(df_daily["AQHI"], bins=30)
plt.title("AQHI Distribution")
plt.xlabel("AQHI")
plt.ylabel("Frequency")
plt.show()