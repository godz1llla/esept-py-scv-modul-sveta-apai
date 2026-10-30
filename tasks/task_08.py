# -*- coding: utf-8 -*-
# ==============================================================================
# Орындаған: Орынбеков Губайдулла | Тобы: Инф-23-1
# Тапсырма 8: 8. Қайталанатын жолдарды анықтап, оларды жойыңыз.
# Қолданылатын Pandas әдістері: duplicated(), drop_duplicates()
# ==============================================================================

import os
import pandas as pd

# Кестенің барлық бағандары экранға толық сыюы үшін баптау:
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)

# CSV файлдың жолын автоматты түрде табу (кез келген папкадан іске қосылады):
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(BASE_DIR, "marketing_data.csv")

myData = pd.read_csv(CSV_PATH)

print("=" * 80)
print('8. Қайталанатын жолдарды анықтап, оларды жойыңыз.')
print("Pandas әдістері:", 'duplicated(), drop_duplicates()')
print("=" * 80 + "\n")

# --- НЕГІЗГІ КОД ---
print("Қайталанатын жолдар саны:", myData.duplicated().sum())
print(myData[myData.duplicated()])

uniqueData = myData.drop_duplicates()
print("Бастапқы өлшем:", myData.shape, "-> Тазаланған өлшем:", uniqueData.shape)

print("\n" + "-" * 80)
print("Түсіндірме:")
print('• duplicated() әдісі кестедегі толықтай қайталанатын (дубликат) жолдарды іздейді және duplicated().sum() олардың санын шығарады.\n• drop_duplicates() әдісі қайталанған жолдарды өшіріп, тек бірегей жазбаларды қалдырады.\nCSV бойынша талдау: Тексеру нәтижесінде қайталанатын жолдар саны 0 болды. drop_duplicates() қолданылғаннан кейін де кестеде барлық 600 бірегей жазба сақталды.')
print("-" * 80)
