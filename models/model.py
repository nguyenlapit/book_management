from odoo import fields, models


class BookCategory(models.Model):
    _name = 'demo.book.cata'

    name = fields.Char(size=100, string='Tên thể loại')
    description = fields.Text(string='Ghi chú')

class BookAuthor(models.Model):
    _name = 'book.author'

    name = fields.Char(size=100,string='Tên tác giả',required=True)
    birthday = fields.Date(string='Ngày sinh',required = True)
    gender = fields.Selection(string="Giới tính", selection=[('0', 'Nam'), ('1', 'Nữ'),('2', 'Giới tính thứ 3'), ], required=True, )
    image = fields.Binary(string="Avatar", attachments = True )
