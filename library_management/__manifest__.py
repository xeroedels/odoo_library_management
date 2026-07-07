{
    'name': 'Library Management',
    'version': '1.0',
    'summary': 'Simple Library Management System',
    'author': 'Sagita S W',
    'category': 'Library',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/book_views.xml',
        'views/member_views.xml',
        'views/borrowing_views.xml'
    ],
    'installable': True,
    'application': True,
}