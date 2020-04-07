from pathlib import Path

def check_argc(size):
  if size != 3:
    print("Example: Hex2Dump.py input.hex output.txt")
    return False
  return True

def check_input_file_name(filename):
  if not Path(filename).is_file():
    print("File doesn`t exist")
    return False
  return True

def check_length(index,length):
  if length < 11:
    print("Line number  ",index," is less than 10 characters long")
    return False
  return True

def check_first_character(index,character):
  if character != ":":
    print("Line number  ",index," does not have the first character ':'")
    return False
  return True

def check_characters(index,line):
  for character in line:
    if character not in "0123456789abcdefABCDEF":
      print("Line number  ",index," has an invalid character!")
      return False
  return True

def write_in_buffer(line):
  buffer = []
  for i in range(0,len(line),2):
    buffer.append(line[i:i+2])
  return buffer

def check_lenght_in_bytes(index,buffer):
  if int(buffer[0],16) > 16:
    print("Line number  ",index," has length more than 16 bytes!")
    return False
  return True

def check_checkSum(index,buffer):
  checksum = 0
  for i in range(0,len(buffer)):
    checksum+=int(buffer[i],16)
  if checksum & 0xff != 0:
      print("Line number  ",index," has an invalid checksum!")
      return False
  return True

def write_in_output(index,buffer,shift):
  adrs = buffer[1]
  adrs+= buffer[2]
  line = ""
  if buffer[3] == '00':
    line = shift.upper() + adrs.upper() + ":"
    for i in range(0,int(buffer[0],16)):
      line += str(buffer[i+4]).upper() + " "
    line += "\n"
    return (True,shift,line)
  if buffer[3] == '01':
      return (False,0,"")
  if buffer[3] == '04':
    if adrs != '0000' or buffer[0] != '02':
      print("Line number  ",index," has an invalid character!")
      return (False,0,"")
    shift = buffer[4] + buffer[5];
    return (True,shift,"");
  print("Line number  ",index," has invalid type!")
  return (False,0,"")

if __name__ == "__main__":main()
