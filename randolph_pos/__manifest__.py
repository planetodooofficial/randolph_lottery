{
    'name': 'Pos Randolph',
    'version': '1.0',
    'category': 'POS',
    'description': "Pos in odoo",
    'depends': ['base', 'point_of_sale', 'pos_retail'],
    'data': [
        'views/pos_template.xml',
        'views/partner_view.xml',
    ],
    'qweb': [
        'static/src/xml/pos_view.xml',
        'static/src/xml/games_template.xml',
    ],
    'installable': True,
}
