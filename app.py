import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import warnings

warnings.filterwarnings("ignore", category=RuntimeWarning)

# Top Navigation
# Ensure tables and charts fit the screen correctly
st.set_page_config(page_title="Employee Attrition Dashboard", layout="wide")
st.title("Employee Attrition Analysis")

# Tabs for navigation
tabs = st.tabs(["Homepage", "Data Analysis"])

# Apply mappings to categorical variables
satisfaction_map = {1: 'Low', 2: 'Medium', 3: 'High', 4: 'Very High'}
education_map = {1: "Below School", 2: "School", 3: "Bachelors", 4: "Masters", 5: "PhD"}
job_level_map = {1: "Entry Level", 2: "Junior Level", 3: "Mid Level", 4: "Senior Level", 5: "Executive Level"}
wlb_map = {1: "Poor", 2: "Average", 3: "Good", 4: "Excellent"}
department_map = {'Research & Development': 'R&D', 'Sales': 'Sales', 'Human Resources': 'HR'}

# Assuming the dataframe 'df' is preloaded or hardcoded
# Replace this with the actual data loading logic if needed
df = pd.read_csv('employee.csv')  # Example of loading a CSV file directly

# Apply mappings to the dataframe
df['EnvironmentSatisfaction'] = df['EnvironmentSatisfaction'].map(satisfaction_map)
df['JobSatisfaction'] = df['JobSatisfaction'].map(satisfaction_map)
df['RelationshipSatisfaction'] = df['RelationshipSatisfaction'].map(satisfaction_map)
df['JobInvolvement'] = df['JobInvolvement'].map(satisfaction_map)

df['Education'] = df['Education'].map(education_map)
df['JobLevel'] = df['JobLevel'].map(job_level_map)
df['WorkLifeBalance'] = df['WorkLifeBalance'].map(wlb_map)

df['PerformanceRating'] = np.where(df['PerformanceRating'] == 3, 'Good', 'Excellent')

df['Department'] = df['Department'].map(department_map)

# Proceed to create the Homepage and Data Analysis tabs

