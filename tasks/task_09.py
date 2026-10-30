# -*- coding: utf-8 -*-
# ==============================================================================
# Орындаған: Орынбеков Губайдулла | Тобы: Инф-23-1
# Тапсырма 9: 9. Бір немесе бірнеше бағанның деректер типін өзгертіңіз.
# Қолданылатын Pandas әдістері: astype(), to_numeric()
# ==============================================================================

import os
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(BASE_DIR, "students_data.csv")

myData = pd.read_csv(CSV_PATH)
num_cols = ["Курс", "Қатысу_пайызы", "Аралық_бақылау", "Емтихан_балы", "GPA", "Стипендия"]

print("=" * 80)
print('9. Бір немесе бірнеше бағанның деректер типін өзгертіңіз.')
print("Pandas әдістері:", 'astype(), to_numeric()')
print("=" * 80 + "\n")

# --- НЕГІЗГІ КОД ---
myData_types = myData.copy()
myData_types["Емтихан_балы"] = myData_types["Емтихан_балы"].astype(float)
myData_types["GPA"] = pd.to_numeric(myData_types["GPA"], errors="coerce")
print("Өзгертілген деректер типтері:")
print(myData_types[["Емтихан_балы", "GPA", "Курс"]].dtypes)

print("\n" + "-" * 80)
print("Түсіндірме:")
print("• astype(float) — 'Емтихан_балы' бағанының деректер типін бүтін саннан (int64) нақты бөлшек санға (float64) түрлендіреді.\n• pd.to_numeric(..., errors='coerce') — баған мәндерін сандық типке ауыстырады (егер мәтіндік қате мәндер кездессе, оларды автоматты түрде NaN етеді).\nCSV бойынша талдау: 'Емтихан_балы' бағаны int64 типінен float64 типіне сәтті ауыстырылды.")
print("-" * 80)
