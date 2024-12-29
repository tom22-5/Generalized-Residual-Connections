import pandas as pd
import glob

# Define the path and file pattern
file_pattern = "./experiment1/model_performance_*.xlsx"

# Initialize an empty list to collect dataframes
all_history = []
all_runtime = []

# Loop through all matching Excel files
for file in glob.glob(file_pattern):
    # Read specific sheet (e.g., "runtimes" or "history")
    df_runtimes = pd.read_excel(file, sheet_name="Runtimes")
    df_history = pd.read_excel(file, sheet_name="History")
    
    # Optionally add a column for file identification
    df_runtimes["Source_File"] = file
    df_history["Source_File"] = file
    
    # Append both sheets to the list
    all_history.append(df_history)
    all_runtime.append(df_runtimes)

# Concatenate all dataframes into one big table
big_history = pd.concat(all_history, ignore_index=True)
big_runtime = pd.concat(all_runtime, ignore_index=True)

# Save the result to a new Excel file
big_history.to_excel("./experiment1/combined_model_performance_history.xlsx", index=False)
big_runtime.to_excel("./experiment1/combined_model_performance_runtime.xlsx", index=False)

print("Concatenation complete. Saved as 'combined_model_performance_*.xlsx'.")
