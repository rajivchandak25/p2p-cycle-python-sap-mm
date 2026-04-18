# ============================================================
# PROJECT: Simulation of Procure-to-Pay (P2P) Cycle
#          using Python, SQL, and Data Analysis (SAP MM Inspired)
# Student: Om Shukla | KIIT University, Bhubaneswar
# Tools  : Python (Pandas, Matplotlib, SQLite)
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import sqlite3
import os

# Create output folders
os.makedirs("data", exist_ok=True)
os.makedirs("charts", exist_ok=True)

print("=" * 60)
print("  SAP MM Inspired: Procure-to-Pay (P2P) Simulation")
print("  Student: Om Shukla | KIIT University, Bhubaneswar")
print("=" * 60)

# ============================================================
# STEP 1: VENDOR CREATION (SAP T-Code: XK01)
# ============================================================
print("\n--- STEP 1: Vendor Master Data ---")

vendors = pd.DataFrame({
    "vendor_id":   ["V001", "V002", "V003", "V004"],
    "vendor_name": [
        "TechSupply Pvt Ltd",
        "InfraGoods Corporation",
        "QuickParts India",
        "SmartBuy Wholesale"
    ],
    "city":        ["Mumbai", "Pune", "Delhi", "Bangalore"],
    "category":    ["Electronics", "Hardware", "Components", "Mixed"],
    "payment_terms": ["Net 30", "Net 45", "Net 30", "Net 60"],
    "rating":      [4.5, 4.2, 3.9, 4.7]
})

print("\nVendor Master Table (SAP XK01 equivalent):")
print(vendors.to_string(index=False))
vendors.to_csv("data/vendors.csv", index=False)
print(f"\n[OK] {len(vendors)} vendors created and saved to data/vendors.csv")

# ============================================================
# STEP 2: MATERIAL CREATION (SAP T-Code: MM01)
# ============================================================
print("\n\n--- STEP 2: Material Master Data ---")

materials = pd.DataFrame({
    "material_id":   ["M001", "M002", "M003", "M004", "M005"],
    "material_name": ["Laptop", "Office Chair", "Network Switch", "Keyboard", "Monitor"],
    "category":      ["Electronics", "Furniture", "Networking", "Accessories", "Electronics"],
    "unit_of_measure": ["EA", "EA", "EA", "EA", "EA"],
    "standard_price": [55000, 8500, 12000, 1800, 18000],
    "stock_available": [50, 30, 20, 100, 40]
})

print("\nMaterial Master Table (SAP MM01 equivalent):")
print(materials.to_string(index=False))
materials.to_csv("data/materials.csv", index=False)
print(f"\n[OK] {len(materials)} materials created and saved to data/materials.csv")

# ============================================================
# STEP 3: PURCHASE REQUISITION (SAP T-Code: ME51N)
# ============================================================
print("\n\n--- STEP 3: Purchase Requisitions ---")

purchase_requisitions = pd.DataFrame({
    "pr_id":        ["PR1001", "PR1002", "PR1003", "PR1004", "PR1005", "PR1006"],
    "pr_date":      ["2024-01-05", "2024-02-10", "2024-03-08",
                     "2024-04-15", "2024-05-20", "2024-06-12"],
    "material_id":  ["M001", "M002", "M003", "M001", "M004", "M005"],
    "quantity":     [5, 10, 4, 3, 20, 6],
    "department":   ["IT Dept", "Admin", "Networking", "IT Dept", "Operations", "Finance"],
    "requested_by": ["Rohan Mehta", "Priya Sharma", "Amit Joshi",
                     "Rohan Mehta", "Neha Gupta", "Suresh Patel"],
    "status":       ["Approved", "Approved", "Approved",
                     "Approved", "Approved", "Approved"]
})

print("\nPurchase Requisition Table (SAP ME51N equivalent):")
print(purchase_requisitions.to_string(index=False))
purchase_requisitions.to_csv("data/purchase_requisitions.csv", index=False)
print(f"\n[OK] {len(purchase_requisitions)} PRs created and saved to data/purchase_requisitions.csv")

