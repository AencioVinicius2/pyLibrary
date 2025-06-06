from product import Product

def generate_products(): 
    list_producs = []

    for x in range(20):
        p = Product(name=f"Product ${x + 1}", price = 4.90 * x)
        list_producs.append(p)
    return list_producs
