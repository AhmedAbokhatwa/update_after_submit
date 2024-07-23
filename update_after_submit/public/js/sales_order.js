frappe.ui.form.on('Sales Order', {
    refresh: function(frm) {
        if (frm.doc.docstatus === 1) {
            frm.add_custom_button(__('Update Conversion Rate'), function() {
                frappe.prompt([
                    {
                        label: 'New Conversion Rate',
                        fieldname: 'new_conversion_rate',
                        fieldtype: 'Data',
                        reqd: 1
                    }
                ], function(values) {
                    let new_conversion_rate = parseFloat(values.new_conversion_rate);

                    frappe.call({
                        method: 'library_management.rate_so.update_conversion_rate',
                        args: {
                            "sales_order_name": frm.doc.name,
                            "new_conversion_rate": new_conversion_rate
                        },
                        callback: function(response) {
                            if (!response.exc) {
                                frappe.msgprint(__('Conversion rate updated successfully'));
                                frm.reload_doc();
                            } else {
                                frappe.msgprint(__('Error updating conversion rate: ' + response.message));
                            }
                        }
                    });
                });
            }, __('Actions'));
        }
    }
});