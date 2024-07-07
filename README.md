# Student_result_predictor-machine_learning-
## Student Performance Prediction with Decision Trees
This project demonstrates the use of a Decision Tree classifier (ID3 algorithm) to predict student performance based on their study hours, attendance, and previous grades.

## Project Description
Dataset: The project uses a CSV file (student_data.csv) containing historical data on student study hours, attendance, previous grades, and their corresponding performance.
Model: A Decision Tree classifier is trained on this data to learn the patterns and relationships between these features and performance.
Prediction: The model can take new student data as input and predict their likely performance.
Feedback Loop: The project also adds the new student data and predicted performance back to the original dataset, creating a continuous learning loop for the model.
## How to Use
## Dataset: Make sure you have a CSV file named student_data.csv with the following columns:

study_hours (float)
attendance (float)
previous_grades (float)
performance (categorical, e.g., "High", "Medium", "Low")
#Dependencies: Install the required libraries:
  pip install pandas scikit-learn
python student_performance_prediction.py

## Input:

Enter the student's study hours, attendance percentage, and previous grades when prompted.
The model will predict their performance.
Project Structure
student_data.csv: The dataset
student_performance_prediction.py: The main Python script
