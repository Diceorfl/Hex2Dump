# Hex2Dump
 ## Convert a HEX file to a DUMP standard / Преобразование файла стандарта HEX в стандарт DUMP  
  
 ### How does it work?  
    1. Input file format: Intel Hex 32  
       Format Description:https://en.wikipedia.org/wiki/Intel_HEX  
    2. Output file format DUMP: 00123456: 12 34 56 78 90  
    3. Input validation:  
      3.1 First character is ":"  
      3.2 Only hexadecimal digits  
      3.3 String length less than 16 bits  
      3.4 Checksum  
    4. Launch command line example: Hex2Dump.py input.hex output.txt  

 ### Как это работает?  
    1. Формат входного файла:	Intel Hex 32     
       Описание формата:	https://ru.wikipedia.org/wiki/Intel_HEX  
    2. Формат выходного файла DUMP:		00123456: 12 34 56 78 90  
    3. Проверка входных данных:  
      3.1	Наличие двоеточия  
      3.2	Только шестнадцатеричные цифры  
      3.3 Длина строки не более 16 байт  
      3.4	Контрольная сумма  
    4.	Пример командной строки запуска: Hex2Dump.py input.hex output.txt  
