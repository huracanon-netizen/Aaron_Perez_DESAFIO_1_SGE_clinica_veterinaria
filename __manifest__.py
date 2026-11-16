{
    'name': "Orivetia",
    'summary': "Gestión de una clínica veterinaria",
    'description': "Registro de dueños y de sus mascotas",
    'author': "Aarón Pérez Ruiz",
    'category': "Services",
    'version': '0.1',
    'depends': ['base'],
    #Lo que hace el data es que como que carga los archivos de seguridad
    # y vistas para que se puedan ver en la interfaz de usuario
    'data': [
        'security/ir.model.access.csv',
        'views/duenyo_view.xml',
        'views/mascota_view.xml',
        'views/consulta_view.xml',
        'views/tratamiento_view.xml',
    ],
    #El demo son los datos de prueba, solo se cargan si la base de datos
    # se ha creado con los datos de demostracion
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
