import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv("data.csv")
filterData = data[data["scenario"] =='04_CustAgeDist']
sns.set_theme(style="whitegrid")
sns.histplot(
    data=filterData,
    x="prep_course",
    bins=5,
    hue="study_hours",
    kde=True

)

plt.title("Customer Age Distribution by Gender")
plt.xlabel("Age")
plt.ylabel("Customer Count")
plt.show()