from unittest.mock import right

from src import masks


def mask_account_card(card: str) -> str:
    '''Функция принимающая тип карты или счета и возвращающая скрытую часть'''
    number = ""
    text = ""
    for i in card:
        if i.isdigit():
            number += i
        else:
            text += i
    if "счет" in text.lower():
        return f"{text}{masks.get_mask_account(number)}"
    else:
        return f"{text}{masks.get_mask_card_number(number)}"


#2024-03-11T02:26:18.671407 --> 11.07.2018
def get_date(date:str) -> str:
    '''Функция принимающая строку в определенном формате и возвращает дд.мм.гггг'''
    date_buffer = ""
    right_date = ""
    for i in date:
        if i != "T" and i != "-":
            date_buffer += i
        elif i == "-":
            continue
        else:
            break
    right_date = date_buffer[-1] + date_buffer[-2] + "." + date_buffer[-4] + date_buffer[-3] + "." + date_buffer[0] + date_buffer[1] + date_buffer[2] + date_buffer[3]
    return right_date