import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv("data.csv")
filterData = data[data["scenario"]=='02_MonthlySales']
techStore = filterData[filterData["school_type"]=="TechStore"]
apparelCo = filterData[filterData["school_type"]=="ApparelCo"]
plt.plot(techStore["study_hours"],techStore["exam_score"],marker="o", label="TechStore")
plt.plot(apparelCo["study_hours"], apparelCo["exam_score"], marker="o", label="ApparelCo")
plt.title("Monthly Revenue Trends (Jan - Jun 2023)")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.legend()
plt.show()