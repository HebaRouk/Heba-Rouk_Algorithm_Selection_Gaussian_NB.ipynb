# -*- coding: utf-8 -*-
"""Heba Rouk_Algorithm_Selection_Gaussian_NB.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Hp1JwS4Z1QyBknKGCAlClcKH7hXFklRZ

# Challenge of the Week: Gaussian Naive Bayes Classifier
---
© 2024, Zaka AI, Inc. All Rights Reserved.

##**Case Study:** Iris Dataset

**Objective:** The objective of this challenge is to make you know about Naive Bayes applied on Numerical Values.

**DataSet Columns:**<br>
*	 Petal Height
*  Petal Width
*  Sepal Height
*  Sepal Width
*  Target: The kind of the Iris flower (Virginica, Setosa, Versicolor)

# Importing Libraries

Start by importing the necessary libraries. For this problem we need the following:


*   Numpy: for numerical calculations
*   Pandas: to deal with the dataset
*   math: to work on the mathematical aspects of Naive Bayes
"""

from google.colab import files
uploaded = files.upload()

# Importing necessary libraries
import numpy as np   # For numerical calculations
import pandas as pd  # To handle datasets
import math          # For mathematical computations in Naive Bayes

"""# Loading the Dataset

Load the dataset in your environment. One thing to note is that the dataset you have does not include names for different columns. This is why you should name the columns by hand as ['Sepal Height', 'Sepal Width', 'Petal Height', 'Petal Width', 'Target']. Then don't forget to show the head of your dataset to get a better insight into it.
"""

import os
import pandas as pd

# Define column names
column_names = ['Sepal Height', 'Sepal Width', 'Petal Height', 'Petal Width', 'Target']

# Check the current working directory
print("Current working directory:", os.getcwd())

# List all files in the current directory
print("Files in the directory:", os.listdir())

# Attempt to load the dataset
try:
    df = pd.read_csv('iris(1).csv', header=None, names=column_names)
    print("Dataset loaded successfully!")
    # Display the first few rows of the dataset
    print("First five rows of the dataset:")
    print(df.head())
except FileNotFoundError:
    print("Error: The file 'iris(1).csv' was not found. Ensure it is in the current directory.")

"""##Data Preprocessing

You may have noticed that the Target Column contains string values rather than numbers. This is why, you will Change the string values to numerical.
"""

import os
import pandas as pd

# Define column names
column_names = ['Sepal Height', 'Sepal Width', 'Petal Height', 'Petal Width', 'Target']

# Check the current working directory
print("Current working directory:", os.getcwd())

# List all files in the current directory
print("Files in the directory:", os.listdir())

# Load the dataset
try:
    df = pd.read_csv('iris(1).csv', header=None, names=column_names)
    print("Dataset loaded successfully!")

    # Display the first few rows of the dataset
    print("First five rows of the dataset:")
    print(df.head())

    # Mapping string values in the Target column to numerical values
    target_mapping = {'Setosa': 0, 'Versicolor': 1, 'Virginica': 2}
    df['Target'] = df['Target'].map(target_mapping)

    # Verifying the changes
    print("\nUpdated Target column:")
    print(df.head())
except FileNotFoundError:
    print("Error: The file 'iris(1).csv' was not found. Ensure it is in the current directory.")

"""Make sure we have no null values, and if we have, remove them."""

import os
import pandas as pd

# Define column names
column_names = ['Sepal Height', 'Sepal Width', 'Petal Height', 'Petal Width', 'Target']

# Check the current working directory
print("Current working directory:", os.getcwd())

# List all files in the current directory
print("Files in the directory:", os.listdir())

# Load the dataset
try:
    df = pd.read_csv('iris(1).csv', header=None, names=column_names)
    print("Dataset loaded successfully!")

    # Display the first few rows of the dataset
    print("First five rows of the dataset:")
    print(df.head())

    # Check for null values
    print("\nChecking for null values:")
    print(df.isnull().sum())

    # Remove rows with null values if any
    if df.isnull().values.any():
        print("\nNull values detected! Removing rows with null values...")
        df = df.dropna()
        print("Rows with null values removed.")
    else:
        print("No null values found in the dataset.")

    # Mapping string values in the Target column to numerical values
    target_mapping = {'Setosa': 0, 'Versicolor': 1, 'Virginica': 2}
    df['Target'] = df['Target'].map(target_mapping)

    # Verifying the changes
    print("\nUpdated Target column:")
    print(df.head())
