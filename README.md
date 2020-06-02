Bangalore Apartments Price Prediction
============================

## Problem Statement

Buying a home, especially in a city like Bengalore, is a tricky choice. While the major factors are same for all major big cities, there are others to be considered for the Silicon Valley of India. With its help millennial crowd, vibrant culture, great climate and a slew of job opportunities, it is difficult to ascertain the price of a house in Bengaluru.

Now with the lingering impact of demonetization, the enforcement of the Real Estate (Regulation and Development) Act (RERA), and the lack of trust in property developers in the city, housing units sold across India in 2017 dropped by 7 percent. In fact, the property prices in Bengaluru fell by almost 5 percent in the second half of 2017, said a study published by property consultancy Knight Frank.


What are the things that a potential home buyer considers before purchasing a house? The location, the size of the property, vicinity to offices, school, parks, restaurants, hospitals or the stereotypical white picket fence? What about the most important factor - the price?

In this circumstances,  this project aims to build a model to predict the price of houses in Bengaluru.


## Data

The data has been collected from [Kaggle](https://www.kaggle.com/amitabhajoy/bengaluru-house-price-data) which was publish under CCO: Public Domain license.


This dataset contains 9 columns and each columns can be accessed by its name.

**Columns**

- area_type: describes the area
- availability: when ity can be possessed or when it is ready
- location: where the house is located in Bengaluru
- size: in BHK or Bedroom (1-10 or more)
- society: what kind of society it belongs to 
- total_sqft: size of the property in square feet
- bath: number of bathrooms
- balcony: number of balcony
- price: Value of the property in lakhs (100,000 = 1 lakhs)


## Data Exploration and Visualization

![alt text](https://github.com/raktim314/Bengalure_House_Price_Prediction/blob/master/figures/price_dist.png)


From the plot above we can see notice the followings:
- distributiojn of price is highly skewed.
- Most of the house price lies below 500,000 INR
- There are outliers in the dataset which can be seen from the virtical lines in the plot.

The Skewness and the Kurtosis of the price of the dataset is **8.064469** and **108.166513** respectively.

![alt text](https://github.com/raktim314/Bengalure_House_Price_Prediction/blob/master/figures/%20balcony.png)

- There are more houses which has 1 or 2 balcony, around 38% each.
- Around 4% of the record has missing balcony value in the dataset.


![alt text](https://github.com/raktim314/Bengalure_House_Price_Prediction/blob/master/figures/%20bath.png)

It can be seen in the graph that a large number of houses have 2 bathrooms though some houses are with 3, 4, 5 or 1 bathrooms.

![alt text](https://github.com/raktim314/Bengalure_House_Price_Prediction/blob/master/figures/%20size.png)

The size of the houses are in BHK, RK or in Bedrooms format. The plot shows that most of the house are 2BHK or 3BHK, around 70% combined.

## Model Building

A baseline model using linear regression algorithm gives the accuracy of 84.5% on test set and average of 82.6% on cross validation score.


After applying grid search for parameter tuning on Linear Regression, Lasso and Decision Tree algorithms, we have got the following results:

| Model  |Best Score   |Best parameter  |
|---|---|---|
|Linear Regression |0.818354   | {'normalize': True} |
|Lasso |0.687477   |{'alpha': 2, 'selection': 'random'}   |
|Decision Tree |0.721503 |{'criterion': 'mse', 'splitter': 'best'} |


## Deployement

A local server has been built up to predict the house price using Flask framework. 



  








