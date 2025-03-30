# streamlit-assignment-app
Assignment Problem - Hungarian Method - Operational Research - Using Streamlit

This is a Streamlit-based web application that uses the Hungarian Algorithm to solve job assignment problems. The app allows users to minimize or maximize assignment costs by manually entering data or uploading a CSV file.

🚀 Features

  1. Manual Entry: Input the cost matrix manually.
  
  2. CSV Upload: Upload a CSV file containing the cost matrix.
  
  3. Optimization: Choose between cost minimization and maximization.
  
  4. Visualization: Displays the cost matrix and optimal assignments.

🛠️ Installation

  1. Clone the Repository
  
    git clone https://github.com/your-username/streamlit-assignment-app.git
    cd streamlit-assignment-app
  
  2. Install Dependencies
  
    pip install -r requirements.txt
  
  3. Run the Application
  
    streamlit run app.py

📂 CSV File Format

If using a CSV file, ensure the format is number of jobs in row, and number of workers in column

📌 Technologies Used

  1. Streamlit (UI Framework)

  2. NumPy (Matrix Operations)

  3. Pandas (Data Handling)

  4. SciPy (Hungarian Algorithm)

🤖 How It Works

1. Choose input method (Manual or CSV).

2. Enter the cost matrix.

3. Select Minimize or Maximize.

4. Click Generate.

5. View the optimal assignments and total cost.

📜 License

  This project is licensed under the MIT License.
  
