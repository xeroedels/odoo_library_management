from odoo import models, fields

class LibraryBorrowing(models.Model):
    _name = "library.borrowing"
    _description = "Library Borrowing"

    book_id = fields.Many2one("library.book", string="Book", required=True)
    member_id = fields.Many2one("library.member", string="Member", required=True)
    date_borrow = fields.Date(string="Borrow Date")
    date_return = fields.Date(string="Return Date")
    status = fields.Selection(
        [
            ('borrowed', 'Borrowed'),
            ('returned', 'Returned'),
        ],
        string="Status",
        default='borrowed'
    )