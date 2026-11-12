import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv("data.csv")
filterData = data[data["scenario"] == '05_AdVsRevenue']
filterData["study_hours"]= pd.to_numeric(filterData["study_hours"])
filterData["exam_score"] =pd.to_numeric(filterData["exam_score"])
sns.set_theme(style="whitegrid")
sns.regplot(
    data=filterData,
    x="exam_score",
    y="study_hours",
    marker="+"
    # scatter_kws={"color":"darkgreen"}
)
plt.title("Impact of Advertising Spend on Total Revenue")
plt.xlabel("Ad Spend ($)")
plt.ylabel("Revenue ($)")
plt.grid(True, linestyle="--", alpha=0.4)
plt.show()

