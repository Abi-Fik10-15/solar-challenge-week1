"""
solar_analysis.py - Core script for profiling and analyzing solar energy data.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(file_path):
    """
    Load dataset from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded dataset.
    """
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()

def clean_data(df):
    """
    Clean missing values by simple imputation.

    Args:
        df (pd.DataFrame): The original dataset.

    Returns:
        pd.DataFrame: Cleaned dataset.
    """
    df_clean = df.copy()
    df_clean.fillna(method='ffill', inplace=True)
    print("Missing values handled using forward fill.")
    return df_clean

def basic_eda(df):
    """
    Generate basic plots for exploratory data analysis.

    Args:
        df (pd.DataFrame): Cleaned dataset.
    """
    print("Summary statistics:\n", df.describe())

    numeric_cols = df.select_dtypes(include='number').columns
    for col in numeric_cols:
        sns.histplot(df[col], kde=True)
        plt.title(f"Distribution of {col}")
        plt.show()

def cross_country_summary(df, country_column, metric_column):
    """
    Group and compare countries based on a metric.

    Args:
        df (pd.DataFrame): Dataset containing country data.
        country_column (str): Column name for countries.
        metric_column (str): Column name for metric to compare.
    """
    summary = df.groupby(country_column)[metric_column].mean().sort_values(ascending=False)
    print("\nAverage", metric_column, "per country:")
    print(summary)

    summary.plot(kind='bar')
    plt.title(f"Average {metric_column} by Country")
    plt.ylabel(metric_column)
    plt.xlabel("Country")
    plt.tight_layout()
    plt.show()

def main():
    # Example file path (update this with your real data path)
    file_path = "data/solar_data.csv"

    df = load_data(file_path)
    if df.empty:
        return

    df_clean = clean_data(df)
    basic_eda(df_clean)

    # Example usage if your data has 'Country' and 'SolarOutput' columns
    if 'Country' in df_clean.columns and 'SolarOutput' in df_clean.columns:
        cross_country_summary(df_clean, 'Country', 'SolarOutput')
    else:
        print("Country or SolarOutput column missing for comparison.")

if __name__ == "__main__":
    main()
