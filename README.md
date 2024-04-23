    MACHINE LEARNING BASED WORKLOAD PREDICTION USING CLOUD COMPUTING

The Task Allocation System is a machine learning-based application designed to automate the process of allocating tasks or resources in a project management or scheduling scenario. It leverages historical data to train classification models and provides a user-friendly interface for task assignment predictions.

Features
1. Data Management:
Data Loading: The system can load data from CSV files containing historical task allocation records. The data is expected to have columns representing features (such as task attributes) and a target variable (e.g., allocated resource).
Data Preprocessing: Missing values in the dataset are handled gracefully to ensure robust model training.
2. Machine Learning:
Model Training: Two classification algorithms are implemented: Random Forest and Support Vector Machine (SVM). These models are trained on the historical data to learn patterns and relationships between task attributes and resource allocation.
Model Evaluation: The accuracy of the trained models is evaluated using a holdout test set to assess their performance.
3. Graphical User Interface (GUI):
User Interaction: The system features a GUI developed using the tkinter library, allowing users to input parameters related to a specific task or resource allocation request.
Prediction Output: Upon entering the required parameters and clicking the "Show" button, the system makes predictions using the trained machine learning models and displays the predicted task allocation or assigned resource.
4. Comparison Visualization:
Model Comparison: A bar plot visualization is generated to compare the accuracies of the Random Forest and SVM classifiers. This visualization provides insights into the relative performance of the two models.
Dependencies
Python 3.x: The project is developed using Python programming language version 3.x.
pandas: Used for data manipulation and handling CSV files.
scikit-learn: Provides machine learning algorithms and tools for model training and evaluation.
tkinter: Enables the creation of the graphical user interface for user interaction.
matplotlib: Used for data visualization, specifically for creating bar plots to compare model accuracies.
seaborn: Enhances the aesthetics of matplotlib plots.
