# -*- coding: utf-8 -*-
from odoo import http

# class ValidationSale(http.Controller):
#     @http.route('/validation_sale/validation_sale/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/validation_sale/validation_sale/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('validation_sale.listing', {
#             'root': '/validation_sale/validation_sale',
#             'objects': http.request.env['validation_sale.validation_sale'].search([]),
#         })

#     @http.route('/validation_sale/validation_sale/objects/<model("validation_sale.validation_sale"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('validation_sale.object', {
#             'object': obj
#         })