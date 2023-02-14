from . import PbOutput_pb2
from . import PbInput_pb2
from . import PbDefines_pb2
from . import PbMessages_pb2
import base64
import sys

if len(sys.argv) < 3 :
    print("pleae input: %s input|output str" % (sys.argv[0]))
    sys.exit(1)

type = sys.argv[1]
str = sys.argv[2]
data = base64.b64decode(str)

if type == "input":
    print("\nPbInput: \"%s\"" % str)
    print("------------------------\n")
    input = PbInput_pb2.PbInput()
    input.ParseFromString(data)
    print(input)
    print("------------------------\n")
elif type == "output":
    print("\nPbOutput: \"%s\"" % str)
    print("------------------------\n")
    output = PbOutput_pb2.PbOutput()
    output.ParseFromString(data)
    print(output)
    print("------------------------\n")
else :
    print("pleae input: %s input|output str" % (sys.argv[0]))

