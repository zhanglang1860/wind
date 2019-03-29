# -*- coding: utf-8 -*-
from odoo import http

# class Wind(http.Controller):
#     @http.route('/wind/wind/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/wind/wind/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('wind.listing', {
#             'root': '/wind/wind',
#             'objects': http.request.env['wind.wind'].search([]),
#         })

#     @http.route('/wind/wind/objects/<model("wind.wind"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('wind.object', {
#             'object': obj
#         })