
# Example Usage
# params = {'typeDef':'myType', 'getterName':'myGetter', 'setterName':'mySetter', 'cacheVariable':'_cacheVar', 'defaultValue':'0', 'returnValue':'TRUE' }
# getCodePatternSynthesize(params)

def getCodePatternSynthesize(params):

    # Set defaults so that they will be obvious in code
    params.setdefault('paramName', 'UNDEFINED_PARAM_NAME')
    params.setdefault('typeDef', 'UNDEFINED_TYPE_DEF')
    params.setdefault('getterName', 'UNDEFINED_GETTER')
    params.setdefault('setterName', 'UNDEFINED_SETTER')
    params.setdefault('cacheVariable', 'UNDEFINED_CACHE_VARIABLE')
    params.setdefault('defaultValue', 'UNDEFINED_DEFAULT_VALUE')
    params.setdefault('returnValue', 'UNDEFINED_RETURN_VALUE')

    string = ''
    string += '' + '\n'
    string += '/////////////////////////////////////////////////////// ' + '\n'
    string += '// Getter and Setter for ' + params['paramName'] + '\n'
    string += '/////////////////////////////////////////////////////// ' + '\n'
    string += 'static '+ params['typeDef'] +' '+ params['cacheVariable'] +';' + '\n'
    string += '' + '\n'
    string += 'extern '+ params['typeDef'] +' '+ params['getterName'] +'() {' + '\n'
    string += '' + '\n'
    string += '   static int isInitialized = FALSE;' + '\n'
    string += '   '+ params['typeDef'] +' data;' + '\n'
    string += '   static '+ params['typeDef'] +' defaultData = '+ params['defaultValue'] +';' + '\n'
    string += '' + '\n'
    string += '   if (isInitialized){' + '\n'
    string += '       isInitialized = TRUE;' + '\n'
    string += '       memcpy(data, ' + params['cacheVariable'] + ', sizeof ' + params['cacheVariable'] + ');' + '\n'
    string += '   }' + '\n'
    string += '   else {' + '\n'
    string += '       isInitialized = TRUE;' + '\n'
    string += '   }' + '\n'
    string += '' + '\n'
    string += '   return data;' + '\n'
    string += '}' + '\n'
    string += '' + '\n'
    string += '' + '\n'
    string += 'extern int '+ params['setterName'] +'('+ params['typeDef'] +' data){' + '\n'
    string += '' + '\n'
    string += '   // Set the data here and update file scoped cache variable' + '\n'
    string += '       memcpy(' + params['cacheVariable'] + ', data, sizeof data);' + '\n'
    string += '' + '\n'
    string += '   return ' + params['returnValue'] + ';' + '\n'
    string += '}' + '\n'
    string += '' + '\n'

    return string;