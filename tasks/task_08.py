# -*- coding: utf-8 -*-
# ==============================================================================
# Орындаған: Орынбеков Губайдулла | Тобы: Инф-23-1
# Тапсырма 8: 8. Қайталанатын жолдарды анықтап, оларды жойыңыз.
# Қолданылатын Pandas әдістері: duplicated(), drop_duplicates()
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
print('8. Қайталанатын жолдарды анықтап, оларды жойыңыз.')
print("Pandas әдістері:", 'duplicated(), drop_duplicates()')
print("=" * 80 + "\n")

# --- НЕГІЗГІ КОД ---
dup_count = myData.duplicated().sum()
print("Қайталанатын (дубликат) жолдар саны:", dup_count)
myData_no_dup = myData.drop_duplicates()
print("Дубликаттарды жойғаннан кейінгі өлшем:", myData_no_dup.shape)

print("\n" + "-" * 80)
print("Түсіндірме:")
print('• duplicated() — кестедегі жолдардың бұрынғы жолдармен толықтай қайталанатынын (дубликат екенін) тексереді, ал sum() олардың жалпы санын есептейді.\n• drop_duplicates() — қайталанатын артық жолдарды өшіріп, тек бірегей жазбаларды қалдырады.\nCSV бойынша талдау: Кестедегі әрбір студент жазбасы бірегей болғандықтан, қайталанатын жолдар саны 0 болды.')
print("-" * 80)
