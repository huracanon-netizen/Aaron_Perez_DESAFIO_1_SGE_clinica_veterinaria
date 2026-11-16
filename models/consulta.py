# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Consulta(models.Model):
    _name = 'clinica_vet.consulta'
    _description = 'Consulta veterinaria'

    name = fields.Char('Motivo', required=True)
    fecha_hora = fields.Datetime('Fecha y hora', default=fields.Datetime.now, required=True)
    estado = fields.Selection([('pendiente', 'Pendiente'), ('realizada', 'Realizada'), ('cancelada', 'Cancelada')], string='Estado', default='pendiente')
    precio = fields.Float('Precio de la consulta')
    precio_total = fields.Float('Precio total', compute='_calcular_total')
    diagnostico = fields.Text('Diagnóstico')
    urgente = fields.Boolean('Urgente', default=False)
    mascota_id = fields.Many2one('clinica_vet.mascota', string='Mascota', required=True)
    tratamiento_ids = fields.Many2many(comodel_name='clinica_vet.tratamiento',relation='clinica_vet_consulta_tratamiento_rel',
    column1='consulta_id', column2='tratamiento_id',string='Tratamientos')

    #Lo que hace es que como que recalcula un campo calculado cuando cambias los campos
    @api.depends('precio', 'tratamiento_ids.precio')
    def _calcular_total(self):
        for consulta in self:
              consulta.precio_total = consulta.precio + sum(t.precio for t in consulta.tratamiento_ids)
        
    # Lo que hace basicamente es para comprobar que los datos esten bien
    @api.constrains('precio')
    def _comprobar_precio(self):
        for consulta in self:
            if consulta.precio < 0:
                raise ValidationError("El precio no puede ser negativo.")

    def action_realizada(self):
        for consulta in self:
            consulta.estado = 'realizada'

    def action_cancelar(self):
        for consulta in self:
            consulta.estado = 'cancelada'