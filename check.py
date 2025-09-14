import pandas as pd

# Load the regular visits data
regular_df = pd.read_csv("regular_visits.csv")

# Step 1: Count how many times each name appears
name_counts = regular_df['Patient Name'].value_counts()

# Step 2: Filter names that appear more than once
repeated_names = name_counts[name_counts > 1]

# Show the result
print("🔁 Patient Names Repeated:")
print(repeated_names)

# Optional: view rows of those repeated names
repeated_df = regular_df[regular_df['Patient Name'].isin(repeated_names.index)]

# Save if needed
repeated_df.to_csv("repeated_names_in_regular.csv", index=False)
