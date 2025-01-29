from src import masks

cart_number = int(input("Введите номер карты: "))
print(masks.get_mask_card_number(cart_number))

account_number = int(input("Введите номер счета: "))
print(masks.get_mask_account(account_number))