# ============================================================
# STEP 4: PURCHASE ORDER (SAP T-Code: ME21N)
# ============================================================
print("\n\n--- STEP 4: Purchase Orders ---")

purchase_orders = pd.DataFrame({
    "po_id":       ["PO2001", "PO2002", "PO2003", "PO2004", "PO2005", "PO2006"],
    "po_date":     ["2024-01-10", "2024-02-14", "2024-03-12",
                    "2024-04-18", "2024-05-22", "2024-06-15"],
    "pr_id":       ["PR1001", "PR1002", "PR1003", "PR1004", "PR1005", "PR1006"],
    "vendor_id":   ["V001", "V003", "V002", "V001", "V004", "V001"],
    "material_id": ["M001", "M002", "M003", "M001", "M004", "M005"],
    "quantity":    [5, 10, 4, 3, 20, 6],
    "unit_price":  [55000, 8500, 12000, 55000, 1800, 18000],
    "total_amount":[275000, 85000, 48000, 165000, 36000, 108000],
    "month":       ["January", "February", "March", "April", "May", "June"]
})

print("\nPurchase Order Table (SAP ME21N equivalent):")
print(purchase_orders.to_string(index=False))
purchase_orders.to_csv("data/purchase_orders.csv", index=False)
print(f"\n[OK] {len(purchase_orders)} POs created and saved to data/purchase_orders.csv")

# ============================================================
# STEP 5: GOODS RECEIPT (SAP T-Code: MIGO)
# ============================================================
print("\n\n--- STEP 5: Goods Receipts ---")

goods_receipts = pd.DataFrame({
    "gr_id":           ["GR3001", "GR3002", "GR3003", "GR3004", "GR3005", "GR3006"],
    "gr_date":         ["2024-01-18", "2024-02-20", "2024-03-19",
                        "2024-04-25", "2024-05-28", "2024-06-22"],
    "po_id":           ["PO2001", "PO2002", "PO2003", "PO2004", "PO2005", "PO2006"],
    "material_id":     ["M001", "M002", "M003", "M001", "M004", "M005"],
    "received_qty":    [5, 10, 4, 3, 20, 6],
    "condition":       ["Good", "Good", "Good", "Good", "Good", "Good"],
    "received_by":     ["Warehouse A", "Warehouse B", "Warehouse A",
                        "Warehouse A", "Warehouse B", "Warehouse B"],
    "movement_type":   ["101", "101", "101", "101", "101", "101"]
})

print("\nGoods Receipt Table (SAP MIGO equivalent):")
print(goods_receipts.to_string(index=False))
goods_receipts.to_csv("data/goods_receipts.csv", index=False)
print(f"\n[OK] {len(goods_receipts)} GRs created and saved to data/goods_receipts.csv")

# ============================================================
# STEP 6: INVOICE GENERATION (SAP T-Code: MIRO)
# ============================================================
print("\n\n--- STEP 6: Vendor Invoices ---")

invoices = pd.DataFrame({
    "invoice_id":    ["INV4001", "INV4002", "INV4003", "INV4004", "INV4005", "INV4006"],
    "invoice_date":  ["2024-01-22", "2024-02-26", "2024-03-25",
                      "2024-04-30", "2024-06-03", "2024-06-27"],
    "po_id":         ["PO2001", "PO2002", "PO2003", "PO2004", "PO2005", "PO2006"],
    "vendor_id":     ["V001", "V003", "V002", "V001", "V004", "V001"],
    "base_amount":   [275000, 85000, 48000, 165000, 36000, 108000],
    "gst_18pct":     [49500,  15300,  8640,  29700,  6480,  19440],
    "total_invoice": [324500, 100300, 56640, 194700, 42480, 127440],
    "payment_status":["Paid", "Paid", "Paid", "Paid", "Pending", "Paid"]
})

