# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

df = pd.read_csv('car_brands_data_v2.csv')

# 1. CSV файлын жүктеп, алғашқы 10 жолын экранға шығару
print("--- 1 ---")
print(df.head(10))

# 2. Жолдар мен бағандардың санын анықтау
print("--- 2 ---")
print("Өлшемі (жол, баған):", df.shape)
print("Бағандар:", df.columns.tolist())

# 3. Деректер типтерін және бос емес мәндер санын анықтау
print("--- 3 ---")
print(df.info())
print("\nБос емес мәндер саны:")
print(df.count())

# 4. Сандық бағандардың негізгі статистикалық сипаттамалары
print("--- 4 ---")
print(df.describe())

# 5. Әр бағандағы бірегей мәндердің санын анықтау
print("--- 5 ---")
print(df.nunique())
print("\nМарка бірегей мәндері:", df["Марка"].unique())
print("Елдер бірегей мәндері:", df["Страна производителя"].unique())

# 6. Бос мәндерді табу
print("--- 6 ---")
print(df.isnull().sum())

# 7. Бос мәндерді жою немесе толтыру
print("--- 7 ---")
print("Бос мәндер саны:")
print(df.isnull().sum())

# Бос мәндерді 0 санымен толтыру
df = df.fillna(0)
print("\nfillna() қолданғаннан кейін:")
print(df.isnull().sum())

# Бос мәндері бар жолдарды жою
df = df.dropna()
print("\nТазартылғаннан кейінгі жолдар саны:", len(df))

# 8. Қайталанатын жолдарды анықтау және жою
print("--- 8 ---")
print("Қайталанатын жолдар саны:", df.duplicated().sum())
df = df.drop_duplicates()
print("drop_duplicates() кейінгі өлшем:", df.shape)

# 9. Деректер типін өзгерту
print("--- 9 ---")
# Қозғалтқыш көлемін float типіне өзгерту
df['Объем двигателя (л)'] = df['Объем двигателя (л)'].str.replace(',', '.', regex=False)
df['Объем двигателя (л)'] = pd.to_numeric(df['Объем двигателя (л)'])
print("Объем двигателя (л) типі:", df['Объем двигателя (л)'].dtype)

# 10. Баған атауларын өзгерту және қажетсіз бағанды жою
print("--- 10 ---")
df = df.rename(columns={'ID': 'Нөмір'})
# Қажетсіз бағанды жою
df = df.drop(columns=['Нөмір'])
print(df.columns)

# 11. Орташа бағадан жоғары автомобильдерді таңдау
print("--- 11 ---")
mean_price = df['Цена (руб)'].mean()
print("Орташа баға:", round(mean_price, 2))
print("Орташа бағадан жоғары автомобильдер саны:", len(df[df['Цена (руб)'] > mean_price]))
print(df[df['Цена (руб)'] > mean_price].head())

# 12. Екі немесе одан да көп шарт бойынша іріктеу
print("--- 12 ---")
# Бағасы орташадан жоғары және өндіруші елі Германия
filtered = df.loc[
    (df['Цена (руб)'] > mean_price) &
    (df['Страна производителя'] == 'Германия')
]
print("Табылған жазбалар саны:", len(filtered))
print(filtered.head())

# 13. Ең үлкен мәні бар 10 жазбаны табу
print("--- 13 ---")
print(df.nlargest(10, 'Цена (руб)'))

# 14. Ең кіші мәндері бар 5 жазбаны табу
print("--- 14 ---")
print(df.nsmallest(5, 'Цена (руб)'))

# 15. Бір немесе бірнеше баған бойынша сұрыптау
print("--- 15 ---")
print(df.sort_values(
    by=['Цена (руб)', 'Год выпуска'],
    ascending=[False, True]
).head())

# 16. Орташа мән, медиана, минимум және максимум
print("--- 16 ---")
print("Орташа мән (mean):\n", df.mean(numeric_only=True))
print("\nМедиана (median):\n", df.median(numeric_only=True))
print("\nМинимум (min):\n", df.min(numeric_only=True))
print("\nМаксимум (max):\n", df.max(numeric_only=True))

# 17. Стандартты ауытқу мен дисперсия
print("--- 17 ---")
print("Стандартты ауытқу (std):\n", df.std(numeric_only=True))
print("\nДисперсия (var):\n", df.var(numeric_only=True))

# 18. 25, 50 және 75-процентильдерді табу
print("--- 18 ---")
print(df['Цена (руб)'].quantile([0.25, 0.50, 0.75]))

# 19. Ең жиі кездесетін мәнді анықтау
print("--- 19 ---")
print("Мода (автомобиль маркасы):\n", df['Марка'].mode())
print("\nЖиіліктер кестесі:\n", df['Марка'].value_counts().head())

# 20. Сандық бағандар арасындағы корреляция
print("--- 20 ---")
print(df.corr(numeric_only=True).round(3))
