#q1
digits <- c(1, 2, 3, 4, 5, 6)
frequency <- c(7, 2, 6, 3, 4, 8)

# Create labels with digits
labels <- paste("Dice ", digits, sep = "")

# Plot pie chart
pie(frequency,
    labels = labels,
    main = "Pie Chart of Dice Roll Frequencies",
    col = rainbow(length(frequency)),
    clockwise = TRUE)


#q2
import pandas as pd 
df = pd.read_csv("StudentsPerformance.csv") 
print("Shape of the dataset (rows, columns):", df.shape) 
print("\n Top 5 rows of the dataset:") 
print(df.head()) 
num_random_rows = 5   
print(f"\n {num_random_rows} Random rows from the dataset:") 
print(df.sample(num_random_rows)) 
print("\n Number of columns:", len(df.columns)) 
print("Column names:") 
print(df.columns.tolist()) 