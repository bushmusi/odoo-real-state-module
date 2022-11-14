{
    'name': 'Guest Book System',
    'version': '11.0.1.0',
    'category': 'Tools',
    'summary': 'Check in Guest Book System System',
    "description": """
        Check in Guest Book System
    """,
    'license':'LGPL-3',
    'data': [
        'data/ir.module.category.csv',
        'data/res.groups.csv',
        'data/guest_book_sequence.xml',
        'data/guest_book_purpose.xml',
        'security/ir.model.access.csv',
        'views/assets.xml',
        'views/guest_book.xml',
        'views/menus.xml',
         'views/email_templates.xml'
    ],
    'demo': [],
    'depends': ['mail','hr'],
    'images': ['static/description/syarif.png'],
    'installable': True,
}
