def time(seconds):

    if seconds < 0 or seconds >= 8640000:
        return


    days, remaining_seconds = divmod(seconds, 24 * 3600)
    hours, remaining_seconds = divmod(remaining_seconds, 3600)
    minutes, remaining_seconds = divmod(remaining_seconds, 60)
    seconds = remaining_seconds

    if days % 10 == 1 and days % 100 != 11:
        days_str = f"{days} день"
    elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20):
        days_str = f"{days} дні"
    else:
        days_str = f"{days} днів"


    time_str = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"


    if days > 0:
        return f"{days_str} {time_str}"
    else:
        return time_str

input_seconds = int(input("Введіть кількість секунд (від 0 до 8640000): "))
print(time(input_seconds))
