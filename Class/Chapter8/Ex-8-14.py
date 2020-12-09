# 바차트
# Seaborn 패키지를 이용한 scatter plot
# Seaborn Matplotlib을 기반으로 다양한 색상 테마와 통계용 차트 등의 기능을 추가한 시각화 패키지

import matplotlib.pyplot as plt
import seaborn as sns

# set 함수는 스타일, 팔레트, 글꼴, 글꼴 크기 등을 설정. 이는 앞으로 그리게 되는 모든 플롯의 그림에 영향을 준다. 즉, 환경변수 설정이다.
sns.set(style="white")

# Load the example mpg dataset
# sns.load_dataset(샘플데이타셋이름)
# mpg 데이터셋은 seaborn에서 기본 제공하는 데이터셋 중 하나
mpg = sns.load_dataset("mpg")

# Plot miles per gallon against horsepower
# with other semantics
# hue : 두가지 변수를 입력받아 점이 2차원 배열로 나타내어질 때 다른 변수에 따라 변수를 색칠하면서 한가지 차원을 추가할 수 있음. 점이 색을 통해 의미를 얻기 때문.
# hue = 해당 컬럼에 따라 색을 지정합니다.
# size : 점의 크기 구분
# sizes : 점의 크기 조절
# palette : 색상 변경
sns.relplot(x="horsepower", y="mpg", hue="origin", size="weight", sizes=(40, 400), alpha=.5, palette="muted", height=6, data=mpg)

plt.show()