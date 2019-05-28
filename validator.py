# -*- coding: utf-8 -*-

import cerberus


def form_validation(fname, lname, dob, dept, access, face):
    schema = {'fname': {'required': True, 'type': 'string', 'empty': False},
              'lname': {'required': True, 'type': 'string', 'empty': False},
              'dob': {'required': True, 'type': 'date', 'empty': False},
              'dept': {'required': True, 'type': 'string', 'empty': False},
              'access': {'required': True, 'type': 'integer', 'empty': False, 'min': 1, 'max': 3},
              'face': {'required': True, 'type': 'integer', 'empty': False, 'min': 128, 'max': 128}}

    document = {'fname': fname,
                'lname': lname,
                'dob': dob,
                'dept': dept,
                'access': access,
                'face': face}

    v = cerberus.Validator(schema)
    print('Cerberus : ', v.validate(document))

    print(v.errors)

    return v.validate(document)
