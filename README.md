# Employee Attrition Analysis

## Overview
This project analyzes employee attrition data to uncover key insights and patterns. The dataset contains information about employees, including demographics, job roles, compensation, and attrition status. The analysis aims to identify factors influencing attrition and provide actionable recommendations for improving employee retention.

---
# Key Insights

1. **R&D Department Dominates Attrition**: The R&D department shows the highest attrition risk, with 56.3% of departures coming from non-attrition cases but only 9.0% from actual attrition.

2. **Younger Employees at Risk**: Employees who left had an average age of 33.6 years, compared to 37.6 years for those who stayed, indicating younger employees are more likely to leave.

3. **Compensation Gap Drives Attrition**: Departed employees earn $2,046 less on average in monthly income compared to retained employees, highlighting the role of compensation in attrition.

4. **Overtime Correlates with Attrition**: Employees working overtime show significantly higher attrition rates (8.6% vs 19.7%) compared to those who do not work overtime.

5. **Managerial Stability Matters**: Employees with longer relationships with their current manager (4.4 years on average) are more likely to stay compared to those with shorter relationships (2.9 years).

6. **Work-Life Balance Needs Improvement**: While 60.7% of employees rate their work-life balance as "Good," only 10.4% rate it as "Excellent," indicating room for improvement.

7. **Stock Options Influence Retention**: Higher stock option levels correlate with retention, with departed employees having an average level of 0.5 compared to 0.8 for retained employees.

8. **Role Tenure and Attrition**: Employees with shorter tenure in their current role (2.9 years on average) are more likely to leave compared to those with longer tenure (4.3 years).

9. **Commute Distance Impacts Retention**: Employees who left had an average commute distance of 10.6 miles, compared to 8.9 miles for those who stayed, suggesting longer commutes may influence attrition.

10. **Performance Ratings and Attrition**: Good performers show higher attrition rates (13.6%) compared to excellent performers (2.5%), indicating a potential performance-attrition paradox.

---
# Strategic Recommendations

1. **Compensation Review**: Address the $2,046 income gap for at-risk employees to improve retention.

2. **Early Career Support**: Focus on employees with less than 8 years of experience to reduce attrition among younger and less experienced staff.

3. **Remote Work Options**: Provide flexible work arrangements to reduce commute burdens for employees living farther from the workplace.

4. **Tenure-Based Retention Programs**: Develop initiatives targeting employees with less than 5 years of tenure to improve long-term retention.

5. **Manager Relationship Building**: Strengthen long-term manager-employee bonds to enhance workplace stability and satisfaction.

6. **Stock Option Optimization**: Increase equity participation to incentivize employees and improve retention rates.

7. **Work-Life Balance Initiatives**: Enhance work-life balance programs to address dissatisfaction and improve employee well-being.

8. **Career Pathway Clarity**: Provide clear career progression opportunities to reduce role stagnation and improve engagement.

9. **Age-Inclusive Culture**: Create engagement programs tailored to younger employees to address their unique needs and reduce attrition.

10. **Recognition of High Performers**: Develop programs to recognize and retain top-performing employees, addressing the performance-attrition paradox.

---
## Deep dive insights

### 1. Employee Distribution by Department
- **R&D**: 65.4% – Primary operational focus. 🧪
- **Sales**: 30.3% – Major support function. 💼
- **HR**: 4.3% – Lean staffing. 👥

### 2. Business Travel Frequency
- **Travel Rarely**: 71% – Mostly locally-based roles. ✈️
- **Travel Frequently**: 18.8%. 🌍
- **Non-Travel**: 10.2%. 🏠

### 3. Education Level Split
- **Bachelor’s**: 38.3% – Majority. 🎓
- **Master’s**: 27.1%. 📘
- **Below School**: 11.6%. 🏫
- **PhD**: 3.3%. 🧑‍🔬

