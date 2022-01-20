# -------------------------------
#Importing Dependencies
# -------------------------------
import os
# Organisation Libraries --------
import pandas as pd

# SQL Libraries -----------------
from sqlalchemy import create_engine
import psycopg2
from sqlalchemy import create_engine
from config import password


# plotly express ----------------
import plotly.express as px

# Importing CSV ----------------------------------------------------------
file_to_load = os.path.join("resources", "multiTimeline.csv")
df = pd.read_csv(file_to_load)
df.head()
print("CSV Read")

df.columns = ["week","home_trends","class_trends"]

# Inserting df into PostgreSQL --------------------------------------------
print("Going to DB")
db_string = f"postgresql://postgres:{password}@127.0.0.1:5432/tempo_proj_db"
engine = create_engine(db_string)
print("Engine Created")
df.to_sql(name="home_v_class", con = engine, if_exists = "replace")
print("Uploaded to DB")

# Querying Data Base ------------------------------------------------------
# psycopg2
print("Pulling From DB")
cn = psycopg2.connect(host = "127.0.0.1", port = "5432", database = "tempo_proj_db", user = "postgres", password = password)
cur = cn.cursor()
cur.execute("Select * FROM home_v_class")
query_results = cur.fetchall()
print("Data Fetched")


# Organizing df for Viz ----------------------------------------------------
print("Organizing New Data")

df = pd.DataFrame(query_results)
df.head()
df.columns = ["dumb", "Date", "Home Gym", "Fitness Class"]
df.drop("dumb", axis =1)

pd.to_datetime(df["Date"])
# column for category
df_melt = df.melt(id_vars = "Date", value_vars = ["Home Gym", "Fitness Class"])
print("Organized New Data")
print(df_melt.head())
# Visualization -------------------------------------------------------------
print("Vizualizing")
tickmode = 'array'
tickvals = []
for date in df_melt["Date"][::4]:
    tickvals.append(date)
fig = px.line(df_melt, x = "Date", y =df_melt["value"], title = "Search Terms: 'Home Gym' v 'Fitness Class'", color = "variable")
fig.show()