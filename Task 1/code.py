import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, StandardScaler
import matplotlib.pyplot as plt

def main():
    # 1. Import dataset and explore basic info
    df = pd.read_csv('Titanic-Dataset.csv')
    print("Basic Information about the dataset:")
    print(df.info())
    print("\nNull values in each column:")
    print(df.isnull().sum())
    print("\nFirst 5 rows:")
    print(df.head())

    # 2. Handle missing values
    num_cols = df.select_dtypes(include=['float64', 'int64']).columns
    num_imputer = SimpleImputer(strategy='median')
    df[num_cols] = num_imputer.fit_transform(df[num_cols])

    cat_cols = df.select_dtypes(include=['object']).columns
    cat_imputer = SimpleImputer(strategy='most_frequent')
    df[cat_cols] = cat_imputer.fit_transform(df[cat_cols])

    # 3. Convert categorical features into numerical using encoding
    for col in cat_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])

    # 4. Standardize numerical columns
    scaler = StandardScaler()
    df[num_cols] = scaler.fit_transform(df[num_cols])

    # 5. Visualize outliers using boxplots
    df[num_cols].boxplot(rot=45)
    plt.title('Boxplots for Numerical Features')
    plt.show()

    # Remove outliers using IQR method
    Q1 = df[num_cols].quantile(0.25)
    Q3 = df[num_cols].quantile(0.75)
    IQR = Q3 - Q1
    df_clean = df[~((df[num_cols] < (Q1 - 1.5 * IQR)) | (df[num_cols] > (Q3 + 1.5 * IQR))).any(axis=1)]

    print('\nNumber of rows after removing outliers:', df_clean.shape[0])

if __name__ == '__main__':
    main()
