#Author Ameena A. Gaji
# Exploratory Data Analysis Tool

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (csv file)
def load_data(file_path):
    return pd.read_csv(file_path)

# MissingValues: Check the gaps/NaN values in the dataset
def check_missing_values(df):

    print("\nMissing Values:")
    print(df.isnull().sum())

# Employ detailed descriptive statistics for a thorough understanding of the dataset
def describe_data(df):

    print("\nData Statistics:")
    print(df.describe())

# Data Visualization using histograms.
def plot_distributions(df):

    num_cols = df.select_dtypes(include=['float64', 'int64']).columns
    for col in num_cols:
        plt.figure(figsize=(6, 6))
        sns.histplot(df[col], kde=True, bins=20)
        plt.title(f'Distribution for {col}')
        plt.show()

# Correlation: Display a correlation matrix to understand the linear relationship between variables.
def plot_correlation_matrix(df):

    plt.figure(figsize=(8, 6))
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm')
    plt.title("Correlation Matrix")
    plt.show()

# CategoricalBalance: Plot count plots for categorical columns to visualize the frequency of different categories.
def plot_categorical_counts(df):

    cat_cols = df.select_dtypes(include=['object', 'bool']).columns
    for col in cat_cols:
        plt.figure(figsize=(8, 6))
        sns.countplot(data=df, x=col)
        plt.title(f'Counts of categories for {col}')
        plt.xticks(rotation=45)
        plt.show()

#Generates pair plots for the columns in the dataset
def pair_plots(df, hue_column=None):

    sns.set_style('whitegrid')

    if hue_column and hue_column in df.columns:
        sns.pairplot(df, hue=hue_column, height=3)
    else:
        sns.pairplot(df, height=3)

    plt.show()

def main():

    #The main function to execute the data exploration steps above.

    # Load the dataset by specifying the file path replace 'your_dataset' with actual dataset
    file_path = 'your_dataset.csv'
    df = load_data(file_path)

    # Check for missing data
    check_missing_values(df)

    # Show basic descriptive statistics
    describe_data(df)

    # Plot distributions of all numerical columns
    plot_distributions(df)

    # Display correlation matrix
    plot_correlation_matrix(df)

    # Plot counts of categorical data
    plot_categorical_counts(df)

    #Generate pair plots
    pair_plots(df)

if __name__ == "__main__":
    main()
