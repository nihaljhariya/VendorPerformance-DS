# # import sqlite3

# # conn = sqlite3.connect("inventory.db")
# # cursor = conn.cursor()

# # cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# # tables = cursor.fetchall()

# # for t in tables:
# #     print(t[0])


# import sqlite3
# import pandas as pd

# # Connect to SQLite database
# conn = sqlite3.connect("inventory.db")

# # Load CSVs and write them to the database with correct table names
# # Load CSVs and write them to the database with correct table names
# # pd.read_csv("data/begin_inventory.csv").to_sql("begin_inventory", conn, index=False, if_exists="replace")
# # pd.read_csv("data/end_inventory.csv").to_sql("end_inventory", conn, index=False, if_exists="replace")
# # pd.read_csv("data/purchase_prices.csv").to_sql("purchase_prices", conn, index=False, if_exists="replace")
# # pd.read_csv("data/purchases.csv").to_sql("purchases", conn, index=False, if_exists="replace")
# # pd.read_csv("data/sales.csv").to_sql("sales", conn, index=False, if_exists="replace")
# # pd.read_csv("data/vendor_invoice.csv").to_sql("vendors", conn, index=False, if_exists="replace")  # use vendor_invoice.csv

# # print("✅ All tables loaded successfully.")


# import sqlite3
# import pandas as pd
# conn = sqlite3.connect("inventory.db")
# df = pd.read_sql_query("SELECT * FROM Vendor_sales_Summary LIMIT 10", conn)
# # print(df)

# import pandas as pd

# tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
# print(tables)