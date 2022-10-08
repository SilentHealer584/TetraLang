import sys

#%!^!   £%£   %%^£   £%£   %%%%   %%£%   %£%%   $$!^

arg = sys.argv[1]

global vars
vars = {}

class Tetralang:
    def decompile(cmd):
        
        if cmd == 1111:
            print('print')
            return
        if cmd == 1112:
            print('input')
            return
        if cmd == 1113:
            print('exec')
            return
        if cmd == 1114:
            print('newvar')
            return
        if cmd == 1121:
            print('"')
            return
        if cmd == 1122:
            print('or')
            return
        if cmd == 1123:
            print('and')
            return
        if cmd == 1124:
            print('not')
            return
        if cmd == 1131:
            print('=')
            return
        if cmd == 1132:
            print('==')
            return
        if cmd == 1133:
            print('a')
            return
        if cmd == 1134:
            print('b')
            return
        if cmd == 1141:
            print('c')
            return
        if cmd == 1142:
            print('d')
            return
        if cmd == 1143:
            print('e')
            return
        if cmd == 1144:
            print('f')
            return
        if cmd == 1211:
            print('g')
            return
        if cmd == 1211:
            print('h')
            return
        if cmd == 1211:
            print('i')
            return
        if cmd == 1211:
            print('j')
            return
        if cmd == 1212:
            print('k')
            return
        if cmd == 1213:
            print('l')
            return
        if cmd == 1214:
            print('m')
            return
        if cmd == 1221:
            print('n')
            return
        if cmd == 1222:
            print('o')
            return
        if cmd == 1223:
            print('p')
            return
        if cmd == 1224:
            print('q')
            return
        if cmd == 1231:
            print('r')
            return
        if cmd == 1232:
            print('s')
            return
        if cmd == 1233:
            print('t')
            return
        if cmd == 1234:
            print('u')
            return
        if cmd == 1241:
            print('v')
            return
        if cmd == 1242:
            print('w')
            return
        if cmd == 1243:
            print('x')
            return
        if cmd == 1244:
            print('y')
            return
        if cmd == 1311:
            print('z')
            return
        if cmd == 1312:
            print('A')
            return
        if cmd == 1313:
            print('B')
            return
        if cmd == 1314:
            print('C')
            return
        if cmd == 1321:
            print('D')
            return
        if cmd == 1322:
            print('E')
            return
        if cmd == 1323:
            print('F')
            return
        if cmd == 1324:
            print('G')
            return
        if cmd == 1331:
            print('H')
            return
        if cmd == 1332:
            print('I')
            return
        if cmd == 1333:
            print('J')
            return
        if cmd == 1334:
            print('K')
            return
        if cmd == 1341:
            print('L')
            return
        if cmd == 1342:
            print('M')
            return
        if cmd == 1343:
            print('N')
            return
        if cmd == 1344:
            print('O')
            return
        if cmd == 1411:
            print('P')
            return
        if cmd == 1412:
            print('Q')
            return
        if cmd == 1413:
            print('R')
            return
        if cmd == 1414:
            print('S')
            return
        if cmd == 1421:
            print('T')
            return
        if cmd == 1422:
            print('U')
            return
        if cmd == 1423:
            print('V')
            return
        if cmd == 1424:
            print('W')
            return
        if cmd == 1431:
            print('X')
            return
        if cmd == 1432:
            print('Y')
            return
        if cmd == 1433:
            print('Z')
            return
        if cmd == 1434:
            print('if')
            return
        if cmd == 1441:
            print('else')
            return
        if cmd == 1442:
            print('for')
            return
        if cmd == 1443:
            print('in')
            return
        if cmd == 1444:
            print(' ')
            return
            
        
        
        if cmd == 211:
            print('0')
            return
        if cmd == 212:
            print('1')
            return
        if cmd == 213:
            print('2')
            return
        if cmd == 214:
            print('3')
            return
        if cmd == 221:
            print('4')
            return
        if cmd == 222:
            print('5')
            return
        if cmd == 223:
            print('6')
            return
        if cmd == 224:
            print('7')
            return
        if cmd == 231:
            print('8')
            return
        if cmd == 232:
            print('9')
            return
        if cmd == 233:
            print('+')
            return
        if cmd == 234:
            print('-')
            return
        if cmd == 241:
            print('*')
            return
        if cmd == 242:
            print('/')
            return
        if cmd == 243:
            print('%')
            return
        if cmd == 244:
            print('**')
            return
            
            
            
        if cmd == 31:
            print('Na')
            return
        if cmd == 32:
            print('Na')
            return
        if cmd == 33:
            print('Na')
            return
        if cmd == 34:
            print('Na')
            return
        
        
        
        if cmd == 4:
            print('Na')
            return
            
            
        else:
            print("FATAL COMPILER ERROR. DON'T CLOSE TERMINAL. SYSTEM FILES MAY BE LOST FOREVER.")
        
    

with open(arg, 'r') as file:
    file = file.read()
    file = file.split("\n")
    linenumber = 0
    for line in file:
        
        linenumber += 1
        if not '%' or not '£' or not '^' or not '!' in line:
            print(f"Fatal error at line: {linenumber}, forbidden character.  Don't close your terminal, system files may be lost forever.")
        
        line1 = line.split(' ')
        for ttbyt in line1:
            ttbyts = list(ttbyt)
            index = ''
            for char in ttbyts:
                if char == '%':
                    index += '1'
                if char == '$':
                    index += '2'
                if char == '^':
                    index += '3'
                if char == '!':
                    index += '4'
            
            #print("CMD INDEX IS:", index)
            
            Tetralang.decompile(int(index))
        
        
        
        
        
        
        
        
        
        