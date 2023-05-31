from datetime import datetime, timedelta


def count_time(str):
     
    if 'мин' in str or'ч' in str or'д' in str:
        number, unit = str.split()

        # Определение времени, прошедшего от текущего момента на основе заданного выражения
        if unit == 'мин.':
            time_delta = timedelta(minutes=int(number))
        elif unit == 'ч.':
            time_delta = timedelta(hours=int(number))
        elif unit == 'д.':
            time_delta = timedelta(days=int(number))
        else:
            raise ValueError("Неверная единица измерения времени")

        # Получение текущей даты и времени
        current_datetime = datetime.now()

        # Вычисление нового datetime значения на основе текущей даты и времени и временного сдвига
        result_datetime = current_datetime - time_delta

        # Преобразование datetime значения в строку в нужном формате
        formatted_datetime = result_datetime.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_datetime
    else:
        return '0001-01-1 01:01:01'

