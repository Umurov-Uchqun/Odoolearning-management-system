# -*- coding: utf-8 -*-
{
    'name': "Education Payment Integration",
    'depends': ['lms_education', 'lms_payment'],
    'auto_install': ['lms_education', 'lms_payment'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/course.xml',
    ],
}
