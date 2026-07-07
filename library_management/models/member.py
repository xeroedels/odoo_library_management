from odoo import models, fields

class LibraryMember(models.Model):
    _name = "library.member"
    _description = "Library Member"

    name = fields.Char(string="Member Name", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone Number")