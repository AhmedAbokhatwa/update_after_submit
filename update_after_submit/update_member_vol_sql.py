# import frappe
# from frappe.model.document import Document


# class xyz (Document):
#     def validate(self):
#         self.items[0].item_name ='test'


# @frappe.whitelist()
# def update():
#     try:
#         ahmed = """
#             SELECT
#                 tc.name AS customer_name,
#                 tc.tax_id,
#                 tvme.tax__number,
#                 tvme.season AS season,
#                 tvme.season_name AS season_name,
#                 tvme.year,
#                 tvme.value,
#                 SUM(tvme.total_amount_in_egp) AS total_amount_in_egp,
#                 SUM(tvme.total_amount_in_usd) AS total_amount_in_usd,
#                 SUM(tvme.quantity_in_tons) AS quantity_in_tons
#             FROM
#                 `tabCustomer` tc
#             LEFT JOIN
#                 `tabVolume Of Member Exports` tvme ON (tc.tax_id = tvme.tax__number)
#             WHERE
#                 tvme.year = YEAR(CURDATE()) - 4
#             GROUP BY
#                 tc.tax_id
#         """
#         ahmed_query = frappe.db.sql(ahmed, as_dict=True)
#         print("Query Result:", ahmed_query)

#         for data in ahmed_query:
#             print("Processing data for Customer:", data['customer_name'])
#             query = """
#                UPDATE `tabVolume Of Member Exports for Three Years` ti
#                 LEFT JOIN `tabCustomer` tc ON tc.name = ti.parent
#                 SET ti.season = %s,
#                     ti.season_name = %s,
#                     ti.total_amount_in_egp = %s,
#                     ti.total_amount_in_usd = %s,
#                     ti.quantity_in_tons = %s,
#                     ti.value = %s
#                  WHERE tc.name = %s
#                 AND ti.parenttype = 'Customer';
#             """
#             # Execute the update query with parameters
#             query_update = frappe.db.sql(query, (
#                 data['season'], data['season_name'], data['total_amount_in_egp'],
#                 data['total_amount_in_usd'], data['quantity_in_tons'], data['value'], data['customer_name']
#             ))
#             frappe.db.commit()
            
#             print("query_update:", query_update)

#         return "Update completed successfully"

#     except Exception as e:
#         frappe.log_error(f"Error in update function: {str(e)}")
#         return "Error occurred, check logs for details"



import frappe
from frappe.model.document import Document


class xyz (Document):
    def validate(self):
        self.items[0].item_name ='test'

@frappe.whitelist()
def update():
    try:
        sql = """
            SELECT
                tc.name AS customer_name,
                tc.tax_id,
                tvme.tax__number,
                tvme.season AS season,
                tvme.season_name AS season_name,
                tvme.year,
                tvme.value,
                SUM(tvme.total_amount_in_egp) AS total_amount_in_egp,
                SUM(tvme.total_amount_in_usd) AS total_amount_in_usd,
                SUM(tvme.quantity_in_tons) AS quantity_in_tons
            FROM
                `tabCustomer` tc
            LEFT JOIN
                `tabVolume Of Member Exports` tvme ON (tc.tax_id = tvme.tax__number)
            WHERE
                tvme.year = YEAR(CURDATE()) - 4
            GROUP BY
                tc.tax_id
        """
        sql_query = frappe.db.sql(sql, as_dict=True)
        print("Query Result:", sql_query)

        for data in sql_query:
            print("Processing data for Customer:", data['customer_name'])
            insert_query = """
                INSERT INTO `tabVolume Of Member Exports for Three Years`
                    (parent, parenttype, season, season_name, total_amount_in_egp, total_amount_in_usd, quantity_in_tons, value)
                VALUES
                    (%s, 'Customer', %s, %s, %s, %s, %s, %s)
            """
            frappe.db.sql(insert_query, (
                data['customer_name'], data['season'], data['season_name'],
                data['total_amount_in_egp'], data['total_amount_in_usd'],
                data['quantity_in_tons'], data['value']
            ))
            frappe.db.commit()
            print(f"Inserted new record for Customer: {data['customer_name']}")

    
        return "Insert/update completed successfully"

    except Exception as e:
        frappe.log_error(f"Error in update function: {str(e)}")
        return "Error occurred, check logs for details"
