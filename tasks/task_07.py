# -*- coding: utf-8 -*-
# ==============================================================================
# Орындаған: Орынбеков Губайдулла | Тобы: Инф-23-1
# Тапсырма 7: 7. Бос мәндерді жою немесе тиісті әдіспен толтыру.
# Қолданылатын Pandas әдістері: dropna(), fillna()
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
print('7. Бос мәндерді жою немесе тиісті әдіспен толтыру.')
print("Pandas әдістері:", 'dropna(), fillna()')
print("=" * 80 + "\n")

# --- НЕГІЗГІ КОД ---
clean_drop = myData.dropna()
clean_fill = myData.copy()
clean_fill["GPA"] = clean_fill["GPA"].fillna(clean_fill["GPA"].mean())
clean_fill["Факультет"] = clean_fill["Факультет"].fillna("Белгісіз")
print("dropna() кейінгі кесте өлшемі:", clean_drop.shape)
print("fillna() кейінгі бос мәндер саны:", clean_fill.isnull().sum().sum())

print("\n" + "-" * 80)
print("Түсіндірме:")
print("• dropna() — кемінде бір ұяшығы бос (NaN) болған жолдарды кестеден толықтай өшіреді.\n• fillna() — бос ұяшықтарды өшірмей, оларды белгілі бір мәнмен (мысалы, сандық 'GPA' бағанын орташа мәнмен, ал мәтіндік 'Факультет' бағанын 'Белгісіз' сөзімен) толтырады.\nCSV бойынша талдау: Бастапқы деректерде бос ұяшықтар болмағандықтан, dropna() әдісінен кейін де барлық 600 жол мен 12 баған өзгеріссіз сақталды.")
print("-" * 80)
