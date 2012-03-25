# Example Usage
# params = {'typeDef':'myType', 'getterName':'myGetter', 'setterName':'mySetter'}
# getCodePatternHeader(params)

def getCodePatternHeader(params):

    # Set defaults so that they will be obvious in code
    params.setdefault('paramName', 'UNDEFINED_PARAM_NAME')
    params.setdefault('typeDef', 'UNDEFINED_TYPE_DEF')
    params.setdefault('getterName', 'UNDEFINED_GETTER')
    params.setdefault('setterName', 'UNDEFINED_SETTER')

    string = ''
    string += '' + '\n'
    string += 'extern '+ params['typeDef'] +' '+ params['setterName'] +'();' + '\n'
    string += 'extern '+ params['typeDef'] +' '+ params['getterName'] +'('+ params['typeDef'] + ' data);' + '\n'

    return string;