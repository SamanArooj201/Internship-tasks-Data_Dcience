import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(page_title="Global Superstore Dashboard", layout="wide")

# Title
st.title("📊 Global Superstore Business Dashboard")
st.markdown("---")

# Load data
@st.cache_data
def load_data():
    df = pd.read_excel(r'D:\InternshipTasksDatasets\global_superstore_2016.xlsx\global_superstore_2016.xlsx')
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("🔍 Filters")

# Region filter
region_options = sorted(df['Region'].unique())
region = st.sidebar.multiselect(
    "Select Region",
    options=region_options,
    default=region_options
)

# Category filter
category_options = sorted(df['Category'].unique())
category = st.sidebar.multiselect(
    "Select Category",
    options=category_options,
    default=category_options
)

# Sub-Category filter
sub_category_options = sorted(df['Sub-Category'].unique())
sub_category = st.sidebar.multiselect(
    "Select Sub-Category",
    options=sub_category_options,
    default=sub_category_options
)

# Apply filters
filtered_df = df[
    (df['Region'].isin(region)) &
    (df['Category'].isin(category)) &
    (df['Sub-Category'].isin(sub_category))
]

# Display KPIs
st.header("📈 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

with col1:
    total_sales = filtered_df['Sales'].sum()
    st.metric("💰 Total Sales", f"${total_sales:,.2f}")

with col2:
    total_profit = filtered_df['Profit'].sum()
    st.metric("💵 Total Profit", f"${total_profit:,.2f}")

with col3:
    avg_profit_margin = (total_profit / total_sales * 100) if total_sales > 0 else 0
    st.metric("📊 Profit Margin", f"{avg_profit_margin:.1f}%")

with col4:
    total_orders = filtered_df['Row ID'].count()
    st.metric("📦 Total Orders", f"{total_orders:,}")

st.markdown("---")

# Charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Sales by Category")
    sales_by_category = filtered_df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(8, 5))
    sales_by_category.plot(kind='bar', ax=ax, color='skyblue')
    ax.set_xlabel('Category')
    ax.set_ylabel('Sales ($)')
    ax.set_title('Total Sales by Category')
    plt.xticks(rotation=45)
    st.pyplot(fig)

with col2:
    st.subheader("📊 Profit by Category")
    profit_by_category = filtered_df.groupby('Category')['Profit'].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(8, 5))
    profit_by_category.plot(kind='bar', ax=ax, color='lightgreen')
    ax.set_xlabel('Category')
    ax.set_ylabel('Profit ($)')
    ax.set_title('Total Profit by Category')
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Top 5 Customers by Sales
st.subheader("🏆 Top 5 Customers by Sales")
top_customers = filtered_df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(5)

fig, ax = plt.subplots(figsize=(10, 6))
top_customers.plot(kind='bar', ax=ax, color='gold')
ax.set_xlabel('Customer Name')
ax.set_ylabel('Sales ($)')
ax.set_title('Top 5 Customers by Sales')
plt.xticks(rotation=45)
st.pyplot(fig)

# Sales trend over time
st.subheader("📅 Sales Trend Over Time")
sales_by_date = filtered_df.groupby('Order Date')['Sales'].sum().reset_index()
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(sales_by_date['Order Date'], sales_by_date['Sales'], color='blue', linewidth=1)
ax.set_xlabel('Order Date')
ax.set_ylabel('Sales ($)')
ax.set_title('Daily Sales Trend')
plt.xticks(rotation=45)
st.pyplot(fig)

# Show filtered data preview
st.markdown("---")
st.subheader("📋 Filtered Data Preview")
st.dataframe(filtered_df[['Order ID', 'Order Date', 'Customer Name', 'Category', 'Sub-Category', 'Sales', 'Profit']].head(100))