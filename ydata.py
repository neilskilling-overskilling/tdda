import numpy as np
import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv("~/Downloads/TDDA/CompaniesHouse/BasicCompanyDataAsOneFile-2024-01-01.csv")
profile = ProfileReport(df, title="Profiling Report")
profile.to_file("your_report.html")