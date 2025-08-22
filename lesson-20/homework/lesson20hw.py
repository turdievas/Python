import pandas as pd
import sqlite3
# Connect to chinook database
conn = sqlite3.connect('chinook.db')

# --- 1. CUSTOMER PURCHASES ANALYSIS ---
# Load Customers and Invoices tables (lowercase names)
customers = pd.read_sql_query("SELECT CustomerId, FirstName, LastName FROM customers", conn)
invoices = pd.read_sql_query("SELECT CustomerId, Total FROM invoices", conn)

# Calculate total amount spent per customer
total_spent = invoices.groupby('CustomerId', as_index=False)['Total'].sum()

# Merge to get customer names
customer_spending = pd.merge(total_spent, customers, on='CustomerId')
customer_spending['FullName'] = customer_spending['FirstName'] + ' ' + customer_spending['LastName']

# Top 5 customers by spending
top5_customers = customer_spending.sort_values(by='Total', ascending=False).head(5)


# --- 2. ALBUM vs INDIVIDUAL TRACK PURCHASES ---
# Load necessary tables (lowercase names)
invoice_lines = pd.read_sql_query("SELECT InvoiceLineId, InvoiceId, TrackId FROM invoice_items", conn)
invoices_table = pd.read_sql_query("SELECT InvoiceId, CustomerId FROM invoices", conn)
tracks = pd.read_sql_query("SELECT TrackId, AlbumId FROM tracks", conn)

# Merge to find which customer bought which tracks from which albums
df = invoice_lines.merge(invoices_table, on='InvoiceId').merge(tracks, on='TrackId')

# Count how many tracks are in each album
album_track_count = tracks.groupby('AlbumId')['TrackId'].count().reset_index()
album_track_count.rename(columns={'TrackId':'AlbumTrackCount'}, inplace=True)

# Count how many tracks each customer bought per album
customer_album_count = df.groupby(['CustomerId','AlbumId'])['TrackId'].count().reset_index()
customer_album_count.rename(columns={'TrackId':'TracksBought'}, inplace=True)

# Merge to compare with album's total tracks
merged = customer_album_count.merge(album_track_count, on='AlbumId')
merged['FullAlbumPurchased'] = merged['TracksBought'] == merged['AlbumTrackCount']

# Determine customer preference
customer_pref = merged.groupby('CustomerId')['FullAlbumPurchased'].all().reset_index()
customer_pref['Preference'] = customer_pref['FullAlbumPurchased'].map({True:'Full albums', False:'Individual tracks'})

# Calculate percentage
pref_summary = customer_pref['Preference'].value_counts(normalize=True) * 100

conn.close()


import caas_jupyter_tools
caas_jupyter_tools.display_dataframe_to_user(name="Top 5 Customers by Total Spending", dataframe=top5_customers)
caas_jupyter_tools.display_dataframe_to_user(name="Customer Purchase Preferences (%)", dataframe=pref_summary.to_frame("Percentage"))
