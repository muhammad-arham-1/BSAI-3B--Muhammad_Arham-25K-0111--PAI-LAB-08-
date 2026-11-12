import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv("data.csv")

filterData = data[data["scenario"]=='03_SalaryDiff']
sns.set_theme(style="whitegrid")
sns.boxplot(
    data=filterData,
    x=filterData["prep_course"],
    y=filterData["exam_score"],
    order=["Entry", "Mid","Senior"],
    palette='Set2',
    )

plt.title("Salary Spread Across Experience Levels")
plt.xlabel("Experience Level")
plt.ylabel("Salary ($)")