print("\nInvoice Table (SAP MIRO equivalent):")
print(invoices.to_string(index=False))
invoices.to_csv("data/invoices.csv", index=False)
print(f"\n[OK] {len(invoices)} invoices created and saved to data/invoices.csv")

# ============================================================
# STEP 7: SQL ANALYSIS using SQLite
# ============================================================
print("\n\n--- STEP 7: SQL Analysis (SQLite) ---")

conn = sqlite3.connect(":memory:")
purchase_orders.to_sql("purchase_orders", conn, index=False, if_exists="replace")
vendors.to_sql("vendors", conn, index=False, if_exists="replace")
invoices.to_sql("invoices", conn, index=False, if_exists="replace")
materials.to_sql("materials", conn, index=False, if_exists="replace")

# SQL Query 1: Total Procurement Cost
q1 = "SELECT SUM(total_amount) AS total_procurement_cost FROM purchase_orders;"
result1 = pd.read_sql(q1, conn)
print("\nSQL Q1 - Total Procurement Cost:")
print(result1.to_string(index=False))

# SQL Query 2: Spending by Vendor
q2 = """
SELECT v.vendor_name, SUM(p.total_amount) AS total_spent
FROM purchase_orders p
JOIN vendors v ON p.vendor_id = v.vendor_id
GROUP BY v.vendor_name
ORDER BY total_spent DESC;
"""
result2 = pd.read_sql(q2, conn)
print("\nSQL Q2 - Spending by Vendor:")
print(result2.to_string(index=False))

# SQL Query 3: Top Material by Quantity
q3 = """
SELECT m.material_name, SUM(p.quantity) AS total_qty, SUM(p.total_amount) AS total_value
FROM purchase_orders p
JOIN materials m ON p.material_id = m.material_id
GROUP BY m.material_name
ORDER BY total_value DESC;
"""
result3 = pd.read_sql(q3, conn)
print("\nSQL Q3 - Material-wise Procurement (by value):")
print(result3.to_string(index=False))

# SQL Query 4: Monthly Spending
q4 = "SELECT month, total_amount FROM purchase_orders ORDER BY po_id;"
result4 = pd.read_sql(q4, conn)
print("\nSQL Q4 - Monthly Spending Trend:")
print(result4.to_string(index=False))

conn.close()

# ============================================================
# STEP 8: PANDAS ANALYSIS
# ============================================================
print("\n\n--- STEP 8: Pandas Analysis ---")

total_cost = purchase_orders["total_amount"].sum()
print(f"\nTotal Procurement Cost  : Rs.{total_cost:,.0f}")

top_vendor_id = purchase_orders.groupby("vendor_id")["total_amount"].sum().idxmax()
top_vendor_name = vendors[vendors["vendor_id"] == top_vendor_id]["vendor_name"].values[0]
top_vendor_spend = purchase_orders.groupby("vendor_id")["total_amount"].sum().max()
print(f"Top Vendor              : {top_vendor_name} (Rs.{top_vendor_spend:,.0f})")

top_material_id = purchase_orders.groupby("material_id")["total_amount"].sum().idxmax()
top_material_name = materials[materials["material_id"] == top_material_id]["material_name"].values[0]
print(f"Most Purchased Material : {top_material_name} (by total spend)")

avg_po_value = purchase_orders["total_amount"].mean()
print(f"Average PO Value        : Rs.{avg_po_value:,.0f}")

paid_invoices = invoices[invoices["payment_status"] == "Paid"]["total_invoice"].sum()
pending_invoices = invoices[invoices["payment_status"] == "Pending"]["total_invoice"].sum()
print(f"Total Invoiced (Paid)   : Rs.{paid_invoices:,.0f}")
print(f"Total Invoiced (Pending): Rs.{pending_invoices:,.0f}")

# ============================================================
# STEP 9: DATA VISUALIZATIONS
# ============================================================
print("\n\n--- STEP 9: Generating Charts ---")

