# -*- coding: utf-8 -*-
# ==============================================================================
# Орындаған: Орынбеков Губайдулла | Тобы: Инф-23-1
# Тапсырма 11: 11. Сандық көрсеткіші (мысалы, GPA) орташа мәннен жоғары жолдарды таңдаңыз.
# Қолданылатын Pandas әдістері: Шарттар, mean()
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
print('11. Сандық көрсеткіші (мысалы, GPA) орташа мәннен жоғары жолдарды таңдаңыз.')
print("Pandas әдістері:", 'Шарттар, mean()')
print("=" * 80 + "\n")

# --- НЕГІЗГІ КОД ---
mean_gpa = myData["GPA"].mean()
above_avg = myData[myData["GPA"] > mean_gpa]
print(f"Орташа GPA: {mean_gpa:.2f}")
print(f"GPA көрсеткіші орташадан жоғары студенттер саны: {len(above_avg)} (600 ішінен)")
print(above_avg.head(10))

print("\n" + "-" * 80)
print("Түсіндірме:")
print("• myData['GPA'].mean() — барлық 600 студенттің орташа GPA көрсеткішін есептейді (нәтижесі: 2.98).\n• myData[myData['GPA'] > mean_gpa] — логикалық шарт арқылы тек GPA балы 2.98-ден жоғары студенттерді сүзіп алады.\nCSV бойынша талдау: Барлығы 600 студенттің ішінен 304 студенттің (50.7%) үлгерім балы университет бойынша орташа деңгейден жоғары.")
print("-" * 80)
