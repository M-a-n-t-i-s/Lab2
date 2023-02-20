import pandas as pd

df = pd.read_csv('weather.csv', encoding='utf-8', index_col=False, parse_dates=[0])
print(df)

years = list(set(df['Day'].dt.year.values))
years.sort()
print(years)

records, hot_january, hot_summer, diff_temp_day = [], [], [], []
for year in years:
    summ, count_summer, summ_summer = 0, 0, 0
    january_count = 0
    count = 0
    for i in df.index:
        if df['Day'].dt.year.values[i] == year:
            summ += df['t'].values[i]
            count += 1
            if df['Day'].dt.month.values[i] == 1:
                if df['t'].values[i] > 0:
                    january_count += 1
            if df['Day'].dt.month.values[i] == 6 or df['Day'].dt.month.values[i] == 7 or df['Day'].dt.month.values[
                i] == 8:
                summ_summer += df['t'].values[i]
                count_summer += 1

        if i != 0 and year == years[0]:
            diff_temp_day.append([abs(df['t'].values[i] - df['t'].values[i-1]), i - 1])



        # if df['Day'].dt.mounth.values[i] ==1:
    records.append([year, "Средняя годовая температура =", int(summ / count)])
    hot_january.append([january_count, year])
    hot_summer.append([int(summ_summer / count_summer), year])
maximum, minimal, maximum_temp_in_january = 0, 0, 0
for entry in records:
    print(*entry)
    if records[0] == entry:
        minimal = entry[2]
        maximum = entry[2]
    if entry[2] < minimal:
        minimal = entry[2]
    if entry[2] > maximum:
        maximum = entry[2]
print("Перове задание", minimal + maximum)

for entry in hot_january:
    if hot_january[0] == entry:
        maximum_temp_in_january = entry[0]
        year_january = entry[1]
    if entry[0] > maximum_temp_in_january:
        maximum_temp_in_january = entry[0]
        year_january = entry[1]
print("Второе задание", year_january)

for entry in hot_summer:
    if hot_summer[0] == entry:
        maximum_hot_summer = entry[0]
        year_summer = entry[1]
    if entry[0] > maximum_hot_summer:
        maximum_hot_summer = entry[0]
        year_summer = entry[1]
print("Третье задание", year_summer)


for entry in diff_temp_day:
    if diff_temp_day[0] == entry:
        diff_day = entry[0]
        index = entry[1]
    if entry[0] > diff_day:
        diff_day = entry[0]
        index = entry[1]
print("Четвертое задание",diff_day)
print(df.iloc[index])
print(df.iloc[1+index])