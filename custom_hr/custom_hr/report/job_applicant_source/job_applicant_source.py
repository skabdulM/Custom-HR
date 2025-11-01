# Copyright (c) 2025, abdul mannan and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns = [
		{"label": "Source", "fieldname": "source", "fieldtype": "Data", "width": 200},
		{"label": "Number of Applicants", "fieldname": "total", "fieldtype": "Int", "width": 200},
	]

	data = frappe.db.sql(
		"""
        SELECT source, COUNT(name) AS total
        FROM `tabJob Applicant`
        GROUP BY source
        ORDER BY total DESC
    """,
		as_dict=True,
	)

	# prepare chart data
	labels = [row["source"] for row in data]
	values = [row["total"] for row in data]

	chart = {
		"data": {"labels": labels, "datasets": [{"name": "Applicants", "values": values}]},
		"type": "bar",
		"height": 300,
	}

	return columns, data, None, chart