# Homepage
with tabs[0]:
    st.header("Dashboard Overview")
    st.write("This dashboard provides insights into employee attrition, including data exploration, visualizations, and analysis of key factors influencing attrition.")

    # Dataset Overview
    st.header("Dataset Overview")
    st.write("This dataset contains information about employees, including demographics, job roles, and attrition status.")
    st.write(f"This dataset contains {df.shape[0]} rows and {df.shape[1]} columns, with each row representing an employee's data.")
    # Add a table with variable details
    st.subheader("Variable Details")
    variable_details = [
        {"Category": "Personal & Demographic", "Variable": "Age", "Description": "Age of the employee", "Type": "Numeric"},
        {"Category": "Personal & Demographic", "Variable": "Gender", "Description": "Employee’s gender identity", "Type": "Categorical"},
        {"Category": "Personal & Demographic", "Variable": "MaritalStatus", "Description": "Employee’s marital status", "Type": "Categorical"},
        {"Category": "Personal & Demographic", "Variable": "Over18", "Description": "Indicates if employee is over 18", "Type": "Categorical"},
        {"Category": "Personal & Demographic", "Variable": "DistanceFromHome", "Description": "Distance between home and office in kilometers", "Type": "Numeric"},
        {"Category": "Personal & Demographic", "Variable": "Education", "Description": "Education level on a scale of 1 to 5", "Type": "Ordinal"},
        {"Category": "Personal & Demographic", "Variable": "EducationField", "Description": "Field of education specialization", "Type": "Categorical"},
        {"Category": "Personal & Demographic", "Variable": "StandardHours", "Description": "Standard work hours per week", "Type": "Numeric"},

        {"Category": "Job & Career", "Variable": "EmployeeNumber", "Description": "Unique employee identifier", "Type": "Numeric"},
        {"Category": "Job & Career", "Variable": "JobRole", "Description": "Employee's current job designation", "Type": "Categorical"},
        {"Category": "Job & Career", "Variable": "Department", "Description": "Department of employment", "Type": "Categorical"},
        {"Category": "Job & Career", "Variable": "JobLevel", "Description": "Job seniority level", "Type": "Ordinal"},
        {"Category": "Job & Career", "Variable": "MonthlyIncome", "Description": "Monthly salary of the employee", "Type": "Numeric"},
        {"Category": "Job & Career", "Variable": "HourlyRate", "Description": "Employee's hourly pay rate", "Type": "Numeric"},
        {"Category": "Job & Career", "Variable": "DailyRate", "Description": "Daily pay rate based on payroll", "Type": "Numeric"},
        {"Category": "Job & Career", "Variable": "MonthlyRate", "Description": "Monthly compensation rate", "Type": "Numeric"},
        {"Category": "Job & Career", "Variable": "StockOptionLevel", "Description": "Number of stock options allocated", "Type": "Ordinal"},
        {"Category": "Job & Career", "Variable": "PerformanceRating", "Description": "Employee’s performance evaluation score", "Type": "Ordinal"},
        {"Category": "Job & Career", "Variable": "PercentSalaryHike", "Description": "Percentage salary increment after appraisal", "Type": "Numeric"},
        {"Category": "Job & Career", "Variable": "OverTime", "Description": "Indicates if the employee works overtime", "Type": "Categorical"},

        {"Category": "Experience & Tenure", "Variable": "YearsAtCompany", "Description": "Years the employee has worked at the company", "Type": "Numeric"},
        {"Category": "Experience & Tenure", "Variable": "YearsWithCurrManager", "Description": "Years spent working with the current manager", "Type": "Numeric"},
        {"Category": "Experience & Tenure", "Variable": "YearsInCurrentRole", "Description": "Years in current job role", "Type": "Numeric"},
        {"Category": "Experience & Tenure", "Variable": "YearsSinceLastPromotion", "Description": "Years since last promotion", "Type": "Numeric"},
        {"Category": "Experience & Tenure", "Variable": "TotalWorkingYears", "Description": "Total years of professional experience", "Type": "Numeric"},
        {"Category": "Experience & Tenure", "Variable": "NumCompaniesWorked", "Description": "Number of companies previously worked at", "Type": "Numeric"},

        {"Category": "Engagement & Satisfaction", "Variable": "Attrition", "Description": "Indicates if the employee left the company", "Type": "Categorical"},
        {"Category": "Engagement & Satisfaction", "Variable": "EnvironmentSatisfaction", "Description": "Satisfaction with workplace environment", "Type": "Ordinal"},
        {"Category": "Engagement & Satisfaction", "Variable": "JobSatisfaction", "Description": "Employee’s satisfaction with their job", "Type": "Ordinal"},
        {"Category": "Engagement & Satisfaction", "Variable": "WorkLifeBalance", "Description": "Perceived work-life balance quality", "Type": "Ordinal"},
        {"Category": "Engagement & Satisfaction", "Variable": "RelationshipSatisfaction", "Description": "Satisfaction with professional relationships", "Type": "Ordinal"},
        {"Category": "Engagement & Satisfaction", "Variable": "JobInvolvement", "Description": "Level of engagement and involvement in work", "Type": "Ordinal"},
        {"Category": "Engagement & Satisfaction", "Variable": "BusinessTravel", "Description": "Frequency of business travel", "Type": "Categorical"},

        {"Category": "Development & Training", "Variable": "TrainingTimesLastYear", "Description": "Number of training sessions attended last year", "Type": "Numeric"},
        {"Category": "Development & Training", "Variable": "EmployeeCount", "Description": "Employee count variable (often constant)", "Type": "Numeric"}
        # Add more variable details as needed
    ]
    variable_details_df = pd.DataFrame(variable_details)
    st.table(variable_details_df.style.hide(axis='index'))

    # Dropdown for continuous columns
    st.subheader("Descriptive Statistics of Continuous Variables")
    continuous_cols = [
        'Age', 'MonthlyIncome', 'MonthlyRate', 'HourlyRate', 'TotalWorkingYears', 'YearsAtCompany',
        'YearsInCurrentRole', 'YearsSinceLastPromotion', 'YearsWithCurrManager', 'PercentSalaryHike', 'DailyRate',
        'DistanceFromHome', 'StockOptionLevel'
    ]
    selected_continuous_col = st.selectbox(
        "Select a continuous variable to view its descriptive statistics:", 
        options=continuous_cols
    )

    if selected_continuous_col:
        st.write(f"Descriptive Statistics for {selected_continuous_col}")
        descriptive_stats = df[selected_continuous_col].describe().to_frame().T
        st.dataframe(descriptive_stats.style.hide(axis='index'), use_container_width=True)

