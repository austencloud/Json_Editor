from copy import deepcopy

def default_value(node):
    schema = deepcopy(node['value'])
    node['schema']['properties']['default'] = schema

property_list = {
    'common': [
        '$id',
        '$schema',
        'title',
        'description',
        'definitions',
        'default'
    ],
    'string': [
        'enum',
        'maxLength',
        'minLength',
        'format',
        'pattern'
    ],
    'integer': [
        'enum',
        'multipleOf',
        'maximum',
        'exclusiveMaximum',
        'minimum'
    ]
}
