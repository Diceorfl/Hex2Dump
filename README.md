# Hex2Dump
 ##Convert a HEX file to a DUMP standard  
 ##Преобразование файла стандарта HEX в стандарт DUMP  

 ###How does it work?  
    • Input file format: Intel Hex 32  
        Format Description:https://en.wikipedia.org/wiki/Intel_HEX  
    • Output file format DUMP: 00123456: 12 34 56 78 90  
    • Input validation:  
        o First character is ":"  
        o Only hexadecimal digits  
        o String length less than 16 bits  
        o Checksum  
    • Launch command line example: Hex2Dump.py input.hex output.txt  

 ###Как это работает?  
    •	Формат входного файла:	Intel Hex 32     
         Описание формата:	https://ru.wikipedia.org/wiki/Intel_HEX  
    •	Формат выходного файла DUMP:		00123456: 12 34 56 78 90  
    •	Проверка входных данных:  
         o	Наличие двоеточия  
         o	Только шестнадцатеричные цифры  
         o	Длина строки не более 16 байт  
         o	Контрольная сумма  
    •	Пример командной строки запуска: Hex2Dump.py input.hex output.txt  
