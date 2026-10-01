import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.DataFrame({
    "Marks": [80, 70, None, 90, 60],
    "Attendance": [90, None, 85, 80, 75],
    "Department": ["CSE", "ECE", "CSE", None, "ECE"]
})
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].median())
df["Attendance"] = df["Attendance"].ffill()
df["Department"] = df["Department"].fillna(df["Department"].mode()[0])
encoder = LabelEncoder()
df["Department"] = encoder.fit_transform(df["Department"])
print(df)
   Marks  Attendance  Department
0   80.0        90.0           0
1   70.0        82.5           1
2   75.0        85.0           0
3   90.0        80.0           0
4   60.0        75.0           1
