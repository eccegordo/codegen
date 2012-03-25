from lib import F_Helpers
from lib import T_Header
from lib import T_Implementation


# # print T_Header.getCodePatternHeader("myType", "myGetter", "mySetter")
# 
# params = {'typeDef':'myType', 'getterName':'myGetter', 'setterName':'mySetter', 'cacheVariable':'_cacheVar', 'defaultValue':'0', 'returnValue':'TRUE' }
# 
# # print T_Implementation.getCodePatternSynthesize(params)
# 
# params = {
# 'paramName':'myParam', 
# 'typeDef':'myType', 
# 'getterName':'myGetter', 
# 'setterName':'mySetter', 
# 'cacheVariable':'_cacheVar', 
# 'defaultValue':'0', 
# 'returnValue':'TRUE'
# }
# 
# paramsEmpty = {}
# 
# print T_Implementation.getCodePatternSynthesize(params)
# 
# print T_Implementation.getCodePatternSynthesize(paramsEmpty)

# params = {'typeDef':'myType', 'getterName':'myGetter', 'setterName':'mySetter', 'cacheVariable':'_cacheVar', 'defaultValue':'0', 'returnValue':'TRUE' }

params = {
'paramName':'myParam', 
'typeDef':'myType', 
'getterName':'myGetter', 
'setterName':'mySetter', 
'cacheVariable':'_cacheVar', 
'defaultValue':'0', 
'returnValue':'TRUE'
}

codeOutput = ''
codeOutput += T_Header.getCodePatternHeader(params)
codeOutput += T_Implementation.getCodePatternSynthesize(params)

# print T_Header.getCodePatternHeader(params)
# print T_Implementation.getCodePatternSynthesize(params)

# fileName = "code.c"
# F_Helpers.writeTemplateFile(fileName, codeOutput)

inFile = "inputs/input_text.txt"
myList = F_Helpers.parseTextFile(inFile)

print myList

from inputs import input_code

myData = input_code.inputData

# inFileCode = "input/input_code.py"
# myData = F_Helpers.loadCodeFromFile(inFileCode)

for item in myData:
    print item

for item in myList:
    print item
# print myData[2]

