
#This section lists all the features and target variable that will be used for training the machine learning models. 
#The features are based on the AQHI formula, which includes the concentrations of 3 pollutants (O3, NO2, PM2.5)

TARGET_VARIABLE = "AQHI_NextDay" #The target variable we want to predict is the AQHI index.

#ARIMA (p, d, q) order, chosen from the ACF/PACF analysis in notebooks/01_eda.ipynb.
#d=0 (stationary series), p=2 (PACF cuts off after ~2 lags), q=0 (ACF tails off slowly, no seasonality).
ARIMA_ORDER = (2, 0, 0)