### 4. Education Field
- **Life Sciences**: 41.7% 🧪
- **Medical**: 31.6% 🩺
- **Technical Degree**: 10.1% 🛠️
- **Marketing**: 5.2% 📈
- **HR**: 1.8% 👥

### 5. Environment Satisfaction
- **High**: 30.8%
- **Very High**: 30.3%
- **Medium**: 19.1%
- **Low**: 19.8%
✅ Majority are satisfied; morale appears healthy.

### 6. Gender Distribution
- **Male**: 60% 🚹
- **Female**: 40% 🚺

### 7. Job Involvement Levels
- **High**: 57%
- **Very High**: 9.8%
- **Medium**: 27.6%
- **Low**: 5.6%
🔍 Opportunity: Encourage deeper involvement beyond just “high.”

### 8. Job Level Hierarchy
- **Entry & Junior**: 36.3% each – Mostly early-career workforce. 🧑‍💼
- **Mid Level**: 14.8%
- **Senior + Executive**: 12.6%

### 9. Job Role Distribution
- **Sales Executive**: 30%
- **Research Scientist**: 20%
- **Laboratory Technician**: 15%
- **Manufacturing Director**: 10%
- **Healthcare Representative**: 8%
- **Manager**: 7%
- **Sales Representative**: 5%
- **Research Director**: 3%
- **Human Resources**: 2%
🧠 Sales and Research roles dominate — points toward core business functions.

### 10. Job Satisfaction Levels
- **Very High**: 31.2%
- **High**: 30.1%
- **Medium**: 19%
- **Low**: 19.7%
📈 Majority feel positive, but nearly 20% report dissatisfaction.

### 11. Marital Status
- **Married**: 45.8% 💍
- **Single**: 32% 🧑‍🤝‍🧑
- **Divorced**: 22.2% 💔
👪 Balanced mix, with married employees forming the largest group.

### 12. OverTime Participation
- **No**: 71.7% 🕒
- **Yes**: 28.3% ⏰
🕒 Most employees do not work overtime — could suggest work-life balance or labor policies.

### 13. Performance Rating
- **Good**: 84.6% ⭐
- **Excellent**: 15.4% 🌟
⭐ Few top-tier performers — possible opportunity to recognize and develop high-performers.

### 14. Relationship Satisfaction
- **High**: 31.2%
- **Very High**: 29.4%
- **Medium**: 20.6%
- **Low**: 18.8%
💬 Workplace relationships are mostly strong — correlates with job satisfaction trends.

### 15. Work-Life Balance Ratings
- **Good**: 60.7%
- **Average**: 23.4%
- **Excellent**: 10.4%
- **Poor**: 5.4%
⚖️ Majority satisfied, but only a small fraction rate it as “Excellent” — room for enhancement.

### 16. Attrition
- **No**: 83.9% ✅
- **Yes**: 16.1% ❌
🚪 Retention appears strong; understanding attrition drivers could further strengthen workforce stability.

## Understanding Key Drivers of Attrition
The data reveals significant variations in employee attrition rates across different organizational dimensions:

### Department-Level Insights
- **R&D Department**: Shows the highest attrition risk with 56.3% of departures coming from non-attrition cases, but only 9.0% from actual attrition.
- **Sales Department**: Has moderate attrition levels (6.3% attrition vs 24.1% non-attrition).
- **HR Department**: Shows the lowest attrition rates (0.8% attrition vs 3.5% non-attrition).

### Business Travel Impact
- **Frequent travelers**: Show higher attrition rates (4.7% attrition vs 14.1% non-attrition).
- **Rare travelers**: Have the highest overall representation (10.6% attrition vs 60.3% non-attrition).
- **Non-travelers**: Show minimal attrition (0.8% vs 9.4%).

### Education Level Correlations
- **PhD holders**: Have the lowest attrition rates (0.3% attrition vs 2.9% non-attrition).
- **Bachelor's degree holders**: Show moderate attrition (6.7% vs 32.2%).
- **Below college education**: Demonstrates varied patterns across different levels.

