from odoo import models, fields


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string="Book Title", required=True)
    author = fields.Char(string="Author")
    isbn = fields.Char(string="ISBN")
    available = fields.Boolean(string="Available", default=True)
    