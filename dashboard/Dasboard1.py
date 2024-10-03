import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import urllib
from func import DataAnalyzer, BrazilMapPlotter

sns.set(style='whitegrid')

# Dataset
datetime_cols = ["order_approved_at", "order_delivered_carrier_date", "order_delivered_customer_date", "order_estimated_delivery_date", "order_purchase_timestamp", "shipping_limit_date"]
all_df = pd.read_csv("https://raw.githubusercontent.com/NerissaNikmatul/E-Commerce-/main/df.csv")
all_df.sort_values(by="order_approved_at", inplace=True)
all_df.reset_index(inplace=True)

# Geolocation Dataset
geolocation = pd.read_csv('https://raw.githubusercontent.com/NerissaNikmatul/E-Commerce-/main/geolocation.csv')
data = geolocation.drop_duplicates(subset='customer_unique_id')

for col in datetime_cols:
    all_df[col] = pd.to_datetime(all_df[col])

min_date = all_df["order_approved_at"].min()
max_date = all_df["order_approved_at"].max()

# Sidebar
st.sidebar.title("E-Commerce Dashboard")

# Date Range
start_date, end_date = st.sidebar.date_input(
    label="Select Date Range",
    value=[min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

# Main
main_df = all_df[(all_df["order_approved_at"] >= str(start_date)) & 
                 (all_df["order_approved_at"] <= str(end_date))]

function = DataAnalyzer(main_df)
map_plot = BrazilMapPlotter(data, plt, urllib, st)

daily_orders_df = function.create_daily_orders_df()
sum_spend_df = function.create_sum_spend_df()
sum_order_items_df = function.create_sum_order_items_df()
review_score, common_score = function.review_score_df()
order_status, common_status = function.create_order_status()

# Title and Overview Section
st.title("E-Commerce Public Data Analysis")
st.write("This dashboard provides insights from E-Commerce public data.")

# Metrics at a Glance
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Orders", f"{daily_orders_df['order_count'].sum()}")
with col2:
    st.metric("Total Revenue", f"{daily_orders_df['revenue'].sum()}")
with col3:
    st.metric("Average Spend", f"{sum_spend_df['total_spend'].mean():.2f}")

# Daily Orders Delivered - Switched to Bar Chart for variety
st.subheader("Daily Orders Delivered")
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x=daily_orders_df["order_approved_at"], 
            y=daily_orders_df["order_count"], 
            color="#90CAF9", ax=ax)
ax.set_xlabel("Order Date")
ax.set_ylabel("Order Count")
ax.tick_params(axis="x", rotation=45)
st.pyplot(fig)

# Customer Spend Money - Line Plot with points highlighted
st.subheader("Customer Spend Money")
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(data=sum_spend_df, x="order_approved_at", y="total_spend", marker="o", linewidth=2, color="#FFA726")
ax.set_xlabel("Order Date")
ax.set_ylabel("Total Spend")
ax.tick_params(axis="x", rotation=45)
st.pyplot(fig)

# Order Items - Stacked Bar Chart
st.subheader("Order Items")
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

sns.barplot(x="product_count", y="product_category_name_english", data=sum_order_items_df.head(5), palette="coolwarm", ax=ax1)
ax1.set_title("Most Sold Products")
ax1.set_xlabel("Number of Sales")

sns.barplot(x="product_count", y="product_category_name_english", data=sum_order_items_df.sort_values(by="product_count").head(5), palette="coolwarm", ax=ax2)
ax2.set_title("Fewest Products Sold")
ax2.set_xlabel("Number of Sales")
ax2.yaxis.set_label_position("right")
ax2.yaxis.tick_right()

st.pyplot(fig)

# Review Score - Pie Chart for Variation
st.subheader("Review Score")
col1, col2 = st.columns(2)

with col1:
    avg_review_score = review_score.mean()
    st.markdown(f"Average Review Score: **{avg_review_score:.2f}**")

with col2:
    most_common_review_score = review_score.value_counts().idxmax()
    st.markdown(f"Most Common Review Score: **{most_common_review_score}**")

fig, ax = plt.subplots(figsize=(8, 6))
review_counts = review_score.value_counts()
ax.pie(review_counts, labels=review_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("viridis", len(review_counts)))
ax.set_title("Distribution of Review Scores")
st.pyplot(fig)

# Footer
st.caption("Data analysis and dashboard created by Nerissa Nikmatul Qoiriyah, 2024.")
