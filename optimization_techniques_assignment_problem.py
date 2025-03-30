import numpy as np
import pandas as pd
from scipy.optimize import linear_sum_assignment
import streamlit as st

def solve_assignment_problem(cost_matrix, option):
    if option == "Maximize":
        new_cost_matrix = cost_matrix * (-1)
    else:
        new_cost_matrix = cost_matrix
    row_ind, col_ind = linear_sum_assignment(new_cost_matrix)

    total_cost = cost_matrix[row_ind, col_ind].sum()
    assignments = list(zip(row_ind, col_ind, cost_matrix[row_ind, col_ind]))
    return assignments, total_cost


def main():
    cost_matrix = []
    st.title("Job Assignment Optimization System")
    st.write("Using Hungarian Algorithm to minimize/maximize job assignment cost.")
    option = st.radio("Choose Input Method: ", ("Manual Entry", "Upload CSV file"))

    if option  == "Manual Entry":
        cost_matrix = []
        num_workers = st.number_input("Enter Number of Workers:", min_value = 1, max_value=10, value= 3, step = 1)
        num_jobs = st.number_input("Enter Number of Jobs:", min_value = 1, max_value=10, value= 3, step = 1)


        for i in range(num_workers) :
            row = st.text_input(f"Enter costs for Worker {i+1} (comma-separated):", "4,2,8")
            cost_matrix.append([int(x) for x in row.split(",")])

        show_cp = st.button("Show Cost Matrix")
        try:
            cost_matrix = np.array(cost_matrix)
            if show_cp and cost_matrix is not None:
                df = pd.DataFrame(cost_matrix, columns=[x for x in range(num_jobs)])
                st.dataframe(df)
        except Exception as e:
            st.error(f"⚠️ Error: {e}")

    else:
        uploaded_file = st.file_uploader("Upload your CSV file", accept_multiple_files=False, type="csv", help="Upload you csv file here.")
        if uploaded_file:
            df = pd.read_csv(uploaded_file, header=None)
            cost_matrix = df.to_numpy()
            st.write("Cost Matrix: ")
            st.dataframe(df)
        else:
            cost_matrix = None
    
    dropdown = st.selectbox("Select: ",["Maximize", "Minimize"],index = 1)
    button = st.button("Generate")

    if cost_matrix is not None and button:
        assignments, total_cost = solve_assignment_problem(cost_matrix, dropdown)
        st.success(f"✅ Optimal Total Cost: {total_cost}")
        st.write("### Optimal Assignments")
        for worker, job, cost in assignments:
            st.write(f"👷 Worker {worker+1} → 🏭 Job {job+1}, Cost: {cost}")


if __name__ == "__main__":
    main()
