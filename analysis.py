import pandas as pd
import numpy as np

# 1. Жүктеу және қарап шығу (Загрузка данных)
df = pd.read_csv("marketing_data.csv")

# Күнді datetime типіне ауыстыру
df['Күні'] = pd.to_datetime(df['Күні'], format='%d.%m.%Y')

print("=" * 60)
print("1. ЖАЛПЫ АҚПАРАТ (ОБЩАЯ ИНФОРМАЦИЯ О ДАННЫХ)")
print("=" * 60)
print(f"Жолдар саны: {df.shape[0]}, Бағандар саны: {df.shape[1]}")
print(df.info())
print("\nАлғашқы 5 жол:")
print(df.head())

# 2. МАРКЕТИНГ ЖӘНЕ БИЗНЕС МЕТРИКАЛАРЫН ЕСЕПТЕУ (РАСЧЕТ KPI С PANDAS & NUMPY)
# CTR (Кликабельность / Көрілімнен клиентке айналу %):
df['CTR_%'] = np.round((df['Клиент саны'] / df['Көрілім']) * 100, 2)

# CR (Конверсия / Клиенттен тапсырысқа айналу %):
df['CR_%'] = np.round((df['Тапсырыс саны'] / df['Клиент саны']) * 100, 2)

# CAC / CPA (Бір тапсырыстың жарнамалық құны):
df['CAC'] = np.round(df['Жарнама шығыны'] / df['Тапсырыс саны'], 2)

# AOV (Орташа чек / Средний чек):
df['AOV'] = np.round(df['Сатылым көлемі'] / df['Тапсырыс саны'], 2)

# ROAS (Жарнаманың қайтарымы / Окупаемость рекламы в %):
df['ROAS_%'] = np.round((df['Сатылым көлемі'] / df['Жарнама шығыны']) * 100, 2)

# ROMI (Таза пайда негізіндегі рентабельділік / Окупаемость инвестиций):
df['ROMI_%'] = np.round(((df['Пайда'] - df['Жарнама шығыны']) / df['Жарнама шығыны']) * 100, 2)

# 3. NUMPY АРҚЫЛЫ ТИІМДІЛІКТІ БАҒАЛАУ (СЕГМЕНТАЦИЯ С NP.SELECT)
conditions = [
    (df['ROMI_%'] >= 100),
    (df['ROMI_%'] >= 50) & (df['ROMI_%'] < 100),
    (df['ROMI_%'] < 50)
]
choices = ['Жоғары тиімділік (High)', 'Орташа тиімділік (Medium)', 'Төмен тиімділік (Low)']
df['Тиімділік_категориясы'] = np.select(conditions, choices, default='Басқа')

print("\n" + "=" * 60)
print("2. МАРКЕТИНГТІК АРНАЛАРДЫ САЛЫСТЫРУ (СРАВНЕНИЕ КАНАЛОВ)")
print("=" * 60)
channel_summary = df.groupby('Жарнама түрі').agg(
    Жарнама_шығыны=('Жарнама шығыны', 'sum'),
    Жалпы_пайда=('Пайда', 'sum'),
    Жалпы_сатылым=('Сатылым көлемі', 'sum'),
    Орташа_CR=('CR_%', 'mean'),
    Орташа_ROAS=('ROAS_%', 'mean')
).sort_values(by='Жалпы_пайда', ascending=False)
print(channel_summary)

print("\n" + "=" * 60)
print("3. МЕНЕДЖЕРЛЕРДІҢ НӘТИЖЕСІ (РЕЗУЛЬТАТЫ МЕНЕДЖЕРОВ)")
print("=" * 60)
manager_summary = df.groupby('Менеджер').agg(
    Тапсырыс_саны=('Тапсырыс саны', 'sum'),
    Сатылым_көлемі=('Сатылым көлемі', 'sum'),
    Таза_пайда=('Пайда', 'sum'),
    Орташа_чек=('AOV', 'mean')
).sort_values(by='Таза_пайда', ascending=False)
print(manager_summary)

print("\n" + "=" * 60)
print("4. КОРРЕЛЯЦИЯЛЫҚ МАТРИЦА (МАТРИЦА КОРРЕЛЯЦИИ ЧИСЛОВЫХ ПОКАЗАТЕЛЕЙ)")
print("=" * 60)
num_cols = ['Жарнама шығыны', 'Көрілім', 'Клиент саны', 'Тапсырыс саны', 'Сатылым көлемі', 'Пайда']
corr_matrix = df[num_cols].corr()
print(np.round(corr_matrix, 3))

print("\n" + "=" * 60)
print("5. СВОДНАЯ ТАБЛИЦА: ТАУАР ЖӘНЕ ҚАЛА БОЙЫНША ПАЙДА (PIVOT TABLE)")
print("=" * 60)
pivot_profit = pd.pivot_table(
    df, 
    values='Пайда', 
    index='Өнім атауы', 
    columns='Қала', 
    aggfunc='sum',
    fill_value=0
)
print(pivot_profit)

# Нәтижені жаңа CSV файлға экспорттау
output_file = "marketing_analysis_results.csv"
df.to_csv(output_file, index=False, encoding='utf-8-sig')
print(f"\nЕсептелген нәтижелер сақталды: {output_file}")
