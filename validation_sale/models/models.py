# -*- coding: utf-8 -t

from odoo import models, fields, api ,_ 
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError


class ConfirmVentas(models.Model):
  
  _inherit = 'sale.order'

  uservalidation = fields.Many2one('res.users', string='Valido por',default=lambda self:self.env.user.id)
  userapprove = fields.Many2one('res.users',string="Aprobado por",default=lambda self:self.env.user.id)

  state = fields.Selection(selection_add=[('validate','Validado'),('approve','Aprobado')])

  @api.one
  def action_validate(self):
    self.write({'state': 'validate'})
    self.write({'uservalidation': self.env.user.id})
    
    #user_validation = self.env.user.id
    #raise ValidationError(user_validation)
    #return super(ConfirmVentas, self).action_validate()

  @api.one
  def action_approve(self):
    self.write({'state': 'approve'})
    self.write({'userapprove':self.env.user.id})