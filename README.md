# Simulation of Procure-to-Pay (P2P) Cycle
### Python | SQL | Pandas | Matplotlib | SAP MM Inspired

**Student:** Om Shukla  
**University:** KIIT University, Bhubaneswar  
**Course:** SAP BCBDC — Data Fundamentals  
**Submission:** April 2026

---

## What This Project Does

This project simulates the complete **Procure-to-Pay (P2P) cycle** — the core process of SAP MM (Materials Management) — using only Python, Pandas, SQLite, and Matplotlib. No SAP GUI access is required.

The P2P cycle includes:

| SAP Step | SAP T-Code | This Project |
|---|---|---|
| Vendor Creation | XK01 | `vendors` DataFrame |
| Material Creation | MM01 | `materials` DataFrame |
| Purchase Requisition | ME51N | `purchase_requisitions` DataFrame |
| Purchase Order | ME21N | `purchase_orders` DataFrame |
| Goods Receipt | MIGO | `goods_receipts` DataFrame |
| Invoice Verification | MIRO | `invoices` DataFrame with 18% GST |

---

## How to Run

### Step 1: Install Dependencies
```bash
pip install pandas matplotlib
```

### Step 2: Run the Main File
```bash
python p2p_simulation.py
```

### Step 3: View Outputs
- All CSV files → `data/` folder
- All charts → `charts/` folder
- Full report → `P2P_Project_Report_OmShukla.docx`

---

## Key Results

| Metric | Value |
|---|---|
| Total Procurement Cost | Rs. 7,17,000 |
| Top Vendor | TechSupply Pvt Ltd (Rs. 5,48,000) |
| Top Material | Laptop (Rs. 4,40,000 — 61% of budget) |
| Top Month | January (Rs. 2,75,000) |
| Invoices Paid | Rs. 8,03,580 (95%) |
| Invoices Pending | Rs. 42,480 (INV4005) |

---

## Folder Structure

```
p2p_project/
├── p2p_simulation.py          ← Run this file
├── README.md
├── data/
│   ├── vendors.csv
│   ├── materials.csv
│   ├── purchase_requisitions.csv
│   ├── purchase_orders.csv
│   ├── goods_receipts.csv
│   └── invoices.csv
└── charts/
    ├── chart1_vendor_spending.png
    ├── chart2_category_split.png
    ├── chart3_monthly_trend.png
    ├── chart4_material_spend.png
    └── chart5_invoice_status.png
```

---

## Charts Generated

1. **Chart 1** — Vendor-wise Procurement Spending (Bar Chart)
2. **Chart 2** — Category-wise Budget Split (Pie Chart)
3. **Chart 3** — Monthly Spending Trend Jan–Jun 2024 (Line Chart)
4. **Chart 4** — Material-wise Procurement Value (Horizontal Bar)
5. **Chart 5** — Invoice Payment Status — Paid vs Pending (Bar Chart)

---

## Tech Stack

- **Python 3.11+** — Core language
- **Pandas** — Data creation and analysis
- **Matplotlib** — Visualizations
- **SQLite3** — In-memory SQL queries (built into Python)
- **VS Code** — Development environment

---

## Business Recommendations (from Analysis)

1. Diversify vendor base — TechSupply Pvt Ltd holds 76% of spending (concentration risk)
2. Clear pending invoice INV4005 from SmartBuy Wholesale (Rs. 42,480)
3. Consolidate Laptop POs quarterly to negotiate volume discounts
4. Pre-approve January and April budgets — peak procurement months
5. Use blanket POs for Keyboards and Accessories to reduce admin effort

---

*Project submitted for SAP BCBDC Data Fundamentals Course — KIIT University, Bhubaneswar*
