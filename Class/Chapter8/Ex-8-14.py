# 바차트
# Seaborn 패키지를 이용한 scatter plot
# Seaborn Matplotlib을 기반으로 다양한 색상 테마와 통계용 차트 등의 기능을 추가한 시각화 패키지

import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="white")

# Load the example mpg dataset
mpg = sns.load_dataset("mpg")

# Plot miles per gallon against horsepower
# with other semantics
sns.relplot(x="horsepower", y="mpg", hue="origin", size="weight", sizes=(40, 400), alpha=.5, palette="muted", height=6, data=mpg)

plt.show()