except FileNotFoundError:
    print("Error: The file 'iris(1).csv' was not found. Ensure it is in the current directory.")

"""#Naive Bayes

##Finding different Classes

First, find how many classes we have in our dataset (although it should always appear in the description of your dataset)
"""

import os
import pandas as pd

# Define column names
column_names = ['Sepal Height', 'Sepal Width', 'Petal Height', 'Petal Width', 'Target']

# Check the current working directory
print("Current working directory:", os.getcwd())

# List all files in the current directory
print("Files in the directory:", os.listdir())

# Load the dataset
try:
    df = pd.read_csv('iris(1).csv', header=None, names=column_names)
    print("Dataset loaded successfully!")

    # Display the first few rows of the dataset
    print("First five rows of the dataset:")
    print(df.head())

    # Mapping string values in the Target column to numerical values
    target_mapping = {'Setosa': 0, 'Versicolor': 1, 'Virginica': 2}
    df['Target'] = df['Target'].map(target_mapping)

    # Find and display unique classes in the 'Target' column
    unique_classes = df['Target'].unique()
    print(f"Unique classes in the dataset: {unique_classes}")
    print(f"Number of classes: {len(unique_classes)}")

except FileNotFoundError:
    print("Error: The file 'iris(1).csv' was not found. Ensure it is in the current directory.")