### Field of Study Impact
- **Life Sciences employees**: Show higher attrition rates (6.1% vs 35.2%).
- **Medical field employees**: Have lower attrition (4.3% vs 27.3%).
- **Technical degrees**: Show minimal attrition (2.2% vs 6.8%).

### Environment Satisfaction Relationship
- **Very High satisfaction**: Employees still show significant non-attrition representation (26.3%).
- **High satisfaction**: Correlates with lower attrition rates (4.2% vs 26.6%).
- **Medium satisfaction**: Shows the lowest attrition (2.9% vs 16.6%).

### Gender Distribution
- **Male employees**: Represent the majority of both attrition (10.2%) and non-attrition (49.8%) cases.
- **Female employees**: Show lower overall attrition rates (5.9% vs 34.1%).

### Strategic Recommendations
- Focus on R&D retention strategies given the department's high representation.
- Address travel-related stress for frequent business travelers.
- Leverage satisfaction data to identify at-risk employee segments.
- Consider gender-specific retention approaches based on observed patterns.

### Job Involvement Patterns
- **High involvement**: Employees show higher attrition rates (8.5% vs 50.5% non-attrition).
- **Medium involvement**: Demonstrates moderate attrition (4.8% vs 20.7%).
- **Very high involvement**: Shows surprisingly low attrition (0.9% vs 8.9%).
- **Low involvement**: Has minimal representation (1.9% vs 3.7%).

### Job Level Hierarchy Impact
- **Entry Level positions**: Show the highest attrition risk (9.7% attrition vs 27.2% non-attrition).
- **Junior Level employees**: Have moderate attrition (3.5% vs 32.8%).
- **Mid Level**: Shows declining attrition (2.2% vs 12.7%).
- **Senior Level**: Has minimal attrition (0.1% vs 6.9%).
- **Executive Level**: Demonstrates lowest attrition (0.3% vs 4.4%).

### Job Satisfaction Correlation
- **Low satisfaction**: Employees show highest attrition rates (4.5% vs 15.2%).
- **High satisfaction**: Has significant attrition (5.0% vs 25.1%).
- **Medium satisfaction**: Shows moderate levels (3.1% vs 15.9%).
- **Very high satisfaction**: Paradoxically shows some attrition (3.5% vs 27.7%).

### Marital Status Influence
- **Single employees**: Represent the highest attrition group (8.2% vs 23.8%).
- **Married employees**: Show moderate attrition (5.7% vs 40.7%).
- **Divorced employees**: Have lower attrition rates (2.2% vs 20.0%).

### Overtime Impact
- **Employees working overtime**: Show significantly higher attrition (8.6% vs 19.7%).
- **No overtime workers**: Demonstrate much lower attrition (7.5% vs 64.2%).

### Performance Rating Effects
- **Good performers**: Show higher attrition (13.6% vs 71.0%).
- **Excellent performers**: Have lower attrition rates (2.5% vs 12.9%).
- **Performance ratings**: Appear inversely correlated with attrition likelihood.

### Relationship Satisfaction
- **High relationship satisfaction**: Shows notable attrition (4.8% vs 26.4%).
- **Very high satisfaction**: Demonstrates moderate attrition (4.4% vs 25.0%).
- **Medium satisfaction**: Has lower attrition (3.1% vs 17.6%).
- **Low satisfaction**: Shows highest attrition relative to group size (3.9% vs 14.9%).

### Work-Life Balance Impact
- **Good work-life balance**: Employees show highest attrition (8.6% vs 52.1%).
- **Poor work-life balance**: Has minimal representation (1.7% vs 3.7%).
- **Average balance**: Shows moderate attrition (3.9% vs 19.5%).
- **Excellent balance**: Demonstrates lower attrition (1.8% vs 8.6%).

