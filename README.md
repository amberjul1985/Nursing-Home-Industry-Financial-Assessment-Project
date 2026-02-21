**Executive Summary**

Upon analyzing the nursing home industry, our team performed a variety of analytical tests and prediction models, including OLS Regression, Random Forest Analysis, Logistic Regression, as well as Lasso, Ridge, and Elastic Analysis, to better assess its financial capabilities and the quality of its services.

This report concludes that the nursing home industry is not suitable for financial investment because of its high-risk profile. Our team has analyzed provider finances and quality ratings to better understand how the industry operates, what are the most valuable factors to the industry, and where the industry could potentially be heading.

**Introduction** 

Background Information: Objectives and Significance of the Analysis

The demand for elder care services has grown sharply in the United States due to the aging population, especially the baby boomer generation. As more people look for long-term care options, nursing homes are becoming increasingly attractive for private investment as well as public health planning. If the industry proves to be financially resilient and sustainable, particularly in the face of recent setbacks like the COVID-19 outbreak, this presents a potentially profitable opportunity for investors.

The purpose of this project is to determine if it would be beneficial for our customer to invest in nursing homes. In order to accomplish this, we will examine an extensive dataset covering nursing homes in the United States between 2015 and 2021. Thus, there will be five main objectives for the analysis:

Evaluate nursing facilities' overall financial performance nationwide,
Identify what important factors affected that performance,
Determine which of those elements affects events the most,
Describe long-term trends in performance and affecting factors,
Analyze the impact of the COVID-19 epidemic .

The significance of this analysis lies in its ability to provide insight into data-driven investment strategies in a sector that directly affects a vulnerable and expanding population segment.

**Methodology**

Data Collection

The data utilized in this research were obtained from the Centers for Medicare & Medicaid Services (CMS). They were made available via the Nursing Homes platform called the Provider Data Catalog and the Care Compare. 

Data from several federal reporting systems is compiled by different sources, including (1) CMS Health Inspection Database, which contains inspection data, penalties, health deficiencies, and nursing home characteristics, (2) Payroll-Based Journal (PBJ) system, which provides comprehensive quarterly staffing records, (3) Minimum Data Set (MDS) National Database which performs clinical evaluations and quality metrics at the resident level, (4) Medicare Claims Data, which documents hospital stays, admissions, and outcomes related to quality.

The datasets utilized were in CSV format, arranged by year and data type, and covered the years 2015–2021. To ensure consistency across sources and years, we downloaded the data, combined and cleaned the datasets, about which we will talk in more detail in the next sections. The facility-level analysis of all datasets allowed for reliable cross-temporal and cross-geographic comparisons.

Data Analysis Techniques 

Firstly, after looking at all of the yearly datasets, we merged them into unified datasets to make the working process easier. After that, we implemented the following methods of data analysis:

(1) Descriptive statistics: To find broad trends in financial performance and care quality over time, we started with simple statistical summaries. This involved figuring out important variables, including total discharges, operating expenses per discharge, and net income per discharge. 
(2) Correlation analysis: We evaluated the connections between the financial results of different facility parameters (e.g., ownership type, staffing levels, quality ratings, and flaws). This helped draw attention to issues with multicollinearity. 
(3) Trend & Time-Series Analysis: In order to detect major shifts in the industry, we studied the evolution of financial performance metrics over time, especially around the start of COVID-19, using visualizations and year-over-year comparisons.
(4) Regression Modeling (OLS): To identify the most statistically significant predictors of net income per discharge, we used Ordinary Least Squares regression with backward elimination. As a result, we were able to determine and analyze linear relationships.
(5) Categorical Modeling (Logistic, Decision Tree, Random Forest): We developed classification models that predicted whether a facility would receive a rating higher than three stars in order to evaluate the quality of the providers.
(6) Machine Learning: Random Forest & Regularized Regression (Lasso, Ridge, ElasticNet): To assess nonlinear correlations and feature importance in financial predictions, we implemented Random Forest analysis.
(7) COVID-19 Impact Assessment: In order to examine the effects of the pandemic on income, costs, and quality scores across areas, we separated COVID-era data (2020–2021). Systemic problems were also identified through region-specific analysis in places that were disproportionately impacted.
Analytical Tools / Software Used

To complete the project, we used a couple of industry-standard tools. At the very beginning, we used Excel for preliminary data review and manual cross-validation. The majority of the work was done using Python to take care of the data handling and visualizations. 
Data Description 
Overview of the Data Sets

As already mentioned, this project makes use of a wide range of datasets from the Centers for Medicare & Medicaid Services (CMS), particularly from the Provider Data Catalog and the Care Compare – Nursing Homes platform. Together, these datasets include information on the quality, operations, and financial aspects of nursing facilities in the US between 2015 and 2021. 

The datasets are as follows:

(1) ProviderInfo includes facility details on nursing homes, such as facility name, address, ownership type, capacity, and certification status.
(2) CostReport gives data on financial performance and expenses, including total revenue, operating expenses, profit margins, and capital costs. 
(3) HealthDeficiencies provides information on inspection violations and deficiency tags, categorized by type, severity, and date. 
(4) QualityMsrMDS gives metrics for the quality of care obtained from MDS evaluations, including but not limited to mobility decline and infection rates.  
(5) Penalties include information about fines and other enforcement measures that noncompliant facilities face. 
(6) CovidVax provides staff and resident vaccination rates for 2020 and 2021.

In addition to being arranged by year, each dataset was supplied in CSV format and included a DataDictionary that offers thorough explanations of every variable.

The combined dataset represents thousands of distinct nursing home facilities with hundreds of thousands of entries spanning all years and tables. A variety of data types are included in the variables, including date/time, numeric (such as total costs, staffing hours), and categorical (such as ownership type, state).

Overall, finding trends, patterns, and important performance drivers in the nursing care sector is made much easier by the wide range and variety of this data.
Data Preprocessing

The raw datasets were carefully preprocessed before any analysis started in order to guarantee accuracy, consistency, and usability across several sources and years. 
Cost Reports

The Cost report files were arranged by year and category, and each dataset from 2015 to 2021 was given its own CSV file. Each set of annual files was combined into a single dataset using Python and the pandas package. In order to preserve each record's temporal context, a new column called "Year" was added during this phase. In many cases, different years or datasets had different column names, requiring harmonization to match naming conventions and allow smooth merging. Once this was done, we added new columns that aggregated much of the financial data. These new columns were the sums of total_discharges_total, Total_Discharges_Title_XVIII, Total_Discharges_Title_XIX, and Total_Discharges_Title_Other. The most important of these new columns is Net_Income_per_Discharge. We used discharges as a proxy for patient counts because there was no count of patients in the original datasets. Discharges are patients who have completed whatever treatment/allotted time. This new column was used as the target variable for many of the future models. 

To improve model accuracy and reduce bias, the preprocessing started by eliminating all rows that lacked the target variable (Net_income_per_discharge). Any row with more than 50% of the independent variables' values missing was eliminated to control the quality of the data. This made sure that only records with enough information were used to train the model. For the remaining data, to impute numerical missing values, we used the median of each corresponding column, which is a reliable technique that is less prone to outliers. And to impute categorical missing values, we used the mode, guaranteeing the dataset's logical consistency. However, we understood that categorical variables do not add much value to the analysis in this case, and that’s why we later deleted the columns containing categorical variables. Furthermore, to avoid model distortion and make sure every data point reflected a distinct observation, duplicate records were eliminated.  

To prevent type-related problems during modeling, we transformed all variables to numeric types after the features and target were established. Then, we used Scikit-learn's StandardScaler to standardize the resulting feature matrix, converting the variables to have a unit variance and zero mean. Standardization was crucial for the Ordinary Least Squares (OLS) regression to avoid variables with larger values disproportionately affecting the model. 

This preprocessed dataset was fed into two different modeling techniques: a Random Forest regression model for non-linear insights and variable importance analysis, and backward elimination using linear regression.

We used a composite key that consisted of rpt_rec_num, provider_ccn, and Year. This connects the datasets Provider Information and Cost Reports. We were able to conduct a thorough examination of financial performance alongside operational and quality measures. 

Provider Info, Health Deficiencies, Quality Measurements, Penalties

All remaining files provided concerning provider information (including the CSV files for Provider Info, Health Deficiencies, Quality Measurements, Penalties) contain important categorical data about the nature of the nursing home industry. The process to clean and prepare these files was centered around making them usable for categorization models, assessing the quality of care provided.

Each CSV, much like the cost reports, was divided into the previously mentioned categories and then by year. Our team, prior to performing any processing, assessed the dictionaries for the datasets and determined which columns within each were of interest and worth keeping.

Provider Information

The first step in processing the data collection was inserting a column in each CSV with the year of the file (ex, ProviderInfo_2015.CSV has a new column, [Year] with data value = “2015”). It was also noted that the COVID-19 years, 2020-2021, had more columns and different names for parallel columns. The next step was to adjust the column titles so that the formatting was consistent for both coding and data preparation (in this case, selecting columns with desired data) purposes; the new columns of the COVID-19 years CSV files would be addressed later. It was decided that in order to properly measure the potential differences between the pre-COVID-19 years CSV files and the COVID-19 years CSV files, any collation needed to first produce two files for separate analysis (one for the range 2015-2019 and the other for the range 2020-2021) for each category. With all the categories collated around the year range, the next step was to select and begin modifying the base file, the anchor to which the other files would join when merging.