"""SO we have 3 classes of flowers.

Remember the basic formula that we used for Naive Bayes. <br>
<img src="https://equatio-api.texthelp.com/svg/%5C%20P(%5Ctextcolor%7B%232B7FBB%7D%7BClass%7D%7C%5Ctextcolor%7B%23E94D40%7D%7BFeatures%7D)%3D%5Cfrac%7BP(%5Ctextcolor%7B%23E94D40%7D%7BFeatures%7D%7C%5Ctextcolor%7B%232B7FBB%7D%7BClass%7D)%5Ccdot%20P%5Cleft(%5Ctextcolor%7B%232B7FBB%7D%7BClass%7D%5Cright)%7D%7BP(%5Ctextcolor%7B%23E94D40%7D%7BFeatures%7D)%7D" alt="P of open paren C l a. s s divides F of e a. t u r e s close paren equals the fraction with numerator P of open paren F of e a. t u r e s divides C l a. s s close paren times P of open paren C l a. s s close paren and denominator P of F of e a. t u r e s">

Since we have 3 classes, and 4 features, we need to calculate the following probabilities.<br>
<img src="https://equatio-api.texthelp.com/svg/P(%5Ctextcolor%7B%232B7FBB%7D%7BClass_0%7D%7C%5Ctextcolor%7B%23E94D40%7D%7BF1%2CF2%2CF3%2CF4%7D)" alt="P of open paren C l a. s s sub 0 divides F of 1 comma F of 2 comma F of 3 comma F of 4 close paren"> <br>
<img src="https://equatio-api.texthelp.com/svg/P(%5Ctextcolor%7B%232B7FBB%7D%7BClass_1%7D%7C%5Ctextcolor%7B%23E94D40%7D%7BF1%2CF2%2CF3%2CF4%7D)" alt="P of open paren C l a. s s sub 1 divides F of 1 comma F of 2 comma F of 3 comma F of 4 close paren"> <br>
<img src="https://equatio-api.texthelp.com/svg/P(%5Ctextcolor%7B%232B7FBB%7D%7BClass_2%7D%7C%5Ctextcolor%7B%23E94D40%7D%7BF1%2CF2%2CF3%2CF4%7D)" alt="P of open paren C l a. s s sub 2 divides F of 1 comma F of 2 comma F of 3 comma F of 4 close paren">

So in reality we need to calculate the following:

<img src="https://equatio-api.texthelp.com/svg/P_0%3DP(%5Ctextcolor%7B%232B7FBB%7D%7B%5Ctextcolor%7B%23E94D40%7D%7BF_1%7D%7D%7C%5Ctextcolor%7B%23E94D40%7D%7B%5Ctextcolor%7B%232B7FBB%7D%7BClass_0%7D%7D)P(%5Ctextcolor%7B%232B7FBB%7D%7B%5Ctextcolor%7B%23E94D40%7D%7BF_2%7D%7D%7C%5Ctextcolor%7B%23E94D40%7D%7B%5Ctextcolor%7B%232B7FBB%7D%7BClass_0%7D%7D)P(%5Ctextcolor%7B%232B7FBB%7D%7B%5Ctextcolor%7B%23E94D40%7D%7BF_3%7D%7D%7C%5Ctextcolor%7B%23E94D40%7D%7B%5Ctextcolor%7B%232B7FBB%7D%7BClass_0%7D%7D)P(%5Ctextcolor%7B%232B7FBB%7D%7B%5Ctextcolor%7B%23E94D40%7D%7BF_4%7D%7D%7C%5Ctextcolor%7B%23E94D40%7D%7B%5Ctextcolor%7B%232B7FBB%7D%7BClass_0%7D%7D)" alt="P sub 0 equals P of open paren F sub 1 divides C l a. s s sub 0 close paren P of open paren F sub 2 divides C l a. s s sub 0 close paren P of open paren F sub 3 divides C l a. s s sub 0 close paren P of open paren F sub 4 divides C l a. s s sub 0 close paren"><img src="https://equatio-api.texthelp.com/svg/P%5Cleft(%5Ctextcolor%7B%232B7FBB%7D%7BClass_0%7D%5Cright)" alt="P of open paren C l a. s s sub 0 close paren"><br><img src="https://equatio-api.texthelp.com/svg/P_1%3DP(%5Ctextcolor%7B%232B7FBB%7D%7B%5Ctextcolor%7B%23E94D40%7D%7BF_1%7D%7D%7C%5Ctextcolor%7B%23E94D40%7D%7B%5Ctextcolor%7B%232B7FBB%7D%7BClass_1%7D%7D)P(%5Ctextcolor%7B%232B7FBB%7D%7B%5Ctextcolor%7B%23E94D40%7D%7BF_2%7D%7D%7C%5Ctextcolor%7B%23E94D40%7D%7B%5Ctextcolor%7B%232B7FBB%7D%7BClass_1%7D%7D)P(%5Ctextcolor%7B%232B7FBB%7D%7B%5Ctextcolor%7B%23E94D40%7D%7BF_3%7D%7D%7C%5Ctextcolor%7B%23E94D40%7D%7B%5Ctextcolor%7B%232B7FBB%7D%7BClass_1%7D%7D)P(%5Ctextcolor%7B%232B7FBB%7D%7B%5Ctextcolor%7B%23E94D40%7D%7BF_4%7D%7D%7C%5Ctextcolor%7B%23E94D40%7D%7B%5Ctextcolor%7B%232B7FBB%7D%7BClass_1%7D%7D)" alt="P sub 1 equals P of open paren F sub 1 divides C l a. s s sub 1 close paren P of open paren F sub 2 divides C l a. s s sub 1 close paren P of open paren F sub 3 divides C l a. s s sub 1 close paren P of open paren F sub 4 divides C l a. s s sub 1 close paren"><img src="https://equatio-api.texthelp.com/svg/P%5Cleft(%5Ctextcolor%7B%232B7FBB%7D%7BClass_1%7D%5Cright)" alt="P of open paren C l a. s s sub 1 close paren"><br>
<img src="https://equatio-api.texthelp.com/svg/P_2%3DP(%5Ctextcolor%7B%232B7FBB%7D%7B%5Ctextcolor%7B%23E94D40%7D%7BF_1%7D%7D%7C%5Ctextcolor%7B%23E94D40%7D%7B%5Ctextcolor%7B%232B7FBB%7D%7BClass_2%7D%7D)P(%5Ctextcolor%7B%232B7FBB%7D%7B%5Ctextcolor%7B%23E94D40%7D%7BF_2%7D%7D%7C%5Ctextcolor%7B%23E94D40%7D%7B%5Ctextcolor%7B%232B7FBB%7D%7BClass_2%7D%7D)P(%5Ctextcolor%7B%232B7FBB%7D%7B%5Ctextcolor%7B%23E94D40%7D%7BF_3%7D%7D%7C%5Ctextcolor%7B%23E94D40%7D%7B%5Ctextcolor%7B%232B7FBB%7D%7BClass_2%7D%7D)P(%5Ctextcolor%7B%232B7FBB%7D%7B%5Ctextcolor%7B%23E94D40%7D%7BF_4%7D%7D%7C%5Ctextcolor%7B%23E94D40%7D%7B%5Ctextcolor%7B%232B7FBB%7D%7BClass_2%7D%7D)P%5Cleft(%5Ctextcolor%7B%232B7FBB%7D%7BClass_2%7D%5Cright)" alt="P sub 2 equals P of open paren F sub 1 divides C l a. s s sub 2 close paren P of open paren F sub 2 divides C l a. s s sub 2 close paren P of open paren F sub 3 divides C l a. s s sub 2 close paren P of open paren F sub 4 divides C l a. s s sub 2 close paren P of open paren C l a. s s sub 2 close paren">

We see which one is the greatest, and based on that we assign the class.

Those probabilities will be approximated using a distribution.
In this example, we will use the Gaussien Distribution.

##Gaussian Probability Density Function

We recall that teh Gaussien Probability density function is given by:
<br>
<img src="https://equatio-api.texthelp.com/svg/f%5Cleft(x%5Cright)%3D%5Cfrac%7B1%7D%7B%5Csqrt%7B2%5Cpi%7D%5Ctextcolor%7B%238D44AD%7D%7B%5Csigma%7D%7D%5Cexp%5Cleft%5C%7B-%5Cfrac%7B%5Cleft(x-%5Ctextcolor%7B%233697DC%7D%7Bmean%7D%5Cright)%5E2%7D%7B2%5Ctextcolor%7B%238D44AD%7D%7B%5Csigma%7D%5E2%7D%5Cright%5C%7D" alt="f of x equals 1 over the square root of 2 pi sigma the exp of open brace negative the fraction with numerator open paren x minus m e a. n close paren squared and denominator 2 sigma squared close brace">

Write a function that computes the probability using the formula above
"""

