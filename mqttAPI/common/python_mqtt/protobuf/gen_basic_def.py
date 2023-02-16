import sys
from . import PbDefines_pb2 as BasicDef

def getRealType(type):
    if type[-1:] == 'T':
        return type[:-1]
    else:
        return type

def printH():

    print'''
/************************************
  This file is generated with tool,
  please do NOT modify it!
*************************************/

#ifndef PY_BASIC_DEF_H
#define PY_BASIC_DEF_H    
    '''
    for type in BasicDef.DESCRIPTOR.enum_types_by_name:

        realType = getRealType(type)
        attr = getattr(BasicDef, type).DESCRIPTOR

        print('''
typedef enum %s_ {''' % realType)

        for val in attr.values:
            print('    %s = %d,' % (val.name, val.number))

        print('} %s;' % (realType))

    for type in BasicDef.DESCRIPTOR.enum_types_by_name:
        realType = getRealType(type)
        attr = getattr(BasicDef, type).DESCRIPTOR
        print('''
extern char* get%sValStr(%s val);''' % (realType, realType))

    print('#endif')


def printC():

    print('''
/************************************
  This file is generated with tool,
  please do NOT modify it!
*************************************/
#include "basic_def.h"    
    ''')
    for type in BasicDef.DESCRIPTOR.enum_types_by_name:
        realType = getRealType(type)
        attr = getattr(BasicDef, type).DESCRIPTOR

        print('''
char* get%sValStr(%s val) {
    
    switch (val) {
    ''' % (realType, realType))

        for val in attr.values:
            print ('        case %s: return "%s(%d)";\n' % (val.name, val.name, val.number)) 

        print('''        default: return "unkown %s";
    }    
}''' % realType)


def printHelp():
    print("usage: %s printC|printH" % (__file__))

if len(sys.argv) != 2:
    printHelp()
    sys.exit(1)

if sys.argv[1] == "printC":
    printC()
elif sys.argv[1] == "printH":
    printH()
else:
    printHelp()
    sys.exit(1)

sys.exit(0)
    