# Data Analysis
with tabs[1]:

    # Data Analysis
    st.header("Data Analysis")

    # Example visualization: Attrition count
    st.subheader("Attrition Percentage")
    attrition_count = df['Attrition'].value_counts(normalize=True) * 100
    attrition_count = attrition_count.reset_index()
    attrition_count.columns = ['Attrition', 'Percentage']
    fig = px.bar(
        attrition_count, 
        x='Attrition', 
        y='Percentage', 
        text='Percentage',
        labels={'x': 'Attrition', 'y': 'Percentage'}, 
        color='Attrition',  # Use color based on Attrition values
        color_discrete_map={'Yes': '#E74C3C', 'No': '#2ECC71'},  # Distinct colors for Yes/No

    )
    fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
    fig.update_layout(
        height=500,  # Adjust height for better visibility
        margin=dict(t=50, b=50, l=50, r=50)  # Add margins for better layout
    )
    st.plotly_chart(fig, use_container_width=True)

    # Dropdown menu for column selection
    st.subheader("Number of Employees by Dimension")
    selected_column = st.selectbox(
        "Select a dimension:", 
        options=[
            'EnvironmentSatisfaction', 'JobSatisfaction', 'RelationshipSatisfaction', 'JobInvolvement', 
            'Education', 'JobLevel', 'WorkLifeBalance', 'PerformanceRating', 'Department',
            'BusinessTravel', 'EducationField', 'Gender', 'JobRole', 'MaritalStatus', 'OverTime'
        ]
    )

    # Display count plot for the selected column
    if selected_column:
        # Calculate percentages
        count_data = df[selected_column].value_counts(normalize=True) * 100
        count_data = count_data.reset_index()
        count_data.columns = [selected_column, 'Percentage']

        # Define consistent color mapping for binary and categorical variables
        color_map = {
            'Yes': '#E74C3C', 'No': '#2ECC71',  # Binary categories
            'Low': '#3498DB', 'Medium': '#9B59B6', 'High': '#1ABC9C', 'Very High': '#F1C40F',  # Satisfaction levels
            'Poor': '#E67E22', 'Average': '#F39C12', 'Good': '#2ECC71', 'Excellent': '#3498DB'  # WorkLifeBalance
        }

        # Create a bar plot with percentages
        fig = px.bar(
            count_data, 
            x=selected_column, 
            y='Percentage', 
            text='Percentage',
            color=selected_column,  # Use color based on the selected column
            color_discrete_map=color_map,  # Apply consistent color mapping
            title=f"Percentage of Employees Across: {selected_column}"
        )
        fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
        fig.update_layout(
            height=500,  # Adjust height to zoom out
            margin=dict(t=50, b=50, l=50, r=50)  # Add margins for better visibility
        )
        st.plotly_chart(fig, use_container_width=True)

    # Countplot of Column 1 by Column 2
    st.subheader("Count of Employees Across Two Dimensions")
    col1, col2 = st.columns(2)

    with col1:
        column1 = st.selectbox(
            "Select the first dimension:", 
            options=[
                'EnvironmentSatisfaction', 'JobSatisfaction', 'RelationshipSatisfaction', 'JobInvolvement', 
                'Education', 'JobLevel', 'WorkLifeBalance', 'PerformanceRating', 'Department',
                'BusinessTravel', 'EducationField', 'Gender', 'JobRole', 'MaritalStatus', 'OverTime'
            ],
            key="column1"
        )

    with col2:
        column2 = st.selectbox(
            "Select the second dimension:", 
            options=[
                'EnvironmentSatisfaction', 'JobSatisfaction', 'RelationshipSatisfaction', 'JobInvolvement', 
                'Education', 'JobLevel', 'WorkLifeBalance', 'PerformanceRating', 'Department',
                'BusinessTravel', 'EducationField', 'Gender', 'JobRole', 'MaritalStatus', 'OverTime'
            ],
            key="column2"
        )

    if column1 != column2:
        # Group data by the two selected columns
        grouped_data = df.groupby([column1, column2]).size().reset_index(name='Count')

        # Create a bar plot for the countplot
        fig = px.bar(
            grouped_data, 
            x=column1, 
            y='Count', 
            color=column2, 
            barmode='group',
            text='Count',  # Display value labels as numbers
            title=f"Count of Employees across {column1} by {column2}"
        )
        fig.update_traces(texttemplate='%{text}', textposition='outside')
        fig.update_layout(
            height=500,  # Adjust height for better visibility
            margin=dict(t=50, b=50, l=50, r=50)  # Add margins for better layout
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Please select two different dimensions.")


    # Countplot by Attrition
    st.subheader("Percentage of Employees Attrited by Dimension")
    attrition_column = st.selectbox(
        "Select a dimension to view percentage of employees who attrited across that dimension:", 
        options=[
            'EnvironmentSatisfaction', 'JobSatisfaction', 'RelationshipSatisfaction', 'JobInvolvement', 
            'Education', 'JobLevel', 'WorkLifeBalance', 'PerformanceRating', 'Department',
            'BusinessTravel', 'EducationField', 'Gender', 'JobRole', 'MaritalStatus', 'OverTime'
        ]
    )

    if attrition_column:
        # Calculate percentages grouped by Attrition
        attrition_data = df.groupby(['Attrition', attrition_column]).size().reset_index(name='Count')
        attrition_data['Percentage'] = attrition_data['Count'] / len(df) * 100

        # Create a bar plot with percentages
        fig = px.bar(
            attrition_data, 
            x=attrition_column, 
            y='Percentage', 
            color='Attrition', 
            text='Percentage',
            barmode='group',
            color_discrete_map={'Yes': '#E74C3C', 'No': '#2ECC71'},  # Distinct colors for Yes/No
            title=f"Percentage of employees who attrited across {attrition_column}"
        )
        fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
        fig.update_layout(
            height=500,  # Adjust height for better visibility
            margin=dict(t=50, b=50, l=50, r=50)  # Add margins for better layout
        )
        st.plotly_chart(fig, use_container_width=True)

    # Mean and Median of Continuous Variables Across Attrition
    st.subheader("Mean and Median of Continuous Variables Across Attrition")

    continuous_cols = [
        'Age', 'MonthlyIncome', 'MonthlyRate', 'HourlyRate', 'TotalWorkingYears', 'YearsAtCompany',
        'YearsInCurrentRole', 'YearsSinceLastPromotion', 'YearsWithCurrManager', 'PercentSalaryHike', 'DailyRate',
        'DistanceFromHome', 'StockOptionLevel'
    ]

    # Dropdown to select a continuous variable
    selected_continuous_col = st.selectbox(
        "Select a continuous variable:", 
        options=continuous_cols
    )

    if selected_continuous_col:
        # Calculate mean and median grouped by Attrition
        mean_data = df.groupby('Attrition')[selected_continuous_col].mean().reset_index()
        median_data = df.groupby('Attrition')[selected_continuous_col].median().reset_index()

        # Display mean and median plots side by side
        col1, col2 = st.columns(2)

        with col1:
            fig_mean = px.bar(
                mean_data, 
                x='Attrition', 
                y=selected_continuous_col, 
                text=selected_continuous_col,
                color='Attrition',
                color_discrete_map={'Yes': '#E74C3C', 'No': '#2ECC71'},
                title=f"Mean of {selected_continuous_col} Across Attrition"
            )
            fig_mean.update_traces(texttemplate='%{text:.2f}', textposition='outside')
            fig_mean.update_layout(
                height=400,  # Adjust height for better visibility
                margin=dict(t=50, b=50, l=50, r=50),  # Add margins for better layout
                uniformtext_minsize=8,  # Ensure text is visible
                uniformtext_mode='show'  # Force text to display
            )
            st.plotly_chart(fig_mean, use_container_width=True)

        with col2:
            fig_median = px.bar(
                median_data, 
                x='Attrition', 
                y=selected_continuous_col, 
                text=selected_continuous_col,
                color='Attrition',
                color_discrete_map={'Yes': '#E74C3C', 'No': '#2ECC71'},
                title=f"Median of {selected_continuous_col} Across Attrition"
            )
            fig_median.update_traces(texttemplate='%{text:.2f}', textposition='outside')
            fig_median.update_layout(
                height=400,  # Adjust height for better visibility
                margin=dict(t=50, b=50, l=50, r=50),  # Add margins for better layout
                uniformtext_minsize=8,  # Ensure text is visible
                uniformtext_mode='show'  # Force text to display
            )
            st.plotly_chart(fig_median, use_container_width=True)

    # Distribution of Continuous Variables
    st.subheader("Distribution of Continuous Variables")

    # Dropdown to select a continuous variable
    selected_dist_col = st.selectbox(
        "Select a continuous variable to view its distribution:", 
        options=continuous_cols,
        key="dist_col"
    )

    if selected_dist_col:
        st.write(f"Distribution of {selected_dist_col}")

        # Create a 1x2 figure layout using Matplotlib
        import matplotlib.pyplot as plt
        import seaborn as sns

        fig, axes = plt.subplots(1, 2, figsize=(12, 5))

        # Overall KDE Plot
        sns.kdeplot(df[selected_dist_col], fill=True, color="#3498DB", ax=axes[0])
        axes[0].set_title(f"Overall KDE Plot of {selected_dist_col}")
        axes[0].set_xlabel(selected_dist_col)
        axes[0].set_ylabel("Density")

        # KDE Plot Across Attrition
        sns.kdeplot(data=df, x=selected_dist_col, hue="Attrition", fill=True, palette={"Yes": "#E74C3C", "No": "#2ECC71"}, ax=axes[1])
        axes[1].set_title(f"KDE Plot of {selected_dist_col} Across Attrition")
        axes[1].set_xlabel(selected_dist_col)
        axes[1].set_ylabel("Density")

        # Adjust layout
        plt.tight_layout()
        st.pyplot(fig)
        
    # Scatterplot Analysis
    st.subheader("Scatterplot Analysis")

    # Create two columns for dropdowns
    col1, col2 = st.columns(2)

    with col1:
        # Dropdown for categorical variables
        selected_categorical_col = st.selectbox(
            "Select a categorical variable:",
            options=[
                'EnvironmentSatisfaction', 'JobSatisfaction', 'RelationshipSatisfaction', 'JobInvolvement', 
                'Education', 'JobLevel', 'WorkLifeBalance', 'PerformanceRating', 'Department',
                'BusinessTravel', 'EducationField', 'Gender', 'JobRole', 'MaritalStatus', 'OverTime'
            ],
            key="categorical_col"
        )

    with col2:
        # Dropdown for continuous variables
        selected_continuous_col = st.selectbox(
            "Select a continuous variable:",
            options=continuous_cols,
            key="scatter_continuous_col"
        )

    if selected_categorical_col and selected_continuous_col:
        # Generate a scatterplot for the selected variables
        fig_scatter = px.scatter(
            df,
            x=selected_categorical_col,
            y=selected_continuous_col,
            color=selected_categorical_col,  # Color by the categorical variable
            title=f"Scatterplot of {selected_continuous_col} Across {selected_categorical_col}",
            labels={selected_categorical_col: "Categorical Variable", selected_continuous_col: "Continuous Variable"},
            color_discrete_map={"Yes": "#E74C3C", "No": "#2ECC71"}  # Optional: Distinct colors for Yes/No if applicable
        )
        fig_scatter.update_layout(
            height=500,  # Adjust height for better visibility
            margin=dict(t=50, b=50, l=50, r=50)  # Add margins for better layout
        )
        st.plotly_chart(fig_scatter, use_container_width=True)

    # Skewness Analysis
    st.subheader("Skewness Analysis")

    # Calculate skewness for each continuous column
    skewness_values = {col: df[col].skew() for col in continuous_cols}

    # Convert skewness values to a DataFrame
    skewness_df = pd.DataFrame(list(skewness_values.items()), columns=["Column", "Skewness"])

    # Plot a barplot of skewness values
    fig = px.bar(
        skewness_df,
        x="Column",
        y="Skewness",
        text="Skewness",
        title="Skewness of Continuous Variables",
        labels={"Skewness": "Skewness Value", "Column": "Continuous Variable"},
    )
    fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    fig.update_layout(
        height=500,  # Adjust height for better visibility
        margin=dict(t=50, b=50, l=50, r=50),  # Add margins for better layout
        xaxis_tickangle=-45  # Rotate x-axis labels for better readability
    )

    # Display the barplot
    st.plotly_chart(fig, use_container_width=True)

    # Normality Test and Group Difference Testing side by side
    st.subheader("Statistical Tests")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Normality Test")
        test_type = st.selectbox(
            "Select the type of Normality Test:",
            options=["Shapiro-Wilk Test", "Kolmogorov-Smirnov Test", "Jarque-Bera Test"],
            key="normality_test"
        )

        if test_type:
            from scipy.stats import shapiro, kstest, jarque_bera

            results = []
            for col in continuous_cols:
                if test_type == "Shapiro-Wilk Test":
                    stat, pvalue = shapiro(df[col])
                elif test_type == "Kolmogorov-Smirnov Test":
                    stat, pvalue = kstest(df[col], 'norm', args=(df[col].mean(), df[col].std()))
                elif test_type == "Jarque-Bera Test":
                    stat, pvalue = jarque_bera(df[col])

                normality = "Normal" if pvalue > 0.05 else "Not Normal"
                results.append({"Column": col, "Test Statistic": round(stat, 4), "P-Value": round(pvalue, 4), "Normality": normality})

            results_df = pd.DataFrame(results)
            st.write("Results of the Normality Test:")
            st.dataframe(results_df.style.hide(axis='index'), use_container_width=True)

    with col2:
        st.subheader("Group Difference Testing")
        group_test_type = st.selectbox(
            "Select the type of Group Difference Test:",
            options=["KS Test", "Brunner-Munzel Test", "Mann Whitney U Test"],
            key="group_difference_test"
        )

        if group_test_type:
            from scipy.stats import ks_2samp, brunnermunzel, mannwhitneyu

            group_results = []
            for col in continuous_cols:
                attrition_yes = df[df['Attrition'] == 'Yes'][col]
                attrition_no = df[df['Attrition'] == 'No'][col]

                if group_test_type == "KS Test":
                    stat, pvalue = ks_2samp(attrition_yes, attrition_no)
                elif group_test_type == "Brunner-Munzel Test":
                    stat, pvalue = brunnermunzel(attrition_yes, attrition_no)
                elif group_test_type == "Mann Whitney U Test":
                    stat, pvalue = mannwhitneyu(attrition_yes, attrition_no, alternative='two-sided')

                distribution = "Same Distribution" if pvalue > 0.05 else "Different Distribution"
                group_results.append({"Column": col, "Test Statistic": round(stat, 4), "P-Value": round(pvalue, 4), "Distribution": distribution})

            group_results_df = pd.DataFrame(group_results)
            st.write("Results of the Group Difference Test:")
            st.dataframe(group_results_df.style.hide(axis='index'), use_container_width=True)

    # Box Plot Analysis
    st.subheader("Box Plot Analysis")

    # Dropdown to select a continuous variable for box plot
    selected_boxplot_col = st.selectbox(
        "Select a continuous variable to generate Box Plots:", 
        options=continuous_cols,
        key="boxplot_col"
    )

    if selected_boxplot_col:
        # Create two columns for side-by-side plots
        col1, col2 = st.columns(2)

        with col1:
            # Generate a box plot for the selected continuous variable
            fig_overall = px.box(
                df,
                y=selected_boxplot_col,
                title=f"Overall Box Plot of {selected_boxplot_col}",
                labels={selected_boxplot_col: "Value"}
            )
            fig_overall.update_layout(
                height=400,  # Adjust height for better visibility
                margin=dict(t=50, b=50, l=50, r=50)  # Add margins for better layout
            )
            fig_overall.update_traces(boxmean=False, quartilemethod='inclusive')
            fig_overall.update_traces(
                hovertemplate='Min: %{y[0]}<br>Q1: %{y[1]}<br>Median: %{y[2]}<br>Q3: %{y[3]}<br>Max: %{y[4]}<extra></extra>'
            )
            st.plotly_chart(fig_overall, use_container_width=True)

        with col2:
            # Generate a box plot for the selected continuous variable across attrition
            fig_attrition = px.box(
                df,
                x="Attrition",
                y=selected_boxplot_col,
                title=f"Box Plot of {selected_boxplot_col} Across Attrition",
                labels={selected_boxplot_col: "Value", "Attrition": "Attrition"},
                color="Attrition",  # Color by Attrition
                color_discrete_map={"Yes": "#E74C3C", "No": "#2ECC71"}  # Distinct colors for Yes/No
            )
            fig_attrition.update_layout(
                height=400,  # Adjust height for better visibility
                margin=dict(t=50, b=50, l=50, r=50)  # Add margins for better layout
            )
            fig_attrition.update_traces(boxmean=False, quartilemethod='inclusive')
            fig_attrition.update_traces(
                hovertemplate='Min: %{y[0]}<br>Q1: %{y[1]}<br>Median: %{y[2]}<br>Q3: %{y[3]}<br>Max: %{y[4]}<extra></extra>'
            )
            st.plotly_chart(fig_attrition, use_container_width=True)

    # Violin Plot Analysis
    st.subheader("Violin Plot Analysis")

    # Dropdown to select a continuous variable for violin plot
    selected_violin_col = st.selectbox(
        "Select a continuous variable to generate Violin Plot:", 
        options=continuous_cols,
        key="violin_col"
    )

    if selected_violin_col:
        # Create two columns for side-by-side plots
        col1, col2 = st.columns(2)

        with col1:
            # Generate a violin plot for the selected continuous variable
            fig_overall_violin = px.violin(
                df,
                y=selected_violin_col,
                box=True,  # Add a box plot inside the violin plot
                points="all",  # Show all points
                title=f"Overall Violin Plot of {selected_violin_col}",
                labels={selected_violin_col: "Value"}
            )
            fig_overall_violin.update_layout(
                height=400,  # Adjust height for better visibility
                margin=dict(t=50, b=50, l=50, r=50)  # Add margins for better layout
            )
            st.plotly_chart(fig_overall_violin, use_container_width=True)

        with col2:
            # Generate a violin plot for the selected continuous variable across attrition
            fig_attrition_violin = px.violin(
                df,
                x="Attrition",
                y=selected_violin_col,
                color="Attrition",  # Color by Attrition
                box=True,  # Add a box plot inside the violin plot
                points="all",  # Show all points
                title=f"Violin Plot of {selected_violin_col} Across Attrition",
                labels={selected_violin_col: "Value", "Attrition": "Attrition"},
                color_discrete_map={"Yes": "#E74C3C", "No": "#2ECC71"}  # Distinct colors for Yes/No
            )
            fig_attrition_violin.update_layout(
                height=400,  # Adjust height for better visibility
                margin=dict(t=50, b=50, l=50, r=50)  # Add margins for better layout
            )
            st.plotly_chart(fig_attrition_violin, use_container_width=True)

    # Correlation Analysis
    st.subheader("Correlation Analysis")

    # Calculate correlation matrix for continuous variables
    correlation_matrix = df[continuous_cols].corr()

    # Display correlation matrix as a table
    st.write("Correlation Matrix:")
    st.dataframe(correlation_matrix.style.hide(axis='index'))

    # Display correlation matrix as an interactive heatmap using Plotly with adjusted settings
    import plotly.figure_factory as ff

    fig_heatmap = ff.create_annotated_heatmap(
        z=correlation_matrix.values,
        x=correlation_matrix.columns.tolist(),
        y=correlation_matrix.index.tolist(),
        colorscale="Blues",  # Use a softer color palette
        showscale=True,
        annotation_text=correlation_matrix.round(2).values
    )
    fig_heatmap.update_layout(
        title="Interactive Heatmap of Correlation Matrix",
        height=600,  # Adjust height for better visibility
        margin=dict(t=50, b=50, l=50, r=50),  # Add margins for better layout
        xaxis=dict(tickangle=0)  # Ensure column names are not rotated
    )
    st.plotly_chart(fig_heatmap, use_container_width=True)

    # Dropdowns to select two variables for pairwise correlation
    st.write("Select two variables to view their correlation:")
    col1, col2 = st.columns(2)

    with col1:
        var1 = st.selectbox("Select first variable:", options=continuous_cols, key="correlation_var1")

    with col2:
        var2 = st.selectbox("Select second variable:", options=continuous_cols, key="correlation_var2")

    if var1 and var2:
        pairwise_correlation = correlation_matrix.loc[var1, var2]
        st.write(f"Correlation between {var1} and {var2}: {pairwise_correlation:.2f}")

    # Feature Engineering Section
    st.subheader("Feature Engineering")

    # Create new variables in the dataframe
    df['Role_Tenure_Ratio'] = (df['YearsInCurrentRole'] / (df['YearsAtCompany'] + 1)).round(3)
    df['ManagerTenureRatio'] = (df['YearsWithCurrManager'] / (df['YearsAtCompany'] + 1)).round(3)
    df['Promotion_Tenure_Ratio'] = (df['YearsSinceLastPromotion'] / (df['YearsAtCompany'] + 1)).round(3)
    df['Log_TotalWorkingYears'] = np.log1p(df['TotalWorkingYears'])
    df['Log_YearsAtCompany'] = np.log1p(df['YearsAtCompany'])
    df['Log_YearsSinceLastPromotion'] = np.log1p(df['YearsSinceLastPromotion'])
    df['Log_MonthlyIncome'] = np.log1p(df['MonthlyIncome'])


    # Drop unnecessary columns
    df.drop(['YearsInCurrentRole', 'YearsWithCurrManager', 'YearsSinceLastPromotion', 'EmployeeNumber'], axis=1, inplace=True)
    
    # Add the 'New Created Features' and 'Transformed Features' sections side by side
    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("New Created Features")
            st.write("We created these features due to their strong correlation amongst each other.")
            st.write("1. **RoleTenureRatio** =  YearsInCurrentRole/YearsAtCompany")
            st.write("2. **ManagerTenureRatio** =  YearsWithCurrManager/YearsAtCompany")
            st.write("3. **Promotion** =  YearsSinceLastPromotion/YearsAtCompany")

        with col2:
            st.subheader("Transformed Features")
            st.write("We performed transformations on the following variables based on their skewness:")
            st.write("1. **TotalWorkingYears** - Log Transformation")
            st.write("2. **YearsAtCompany** - Log Transformation")
            st.write("3. **YearsSinceLastPromotion** - Log Transformation")
            st.write("4. **MonthlyIncome** - Log Transformation")
    
    # Add a header before showing the dataframe
    st.header("Sneakpeek Before Training")

    # Display the updated dataframe
    st.dataframe(df.head(), use_container_width=True)

# Adjust the slider to make it visually thicker
st.markdown("""
<style>
    .stSlider > div > div > div > div {
        height: 10px;
    }
</style>
""", unsafe_allow_html=True)

st.subheader("Train-Test Split")
test_size = st.slider("Select test size (between 0 and 1):", min_value=0.0, max_value=1.0, value=0.2, step=0.01)

# Perform train-test split
y = df['Attrition']
x = df.drop(['Attrition','Over18'], axis=1)
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size, random_state=42)

