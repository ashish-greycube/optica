import frappe

def execute():
    citas = frappe.get_all("Cita", order_by="creation asc")
    for index, cita in enumerate(citas):
        cita_date = frappe.get_value("Cita", cita.name, "fecha")
        new_name = "ACC-CITA-{}-{:05d}".format(cita_date.year, index)
        frappe.rename_doc("Cita", cita.name, new_name, ignore_permissions=True)