import math

def gaussian_probability(x, mean, std_dev):
    """
    Compute the Gaussian (normal) probability density function for a given x.

    Parameters:
    x : float : Feature value for which the probability is being calculated
    mean : float : Mean of the feature values for the given class
    std_dev : float : Standard deviation of the feature values for the given class

    Returns:
    float : Gaussian probability for the given feature value x
    """
    exponent = math.exp(-((x - mean) ** 2) / (2 * (std_dev ** 2)))
    return (1 / (math.sqrt(2 * math.pi) * std_dev)) * exponent

"""##Naive Bayes Implementation

Write a naive bayes function that receives as input the dataframe df, the features, and the target name, and it returns the predicted class as output.
"""

import numpy as np

def naive_bayes(df, features, target_name):


    # Step 1: Calculate the class priors (P(Class))
    class_priors = df[target_name].value_counts(normalize=True)  # P(Class)

    # Step 2: Calculate mean and std deviation for each feature per class
    mean_std_per_class = {}
    for label in class_priors.index:
        class_data = df[df[target_name] == label]
        mean_std_per_class[label] = {
            feature: (class_data[feature].mean(), class_data[feature].std())
            for feature in features
        }

    # Step 3: Gaussian Probability Density Function for continuous data
    def gaussian_probability(x, mean, std_dev):
        exponent = np.exp(-((x - mean) ** 2) / (2 * (std_dev ** 2)))
        return (1 / (np.sqrt(2 * np.pi) * std_dev)) * exponent

    # Step 4: Calculate the posterior probability for each class
    posteriors = {}
    for label in class_priors.index:
        prior = class_priors[label]  # P(Class)
        likelihood = 1  # P(Feature | Class), initially set to 1

        # Calculate likelihood for each feature in the class
        for feature in features:
            feature_value = df[feature]
            mean, std_dev = mean_std_per_class[label][feature]
            likelihood *= gaussian_probability(feature_value, mean, std_dev)

        # Posterior probability is P(Class) * P(Features | Class)
        posteriors[label] = prior * likelihood

    # Step 5: Predict the class with the highest posterior probability
    # Use np.argmax to find the class with the highest posterior probability
    predicted_class = np.argmax([posteriors[label] for label in class_priors.index])

    return predicted_class