COLORS = ["#1F4E79", "#2E75B6", "#9DC3E6", "#BDD7EE", "#DEEAF1"]
plt.rcParams["font.family"] = "DejaVu Sans"

# --- Chart 1: Vendor-wise Spending (Bar Chart) ---
vendor_spend = purchase_orders.groupby("vendor_id")["total_amount"].sum().reset_index()
vendor_spend = vendor_spend.merge(vendors[["vendor_id","vendor_name"]], on="vendor_id")
vendor_spend = vendor_spend.sort_values("total_amount", ascending=False)

fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(vendor_spend["vendor_name"], vendor_spend["total_amount"],
              color=COLORS[:len(vendor_spend)], edgecolor="white", linewidth=0.8)
for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 3000,
            f"Rs.{bar.get_height()/1000:.0f}K", ha="center", va="bottom",
            fontsize=10, fontweight="bold", color="#1F4E79")
ax.set_title("Vendor-wise Procurement Spending", fontsize=14, fontweight="bold",
             color="#1F4E79", pad=15)
ax.set_xlabel("Vendor Name", fontsize=11)
ax.set_ylabel("Total Amount (Rs.)", fontsize=11)
ax.set_ylim(0, 620000)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"Rs.{x/1000:.0f}K"))
ax.spines[["top","right"]].set_visible(False)
ax.tick_params(axis="x", rotation=10)
plt.tight_layout()
plt.savefig("charts/chart1_vendor_spending.png", dpi=150, bbox_inches="tight")
plt.close()
print("[OK] Chart 1 saved: charts/chart1_vendor_spending.png")

# --- Chart 2: Category-wise Budget Split (Pie Chart) ---
cat_spend = purchase_orders.merge(materials[["material_id","category"]], on="material_id")
cat_totals = cat_spend.groupby("category")["total_amount"].sum()

fig, ax = plt.subplots(figsize=(7, 6))
wedge_colors = ["#1F4E79","#2E75B6","#9DC3E6","#BDD7EE"]
wedges, texts, autotexts = ax.pie(
    cat_totals.values, labels=cat_totals.index,
    autopct="%1.1f%%", colors=wedge_colors,
    startangle=140, pctdistance=0.75,
    wedgeprops={"edgecolor":"white","linewidth":2}
)
for t in autotexts:
    t.set_fontsize(11); t.set_fontweight("bold"); t.set_color("white")
ax.set_title("Category-wise Procurement Budget Split",
             fontsize=13, fontweight="bold", color="#1F4E79", pad=15)
plt.tight_layout()
plt.savefig("charts/chart2_category_split.png", dpi=150, bbox_inches="tight")
plt.close()
print("[OK] Chart 2 saved: charts/chart2_category_split.png")

# --- Chart 3: Monthly Spending Trend (Line Chart) ---
month_order = ["January","February","March","April","May","June"]
purchase_orders["month"] = pd.Categorical(purchase_orders["month"],
                                          categories=month_order, ordered=True)
monthly = purchase_orders.sort_values("month").groupby("month")["total_amount"].sum()

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(monthly.index, monthly.values, marker="o", linewidth=2.5,
        markersize=8, color="#1F4E79", markerfacecolor="#2E75B6",
        markeredgecolor="#1F4E79", markeredgewidth=1.5)
ax.fill_between(range(len(monthly)), monthly.values, alpha=0.15, color="#2E75B6")
for i, (m, v) in enumerate(zip(monthly.index, monthly.values)):
    ax.annotate(f"Rs.{v/1000:.0f}K", (i, v), textcoords="offset points",
                xytext=(0, 12), ha="center", fontsize=9.5,
                fontweight="bold", color="#1F4E79")
ax.set_xticks(range(len(monthly)))
ax.set_xticklabels(monthly.index, rotation=15)
ax.set_title("Monthly Procurement Spending Trend (2024)",
             fontsize=14, fontweight="bold", color="#1F4E79", pad=15)
