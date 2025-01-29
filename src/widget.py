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



def get_date(date:str) -> str:
    '''Функция принимающая строку в определенном формате и возвращает дд.мм.гггг'''
    pass