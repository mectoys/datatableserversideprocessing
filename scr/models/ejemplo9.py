from scr.database.connectDB import get_connection_SQLSERVER_HighChartDB


class ejemplo9:
    @staticmethod
    def get_ProductList():
        connection = get_connection_SQLSERVER_HighChartDB()
        with connection.cursor() as cursor:
            try:
                query = "SELECT CO_ITEM, ISNULL(DE_ITEM,'---') AS DE_ITEM FROM Productos"
                cursor.execute(query)
                result = cursor.fetchall()
                formatted_result = [{'CO_ITEM': str(row[0]), 'DE_ITEM': row[1]} for row in result]
                return formatted_result
            except Exception as e:
                print(f"Error en la consulta: {str(e)}")
                return []