The CSV files for Provider Information were the perfect candidate(s) for the base file, setting the primary keys for all the data sets as provider federal number [Provnum] and year of the instance [Year]. The first task was to select the previously determined relevant columns to keep. The next step was an assessment to find any null values and determine the distributions of the columns, if it was necessary to fill the nulls. Upon viewing the nulls reports, and in proportion to the total size of the data sets, a maximum of 3016 nulls (3.87%) within a total of 78025 data values in the PreCOVID-19 files and a maximum of 4545 nulls (14.85%) within a total of 30612 data values in the COVID-19 files being removed would not disrupt the distributions of the existing columns. IQR was also applied to all numeric values to reduce the number of outliers in the data, which brought down the data value counts to 32779 and 11033, respectively. This reduction of data values in the interim is recognized as being meaningfully substantive and potentially a problem for properly assessing the ability of the data set to properly reflect information about the providers. This deduction is important because while the distributions were more or less normalized, any risk of outliers reducing the effectiveness of the model must be reduced. Later on, before the completion of the data preparation, more instances will be added as means to cover for missing information.

Deficiencies

The next datasets to prepare were the Deficiencies. which marks the type of citations a provider will receive for issues that the provider will have (i.e., fire safety, health procedures, health inspection failures, etc.). This dataset does have a collection of data that might be important if assessing the capabilities and efficacy of a particular provider, however, for our team’s purposes, there is a need for reduction. Functionally, an investor at this point in time trying to better understand the industry only needs to understand how many times this is an occurrence and if the quantity of these citations has been increasing over time. That is why it was decided to create a new column [DeficiencyCount], which aggregated the number of times a deficiency occurred for a provider within a year. This was performed via a loop that used [deficiency tag] to form the counts. What remained was the composite primary key and [DeficiencyCount]. This was then inner-joined with the previous provider info dataset, producing a new base file. When merging, the data types for the composite keys need to match, and so they are casted as strings while the merge occurs.

Quality Measurement

Centers for Medicare & Medicaid Services (CMS) performs an assessment of each provider every year and calculates their measure scores and determines the measure average. Measures are incidents of note, both positive and negative, that occur and are reported during a year. Amongst the variables within the dataset, the most important are the measure descriptions/code, the stay type, the measure scores, and the measure average.

There are multiple instances a provider can have per year, and CMS measures each of them. Given the way we wanted to structure our dataset with the composite keys and how we wanted to conduct analysis, the number of rows had to be reduced so that there was only one instance per provider per year. The way to do this was by means of consolidating, in particular, combining both [stay_type] and [measure_description]. Running through a for loop, it would assess the stay type of the instance and delegate each stay into its own category. Then, the measure scores for a provider for a year would be summed, and the average would be calculated. If this average was greater than a preset threshold of 20, it would be considered a positive measure or else not (marked by adding to a count). With these aggregations performed, the file would be inner-joined again to the base file.

Penalties

Providers incur penalties and fines depending on the nature of the deficiencies. Similar to the deficiencies, all that is needed for an investor to understand is the number of penalties a provider incurs and the dollar amount of fines a provider has incurred within a year. A for loop performs both the counting of the penalties and the summing of the fines. Lastly, the file is merged with the base file. In this instance, though, the pre-COVID-19 files did not provide enough material to use in predictive modelling, so the information was removed.

Final Data Preparation

With all the category files combined into one, each for both ranges, the final data preparation can be made to help better assess the provider information. The team decided it was best to create dummy variables for the following columns: 
[ownership_type] = data was reduced to only include government, Nonprofit, and for-profit
[CERTIFICATION] = includes Medicaid, Medicare, and both
[ZIPREGION] = reduction of Zip Code to its region (first digit)
[Score_High] = Target Variable

Centers for Medicare & Medicaid Services (CMS) include a rating system that scores providers each year on a scale from 1-5. The target variable needs to be a binary which assesses whether or not a provider scores high; in this case, a score above 3 is high (1 = True, 0 = False).

The final step was that there were some instances that were missing, specifically years for each provider (in particular, the pre-COVID-19 years), which needed imputation. Using a for loop grouping by provider federal number, the provider years would be checked against the range included in a list and if the year did not exist it would be filled with the median values of that provider (ex: Pr#15014 is missing two years from the range, inserts two rows for the missing years with values that correspond with the median values for that provider).

Thus, the dataset is ready for categorical modeling and analysis.

Diagnostics

Prior to moving on to more complex modeling, we first assessed the overall financial performance of U.S. nursing facilities between 2015 and 2021. Standardized net income per discharge (Z-score) and average operating expense per discharge (in USD) are two important metrics that we compared in Appendix 15. According to the analysis, net income showed a rather steady rising trend through 2018, but starting in 2019, when COVID-19-related factors began to increase, it started to decrease sharply. Operating costs also showed a declining trend over the same period, most likely as a result of both operational reductions and a decrease in patient volume. The steady correlation between these two patterns implies that, particularly during and after the pandemic, financial performance has become more unpredictable and less sustainable in recent years.
