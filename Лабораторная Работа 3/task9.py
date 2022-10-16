salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
delta=0

need_money = 0  # количество денег, чтобы прожить 10 месяцев
while months != 0:
    delta = salary - spend
    spend=spend*(1+increase)
    months = months-1
    need_money +=(-1*delta)
# TODO Оформить решение

print(round(need_money))