"""Test Naive Bayes with a prediction.

Get the corresponding class for a flower having the following features [4.9, 3.0,	1.4,	0.2].
"""

import numpy as np

def naive_bayes(df, features, target_name, new_data):


    # Step 1: Calculate the class priors (P(Class))
    class_priors = df[target_name].value_counts(normalize=True)  # P(Class)

    # Step 2: Calculate mean and std deviation for each feature per class
    mean_std_per_class = {}
    for label in class_priors.index:
        class_data = df[df[target_name] == label]
        mean_std_per_class[label] = {
            feature: (class_data[feature].mean(), class_data[feature].std())
            for feature in features
        }

    # Step 3: Gaussian Probability Density Function for continuous data
    def gaussian_probability(x, mean, std_dev):
        exponent = np.exp(-((x - mean) ** 2) / (2 * (std_dev ** 2)))
        return (1 / (np.sqrt(2 * np.pi) * std_dev)) * exponent

    # Step 4: Calculate the posterior probability for each class
    posteriors = {}
    for label in class_priors.index:
        prior = class_priors[label]  # P(Class)
        likelihood = 1  # P(Feature | Class), initially set to 1

        # Calculate likelihood for each feature in the class
        for i, feature in enumerate(features):
            feature_value = new_data[i]
            mean, std_dev = mean_std_per_class[label][feature]
            likelihood *= gaussian_probability(feature_value, mean, std_dev)

        # Posterior probability is P(Class) * P(Features | Class)
        posteriors[label] = prior * likelihood

    # Step 5: Predict the class with the highest posterior probability
    predicted_class = np.argmax([posteriors[label] for label in class_priors.index])

    return predicted_class

"""See the performance of our NB model

Now here we will splot our data between 2 sets:

*   One from which the Naive Bayes Model will take the probabilities. (The **old** set) 80%
*   one that it hasn't seen before to test on it (The **new** set) 20%
"""

import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from math import pi, sqrt, exp
from sklearn.metrics import accuracy_score

# Step 1: Load and preprocess the dataset
column_names = ['Sepal Height', 'Sepal Width', 'Petal Height', 'Petal Width', 'Target']
file_path = 'iris(1).csv'

# Check if the file exists in the current directory
if not os.path.isfile(file_path):
    print(f"The file {file_path} does not exist. Please check the file name and path.")
else:
    # Loading dataset
    df = pd.read_csv(file_path, header=None, names=column_names)

    # Map target labels to numeric values
    target_mapping = {'Setosa': 0, 'Versicolor': 1, 'Virginica': 2}
    df['Target'] = df['Target'].map(target_mapping)

    # Step 2: Splitting the dataset (80% training, 20% testing)
    features = ['Sepal Height', 'Sepal Width', 'Petal Height', 'Petal Width']
    target_name = 'Target'

    X = df[features]
    y = df[target_name]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Step 3: Implement Naive Bayes Function
    def gaussian_probability(x, mean, std_dev):
        return (1 / (sqrt(2 * pi) * std_dev)) * exp(-0.5 * ((x - mean) ** 2) / (std_dev ** 2))

    def naive_bayes(df, features, target_name):
        # Step 4: Calculate class probabilities and conditional probabilities
        # Calculate P(C)
        class_probs = df[target_name].value_counts(normalize=True).to_dict()

        # Calculate mean and std dev for each feature and class
        feature_stats = {}
        for feature in features:
            feature_stats[feature] = {}
            for class_value in class_probs:
                class_subset = df[df[target_name] == class_value]
                feature_stats[feature][class_value] = {
                    'mean': class_subset[feature].mean(),
                    'std': class_subset[feature].std()
                }

        # Step 5: Make prediction for a given data point
        def predict(features_values):
            # Calculate the probability for each class
            probabilities = {}
            for class_value in class_probs:
                class_prob = class_probs[class_value]
                feature_probs = 1
                for i, feature in enumerate(features):
                    mean = feature_stats[feature][class_value]['mean']
                    std = feature_stats[feature][class_value]['std']
                    feature_prob = gaussian_probability(features_values[i], mean, std)
                    feature_probs *= feature_prob
                probabilities[class_value] = class_prob * feature_probs
            return max(probabilities, key=probabilities.get)

        return predict

    # Step 6: Train Naive Bayes Model
    naive_bayes_model = naive_bayes(df, features, target_name)

    # Step 7: Make Predictions on Test Set
    predictions = []
    for index, row in X_test.iterrows():
        predicted_class = naive_bayes_model(row[features].values)
        predictions.append(predicted_class)

    # Step 8: Evaluate the model
    accuracy = accuracy_score(y_test, predictions)
    print(f"Accuracy of the Naive Bayes model on the test set: {accuracy * 100:.2f}%")

