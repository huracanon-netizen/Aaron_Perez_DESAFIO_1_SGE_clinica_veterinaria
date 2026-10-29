from odoo import models, fields, api


class Duenyo(models.Model):
    _name = 'clinica_vet.duenyo'
    _description = 'Dueño de mascota'

    nombre = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos', required=True)
    telefono = fields.Char(string='Teléfono')
    email = fields.Char(string='Email')
    fecha_alta = fields.Date(string='Fecha de alta')
    es_cliente_habitual = fields.Boolean(string='Cliente habitual', default=False)
    notas = fields.Text(string='Notas')
    mascota_ids = fields.One2many('clinica_vet.mascota', 'duenyo_id', string='Mascotas')
    peso_total = fields.Float(string='Peso total de sus mascotas', compute='_calcular_peso_total')

    @api.depends('mascota_ids.peso')
    def _calcular_peso_total(self):
        for record in self:
            record.peso_total = sum(record.mascota_ids.mapped('peso'))