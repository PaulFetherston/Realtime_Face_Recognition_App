# -*- coding: utf-8 -*-

# Paul Fetherston
#
# Student No: 2898842
#
# BSCH 4th year development project
#
# 31/05/2019

import cerberus


def form_validation(fname, lname, dob, dept, access, face):
    """Method to perform validation on user data"""

    # Create a schema of conditionals for each piece of data
    schema = {'fname': {'required': True, 'type': 'string', 'empty': False},
              'lname': {'required': True, 'type': 'string', 'empty': False},
              'dob': {'required': True, 'type': 'date', 'empty': False},
              'dept': {'required': True, 'type': 'string', 'empty': False},
              'access': {'required': True, 'type': 'integer', 'empty': False, 'min': 1, 'max': 3},
              'face': {'required': True, 'type': 'integer', 'empty': False, 'min': 128, 'max': 128}}
    # Create your document of data to be tested
    document = {'fname': fname,
                'lname': lname,
                'dob': dob,
                'dept': dept,
                'access': access,
                'face': face}
    # Initiase a validator with the schema
    v = cerberus.Validator(schema)

    # Print to console if validation was successful or not
    print('Cerberus : ', v.validate(document))
    # Print to console any validation errors
    print(v.errors)
    # Validate document on the validator
    # Returns True if all pass - False if any fails
    return v.validate(document)
