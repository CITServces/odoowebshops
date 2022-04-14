# Copyright (C) Apr,17 2020, Emipro Technologies Pvt. Ltd.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    # About Module
    'name': 'Ecommerce Extended',
    'category': 'Extra Tools',
    'version': '12.0.0.1',
    'license': 'AGPL-3',
    'description': """

    """,

    # Dependencies
    'depends': ['website_sale_wishlist'],

    # Views
    'data': [
        'view/product_template.xml',
	    'view/mail_template.xml',
	    'template/templates.xml',
        'data/data.xml'
    ],

    # Author
    'author': 'Emipro Technologies Pvt. Ltd.',
    'website': 'http://www.emiprotechnologies.com',

    # Technical
    'installable': True,
}
