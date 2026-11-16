from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Mascota(models.Model):
    _name = 'clinica_vet.mascota'
    _description = 'Mascota'
    #El _rec_name es el campo que se enseña cuando se elige una mascota desde otro modelo
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre', required=True, help='Nombre de la mascota')
    especie = fields.Selection([('perro', 'Perro'), ('gato', 'Gato'), ('otro', 'Otro')], string='Especie', default='perro', required=True)
    raza = fields.Char(string='Raza')
    peso = fields.Float(string='Peso (kg)')
    fecha_nacimiento = fields.Date(string='Fecha de nacimiento')
    edad = fields.Integer(string='Edad', compute='_calcular_edad')
    #Binary es para que se pueda subir una imagen
    foto = fields.Binary(string='Foto')
    # Many2one una relación donde muchos registros de un modelo están
    # relacionados con uno solo de otro modelo
    duenyo_id = fields.Many2one('clinica_vet.duenyo', string='Dueño', required=True)
    #api.depends es para que no haya error
    @api.depends('fecha_nacimiento')
    def _calcular_edad(self):
        hoy = fields.Date.today()
        for mascota in self:
            if mascota.fecha_nacimiento:
                if mascota.fecha_nacimiento > hoy:
                    raise ValidationError("La fecha de nacimiento no puede ser futura.")
                mascota.edad = (hoy - mascota.fecha_nacimiento).days // 365
            else:
                mascota.edad = 0