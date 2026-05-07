
# # Import pandas library for data handling
# import pandas as pd
# # Import matplotlib for plotting
# import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression

# # Load the dataset from CSV file
# df = pd.read_csv("C:\\Users\\Lenovo\\Downloads\\3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69.csv")

# # Convert all column names to lowercase (avoids case issues like Date vs date)
# df.columns = df.columns.str.lower()

# # Display first 5 rows to understand structure
# print(df.head())

# # Display column names to know available features
# print(df.columns)


# # Display summary statistics of dataset
# print("\nSummary Statistics:\n")
# print(df.describe())


# # Remove missing values
# df = df.dropna()

# # Check unique cities and states
# print("\nNumber of unique cities:", df['city'].nunique())
# print("Number of unique states:", df['state'].nunique())

# # Convert 'last_update' into datetime format
# df['last_update'] = pd.to_datetime(df['last_update'])




# # Calculate average pollution (using pollutant_avg) per city
# city_avg = df.groupby("city")["pollutant_avg"].mean().sort_values(ascending=False)

# # Top 10 polluted cities
# print("top 10 polluted cities:")
# print(city_avg.head(10))
# # Plot top 10 polluted cities
# city_avg.head(10).plot(kind='bar')
# plt.title("Top 10 Most Polluted Cities")
# plt.xlabel("City")
# plt.ylabel("Average Pollution Level")
# plt.xticks(rotation=45)
# plt.show()



# # Plot least polluted cities
# city_avg.tail(10).plot(kind='bar', color='green')
# plt.title("Top 10 Least Polluted Cities")
# plt.xlabel("City")
# plt.ylabel("Average Pollution Level")
# plt.xticks(rotation=45)
# plt.show()


# # Average pollution per pollutant type
# pollutant_avg = df.groupby("pollutant_id")["pollutant_avg"].mean().sort_values(ascending=False)

# print(pollutant_avg)
# # Plot pollutant comparison
# pollutant_avg.plot(kind='bar')

# plt.title("Average Pollution by Pollutant Type")
# plt.xlabel("Pollutant")
# plt.ylabel("Average Value")
# plt.show()



# # Average pollution per state
# state_avg = df.groupby("state")["pollutant_avg"].mean().sort_values(ascending=False)

# print(state_avg.head(10))
# # Plot
# state_avg.head(10).plot(kind='bar')

# plt.title("Top Polluted States")
# plt.xlabel("State")
# plt.ylabel("Average Pollution")
# plt.show()


# # Distribution
# df["pollutant_avg"].plot(kind='hist', bins=20)

# plt.title("Pollution Distribution")
# plt.xlabel("Pollution Level")
# plt.show()


# # Correlation between numerical columns
# print("\nCorrelation Matrix:\n")
# print(df.corr(numeric_only=True))




# # Use engine size to predict price
# # X = df[["engineSize"]]
# # y = df["price"]

# # Split data
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
  
# # Train model
# model = LinearRegression()
# model.fit(X_train, y_train)

# # Predict
# y_pred = model.predict(X_test)

# print("\nPredicted Prices:\n", y_pred[:5])


# plt.scatter(X, y, color='blue')
# plt.plot(X_test, y_pred, color='red')

# plt.title("Engine Size vs Price (Regression)")
# plt.xlabel("Engine Size")
# plt.ylabel("Price")
# plt.show()


# -------------------------------
# IMPORT LIBRARIES
# -------------------------------
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Apply clean style
plt.style.use('ggplot')

# -------------------------------
# LOAD DATA
# -------------------------------
df = pd.read_csv("C:\\Users\\Lenovo\\Downloads\\3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69.csv")

# Clean column names
df.columns = df.columns.str.lower().str.strip()

# Preview
print(df.head())
print("\nColumns:\n", list(df.columns))

# -------------------------------
# BASIC ANALYSIS (UNIT V)
# -------------------------------
print("\nSummary Statistics:\n")
print(df.describe())

# Remove missing values
df = df.dropna()

# Unique counts
print("\nUnique Cities:", df['city'].nunique())
print("Unique States:", df['state'].nunique())

# Convert date
df['last_update'] = pd.to_datetime(df['last_update'], errors='coerce')

# -------------------------------
# CITY ANALYSIS
# -------------------------------
city_avg = df.groupby("city")["pollutant_avg"].mean().sort_values(ascending=False)

print("\nTop 10 Polluted Cities:\n")
print(city_avg.head(10))

# Top polluted cities graph
plt.figure(figsize=(10,6))
city_avg.head(10).plot(kind='bar', color='crimson')
plt.title("Top 10 Most Polluted Cities", fontsize=14, fontweight='bold')
plt.xlabel("City")
plt.ylabel("Average Pollution")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Least polluted cities graph
plt.figure(figsize=(10,6))
city_avg.tail(10).plot(kind='bar', color='seagreen')
plt.title("Top 10 Least Polluted Cities", fontsize=14, fontweight='bold')
plt.xlabel("City")
plt.ylabel("Average Pollution")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# -------------------------------
# POLLUTANT ANALYSIS
# -------------------------------
pollutant_avg = df.groupby("pollutant_id")["pollutant_avg"].mean().sort_values(ascending=False)

print("\nPollutant Comparison:\n")
print(pollutant_avg)

plt.figure(figsize=(8,5))
ax = pollutant_avg.plot(kind='bar', color='royalblue')

plt.title("Average Pollution by Pollutant Type", fontsize=14, fontweight='bold')
plt.xlabel("Pollutant")
plt.ylabel("Average Value")

# Add values on bars
for i, v in enumerate(pollutant_avg):
    ax.text(i, v, f"{v:.1f}", ha='center', fontsize=10)

plt.tight_layout()
plt.show()

# -------------------------------
# STATE ANALYSIS
# -------------------------------
state_avg = df.groupby("state")["pollutant_avg"].mean().sort_values(ascending=False)

print("\nTop Polluted States:\n")
print(state_avg.head(10))

plt.figure(figsize=(10,6))
state_avg.head(10).plot(kind='bar', color='darkorange')

plt.title("Top Polluted States", fontsize=14, fontweight='bold')
plt.xlabel("State")
plt.ylabel("Average Pollution")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

# -------------------------------
# DISTRIBUTION
# -------------------------------
plt.figure(figsize=(8,5))
plt.hist(df["pollutant_avg"], bins=20, edgecolor='black')

plt.title("Pollution Distribution", fontsize=14, fontweight='bold')
plt.xlabel("Pollution Level")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()

# -------------------------------
# CORRELATION (UNIT V)
# -------------------------------
print("\nCorrelation Matrix:\n")
print(df.corr(numeric_only=True))

# -------------------------------
# REGRESSION (UNIT VI)
# -------------------------------
# Predict avg pollution using min pollution

X = df[["pollutant_min"]]
y = df["pollutant_avg"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

print("\nSample Predictions:\n", y_pred[:5])

# Regression graph
plt.figure(figsize=(8,5))
plt.scatter(X, y, color='blue', alpha=0.5, label='Actual Data')
plt.plot(X_test, y_pred, color='red', label='Regression Line')

plt.title("Regression: Min Pollution vs Avg Pollution", fontsize=14, fontweight='bold')
plt.xlabel("Pollutant Min")
plt.ylabel("Pollutant Avg")
plt.legend()

plt.tight_layout()
plt.show()