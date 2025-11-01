frappe.ui.form.on("Employee", {
	refresh: function (frm) {
		add_print_button(frm);
	},
});

function add_print_button(frm) {
	if (frm.doc.workflow_state !== "Exit") return;

	frm.add_custom_button(
		__("Experience Certificate"),
		() => {
			const api = "/api/method/nms_erp.api.download_pdf";
			const query = `doctype=${frm.doctype}&docname=${frm.doc.name}&format=Employee Experience`;
			window.open(`${api}?${query}`, "_blank");
		},
		"Print"
	);
}
