app_name = "update_after_submit"
app_title = "Update After Submit"
app_publisher = "Ahmed Abukhatwa"
app_description = "Update after submit in sales orders which is submited"
app_email = "ahmedreda199785@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/update_after_submit/css/update_after_submit.css"
# app_include_js = "/assets/update_after_submit/js/update_after_submit.js"

# include js, css files in header of web template
# web_include_css = "/assets/update_after_submit/css/update_after_submit.css"
# web_include_js = "/assets/update_after_submit/js/update_after_submit.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "update_after_submit/public/scss/website"
x
# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Sales Order" : "public/js/sales_order.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "update_after_submit.utils.jinja_methods",
# 	"filters": "update_after_submit.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "update_after_submit.install.before_install"
# after_install = "update_after_submit.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "update_after_submit.uninstall.before_uninstall"
# after_uninstall = "update_after_submit.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "update_after_submit.utils.before_app_install"
# after_app_install = "update_after_submit.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "update_after_submit.utils.before_app_uninstall"
# after_app_uninstall = "update_after_submit.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "update_after_submit.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"update_after_submit.tasks.all"
# 	],
# 	"daily": [
# 		"update_after_submit.tasks.daily"
# 	],
# 	"hourly": [
# 		"update_after_submit.tasks.hourly"
# 	],
# 	"weekly": [
# 		"update_after_submit.tasks.weekly"
# 	],
# 	"monthly": [
# 		"update_after_submit.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "update_after_submit.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "update_after_submit.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "update_after_submit.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["update_after_submit.utils.before_request"]
# after_request = ["update_after_submit.utils.after_request"]

# Job Events
# ----------
# before_job = ["update_after_submit.utils.before_job"]
# after_job = ["update_after_submit.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"update_after_submit.auth.validate"
# ]
