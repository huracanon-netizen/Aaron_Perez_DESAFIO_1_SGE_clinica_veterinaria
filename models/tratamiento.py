# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Tratamiento(models.Model):
    _name = 'clinica_vet.tratamiento'
    _description = 'Tratamiento'

    name = fields.Char('Nombre', required=True)
    descripcion = fields.Text('Descripción')
    precio = fields.Float('Precio')
    duracion_minutos = fields.Integer('Duración (min)', default=30)
    categoria = fields.Selection([('vacuna', 'Vacuna'), ('cirugia', 'Cirugía'), ('analisis', 'Análisis'), ('otro', 'Otro')], string='Categoría', default='otro')
    activo = fields.Boolean('Disponible', default=True)
    fecha_alta = fields.Date('Fecha de alta', default=fields.Date.today)
    # Many2many es una relación donde muchos registros de un modelo están relacionados
    # con muchos registros de otro modelo
    consulta_ids = fields.Many2many( comodel_name='clinica_vet.consulta',relation='clinica_vet_consulta_tratamiento_rel',
    column1='tratamiento_id',column2='consulta_id',string='Consultas'
    )
    # Lo que hace basicamente es para comprobar que los datos esten bien
    @api.constrains('precio')
    def _comprobar_precio(self):
        for tratamiento in self:
            if tratamiento.precio < 0:
                raise ValidationError("El precio no puede ser negativo.")
                #Raise es para lanzar un error