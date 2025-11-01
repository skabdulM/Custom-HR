import frappe
from frappe.utils.pdf import get_pdf


@frappe.whitelist()
def download_pdf(doctype, docname, format):
	html = frappe.get_print(doctype, docname, format)

	frappe.local.response.filename = format.replace(" ", "_") + ".pdf"
	frappe.local.response.filecontent = get_pdf(html)
	frappe.local.response.type = "pdf"
