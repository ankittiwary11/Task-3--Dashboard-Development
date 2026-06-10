# Task 3 — Dashboard Development

**Internship:** CodTech IT Solutions Pvt. Ltd.

**Domain:** Data Analytics

**Intern Name:** Ankit Tiwary

**Intern ID:** CITS538

**Mentor:** Neela Santhosh Kumar

**Duration:** 4 Weeks

---

## 📌 Task Overview

Build an **interactive, multi-chart analytical dashboard** using Python and Dash (Plotly) that allows users to explore a sales dataset through dynamic filters and visualisations.

---

## 🛠️ Technologies Used

| Tool / Library | Purpose |
|---|---|
| Python 3.14.5 | Core programming language |
| Dash 2.17 | Web dashboard framework |
| Plotly 5.22 | Interactive chart library |
| Pandas 2.2 | Data loading and transformation |

---

## 📂 Project Structure

```
Task-3-Dashboard/
│
├── dashboard.py        # Main Dash application (all charts + callbacks)
├── sales_data.csv      # Dataset — 120 rows of retail sales records
└── README.md           # Project documentation (this file)
```

---

## 📊 Dataset Description

**File:** `sales_data.csv`
**Records:** 120 rows | **Columns:** 10

| Column | Description |
|---|---|
| Date | Transaction date (2024) |
| Region | North / South / East / West |
| Category | Electronics / Furniture / Office Supplies |
| Product | Laptop, Mobile Phone, Chair, Desk, etc. |
| Sales | Revenue in INR (₹) |
| Profit | Profit in INR (₹) |
| Quantity | Units sold |
| Customer_Segment | Corporate / Consumer / Home Office |
| Month | Derived — year-month string |
| Profit_Margin | Derived — profit as % of sales |

---

## 📈 Dashboard Features

### 🔽 Interactive Filters (Dropdowns)
- **Region** — Filter all charts by geographic region
- **Category** — Filter by product category
- **Customer Segment** — Filter by business segment

### 📌 KPI Cards (auto-update on filter change)
- 💰 Total Sales (₹)
- 📈 Total Profit (₹)
- 🛒 Total Orders (count)
- 🎯 Average Profit Margin (%)

### 📉 Charts
1. **Line Chart** — Monthly Sales & Profit trend over 12 months
2. **Horizontal Bar Chart** — Sales comparison by Region
3. **Donut Pie Chart** — Sales share by Product Category
4. **Bubble Scatter Plot** — Sales vs Profit (bubble size = Quantity sold)
5. **Heatmap** — Sales intensity across Category × Region matrix

---

## 🚀 How to Run

### Step 1 — Clone or Download the repository
```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd Task-3-Dashboard
```

### Step 2 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 3 — Run the dashboard
```bash
python dashboard.py
```

### Step 4 — Open in browser
```
http://127.0.0.1:8050/
```

> The dashboard will automatically reload if you edit the code while `debug=True`.

---

## 🖼️ Dashboard Preview

> *(Add a screenshot of the running dashboard here before submitting)*
> 
> To take a screenshot: run the app → open `http://127.0.0.1:8050/` in browser → press `Ctrl+Shift+S` or use the Snipping Tool → save as `screenshot.png` in this folder.

---

## 🔑 Key Learnings

- Building multi-page interactive dashboards with **Dash callbacks**
- Creating **linked filters** that update all visualisations simultaneously
- Designing dark-themed, professional UI layouts using inline CSS in Dash
- Data aggregation and transformation with **Pandas** (groupby, pivot_table)
- Using **Plotly Express** and **Plotly Graph Objects** for different chart types

---

*Submitted as part of CodTech IT Solutions Pvt. Ltd. — Data Analytics Virtual Internship*
