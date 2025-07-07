import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

df = pd.read_csv('churn-bigml-80 - churn-bigml-80.csv')

print(df.head())

# Handle missing data
print(df.isnull().sum())
df.fillna(df.mean(numeric_only=True), inplace=True)

# Encode categorical variables
categorical_cols = ['International plan', 'Voice mail plan','Churn']
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])

df=pd.get_dummies(df, columns=['State'], drop_first=True)

# Normalize numerical features
X = df.drop('Churn', axis=1)
y = df['Churn']

scaler=StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

print("Preprocessing complete. Training set size:", X_train.shape, "Testing set size:", X_test.shape)
              
