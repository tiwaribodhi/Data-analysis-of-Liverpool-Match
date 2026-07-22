# Liverpool Match Data Analysis  

This project uses **Python (NumPy, Pandas, Matplotlib)** to analyze Liverpool’s football performance across multiple dimensions such as home vs away, match outcomes, efficiency, and momentum. It provides **visual insights** to better understand the club’s strengths and weaknesses.  

---

## 📑 Table of Contents  
1. [Overview](#-overview)  
2. [Dataset](#-dataset)  
3. [Analysis & Visualizations](#-analysis--visualizations)  
   - [Home vs Away Performance Gap](#1-home-vs-away-performance-gap)  
   - [Match Outcome Breakdown](#2-match-outcome-breakdown)  
   - [Shot Efficiency vs Goals](#3-shot-efficiency-vs-goals)  
   - [Opponent Strength Effect](#4-opponent-strength-effect)  
   - [Last 5 Match Momentum](#5-last-5-match-momentum)
   - [Fouls vs Match Result](#6-fouls-vs-match-result)  
   - [Seasonality — Monthly Goals & Win Rate](#7-seasonality--monthly-goals--win-rate)  
   - [Season-over-Season Performance](#8-season-over-season-performance)  
   - [Defensive Vulnerability](#9-defensive-vulnerability)  
   - [Correlation Between Key Match Statistics](#10-correlation-between-key-match-statistics)    
4. [Results](#-results)  
5. [Tech Used](#-tech-used)  

---

## 🔎 Overview  
Football performance analysis is crucial for clubs to evaluate strategies, identify weaknesses, and optimize results. This project focuses on **Liverpool FC’s match data** and answers key performance questions such as:  

- Does playing at home give Liverpool a significant edge?  
- How are wins, draws, and losses distributed over the season?  
- Is shot efficiency a real indicator of scoring success?  
- Do strong possession-based opponents reduce Liverpool’s goal output?  
- Does momentum from recent matches correlate with results?  

Through **bar charts, pie charts, scatter plots, line plots, and box plots**, this project provides actionable insights into performance patterns.  

---

## 📂 Dataset  
The project expects a CSV file named `Liverpool.csv` with columns such as:  
- `Is_Home` → 1 if match at home, 0 if away  
- `Goals` → Goals scored by Liverpool  
- `Opponent_Goals` → Goals conceded  
- `Result` → 1 (Win), 0 (Draw), -1 (Loss)  
- `Shot_Efficiency` → Measure of shooting efficiency  
- `Opponent` → Name of opponent club  
- `Opponent_Possession` → Avg possession % of opponent  
- `Last5_Win_Rate` → Win rate in last 5 matches before this game  

---

## 📊 Analysis & Visualizations  

### 1. Home vs Away Performance Gap  
- **Question**: Does Liverpool perform significantly better at home than away?  
- **Visualization**: Side-by-side bar chart (avg goals scored & conceded at home vs away).  
- **Insight**: Highlights performance consistency across venues.  

### 2. Match Outcome Breakdown  
- **Question**: What is the distribution of Wins, Draws, and Losses?  
- **Visualization**: Pie chart with percentage breakdown.  
- **Insight**: Gives a quick overview of season performance.  

### 3. Shot Efficiency vs Goals  
- **Question**: Does higher shot efficiency lead to more goals?  
- **Visualization**: Scatter plot of `Shot_Efficiency` vs `Goals` with trend line.  
- **Insight**: Identifies whether efficiency translates into scoring.  

### 4. Opponent Strength Effect  
- **Question**: Do Liverpool struggle more against stronger possession teams?  
- **Visualization**: Line plot of opponent possession vs goals scored (highlight top 3 toughest opponents).  
- **Insight**: Helps find teams that suppress Liverpool’s attacking power.  

### 5. Last 5 Match Momentum  
- **Question**: Does recent momentum influence match outcomes?  
- **Visualization**: Boxplot of `Last5_Win_Rate` grouped by result (Win/Draw/Loss).  
- **Insight**: Shows whether form momentum predicts success.

### 6. Fouls vs Match Result  
- **Question**: Does the number of fouls committed vary depending on match result?  
- **Visualization**: Box plot of **Fouls** grouped by **Result (Win / Draw / Loss)**.  
- **Insight**: Evaluates whether discipline or physicality differs based on the match outcome.  

### 7. Seasonality — Monthly Goals & Win Rate  
- **Question**: Does Liverpool experience seasonal fluctuations in scoring and win rate across different months?  
- **Visualization**: Dual-axis line chart of **Average Goals** and **Win Rate (%)** grouped by month.  
- **Insight**: Identifies seasonal peaks and dips in Liverpool's attacking performance and success rate.  

### 8. Season-over-Season Performance  
- **Question**: How has Liverpool's performance changed across different seasons in terms of goals, possession, and win percentage?  
- **Visualization**: Grouped bar chart comparing **Average Goals**, **Average Possession**, and **Win Percentage** for each season.  
- **Insight**: Tracks long-term improvement or decline in team performance across seasons.  

### 9. Defensive Vulnerability  
- **Question**: Is there a relationship between opponent shots on target and goals conceded?  
- **Visualization**: Scatter plot with a regression trend line between **Opponent Shots on Target** and **Opponent Goals**.  
- **Insight**: Assesses Liverpool's defensive solidity under increasing attacking pressure.  

### 10. Correlation Between Key Match Statistics  
- **Question**: What relationships exist between Liverpool's key match statistics?  
- **Visualization**: Correlation heatmap across **Goals**, **Possession**, **Shots**, **Shots on Target**, **Pass Accuracy**, **Corners**, **Crosses**, **Fouls**, and **Last 5 Win Rate**.  
- **Insight**: Highlights which match statistics are most strongly associated with scoring and overall performance.
---

## 📊 Results  
From the analysis, some clear insights emerge:  
- **Home vs Away** → Liverpool generally scores more and concedes less at home.  
- **Match Outcomes** → The pie chart shows a higher proportion of wins compared to draws and losses.  
- **Shot Efficiency** → Positive correlation with goals scored, indicating efficient shooting is key.  
- **Opponent Possession** → High-possession teams tend to suppress Liverpool’s scoring, with the toughest 3 highlighted.  
- **Momentum Effect** → Higher last 5 match win rates are associated with more frequent wins.
- **Discipline:** Foul counts remain relatively consistent across wins, draws, and losses, indicating that committing more fouls has little direct influence on match outcomes.
- **Seasonality:** Goals scored and win rate display moderate seasonal variation, with a noticeable dip during **October–November** and stronger performances in the later months of the season.
- **Season Trends:** The **2024 season** recorded both the highest average goals scored and the highest win percentage, while **2015** showed the weakest overall performance.
- **Defensive Quality:** An increase in opponent shots on target generally leads to more goals conceded. However, the relationship is only moderate, suggesting that defensive organization and goalkeeping quality also significantly influence outcomes.
- **Key Correlations:** **Shots on Target** exhibits the strongest positive relationship with goals scored, while **Possession** is positively correlated with **Pass Accuracy**, reinforcing Liverpool's possession-oriented playing style.  

---

## 🛠 Tech Used  
This project is built using the following technologies:  
- **Python 3.x** → Core programming language  
- **NumPy** → Numerical operations and array handling  
- **Pandas** → Data cleaning and manipulation  
- **Matplotlib** → Data visualization and charting  
