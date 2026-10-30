# -*- coding: utf-8 -*-
# ==============================================================================
# Орындаған: Орынбеков Губайдулла | Тобы: Инф-23-1
# Тапсырма 17: 17. Стандартты ауытқу мен дисперсияны есептеңіз.
# Қолданылатын Pandas әдістері: std(), var()
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
print('17. Стандартты ауытқу мен дисперсияны есептеңіз.')
print("Pandas әдістері:", 'std(), var()')
print("=" * 80 + "\n")

# --- НЕГІЗГІ КОД ---
stats_17 = pd.DataFrame({
    "Стандартты ауытқу (std)": myData[num_cols].std().round(2),
    "Дисперсия (var)": myData[num_cols].var().round(2)
})
print(stats_17)

print("\n" + "-" * 80)
print("Түсіндірме:")
print('• std() (стандартты ауытқу) және var() (дисперсия, яғни std квадраты) — деректердің орташа мәннен қаншалықты алшақ шашырағанын көрсетеді.\nCSV бойынша талдау: GPA бойынша стандартты ауытқу небәрі 0.38 балды құрайды (дисперсиясы 0.14), ал Емтихан балы бойынша std = 8.44 балл.')
print("-" * 80)
