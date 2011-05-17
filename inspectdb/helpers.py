import keyword
import re


uncamel_patterns = (
    re.compile('(.)([A-Z][a-z]+)'),
    re.compile('([a-z0-9])([A-Z])'),
    )

invalid_pat = re.compile(r'[^a-z0-9_]')
limit_pat = re.compile(r'_{2,}')


def uncamel(s):
    """
    Make camelcase lowercase and use underscores.

        >>> uncamel('CamelCase')
        'camel_case'
        >>> uncamel('CamelCamelCase')
        'camel_camel_case'
        >>> uncamel('Camel2Camel2Case')
        'camel2_camel2_case'
        >>> uncamel('getHTTPResponseCode')
        'get_http_response_code'
        >>> uncamel('get2HTTPResponseCode')
        'get2_http_response_code'
        >>> uncamel('HTTPResponseCode')
        'http_response_code'
        >>> uncamel('HTTPResponseCodeXYZ')
        'http_response_code_xyz'
    """
    for pat in uncamel_patterns:
        s = pat.sub(r'\1_\2', s)
    return s.lower()


def to_attname(s):
    s = uncamel(s)
    s = invalid_pat.sub('_', s)
    s = limit_pat.sub('_', s)
    s = s.strip('_')
    if keyword.iskeyword(s):
        s = s + '_field'
    return s

