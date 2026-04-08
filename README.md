#  Authentication Log Analysis & Risk Insights

##  Overview

With the increasing reliance on digital systems, monitoring authentication activity has become critical for detecting security threats such as brute-force attacks, unauthorized access attempts, and abnormal user behavior.

This project presents a data-driven approach to analyzing authentication logs by transforming raw log data into meaningful insights. It leverages Python-based data processing techniques to examine access patterns, compute failure rates, and identify potentially suspicious users and IP addresses.

The analysis involves data cleaning, feature engineering, and aggregation to uncover hidden trends in login behavior. Since the dataset does not contain explicit authentication outcomes, additional attributes such as login status and timestamps are simulated to enable realistic analysis.

The project generates structured reports and visualizations that help in understanding system access patterns and highlighting high-risk entities. It serves as a foundational implementation of log analysis and can be extended into real-world cybersecurity monitoring systems.


---

##  Key Features

* 📊 User-level failure rate analysis
* 🌐 IP-level risk detection
* 🚨 Identification of suspicious users/IPs
* 📈 Multiple visualizations (Bar, Pie, Line charts)
* 📄 Automated report generation (CSV files)

---

## Tech Stack

* **Python**
* **Pandas** – Data manipulation
* **Matplotlib** – Data visualization

---

## Project Structure

```
Authentication log analysis/
│── data/                  # Input dataset (Kaggle)
│── scripts/               # Analysis scripts
│── output/                # Generated reports & charts
│── README.md
│── requirements.txt
```

---

## Outputs

### Reports Generated

* `user_report.csv` – User-level statistics
* `ip_report.csv` – IP-level statistics
* `suspicious_users.csv` – High-risk users/IPs
* `ip_frequency.csv` – Most active IP addresses

### Visualizations

* **User Failure Rates** → Bar Chart
* **IP Failure Rates** → Pie Chart
* **IP Activity Frequency** → Line Chart

---

## Dataset

The dataset used in this project is sourced from **Kaggle** and contains client-hostname mapping data.
Since the dataset does not include authentication fields, additional attributes such as login status and timestamps are simulated for analysis.

---

## Methodology

* Data cleaning and preprocessing
* Feature engineering (status, timestamps)
* Aggregation using group-by operations
* Failure rate computation
* Risk threshold-based detection
* Visualization of insights

---

## Future Enhancements

* Integration with real authentication datasets
* Time-based attack pattern analysis
* Interactive dashboard using Streamlit
* Machine learning-based anomaly detection


## 📌 Note

This project is intended for learning and demonstration purposes in cybersecurity and data analysis.
