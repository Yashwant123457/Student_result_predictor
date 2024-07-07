import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv('student_data.csv')

# Define features (X) and target variable (y)
X = data.drop('performance', axis=1)
y = data['performance']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Decision Tree classifier using ID3 algorithm
id3_classifier = DecisionTreeClassifier(criterion='entropy')

# Train the classifier on the training data
id3_classifier.fit(X_train, y_train)

# Make predictions on the test data
y_pred = id3_classifier.predict(X_test)

# Evaluate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Take input from the user for the test instance
try:
    study_hours = float(input("Enter study hours: "))
    attendance = float(input("Enter attendance percentage: "))
    previous_grades = float(input("Enter previous grades: "))
except ValueError:
    print("Invalid input. Please enter numerical values.")
    exit()

# Create a DataFrame for the user input
new_student_data = pd.DataFrame({
    'study_hours': [study_hours],
    'attendance': [attendance],
    'previous_grades': [previous_grades]
})

# Predict student performance for the user input
prediction = id3_classifier.predict(new_student_data)
print(f"Predicted Performance: {prediction[0]}")

# Add the new data along with the result to the existing CSV file
new_student_data['performance'] = prediction[0]
data = data._append(new_student_data, ignore_index=True)
data.to_csv('student_data.csv', index=False)
