import requests

def get_JSON_product(item_number: str):
    print(item_number)
    result = requests.get(f"https://card.wb.ru/cards/v1/detail?appType=1&curr=rub&dest=-1257786&spp=30&nm={item_number}").json()
    try:
        return result["data"]["products"][0]
    except:
        return None

def all_qty(list_sizes: list):
    summ = 0
    for i in list_sizes:
        for j in i["stocks"]:
            summ += j["qty"]
    return summ

def get_product_card(item_number: str):
    result = get_JSON_product(item_number)

    if result is None:
        return "Вы ввели несуществующий артикул"

    product_dict = {
        "name": result["name"],
        "id": result["id"],
        "priceU": result["priceU"],
        "salePriceU": result["salePriceU"],
        "reviewRating": result["reviewRating"],
        "sizes": result["sizes"],
    }

    product_card = (
    f"""
    {product_dict["name"]}
    Артикл:{product_dict["id"]}
    Цена без скидки:{str(product_dict["priceU"])[0:-2]}
    Цена со скидкой:{str(product_dict["salePriceU"])[0:-2]}
    Рейтинг товара:{product_dict["reviewRating"]}
    Кол-во:{all_qty(product_dict["sizes"])}
    """
    )

    return product_card