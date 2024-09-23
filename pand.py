import pandas as pd

hotels = pd.read_csv("hotel_booking_data.csv")

hotels.head()

# hotels.info()

hotels.describe()

num_rows = hotels.shape[0]
print(f"Количество строк: {num_rows}")


missing_data = hotels.isnull().sum()

# Вывод столбца с наибольшим количеством пропущенных данных
column_with_most_missing = missing_data.idxmax()
max_missing_values = missing_data.max()

print(f"Столбец с наибольшим количеством пропущенных данных: {column_with_most_missing}")
print(f"Количество пропущенных значений в этом столбце: {max_missing_values}")

