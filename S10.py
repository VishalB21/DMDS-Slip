#q1
# Create a numeric vector
vec <- c(12, 45, 7, 89, 23, 56, 3, 78)

# Find maximum and minimum
max_val <- max(vec)
min_val <- min(vec)

# Display results
print(paste("Vector Elements:", toString(vec)))
print(paste("Maximum Value:", max_val))
print(paste("Minimum Value:", min_val))


#q2
import pandas as pd 
from mlxtend.frequent_patterns import apriori, association_rules 
from mlxtend.preprocessing import TransactionEncoder 
try: 
df = pd.read_csv("Iris.csv") 
except FileNotFoundError: 
print("Error: 'Iris.csv' not found. Please ensure the file is in the same directory.") 
exit() 

df['sepal_length_bin'] = pd.cut(df['sepal_length'], bins=3, labels=['short', 'medium', 
'long']) 
df['sepal_width_bin'] = pd.cut(df['sepal_width'], bins=3, labels=['narrow', 'medium', 
'wide']) 
df['petal_length_bin'] = pd.cut(df['petal_length'], bins=3, labels=['small', 'medium', 
'large']) 
df['petal_width_bin'] = pd.cut(df['petal_width'], bins=3, labels=['thin', 'medium', 'thick']) 
transactions = [] 
for index, row in df.iterrows(): 
transaction = [ 
f"sepal_length_{row['sepal_length_bin']}", 
f"sepal_width_{row['sepal_width_bin']}", 
f"petal_length_{row['petal_length_bin']}", 
f"petal_width_{row['petal_width_bin']}", 
f"species_{row['species']}" 
] 
transactions.append(transaction) 
te = TransactionEncoder() 
te_ary = te.fit(transactions).transform(transactions) 
df_encoded = pd.DataFrame(te_ary, columns=te.columns_) 
frequent_itemsets = apriori(df_encoded, min_support=0.05, use_colnames=True) 
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7) 
print("Frequent Itemsets:") 
print(frequent_itemsets) 
print("\nAssociation Rules:") 
print(rules)