### Strategic Insights
- Entry-level retention requires immediate attention given high attrition rates.
- Overtime management is crucial - overtime strongly correlates with attrition.
- Performance-attrition paradox suggests good performers may be leaving for better opportunities.
- Work-life balance initiatives may help retain employees with good current balance.
- Single employee support programs could address this high-risk demographic.

---

## Quantitative Insights

### Demographic & Compensation Patterns

#### Age Distribution
- **Employees who left**: Average age of 33.6 years.
- **Employees who stayed**: Average age of 37.6 years.
- **Insight**: Younger employees show higher attrition tendency (4-year difference).

#### Compensation Analysis
- **Monthly Income**:
  - Departed employees: $4,787 average.
  - Retained employees: $6,833 average.
  - **Gap**: $2,046 difference suggests compensation plays a significant role.
- **Monthly Rate**:
  - Departed: $14,539 average.
  - Retained: $14,406 average.
  - **Insight**: Minimal difference indicates rate structure isn't the primary factor.
- **Hourly Rate**:
  - Departed: $65.6 average.
  - Retained: $66.6 average.
  - **Insight**: Negligible difference in hourly compensation.

### Career Progression Indicators

#### Experience & Tenure
- **Total Working Years**:
  - Departed: 8.2 years average experience.
  - Retained: 11.3 years average experience.
  - **Insight**: Less experienced employees more likely to leave.
- **Years at Company**:
  - Departed: 5.1 years average tenure.
  - Retained: 7.4 years average tenure.
  - **Insight**: Shorter tenure correlates with higher attrition risk.
- **Years in Current Role**:
  - Departed: 2.9 years average.
  - Retained: 4.3 years average.
  - **Insight**: Role stability linked to retention.

#### Promotion & Management
- **Years Since Last Promotion**:
  - Departed: 1.9 years average.
  - Retained: 2.2 years average.
  - **Insight**: Recent promotion timing shows minimal impact.
- **Years with Current Manager**:
  - Departed: 2.9 years average.
  - Retained: 4.4 years average.
  - **Insight**: Longer manager relationships correlate with retention.

### Performance & Work Conditions

#### Salary Progression
- **Percent Salary Hike**:
  - Departed: 15.2% average.
  - Retained: 15.2% average.
  - **Insight**: Salary increases don't differentiate attrition risk.

#### Work Schedule & Location
- **Daily Rate**:
  - Departed: $804 average.
  - Retained: $813 average.
  - **Insight**: Minimal difference in daily compensation.
- **Distance from Home**:
  - Departed: 10.6 average distance.
  - Retained: 8.9 average distance.
  - **Insight**: Longer commutes associated with higher attrition.

#### Stock Options
- **Stock Option Level**:
  - Departed: 0.5 average level.
  - Retained: 0.8 average level.
  - **Insight**: Higher stock option levels correlate with retention.

### Key Risk Factors Identified

#### High Risk Indicators
- Lower monthly income (-$2,046 difference).
- Younger age (4-year difference).
- Less total experience (3.1-year difference).
- Shorter company tenure (2.3-year difference).
- Longer commute distance (+1.7 difference).
- Lower stock option levels (0.3-point difference).

#### Moderate Risk Indicators
- Shorter time in current role (1.4-year difference).
- Less time with current manager (1.5-year difference).

#### Non-Differentiating Factors
- Salary hike percentages (identical averages).
- Hourly rates (minimal difference).
- Monthly rates (minimal difference).
- Daily rates (minimal difference).

### Strategic Recommendations

#### Immediate Actions
1. **Compensation review**: Address $2,046 income gap for at-risk employees.
2. **Early career support**: Focus on employees with <8 years experience.
3. **Remote work options**: Reduce commute burden for distant employees.

#### Medium-term Initiatives
1. **Tenure-based retention programs**: Target employees with <5 years company tenure.
2. **Manager relationship building**: Strengthen long-term manager-employee bonds.
3. **Stock option optimization**: Enhance equity participation for retention.

