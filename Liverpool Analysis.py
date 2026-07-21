import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\DELL\Downloads\Liverpool.csv")

"""
Ques. Home vs Away Performance Gap

Problem:
Does Liverpool perform significantly better at home than away?
Create a side-by-side bar chart comparing average Goals scored and average Goals conceded in Home vs Away matches.
Add exact values above each bar.

"""

home_goals = df[df['Is_Home'] == 1]['Goals'].mean()
home_conceded = df[df['Is_Home'] == 1]['Opponent_Goals'].mean()

away_goals = df[df['Is_Home'] == 0]['Goals'].mean()
away_conceded = df[df['Is_Home'] == 0]['Opponent_Goals'].mean()

labels = ['Home', 'Away']
goals_scored = [home_goals, away_goals]
goals_conceded = [home_conceded, away_conceded]

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(len(labels))  # [0, 1] → positions for Home, Away
width = 0.35  # bar width

fig, ax = plt.subplots(figsize=(8, 6))
bars1 = ax.bar(x - width/2, goals_scored, width, label='Goals Scored', color='green')
bars2 = ax.bar(x + width/2, goals_conceded, width, label='Goals Conceded', color='red')

# Add labels, title, ticks
ax.set_ylabel('Average Goals')
ax.set_title('Liverpool Home vs Away Performance')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.2f}',
                    xy=(bar.get_x() + bar.get_width()/2, height),
                    xytext=(0, 3),  # 3 points above bar
                    textcoords="offset points",
                    ha='center', va='bottom')

plt.tight_layout()
plt.show()

"""
Analysis:
The bar chart compares Liverpool's average goals scored and goals conceded
in home and away matches. The visualization clearly highlights the team's
performance difference based on match location.

Conclusion:
Liverpool performs noticeably better at home, scoring more goals while
conceding fewer compared to away matches. This suggests that home advantage
has a positive impact on the team's overall performance.

"""



"""
Ques. Match Outcome Breakdown

Problem:
The club’s management wants a clear view of how often matches end in Win, Draw, or Loss.

Create a pie chart showing the distribution of results (Result column).

Use percentages and labels.

Add a title: “Liverpool Match Outcomes”.

"""

h1 = df[df['Result'] == 1]['Result'].value_counts().reset_index()
h2 = df[df['Result'] == 0]['Result'].value_counts().reset_index()
h3 = df[df['Result'] == -1]['Result'].value_counts().reset_index()

g = [h1.iloc[0, 1], h2.iloc[0, 1], h3.iloc[0, 1]]
label = ['Win', 'Draw', 'Loss']

plt.pie(g, labels=label, autopct='%1.1f%%')
plt.title('Liverpool Match Outcomes')
plt.show()

"""
Analysis:
The pie chart illustrates the proportion of matches that ended in wins,
draws, and losses. It provides a quick overview of Liverpool's overall
performance across the season.

Conclusion:
A larger share of wins indicates strong overall team performance. The
distribution also helps identify how frequently Liverpool drops points
through draws or losses.

"""



"""Ques. Shot Efficiency vs Goals

Problem:
Is higher shot efficiency actually leading to more goals?

Plot a scatter plot with Shot_Efficiency on the x-axis and Goals on the y-axis.

Add a trend line to show the overall relationship. **bold text**

"""

x = df['Shot_Efficiency']
y = df['Goals']

x = x.replace([np.inf, -np.inf], np.nan)
y = y.replace([np.inf, -np.inf], np.nan)
mask = ~(x.isna() | y.isna())
x, y = x[mask], y[mask]

plt.scatter(x, y, alpha=0.5)

m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b, color='red', label='Trendline')

plt.xlabel("Shot Efficiency")
plt.ylabel("Goals")
plt.title("Shot Efficiency vs Goals")
plt.legend()
plt.show()

"""
Analysis:
The scatter plot and trend line examine the relationship between shot
efficiency and the number of goals scored. Each point represents an
individual match, while the trend line shows the overall direction of the
relationship.

Conclusion:
The upward trend suggests that higher shot efficiency generally leads to
more goals. Although some matches deviate from the trend, efficient
finishing appears to be an important factor in Liverpool's attacking success.

"""



"""Ques. Opponent Strength Effect

Problem:
Do Liverpool struggle more against strong teams (high possession opponents)?

Create a line plot of Opponent_Possession vs Goals scored by Liverpool.

Group by Opponent (take average values per opponent) and sort by possession.

Highlight top 3 toughest opponents in red markers. **bold text**
"""

df_grouped = df.groupby("Opponent").agg({
    "Opponent_Possession": "mean",
    "Goals": "mean"
}).reset_index()

df_grouped = df_grouped.sort_values(by="Opponent_Possession")

plt.figure(figsize=(16,10))

plt.plot(df_grouped["Opponent_Possession"], df_grouped["Goals"], marker='o')
top3 = df_grouped.nlargest(3, "Opponent_Possession")
plt.scatter(top3["Opponent_Possession"], top3["Goals"], color="red", s=100, label="Top 3")

plt.xlabel("Opponent Possession (%)")
plt.ylabel("Avg Goals by Liverpool")
plt.title("Opponent Strength Effect on Goals")
plt.legend()
plt.show()

"""
Analysis:
This line chart compares opponents' average possession with the average
number of goals scored by Liverpool against them. The top three opponents
with the highest possession are highlighted.

Conclusion:
Higher opponent possession does not always result in fewer Liverpool goals.
This suggests that Liverpool can remain offensively effective even against
teams that dominate possession, reflecting tactical flexibility.

"""



"""Ques. Last 5 Match Momentum

Problem:
Does recent momentum (Last5_Win_Rate) correlate with match outcome?

Create a box plot of Last5_Win_Rate split by Result (Win/Draw/Loss).

Check if higher momentum → more wins. **bold text** *italicized text*
"""

h1 = df[df['Result'] == 1]['Last5_Win_Rate']
h2 = df[df['Result'] == 0]['Last5_Win_Rate']
h3 = df[df['Result'] == -1]['Last5_Win_Rate']

g = [h1, h2,h3]

plt.figure(figsize=(8,6))
plt.boxplot(g, labels=['Win', 'Draw', 'Loss'])
plt.title('Liverpool Match Outcomes')
plt.show()

"""
Analysis:
The box plot compares Liverpool's recent five-match win rate across match
outcomes (Win, Draw, and Loss). It helps identify whether recent form
influences future results.

Conclusion:
Winning matches generally corresponds to a higher recent win rate, while
losses tend to occur when recent form is weaker. This indicates that positive
momentum can contribute to better match outcomes.

"""



"""
Ques. Is there a strong relationship between shot efficiency and the number of goals
scored by Liverpool?
"""

sns.regplot(data=df, x="Shot_Efficiency", y="Goals")
plt.xlabel("Shot Efficiency")
plt.ylabel("Goals Scored")
plt.title("Shot Efficiency vs Goals Scored")
plt.show()

"""
Analysis:
The regression plot measures the strength and direction of the relationship
between shot efficiency and goals scored. The fitted regression line
summarizes the overall trend in the data.

Conclusion:
The positive slope indicates a positive correlation between shot efficiency
and goals scored. Improving shot conversion is therefore likely to increase
Liverpool's goal output over time.

"""