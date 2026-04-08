import pandas as pd
import matplotlib.pyplot as plt
import os
import random


# ---------------------------
# SETUP
# ---------------------------

# Create output folder
os.makedirs("output", exist_ok=True)

# Load dataset
df = pd.read_csv("data/client_hostname.csv")

print("Columns in dataset:", df.columns)

# ---------------------------
# DATA CLEANING & PREPARATION
# ---------------------------

# Rename columns
df.rename(columns={
    'client': 'ip_address'
}, inplace=True)

# Create user_id (same as IP)
df['user_id'] = df['ip_address']

# Create fake login status (since dataset doesn't have it)
df['status'] = [random.choice(['success', 'fail']) for _ in range(len(df))]

# Create fake timestamps
df['timestamp'] = pd.date_range(start='2026-01-01', periods=len(df), freq='min')

df['timestamp'] = pd.to_datetime(df['timestamp'])

# ---------------------------
# 1. USER ANALYSIS
# ---------------------------

user_stats = df.groupby('user_id')['status'].value_counts().unstack().fillna(0)

# Handle missing columns safely
user_stats['fail'] = user_stats.get('fail', 0)
user_stats['success'] = user_stats.get('success', 0)

# Calculate failure rate
user_stats['failure_rate'] = user_stats['fail'] / (user_stats['fail'] + user_stats['success'] + 1e-5)

# Sort by highest risk
user_stats = user_stats.sort_values(by='failure_rate', ascending=False)

# Save report
user_stats.to_csv("output/user_report.csv")

print("\n📊 User Report:\n", user_stats.head())


# ---------------------------
# 2. IP ANALYSIS
# ---------------------------

ip_stats = df.groupby('ip_address')['status'].value_counts().unstack().fillna(0)

ip_stats['fail'] = ip_stats.get('fail', 0)
ip_stats['success'] = ip_stats.get('success', 0)

ip_stats['failure_rate'] = ip_stats['fail'] / (ip_stats['fail'] + ip_stats['success'] + 1e-5)

ip_stats = ip_stats.sort_values(by='failure_rate', ascending=False)

# Save report
ip_stats.to_csv("output/ip_report.csv")

print("\n🌐 IP Report:\n", ip_stats.head())


# ---------------------------
# 3. DETECT SUSPICIOUS USERS
# ---------------------------

THRESHOLD = 0.7

suspicious_users = user_stats[user_stats['failure_rate'] > THRESHOLD]

suspicious_users.to_csv("output/suspicious_users.csv")

print("\n🚨 Suspicious Users:\n", suspicious_users)


# ---------------------------
# 4. EXTRA: IP FREQUENCY (BONUS)
# ---------------------------

ip_frequency = df['ip_address'].value_counts()
ip_frequency.to_csv("output/ip_frequency.csv")

print("\n📈 IP Frequency:\n", ip_frequency.head())


# ---------------------------
# 5. VISUALIZATION
# ---------------------------

# 1. USER FAILURE RATE → BAR CHART
user_stats['failure_rate'].head(10).plot(kind='bar', title="Top 10 User Failure Rates")
plt.ylabel("Failure Rate")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/user_failure_rates.png")
plt.clf()


# 2. IP FAILURE RATE → PIE CHART
ip_stats['failure_rate'].head(5).plot(
    kind='pie',
    title="Top 5 IP Failure Rates",
    autopct='%1.1f%%'
)
plt.ylabel("")  # removes default ylabel
plt.tight_layout()
plt.savefig("output/ip_failure_rates.png")
plt.clf()


# 3. IP FREQUENCY → LINE CHART
ip_frequency.head(10).plot(
    kind='line',
    marker='o',
    title="Top 10 Most Active IPs"
)
plt.ylabel("Number of Requests")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/ip_frequency.png")
plt.clf()

print("\n✅ Charts saved with different styles in 'output/' folder")