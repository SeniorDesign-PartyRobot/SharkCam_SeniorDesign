from . import PbOutput_pb2

output = PbOutput_pb2.PbOutput()

print('''
/*
  NOTICE: this file automatically generated with script, do not modify it unless using the script
*/

#include "AsyncController.h"

namespace Platform {

    bool AsyncController::matchRpcReq(const pb::PbRpcReq &rpc, const pb::PbOutput &output) {

        std::string method = rpc.method();

        if(method != "query") {
            return false;
        }

        std::string attr = rpc.params(0);
''')

for idx in output.DESCRIPTOR.fields:

    check = ""
    if idx.containing_oneof:
        check = "return output.%s_case();" % (idx.containing_oneof.name);        
    else:
        check = "return true;"

    print('''
        if(attr == "%s") {
            %s
        }''' % (idx.name, check))

print('''
    }
}
''')



