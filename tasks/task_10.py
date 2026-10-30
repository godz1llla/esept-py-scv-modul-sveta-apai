# -*- coding: utf-8 -*-
# ==============================================================================
# Орындаған: Орынбеков Губайдулла | Тобы: Инф-23-1
# Тапсырма 10: 10. Бағандардың атауларын өзгерту және қажетсіз бағандарды жою.
# Қолданылатын Pandas әдістері: rename(), drop()
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
print('10. Бағандардың атауларын өзгерту және қажетсіз бағандарды жою.')
print("Pandas әдістері:", 'rename(), drop()')
print("=" * 80 + "\n")

# --- НЕГІЗГІ КОД ---
myData_renamed = myData.rename(columns={"Оқу_түрі": "Оқу_негізі"})
myData_dropped = myData_renamed.drop(columns=["Студент_ID"])
print("Жаңартылған бағандар саны:", myData_dropped.shape[1])
print("Жаңартылған баған атаулары:", myData_dropped.columns.tolist())
print(myData_dropped.head(5))

print("\n" + "-" * 80)
print("Түсіндірме:")
print("• rename(columns={'Оқу_түрі': 'Оқу_негізі'}) — бағанның атауын жаңа атауға ('Оқу_негізі') өзгертеді.\n• drop(columns=['Студент_ID']) — талдауға қажет емес реттік 'Студент_ID' бағанын кестеден өшіреді.\nCSV бойынша талдау: 'Студент_ID' бағаны жойылғаннан кейін кестеде 12 бағанның орнына 11 мазмұндық баған қалды.")
print("-" * 80)