"""Now use the function you built and get the corresponding testing predictions, and then compute the accuracy of your model."""

import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from math import pi, sqrt, exp
from sklearn.metrics import accuracy_score

# Step 1: Load and preprocess the dataset
column_names = ['Sepal Height', 'Sepal Width', 'Petal Height', 'Petal Width', 'Target']
file_path = 'iris(1).csv'

# Check if the file exists in the current directory
if not os.path.isfile(file_path):
    print(f"The file {file_path} does not exist. Please check the file name and path.")
else:
    # Loading dataset
    df = pd.read_csv(file_path, header=None, names=column_names)

    # Map target labels to numeric values
    target_mapping = {'Setosa': 0, 'Versicolor': 1, 'Virginica': 2}
    df['Target'] = df['Target'].map(target_mapping)

    # Step 2: Splitting the dataset (80% training, 20% testing)
    features = ['Sepal Height', 'Sepal Width', 'Petal Height', 'Petal Width']
    target_name = 'Target'

    X = df[features]
    y = df[target_name]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Step 3: Implement Naive Bayes Function
    def gaussian_probability(x, mean, std_dev):
        return (1 / (sqrt(2 * pi) * std_dev)) * exp(-0.5 * ((x - mean) ** 2) / (std_dev ** 2))

    def naive_bayes(df, features, target_name):
        # Step 4: Calculate class probabilities and conditional probabilities
        # Calculate P(C)
        class_probs = df[target_name].value_counts(normalize=True).to_dict()

        # Calculate mean and std dev for each feature and class
        feature_stats = {}
        for feature in features:
            feature_stats[feature] = {}
            for class_value in class_probs:
                class_subset = df[df[target_name] == class_value]
                feature_stats[feature][class_value] = {
                    'mean': class_subset[feature].mean(),
                    'std': class_subset[feature].std()
                }

        # Step 5: Make prediction for a given data point
        def predict(features_values):
            # Calculate the probability for each class
            probabilities = {}
            for class_value in class_probs:
                class_prob = class_probs[class_value]
                feature_probs = 1
                for i, feature in enumerate(features):
                    mean = feature_stats[feature][class_value]['mean']
                    std = feature_stats[feature][class_value]['std']
                    feature_prob = gaussian_probability(features_values[i], mean, std)
                    feature_probs *= feature_prob
                probabilities[class_value] = class_prob * feature_probs
            return max(probabilities, key=probabilities.get)

        return predict

    # Step 6: Train Naive Bayes Model
    naive_bayes_model = naive_bayes(df, features, target_name)

    # Step 7: Make Predictions on Test Set
    predictions = []
    for index, row in X_test.iterrows():
        predicted_class = naive_bayes_model(row[features].values)
        predictions.append(predicted_class)

    # Step 8: Evaluate the model
    accuracy = accuracy_score(y_test, predictions)
    print(f"Accuracy of the Naive Bayes model on the test set: {accuracy * 100:.2f}%")