from flask import Blueprint, render_template, request, jsonify
from scr.models.ejemplo9 import ejemplo9

main = Blueprint('dtserverside_bp', __name__)

@main.route('/ejemplo9')
def showsample9():
    return  render_template('/ejemplo9.html')

@main.route('/listproducts')
def get_ListProducts():
    products = ejemplo9.get_ProductList()
    print(products)
    # Obtener parametros enviados por  DT
    draw = int(request.args.get('draw', 1))
    start = int(request.args.get('start', 0))
    lenght = int(request.args.get('lenght', 10))
    search_value = request.args.get('search[value]', '')

    # ORDERNAR POr la columna especificada
    order_column_index = int(request.args.get('order[0][column]', 0))
    order_column_name = request.args.get('order[{}][data]'.format(order_column_index), 'CO_ITEM')
    order_dir = request.args.get('order[0][dir]', 'asc')

    # Filtrar los datos
    if search_value:
        products = [product for product in products if
                    search_value.lower() in str(product['CO_ITEM']).lower() or search_value.lower() in product[
                        'DE_ITEM'].lower()]
    # ORDER LOS DATOS
    products.sort(key=lambda x: x[order_column_name], reverse=(order_dir == 'desc'))
    # Numero total de reg. despes de filtrar
    total_filtered = len(products)
    # paginación de los datos
    filtered_products = products[start:start + lenght]

    # Estructurar la respuesta del data table

    response = {
        'draw': draw,
        'recordsTotal': len(products),
        'recordsFiltered': total_filtered,
        'data': filtered_products
    }
    return jsonify(response)
