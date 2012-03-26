import sys
from lib import F_Helpers
from lib import T_Header
from lib import T_Implementation


if len(sys.argv) < 3:
    sys.exit('Usage: python %s [out_file] [inputs_file] [is_single_file=True]' % sys.argv[0])


out_file = sys.argv[1]
inputs_file = "inputs/" + sys.argv[2]
isSingleFile = sys.argv[3]

print isSingleFile

myList = F_Helpers.parseTextFile(inputs_file)

if isSingleFile == "True":
    print "Is single file output using the following parameters"
    print myList

headerData = ''
codeData = ''

for item in myList:
    paramName = item[1]
    typeDef = item[0]
    getterName = "get" + item[1]
    setterName = "set" + item[1]
    cacheVariable = "_cache" + item[1]
    if typeDef == "char *":
        defaultValue = "0\0"
    elif typeDef == "int":
        defaultValue = "0"
    else:
        defaultValue = "{0}"
    returnValue = "TRUE"
    params = {
    'paramName':paramName, 
    'typeDef':typeDef, 
    'getterName':getterName, 
    'setterName':setterName, 
    'cacheVariable':cacheVariable, 
    'defaultValue':defaultValue, 
    'returnValue':returnValue
    }

    if isSingleFile == "True":
        headerData += T_Header.getCodePatternHeader(params)
        codeData += T_Implementation.getCodePatternSynthesize(params)
    else:
        headerData = T_Header.getCodePatternHeader(params)
        fileName = paramName + ".h"
        F_Helpers.writeTemplateFile(fileName, headerData)

        codeData = T_Implementation.getCodePatternSynthesize(params)
        fileName = paramName + ".c"
        F_Helpers.writeTemplateFile(fileName, codeData)

if isSingleFile == "True":
    fileName = out_file + ".h"
    F_Helpers.writeTemplateFile(fileName, headerData)

    fileName = out_file + ".c"
    F_Helpers.writeTemplateFile(fileName, codeData)
