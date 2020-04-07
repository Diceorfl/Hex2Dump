import sys
import Hex2DumpCheck

if not Hex2DumpCheck.check_argc(len(sys.argv)):sys.exit(1)
if not Hex2DumpCheck.check_input_file_name(str(sys.argv[1])):sys.exit(1)
try:
    input = open(str(sys.argv[1]),"r")
except IOError:
    print("File not available")
    sys.exit(1)
output = open(str(sys.argv[2]),"w")
shift = "0000"
for index,line in enumerate(input,1):
    line = line.replace("\n","")
    if not Hex2DumpCheck.check_length(index,len(line)):break
    if not Hex2DumpCheck.check_first_character(index,line[0]):break
    if not Hex2DumpCheck.check_characters(index,line[1:]):break
    buffer = Hex2DumpCheck.write_in_buffer(line[1:])
    if not Hex2DumpCheck.check_lenght_in_bytes(index,buffer):break
    if not Hex2DumpCheck.check_checkSum(index,buffer):break
    answer = Hex2DumpCheck.write_in_output(index,buffer,shift)
    shift = answer[1]
    if not answer[0]:break
    if answer[2] != "":output.write(answer[2])
input.close()
output.close()
