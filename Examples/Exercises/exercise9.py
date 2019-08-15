# Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.

def convert(seconds):
    days = seconds // (24 * 3600)
    seconds %= 24 * 3600
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    # {days:02}, бодавляет нули слева до 2 знаков
    print(f'{days:02}д. {hours:02}:{minutes:02}:{seconds:02}')


convert(1234565)
convert(123455)
