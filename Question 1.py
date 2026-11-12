import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv("data.csv")
filterData = data[data["scenario"] == '01_StudyVsScore']
sns.set_theme(style="whitegrid")
sns.scatterplot(
    data=filterData,
    x="study_hours",
    y="exam_score",
    hue="prep_course",
    style="prep_course"
)

plt.title("Study Hours vs. Exam Score by Prep Course Status")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.grid(True, linestyle="--", alpha=0.4)
plt.show()