#### Long-term Strategies
1. **Career pathway clarity**: Reduce role stagnation for 2-3 year tenures.
2. **Age-inclusive culture**: Create engagement programs for younger workforce.
3. **Compensation benchmarking**: Ensure competitive total compensation packages.

---

## 📊 Insights from Employee Attributes Distribution

### 🔍 Overview
The image presents the **distribution plots of various continuous variables** related to employee demographics, compensation, tenure, and performance. These plots help identify patterns, anomalies, and central tendencies across employee data.

---

### 🧠 Variable-Level Insights

#### 1. **Age**
- Unimodal distribution centered around **35 years**.
- Most employees are between **25 and 60**.

#### 2. **Monthly Income**
- **Right-skewed** with most employees earning between **0 and 10,000** units.
- A few high earners create a long tail.

#### 3. **Monthly Rate**
- Fairly **uniform distribution** with a gentle peak around **10,000–15,000**.

#### 4. **Hourly Rate**
- **Bimodal** distribution peaking around **40 and 80**.
- Common rates lie between **20 and 100**.

#### 5. **Total Working Years**
- **Right-skewed**; most employees have **<20 years** of experience.
- Peak around **10 years**, suggesting a relatively young workforce.

#### 6. **Years at Company**
- Peaks at around **5 years**, with most having **<10 years** tenure.

#### 7. **Years in Current Role**
- **Bimodal** with clusters around **2 and 7 years**.
- Indicates a mix of newer and seasoned employees in roles.

#### 8. **Years Since Last Promotion**
- Strong peak at **0 years**, suggesting many were promoted recently or not at all.
- Most have **<5 years** since last promotion.

#### 9. **Years with Current Manager**
- Similar bimodal trend to current role, with peaks at **2 and 7 years**.
- Reflects management continuity or role transitions.

#### 10. **Percent Salary Hike**
- **Unimodal** with peak around **15%**.
- Majority hikes fall between **10–20%**.

#### 11. **Daily Rate**
- Uniform distribution with visible concentrations around **500 and 1000** units.

#### 12. **Distance From Home**
- **Right-skewed**, peaking around **1–2 miles**.
- Most employees live **<10 miles** from the workplace.

#### 13. **Stock Option Level**
- **Bimodal** with dominant levels at **0 and 1**.
- Few employees hold higher-level stock options.

---

### 🧩 Takeaways for Further Analysis
- **Promotion frequency** and **manager tenure** may offer clues about career growth or stagnation.
- **Income variables** show expected skew toward lower ranges, good candidates for **log transformation** in modeling.
- **Bimodal patterns** (Hourly Rate, Years in Role) could indicate **distinct employee groups** worth segmenting.

## Methodology

### Data Preprocessing
- Dropped irrelevant columns (e.g., `EmployeeCount`). 🗑️
- Mapped categorical variables to meaningful labels (e.g., satisfaction levels). 🗂️

### Exploratory Data Analysis (EDA)
- Visualized employee distribution across various dimensions (e.g., department, job role). 📊
- Analyzed attrition rates by demographic and organizational factors. 📈

### Statistical Testing
- **Normality Tests**: Shapiro-Wilk, Kolmogorov-Smirnov, and Jarque-Bera tests. 🧪
- **Group Difference Testing**: Mann-Whitney U Test for non-normal distributions. 📉

### Visualization
- Count plots, heatmaps, and distribution plots to identify patterns and anomalies. 🖼️

---

## Tools Used
- **Python Libraries**: Pandas, NumPy, Matplotlib, Seaborn, Plotly. 🐍
- **Statistical Tests**: SciPy for normality and group difference testing. 📊

---

## Conclusion
This analysis provides a comprehensive understanding of employee attrition patterns and offers actionable insights to improve retention strategies. By addressing key risk factors and implementing targeted initiatives, organizations can enhance employee satisfaction and reduce attrition rates. 🎯
