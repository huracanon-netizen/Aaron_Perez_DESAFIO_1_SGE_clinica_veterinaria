{
    'name': "Orivetia",
    'summary': "Gestión de una clínica veterinaria",
    'description': "Registro de dueños y de sus mascotas",
    'author': "Aarón Pérez Ruiz",
    'category': "Services",
    'version': '0.1',
    'depends': ['base'],
    'data': ['security/ir.model.access.csv','views/duenyo_view.xml',
    'views/mascota_view.xml',],
    'installable': True,
    'application': True,
}
