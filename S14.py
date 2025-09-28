#q1
employees <- list("John", "Emma", "Raj", "Sophia", "Amit")

print("Employee List:")
print(employees)

employees <- append(employees, "Karan")
print("After Adding Karan at the end:")
print(employees)

employees <- employees[-3]
print("After Removing 3rd Employee:")
print(employees)

#q2
import pandas as pd 
from mlxtend.preprocessing import TransactionEncoder 
from mlxtend.frequent_patterns import apriori, association_rules 
Learning-with-R-datasets/master/groceries.csv 
transactions = [ 
    ['milk', 'bread', 'nuts', 'apple'], 
    ['milk', 'bread'], 
    ['milk', 'bread', 'nuts'], 
    ['bread', 'apple'], 
    ['milk', 'apple'], 
    ['bread', 'nuts'], 
    ['milk', 'bread', 'apple'], 
    ['nuts', 'apple'], 
    ['milk', 'bread', 'nuts', 'apple'], 
    ['milk', 'bread', 'apple'] 
] 
 
te = TransactionEncoder() 
te_ary = te.fit(transactions).transform(transactions) 
df = pd.DataFrame(te_ary, columns=te.columns_) 
 
frequent_itemsets = apriori(df, min_support=0.3, use_colnames=True) 
 
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.6) 
 
print("Frequent Itemsets:") 
print(frequent_itemsets) 
 
print("\n Association Rules:") 
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])