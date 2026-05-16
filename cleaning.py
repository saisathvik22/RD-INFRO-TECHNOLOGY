import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
df = pd.read_csv("data.csv")
X = df[['experience']]
Y = df['salary']

X_train,X_test,y_train,y_test = train_test_split(
    X,Y, test_size = 0.2, random_state = 42
)
model = LinearRegression()
model.fit(X_train,y_train)

prediction = model.predict([[5]])

print("Predicted Salary for 5 years experience:")
print(prediction)