ax.set_ylabel("Total Spending (Rs.)", fontsize=11)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"Rs.{x/1000:.0f}K"))
ax.spines[["top","right"]].set_visible(False)
ax.set_ylim(0, 330000)
plt.tight_layout()
plt.savefig("charts/chart3_monthly_trend.png", dpi=150, bbox_inches="tight")
plt.close()
print("[OK] Chart 3 saved: charts/chart3_monthly_trend.png")

# --- Chart 4: Material-wise Spend (Horizontal Bar) ---
mat_spend = purchase_orders.merge(materials[["material_id","material_name"]], on="material_id")
mat_totals = mat_spend.groupby("material_name")["total_amount"].sum().sort_values()

fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.barh(mat_totals.index, mat_totals.values,
               color=COLORS[:len(mat_totals)][::-1], edgecolor="white")
for bar in bars:
    ax.text(bar.get_width() + 3000, bar.get_y() + bar.get_height()/2,
            f"Rs.{bar.get_width()/1000:.0f}K",
            va="center", fontsize=10, fontweight="bold", color="#1F4E79")
ax.set_title("Material-wise Procurement Value",
             fontsize=14, fontweight="bold", color="#1F4E79", pad=15)
ax.set_xlabel("Total Spend (Rs.)", fontsize=11)
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"Rs.{x/1000:.0f}K"))
ax.spines[["top","right"]].set_visible(False)
ax.set_xlim(0, 530000)
plt.tight_layout()
plt.savefig("charts/chart4_material_spend.png", dpi=150, bbox_inches="tight")
plt.close()
print("[OK] Chart 4 saved: charts/chart4_material_spend.png")

# --- Chart 5: Invoice Payment Status (Stacked / Grouped Bar) ---
paid_amt    = invoices[invoices["payment_status"] == "Paid"]["total_invoice"].sum()
pending_amt = invoices[invoices["payment_status"] == "Pending"]["total_invoice"].sum()

fig, ax = plt.subplots(figsize=(6, 5))
categories = ["Paid", "Pending"]
amounts = [paid_amt, pending_amt]
bar_colors = ["#1F4E79", "#BDD7EE"]
bars = ax.bar(categories, amounts, color=bar_colors, width=0.4, edgecolor="white")
for bar, amt in zip(bars, amounts):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 3000,
            f"Rs.{amt/1000:.1f}K", ha="center", va="bottom",
            fontsize=11, fontweight="bold", color="#1F4E79")
ax.set_title("Invoice Payment Status Summary",
             fontsize=13, fontweight="bold", color="#1F4E79", pad=15)
ax.set_ylabel("Total Invoice Value (Rs.)", fontsize=11)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"Rs.{x/1000:.0f}K"))
ax.spines[["top","right"]].set_visible(False)
ax.set_ylim(0, 850000)
plt.tight_layout()
plt.savefig("charts/chart5_invoice_status.png", dpi=150, bbox_inches="tight")
plt.close()
print("[OK] Chart 5 saved: charts/chart5_invoice_status.png")

# ============================================================
# FINAL SUMMARY
# ============================================================
print("\n" + "=" * 60)
print("  FINAL SUMMARY - P2P SIMULATION COMPLETE")
print("=" * 60)
print(f"  Vendors Created         : {len(vendors)}")
print(f"  Materials Created       : {len(materials)}")
print(f"  Purchase Requisitions   : {len(purchase_requisitions)}")
print(f"  Purchase Orders         : {len(purchase_orders)}")
print(f"  Goods Receipts          : {len(goods_receipts)}")
print(f"  Invoices Generated      : {len(invoices)}")
print(f"  Total Procurement Cost  : Rs.{total_cost:,.0f}")
print(f"  Top Vendor              : {top_vendor_name}")
print(f"  Most Purchased Material : {top_material_name}")
print(f"  Charts Generated        : 5")
print("=" * 60)
print("\n[DONE] All files saved in /data/ and /charts/ folders.")
