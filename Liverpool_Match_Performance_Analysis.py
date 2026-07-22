"""
Liverpool Match Performance Analysis
A data analysis project exploring attacking, defensive, and seasonal 
performance trends using Python (Pandas, Matplotlib, Seaborn).
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"Liverpool.csv")

# Dataset: Liverpool match-level performance data
# Rows: [fill in actual number, e.g. df.shape[0]]
# Time period: [fill in, e.g. 2023-24 season]
# Result column: 1 = Win, 0 = Draw, -1 = Loss
# Key columns: Goals, Opponent_Goals, Shot_Efficiency, Last5_Win_Rate, Is_Home, Opponent_Possession

"""
Ques 1. Home vs Away Performance Gap

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
Ques 2. Match Outcome Breakdown

Problem:
The club’s management wants a clear view of how often matches end in Win, Draw, or Loss.

Create a pie chart showing the distribution of results (Result column).

Use percentages and labels.

Add a title: “Liverpool Match Outcomes”.

"""
counts = df['Result'].value_counts()
g = [counts.get(1, 0), counts.get(0, 0), counts.get(-1, 0)]
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
Reducing the number of drawn matches specifically could be a realistic
opportunity area to convert more points into wins.

"""



"""
Ques 3. Shot Efficiency vs Goals

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



"""
Ques 4. Opponent Strength Effect

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

plt.figure(figsize=(10, 6))

# Plot all opponents as scatter points
plt.scatter(df_grouped["Opponent_Possession"], df_grouped["Goals"], 
            color='steelblue', s=60, alpha=0.6, label='Opponents')

# Highlight top 3 toughest opponents (highest possession)
top3 = df_grouped.nlargest(3, "Opponent_Possession")
plt.scatter(top3["Opponent_Possession"], top3["Goals"], 
            color='red', s=120, label='Top 3 Toughest', zorder=5)

# Label only the top 3 with their opponent name
for _, row in top3.iterrows():
    plt.annotate(row['Opponent'], 
                 (row['Opponent_Possession'], row['Goals']),
                 textcoords="offset points", xytext=(6, 6), fontsize=9)

plt.xlabel("Opponent Possession (%)")
plt.ylabel("Avg Goals by Liverpool")
plt.title("Opponent Strength Effect on Goals")
plt.legend()
plt.tight_layout()
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
This flexibility could be a key strength when facing possession-heavy
opponents in future fixtures.

"""



"""
Ques 5. Last 5 Match Momentum

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
plt.boxplot(g, tick_labels=['Win', 'Draw', 'Loss'])
plt.title('Last 5 Match Win Rate by Outcome')
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
Tracking this momentum score before each match could help the coaching staff
identify fixtures where the team is at higher risk of dropping points.

"""

"""
Ques 6.Does the number of fouls committed vary depending on Liverpool's match result?
"""
df['Result_Label'] = df['Result'].map({
    1: 'Win',
    0: 'Draw',
    -1: 'Loss'
})

plt.figure(figsize=(8,6))

sns.boxplot(
    data=df,
    x='Result_Label',
    y='Fouls'
)

plt.xlabel("Match Result")
plt.ylabel("Number of Fouls")
plt.title("Fouls by Match Result")

plt.show()

"""
Analysis:
The box plot compares the distribution of fouls committed in wins, losses, and draws. 
The median foul count is similar across all three outcomes (around 10–11 fouls), 
indicating that Liverpool maintains a relatively consistent level of physical play 
regardless of the match result. The interquartile ranges are also comparable, 
suggesting similar variability in foul counts across match outcomes. A few high-foul 
outliers are present in each category, representing unusually physical matches.

Result:
Liverpool's foul count remains relatively consistent across wins, draws, and losses, 
indicating that fouls alone are not a significant factor influencing match outcomes.
"""


"""
Ques 7.Does Liverpool experience seasonal fluctuations in scoring performance and win 
rate across different months?

"""
df['Win'] = (df['Result'] == 1).astype(int)
month_map = {
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr',
    5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug',
    9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
}

df['Month_Label'] = df['Month'].map(month_map)
monthly = (
    df.groupby(['Month', 'Month_Label'])
      .agg(
          Avg_Goals=('Goals', 'mean'),
          Win_Rate=('Win', 'mean')
      )
      .reset_index()
)
monthly['Win_Rate'] = monthly['Win_Rate'] * 100
monthly = monthly.sort_values('Month')
plt.figure(figsize=(10,6))

ax = sns.lineplot(
    data=monthly,
    x='Month_Label',
    y='Avg_Goals',
    marker='o',
    label='Average Goals'
)

ax2 = ax.twinx()

sns.lineplot(
    data=monthly,
    x='Month_Label',
    y='Win_Rate',
    marker='s',
    color='red',
    label='Win Rate (%)',
    ax=ax2
)

ax.set_xlabel("Month")
ax.set_ylabel("Average Goals")
ax2.set_ylabel("Win Rate (%)")

plt.title("Average Goals and Win Rate by Month")

ax.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.show()

"""

Analysis:
The line chart compares Liverpool's average goals scored and win rate throughout the 
year. Average goals generally increase from January to September, with noticeable 
peaks in September and December. The win rate follows a similar pattern, reaching 
its highest level in June before remaining relatively stable through the second half 
of the year. Both metrics experience a decline in October and November, indicating a 
temporary dip in team performance before recovering in December.

