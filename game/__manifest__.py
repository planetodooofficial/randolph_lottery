{
    'name': 'Game',
    'version': '1.0',
    'category': 'Private',
    'complexity': 'easy',
    'description': "Game in odoo",
    'depends': ['base', 'website', 'web', 'contacts', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/withdraw_view.xml',
        'views/customer_transaction_view.xml',
        'views/game_template_view.xml',
        'views/game_one_view.xml',
        'views/game_two_view.xml',
        'views/game_data_view.xml',
        'views/lottery_draw_view.xml',
        'views/pdf_receipt_view.xml',
        'views/wheel_game_data_view.xml',
        'views/lottery_wheel_view.xml',
        'views/claim_buttom_template.xml',
        'views/moncash_api_view.xml',
        'views/choose_user_template.xml',
        'views/agent_customer_reg_view.xml',
        'views/moncash_button_view.xml',
        'views/moncash_payment_form_view.xml',
        'views/wallet_template_view.xml',
        'views/withdraw_request_view.xml',
        'views/bolet_game_template_view.xml',
    ],
    'installable': True,
}