# Display the shapes of the resulting datasets
st.write("Train-Test Split Results:")
st.write(f"Training set size: {x_train.shape[0]} samples")
st.write(f"Test set size: {x_test.shape[0]} samples")

# After train-test split and displaying shapes, add download buttons one below the other
st.download_button(
    label="Download Train Data",
    data=pd.concat([x_train, y_train], axis=1).to_csv(index=False),
    file_name="train_data.csv",
    mime="text/csv"
)
st.download_button(
    label="Download Test Data",
    data=pd.concat([x_test, y_test], axis=1).to_csv(index=False),
    file_name="test_data.csv",
    mime="text/csv"
)

# Define columns for preprocessing
oe_cols = ['EnvironmentSatisfaction', 'JobSatisfaction', 'RelationshipSatisfaction', 'JobInvolvement', 'Education', 'JobLevel', 'WorkLifeBalance']
ohe_cols = ['EducationField', 'Gender', 'OverTime', 'MaritalStatus']

sc_cols = []
for i in df.columns:
    if df[i].dtype != 'O':
        sc_cols.append(i)

# Define categories for OrdinalEncoder
oe_categories = [
    ['Low', 'Medium', 'High', 'Very High'],
    ['Low', 'Medium', 'High', 'Very High'],
    ['Low', 'Medium', 'High', 'Very High'],
    ['Low', 'Medium', 'High', 'Very High'],
    ["Below School", "School", "Bachelors", "Masters", "PhD"],
    ["Entry Level", "Junior Level", "Mid Level", "Senior Level", "Executive Level"],
    ["Poor", "Average", "Good", "Excellent"]
]

