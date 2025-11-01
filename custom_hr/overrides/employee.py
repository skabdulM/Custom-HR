import frappe
from frappe.utils import nowdate


def on_update_employee(doc, method=None):
	if doc.workflow_state == "Confirmed" and not doc.final_confirmation_date:
		doc.final_confirmation_date = nowdate()
