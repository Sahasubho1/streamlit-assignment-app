# Job Assignment Streamlit App

This is a Streamlit-based web application that uses the Hungarian Algorithm to solve job assignment problems. The app allows users to minimize or maximize assignment costs by manually entering data or uploading a CSV file.

## Features
- Manual Entry: Input the cost matrix manually.
- CSV Upload: Upload a CSV file containing the cost matrix.
- Optimization: Choose between cost minimization and maximization.
- Visualization: Displays the cost matrix and optimal assignments.

## Technologies Used
- Streamlit (UI Framework)
- NumPy (Matrix Operations)
- Pandas (Data Handling)
- SciPy (Hungarian Algorithm)

## Installation
- Clone the Repository
```
    git clone https://github.com/subhasishsaha/assignment-application.git
    cd streamlit-assignment-app
 ```
- Install Dependencies
 ```
    pip install -r requirements.txt
 ```
- Run the Application
```
    streamlit run app.py
```
## CSV File Format

If using a CSV file, ensure the format is number of jobs in row, and number of workers in column

## How It Works
- Choose input method (Manual or CSV).
- Enter the cost matrix.
- Select Minimize or Maximize.
- Click Generate.
- View the optimal assignments and total cost.

  
