import pandas as pd
s = pd.Series (["X","Y","T","Ramu","Real Madrid", "CUBA", None, "bird","balls","dogshed"])
upper = s.str.upper()
lower = s.str.lower()
length = s.str.len()

print("Upper case:\n", upper)
print("\nLower case:\n", lower)
print("\nLength:\n", length)
                