------------------------------------------------------------
        SIMPLE LINEAR REGRESSION - SALARY PREDICTION
------------------------------------------------------------

PROJECT OVERVIEW:
This project implements a Simple Linear Regression model in Python
to predict an employee’s salary based on their years of experience.
It demonstrates the process of data loading, model training,
evaluation, visualization, and user-based prediction.

------------------------------------------------------------
AIM:
To develop a machine learning model that estimates salary from
years of experience using Simple Linear Regression.

------------------------------------------------------------
OBJECTIVES:
- Understand and implement Simple Linear Regression
- Train, test, and evaluate a regression model using scikit-learn
- Visualize the data and regression line using Matplotlib
- Accept user input for real-time salary prediction

------------------------------------------------------------
TECHNOLOGIES USED:
Programming Language: Python

Libraries:
- pandas           (Data handling)
- scikit-learn     (Machine learning model)
- matplotlib       (Data visualization)

------------------------------------------------------------
PROJECT STRUCTURE:

Salary_Prediction/
│
├── salary_prediction.py      -> Main program file
├── README.txt                -> Project documentation
└── requirements.txt           -> Library dependencies (optional)

------------------------------------------------------------
HOW IT WORKS:

1. DATA LOADING:
   Loads a dataset with two columns:
   - YearsExperience
   - Salary

2. MODEL TRAINING:
   - Data is split into training (70%) and testing (30%) sets.
   - A Linear Regression model is trained on the training data.

3. MODEL EVALUATION:
   Model performance is evaluated using:
   - Mean Absolute Error (MAE)
   - Mean Absolute Percentage Error (MAPE)
   - Mean Squared Error (MSE)

4. VISUALIZATION:
   - Displays scatter plot of actual data (blue dots)
   - Plots regression line (red line)

5. USER INPUT PREDICTION:
   - Accepts user input for experience (in years)
   - Predicts and displays corresponding salary

------------------------------------------------------------
HOW TO RUN THE PROGRAM:

Step 1: Install required libraries
----------------------------------
pip install pandas scikit-learn matplotlib

Step 2: Run the program
-----------------------
python salary_prediction.py

Step 3: Example Output
----------------------

📈 Simple Linear Regression Model (Salary vs Experience)
Intercept (b₀): 25792.20
Coefficient (b₁): 9449.96

🔍 Model Evaluation:
Mean Absolute Error (MAE): 3426.43
Mean Absolute Percentage Error (MAPE): 5.36%
Mean Squared Error (MSE): 17237649.13

💬 Predict Salary Based on Your Experience
Enter your experience in years: 5
💼 Predicted Salary for 5.0 years of experience: ₹72,042.98

------------------------------------------------------------
SAMPLE VISUALIZATION:
Blue dots - Actual salary data
Red line  - Predicted regression line

------------------------------------------------------------
FUTURE ENHANCEMENTS:
- Add a graphical user interface (Tkinter)
- Create a web version using Streamlit
- Include multiple input features for better predictions

------------------------------------------------------------
AUTHOR:
Your Name
Email: your.email@example.com
GitHub: https://github.com/your-github-profile

------------------------------------------------------------
LICENSE:
This project is open-source and free for educational use.
------------------------------------------------------------