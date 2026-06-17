![image alt](https://github.com/gowrivinod/customer-segmentation-ecommerce/blob/6834a0a3ffab684b5308adca82e7032620a10dd6/Photos/Screenshot%202026-06-17%20at%209.52.58%E2%80%AFPM.png)
![image alt](https://github.com/gowrivinod/customer-segmentation-ecommerce/blob/01b902bface7404e40297432f43738cff6d49ac0/Photos/Screenshot%202026-06-17%20at%209.53.22%E2%80%AFPM.png)     
![image alt](https://github.com/gowrivinod/customer-segmentation-ecommerce/blob/01b902bface7404e40297432f43738cff6d49ac0/Photos/Screenshot%202026-06-17%20at%209.53.52%E2%80%AFPM.png)
![image alt](https://github.com/gowrivinod/customer-segmentation-ecommerce/blob/01b902bface7404e40297432f43738cff6d49ac0/Photos/Screenshot%202026-06-17%20at%209.54.09%E2%80%AFPM.png)


# Customer Segmentation Engine

**Project:** Unsupervised ML-based customer segmentation using RFM analysis  
**Dataset:** UK Online Retail Dataset (541,909 transactions, 4,372 customers)  
**Stack:** Python · pandas · scikit-learn · KMeans · DBSCAN · Streamlit

## Business Problem
Retail marketing budgets are wasted on untargeted campaigns. 
This project segments customers by purchase behavior to enable targeted marketing — 
reducing cost while increasing conversion.

## Approach
1. Data cleaning — removed nulls, cancellations, returns
2. RFM feature engineering — Recency, Frequency, Monetary value per customer
3. Log transform + StandardScaler normalization
4. KMeans clustering (k=4 via elbow method)
5. DBSCAN comparison
6. Segment profiling + business recommendations
7. Interactive Streamlit dashboard

## Results
*(to be updated after clustering)*

## How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Results

| Segment | Customers | % Customers | Avg Spend | % Revenue |
|---|---|---|---|---|
| Champions | 802 | 18.7% | £4,198 | 55.6% |
| Loyal Customers | 1,165 | 27.1% | £1,540 | 29.6% |
| New / Promising | 827 | 19.3% | £501 | 6.8% |
| Lost / Hibernating | 1,500 | 34.9% | £324 | 8.0% |

**Key finding:** Champions (18.7% of customers) drive 55.6% of total revenue.  
Reallocating 30% of marketing spend from Lost/Hibernating to Champions + New/Promising = estimated 2–3x campaign ROI.

**DBSCAN comparison:** Found only 2 clusters with 0.8% noise points — confirms KMeans better captures business-meaningful segmentation for this dataset.
