import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(f"postgresql://{os.environ['PSQL_USER']}@localhost:5432/{os.environ['PSQL_DB']}")

years = range(2000, 2024)
for year in years:
    csv_path = os.path.join(os.path.dirname(__file__), "..", "rawdata", f"{year}_data.csv")
    try:
      df = pd.read_csv(csv_path, encoding='utf-8')
    except UnicodeDecodeError:
      df = pd.read_csv(csv_path, encoding='latin-1')
    df.to_sql("compiled_epa_data", engine, if_exists="append")