Result:
Liverpool demonstrates moderate seasonality in performance, with stronger attacking 
output and higher win rates during the middle and latter part of the year. The decline 
observed in October and November may indicate a short performance slump, followed by a 
strong recovery in December.
"""


"""
Ques 8. How has Liverpool's performance changed across different seasons in terms of
average goals scored, average possession, and win percentage?
"""

season_stats = (
    df.groupby("Season")
      .agg(
          Avg_Goals=("Goals", "mean"),
          Avg_Possession=("Possession", "mean"),
          Win_Percentage=("Result", lambda x: (x == 1).mean() * 100)
      )
      .reset_index()
)

x = np.arange(len(season_stats))
width = 0.25

fig, ax = plt.subplots(figsize=(10, 6))

bars1 = ax.bar(x - width, season_stats["Avg_Goals"], width, label="Avg Goals")
bars2 = ax.bar(x, season_stats["Avg_Possession"], width, label="Avg Possession")
bars3 = ax.bar(x + width, season_stats["Win_Percentage"], width, label="Win %")

ax.set_xticks(x)
ax.set_xticklabels(season_stats["Season"])
ax.set_xlabel("Season")
ax.set_ylabel("Value")
ax.set_title("Season-wise Performance")
ax.legend()

# Add labels
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        ax.text(
            bar.get_x() + bar.get_width()/2,
            bar.get_height(),
            f"{bar.get_height():.1f}",
            ha="center",
            va="bottom",
            fontsize=9
        )

plt.tight_layout()
plt.show()

"""
Analysis

The grouped bar chart compares Liverpool's average goals, average possession, and win 
percentage for each season from 2013 to 2025. Average goals remained relatively stable, 
generally ranging between 1.9 and 2.5 goals per match, indicating consistent attacking 
performance across seasons. Average possession also remained consistently high, 
fluctuating between 54% and 64%, reflecting Liverpool's possession-based playing style. 
In contrast, win percentage showed greater variation, with strong performances in 2018 
(67.7%), 2019 (70.8%), and 2024 (76.6%), while 2015 recorded the lowest win percentage 
(48.3%). The 2024 season combined both the highest average goals and the highest win 
percentage, indicating Liverpool's most successful overall performance during the observed 
period.

Result

Liverpool maintained consistent attacking output and ball possession throughout the 
seasons, but win percentage varied considerably. The 2024 season was the strongest, 
achieving the highest average goals and win percentage, while 2015 was the weakest, 
with the lowest average goals and win rate. This suggests that although maintaining high 
possession is important, converting attacking opportunities into goals has a greater 
impact on achieving victories.
"""

"""
Ques 9.Is there a relationship between the number of shots on target faced by Liverpool and the 
number of goals conceded?
"""

x = df["Opponent_Shots_On_Target"]
y = df["Opponent_Goals"]

m, b = np.polyfit(x, y, 1)

plt.figure(figsize=(8, 6))
plt.scatter(x, y, alpha=0.7, edgecolors="black")
plt.plot(x, m*x + b, color="red", label="Trend Line")

plt.xlabel("Opponent Shots on Target")
plt.ylabel("Opponent Goals")
plt.title("Opponent Shots on Target vs Opponent Goals")
plt.legend()
plt.grid(alpha=0.3)

plt.show()


"""
Analysis

The scatter plot examines the relationship between Opponent Shots on Target and Opponent 
Goals conceded, with each point representing a match and the red trend line indicating the 
overall relationship. The upward-sloping trend line shows a positive correlation, meaning 
that as opponents register more shots on target, Liverpool generally concedes more goals. 
However, the data points are widely scattered around the trend line, indicating that the 
relationship is moderate rather than perfect. Some matches with a high number of shots on 
target still resulted in few goals conceded, while others produced multiple goals, 
suggesting that defensive quality and goalkeeper performance also influence the outcome.

Result

The analysis indicates a positive relationship between opponent shots on target and goals 
conceded. Matches in which Liverpool allowed more shots on target were generally associated
with conceding more goals. However, the noticeable variation in the data suggests that 
shots on target alone do not fully determine goals conceded, and additional factors such 
as defensive organization, goalkeeping effectiveness, and shot quality also play an 
important role.
"""

"""
Ques 10.What relationships exist between Liverpool's key match statistics
"""

numeric_cols = ['Goals', 'Possession', 'Shots', 'Shots_On_Target', 'Pass_Accuracy', 
                 'Corners', 'Crosses', 'Fouls', 'Last5_Win_Rate']
corr_matrix = df[numeric_cols].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Between Key Match Statistics')
plt.tight_layout()
plt.show()

"""
Analysis

The correlation heatmap displays the strength and direction of relationships between key 
match statistics using correlation coefficients ranging from -1 to +1. The strongest 
positive correlation is observed between Shots and Shots on Target (0.65), indicating 
that matches with more shots generally result in more shots on target. Goals and Shots 
on Target (0.58) also show a strong positive relationship, suggesting that creating 
accurate shooting opportunities contributes to higher goal scoring. Possession and Pass 
Accuracy (0.56) exhibit a strong positive correlation, reflecting that teams maintaining 
greater ball possession tend to complete passes more accurately. Additionally, Corners and 
Crosses (0.53) and Shots and Corners (0.52) demonstrate moderate positive relationships, 
indicating that attacking pressure often leads to more set-piece opportunities. Most other 
variables show weak or negligible correlations, while Fouls display weak negative 
relationships with several performance metrics, suggesting they have little direct 
influence on overall match performance.

Result

The analysis indicates that attacking metrics are closely interconnected, with Shots on 
Target emerging as one of the strongest indicators of goal scoring. Maintaining high 
possession is associated with better passing accuracy, supporting Liverpool's possession-
based playing style. However, variables such as Fouls and Last5_Win_Rate exhibit very weak 
correlations with most statistics, suggesting they have limited direct impact on individual
match performance. Overall, the findings highlight that creating quality scoring 
opportunities and maintaining effective ball control are the key factors associated with 
Liverpool's on-field success.
"""
