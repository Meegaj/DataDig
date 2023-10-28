# DataDig
Ameena Gaji (Craft and Hawkins Department of Petroleum Engineering), agaji1@lsu.edu

DataDig is an advanced Python tool designed for efficient exploratory data analysis, offering automated insights into data distributions, missing values etc. Streamline your initial data review process with DataDig.

<img width="626" alt="Screenshot 2023-10-26 202459" src="https://github.com/Meegaj/DataDig/assets/125159642/9bcaba4b-376d-45eb-8bdd-03595855e576">

This Python tool is an all-in-one exploratory data analysis tool designed to provide a quick, insightful analysis of any dataset loaded into it. Below are the key functionalities:

#Dataset Loading:

Features a load_data function that simplifies importing a CSV file into a pandas DataFrame.

#Missing Data Identification:

Incorporates a check_missing_values function, providing a quick summary of missing (NaN) values in the dataset which is crucial for preprocessing.

#Comprehensive Descriptive Statistics:

Utilizes a describe_data function to offer essential descriptive statistics, giving an insight of the dataset's overall distribution.

#Data Distribution:

Contains a plot_distributions function, generating histograms for numerical columns, crucial for understanding each variable's distribution and identifying outliers or errors.

#Correlation Matrix:

Provides a plot_correlation_matrix function that creates a visual heatmap of the correlation between variables.

#Categorical Data Analysis:

Integrates a plot_categorical_counts function, plotting the distribution of categorical variables to understand their influence.

#Pair Plots:

Features a pair_plots function that generates pair plots of the dataset's features, helping identify structured relationships between variables. Accepts an optional 'hue' argument to differentiate levels of a category with color.

#Automated Execution:

Coordinates the exploratory data analysis process through a main function, which sequentially calls the aforementioned functions, ensuring a logical flow of the data analysis steps.

# Usage Note:

Before running the script, users need to replace 'your_dataset.csv' with the file path of their specific dataset.

# References
DataDig is free for commercial and research use. Feel free to use the code.
If you make use of DataDig, please reference appropriately. 
