# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

df = pd.read_csv('computer_tech_catalog_kz_v2.csv', sep=';')

# 1. Алғашқы 10 жолды шығару
print("--- 1 ---")
print(df.head(10))

# 2. Жолдар мен бағандардың санын анықтау
print("--- 2 ---")
print("Өлшемі (жол, баған):", df.shape)
print("Бағандар:", df.columns.tolist())

# 3. Деректер типтері және бос емес мәндер саны
print("--- 3 ---")
df.info()
print("\nБос емес мәндер саны:")
print(df.count())

# 4. Сандық бағандардың статистикалық сипаттамалары
print("--- 4 ---")
print(df.describe())

# 5. Әр бағандағы бірегей мәндердің санын анықтау
print("--- 5 ---")
print(df.nunique())
print("\nКатегория бірегей мәндері:", df["Категория"].unique())
print("Статус бірегей мәндері:", df["Статус"].unique())

# 6. Бос мәндерді анықтау
print("--- 6 ---")
print(df.isnull().sum())

# 7. Бос мәндерді жою немесе тиісті әдіспен толтыру
print("--- 7 ---")
print("Бос мәндер саны:")
print(df.isnull().sum())

# 1. Бос мәндерді 0 санымен толтыру
df = df.fillna(0)
print("\nfillna() қолданғаннан кейін:")
print(df.isnull().sum())

# 2. Бос мәндері бар жолдарды жою
df = df.dropna()
print("\nТазартылғаннан кейінгі жолдар саны:", len(df))

# 8. Қайталанатын жолдарды анықтау және жою
print("--- 8 ---")
print("Қайталанатын жолдар саны:", df.duplicated().sum())
df = df.drop_duplicates()
print("drop_duplicates() кейінгі өлшем:", df.shape)

# 9. Бір немесе бірнеше бағанның дерек типін өзгерту
print("--- 9 ---")
df['Цена_USD'] = pd.to_numeric(df['Цена_USD'], errors='coerce')
df['Количество_на_складе'] = df['Количество_на_складе'].astype(int)
print("Цена_USD типі:", df['Цена_USD'].dtype)
print("Количество_на_складе типі:", df['Количество_на_складе'].dtype)

# 10. Бағандардың атауларын өзгерту және қажетсіз бағандарды жою
print("--- 10 ---")
df = df.rename(columns={'№': 'ID'})
df = df.drop(columns=['ID'])
print(df.columns)

# 11. Орташа бағадан жоғары тауарларды таңдау
print("--- 11 ---")
mean_price = df['Цена_USD'].mean()
print("Орташа баға:", mean_price)
print("Орташа бағадан жоғары тауарлар саны:", len(df[df['Цена_USD'] > mean_price]))
print(df[df['Цена_USD'] > mean_price].head())

# 12. Екі шарт бойынша мәліметтерді іріктеу
print("--- 12 ---")
filtered = df.loc[
    (df['Цена_USD'] > mean_price) &
    (df['Город_склада'] == 'Алматы')
]
print("Табылған жазбалар саны:", len(filtered))
print(filtered.head())

# 13. Ең қымбат 10 тауарды табу
print("--- 13 ---")
print(df.nlargest(10, 'Цена_USD'))

# 14. Ең арзан 5 тауарды табу
print("--- 14 ---")
print(df.nsmallest(5, 'Цена_USD'))

# 15. Баға және қоймадағы саны бойынша сұрыптау
print("--- 15 ---")
print(df.sort_values(
    by=['Цена_USD', 'Количество_на_складе'],
    ascending=[False, True]
).head(10))

# 16. Орташа мән, медиана, минимум және максимум
print("--- 16 ---")
print("Орташа мән (mean):")
print(df.mean(numeric_only=True))

print("\nМедиана (median):")
print(df.median(numeric_only=True))

print("\nМинимум (min):")
print(df.min(numeric_only=True))

print("\nМаксимум (max):")
print(df.max(numeric_only=True))

# 17. Стандартты ауытқу және дисперсия
print("--- 17 ---")
print("Стандартты ауытқу (std):")
print(df.std(numeric_only=True))

print("\nДисперсия (var):")
print(df.var(numeric_only=True))

# 18. 25, 50 және 75 процентильдерін табу
print("--- 18 ---")
print(df['Цена_USD'].quantile([0.25, 0.50, 0.75]))

# 19. Ең жиі кездесетін мәнді анықтау
print("--- 19 ---")
print("Мода (тауар атауы):")
print(df['Наименование'].mode())

print("\nЖиіліктер кестесі:")
print(df['Наименование'].value_counts().head())

# 20. Сандық бағандар арасындағы корреляция
print("--- 20 ---")
print(df.corr(numeric_only=True).round(3))