# Import necessary libraries
from sklearn.preprocessing import LabelEncoder, StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.compose import ColumnTransformer

# Define transformations
tnf = [
    ('ohe', OneHotEncoder(drop='first', sparse_output=False), ohe_cols),
    ('oe', OrdinalEncoder(categories=oe_categories), oe_cols),
    ('sc', StandardScaler(), sc_cols)
]

# Create ColumnTransformer
ct = ColumnTransformer(tnf, remainder='drop')

# Apply transformations to x_train and x_test
x_train_tnf = ct.fit_transform(x_train)
x_test_tnf = ct.transform(x_test)

# Encode target variable
target_encoder = LabelEncoder()
y_train_tnf = target_encoder.fit_transform(y_train)
y_test_tnf = target_encoder.transform(y_test)


# Import necessary libraries for model training and evaluation
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Add a header for model selection
st.header("Model Attrition")

# Move model_options definition above the dropdown and button columns
model_options = {
    "Logistic Regression": LogisticRegression(class_weight='balanced'),
    "Decision Tree (Gini)": DecisionTreeClassifier(criterion='gini'),
    "Decision Tree (Entropy)": DecisionTreeClassifier(criterion='entropy', max_depth=5),
    "Random Forest": RandomForestClassifier(n_estimators=50, criterion='gini')
}

