
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Mascota(models.Model):
    _name = 'clinica_vet.mascota'
    _description = 'Mascota'

    nombre = fields.Char(string='Nombre', required=True, help='Nombre de la mascota')
    especie = fields.Selection(selection=[('perro', 'Perro'),('gato', 'Gato'),
    ('otro', 'Otro')],string='Especie', default='perro', required=True)
    raza = fields.Char(string='Raza')
    peso = fields.Float(string='Peso (kg)')
    edad = fields.Integer(string='Edad')
    fecha_nacimiento = fields.Date(string='Fecha de nacimiento')
    duenyo_id = fields.Many2one('clinica_vet.duenyo', string='Dueño', required=True)

    @api.constrains('fecha_nacimiento')
    def _check_fecha_nacimiento(self):
        for record in self:
            if record.fecha_nacimiento and record.fecha_nacimiento > fields.Date.today():
                raise ValidationError("La fecha de nacimiento no puede ser futura.")
