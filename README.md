# Internship-tasks-Data_Dcience

Task 1: Term Deposit Subscription Prediction (Bank Marketing)

Dataset Link

https://archive.ics.uci.edu/dataset/222/bank+marketing

Objective

To predict whether a bank customer will subscribe to a term deposit during a marketing campaign, enabling data-driven targeting and improved campaign efficiency.

Approach

Loaded and explored the Bank Marketing dataset from the UCI Machine Learning Repository.
Performed feature encoding to handle categorical variables.
Trained and compared Logistic Regression and Random Forest classifiers.
Evaluated model performance using Confusion Matrix, F1-Score, and ROC Curve.
Applied SHAP and LIME to interpret individual predictions and enhance model transparency.

Key Insights

The Random Forest model outperformed Logistic Regression, achieving an F1-Score of 0.3407 and an AUC of 0.9135.
The most influential features in predicting subscription were:
Duration of the call
Balance (customer’s account balance)
Age of the customer
Day of the month contacted
Previous outcome (success or failure of prior contacts)
The model’s high AUC score indicates strong discriminatory power, making it effective for identifying potential subscribers.
Business Recommendations
Prioritize customers with high predicted probabilities for future campaigns to maximize conversion rates.
Use model explanations (via SHAP/LIME) to understand customer behavior and tailor communication strategies.
Optimize campaign resources by focusing on segments with the strongest predictive indicators.

Task 2: Customer Segmentation Using Unsupervised Learning

Dataset Link

https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python

Objective

To segment customers based on their spending habits and propose targeted marketing strategies for each cluster, enabling personalized customer engagement and improved resource allocation.

Approach

Conducted Exploratory Data Analysis (EDA) to understand customer behavior patterns across spending scores and annual income.
Applied K-Means Clustering to identify natural customer segments.
Used PCA and t-SNE for dimensionality reduction and visualization of clusters.
Analyzed cluster characteristics to derive actionable marketing strategies.

Key Insights

Optimal number of clusters identified using the elbow method: 5 distinct customer segments.
Key segmentation drivers:
Annual Income
Spending Score (1–100 scale based on spending behavior)
PCA and t-SNE visualizations confirmed clear separation between clusters, validating the segmentation quality.

Business Impact

Enables personalized marketing campaigns tailored to each segment's behavior and preferences.
Improves customer retention by addressing specific needs of each group.
Optimizes marketing spend by focusing resources on high-potential segments.

Task 5: Interactive Business Dashboard in Streamlit

Dataset Link

https://www.kaggle.com/datasets/vivek468/superstore-dataset-final

Objective

To develop an interactive business intelligence dashboard for analyzing sales, profit, and segment-wise performance, enabling stakeholders to explore key metrics dynamically.

Approach

Cleaned and prepared the Global Superstore dataset to ensure data quality and consistency.
Built an interactive Streamlit dashboard with intuitive filters for Region, Category, and Sub-Category.
Designed visualizations to display Key Performance Indicators (KPIs):
Total Sales
Total Profit
Top 5 Customers by Sales
Integrated interactive charts to explore trends and performance across dimensions.

Key Features

Dynamic Filtering: Users can drill down by Region, Category, and Sub-Category to view performance at granular levels.
Real-Time KPIs: Key metrics update instantly based on selected filters.
Top Customer Analysis: Identifies highest-value customers for targeted retention and upselling.
Visual Analytics: Clean, intuitive charts enable quick interpretation of sales and profit trends.

Business Impact

Empowers business users with self-service analytics without requiring technical expertise.
Enables data-driven decision-making for inventory planning, marketing allocation, and customer relationship management.
Serves as a scalable template for embedding analytics into business workflows.