# Dropdown for model selection
selected_model_name = st.selectbox("Select a model to run:", options=list(model_options.keys()))
# Run Model button below the dropdown
run_model_clicked = st.button("Run Model")

# Store recall for class 1 for each model
if 'recall_scores' not in st.session_state:
    st.session_state['recall_scores'] = {}

if run_model_clicked:
    selected_model = model_options[selected_model_name]
    selected_model.fit(x_train_tnf, y_train_tnf)
    y_pred = selected_model.predict(x_test_tnf)
    precision = precision_score(y_test_tnf, y_pred, average=None)
    recall = recall_score(y_test_tnf, y_pred, average=None)
    f1 = f1_score(y_test_tnf, y_pred, average=None)
    accuracy = accuracy_score(y_test_tnf, y_pred)
    metrics_df = pd.DataFrame({
        "Metric": ["Precision", "Recall", "F1-Score", "Accuracy"],
        "No (0)": [precision[0], recall[0], f1[0], accuracy],
        "Yes (1)": [precision[1], recall[1], f1[1], accuracy]
    })
    # Save recall for class 1 for the selected model
    st.session_state['recall_scores'][selected_model_name] = recall[1]

    # Create a DataFrame for metrics
    metrics_df = pd.DataFrame({
        "Metric": ["Precision", "Recall", "F1-Score", "Accuracy"],
        "No (0)": [precision[0], recall[0], f1[0], accuracy],
        "Yes (1)": [precision[1], recall[1], f1[1], accuracy]
    })

    # Display metrics, ROC Curve, and additional plots based on the selected model
    col1, col2 = st.columns(2)

    with col1:
        # Display metrics in a table without row indices
        st.subheader("Model Performance Metrics")
        st.table(metrics_df.style.hide(axis='index'))

    with col2:
        if selected_model_name in ["Logistic Regression", "Decision Tree (Gini)", "Decision Tree (Entropy)", "Random Forest"]:
            from sklearn.metrics import roc_curve, auc
            import plotly.graph_objects as go

            # Calculate probabilities and ROC curve
            y_prob = selected_model.predict_proba(x_test_tnf)[:, 1]
            fpr, tpr, _ = roc_curve(y_test_tnf, y_prob)
            roc_auc = auc(fpr, tpr)

            # Create the AUC-ROC curve using Plotly
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=fpr, y=tpr, mode='lines', name=f'AUC = {roc_auc:.2f}', line=dict(color='blue')))
            fig.add_trace(go.Scatter(x=[0, 1], y=[0, 1], mode='lines', name='Random Guess', line=dict(color='red', dash='dash')))

            # Update layout for a larger square format
            fig.update_layout(
                title='ROC Curve',
                xaxis_title='False Positive Rate',
                yaxis_title='True Positive Rate',
                legend=dict(x=0.5, y=0.5, xanchor='center', yanchor='middle'),
                width=600,  # Adjusted size for side-by-side display
                height=500,  # Adjusted size for side-by-side display
                margin=dict(t=40, b=40, l=40, r=40),  # Adjust margins for better layout
                plot_bgcolor='rgba(0,0,0,0)',  # Transparent background
            )

            # Display the plot
            st.subheader("ROC Curve")
            st.plotly_chart(fig)

    # Fix: define feature_importances before fallback feature_names logic
    if selected_model_name in ["Logistic Regression", "Decision Tree (Gini)", "Decision Tree (Entropy)", "Random Forest"]:
        import plotly.express as px
        # Get feature importances first
        if hasattr(selected_model, 'coef_'):
            feature_importances = abs(selected_model.coef_[0])
        else:
            feature_importances = selected_model.feature_importances_
        # Get feature names after transformation
        try:
            if hasattr(ct, 'get_feature_names_out'):
                feature_names = ct.get_feature_names_out()
            else:
                feature_names = [f'Feature_{i}' for i in range(len(feature_importances))]
        except Exception:
            feature_names = [f'Feature_{i}' for i in range(len(feature_importances))]

        # Ensure feature importance array matches the number of features
        if len(feature_importances) != len(feature_names):
            st.error(f"Feature importance array length ({len(feature_importances)}) does not match the number of features ({len(feature_names)}).")
        else:
            importance_df = pd.DataFrame({"Feature": feature_names, "Importance": feature_importances})
            importance_df = importance_df.sort_values(by="Importance", ascending=False)
            fig_importance = px.bar(
                importance_df,
                x="Feature",
                y="Importance",
                text="Importance",
                title="Feature Importance",
                labels={"Importance": "Importance Value", "Feature": "Feature"},
            )
            fig_importance.update_traces(texttemplate='%{text:.2f}', textposition='outside')
            fig_importance.update_layout(
                height=500,
                margin=dict(t=50, b=50, l=50, r=50),
                xaxis_tickangle=-45
            )
            st.plotly_chart(fig_importance)

# At the end of Data Analysis Tab: Guess Winner Model button
st.markdown("---")
st.subheader("Compare Models: Guess Winner Model")
if st.button("Guess Winner Model"):
    recall_scores = st.session_state.get('recall_scores', {})
    if recall_scores:
        winner_model = max(recall_scores, key=recall_scores.get)
        st.success(f"The best model is: {winner_model} (Recall for Yes/Class 1: {recall_scores[winner_model]:.2f})")
    else:
        st.warning("No models have been run yet. Please run models to compare.")

