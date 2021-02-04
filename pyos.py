#!/usr/bin/python
#using namescape std
#pyos.py-Python Optrating System

import os,sys,math,cmath,time
import random,turtle,tkinter
import json,pickle
import subprocess as r

#values
USERINDEX = None
USERPASSWD = {
    "OPERATOR":"pyosadmin",
    "GUEST":"pyosadmin"
    }
#end


def printtitle(TITLESTYLE):
    title1="""
888888
8888888
55    77
55    777
55    969
55    777  787        787   000000     5656556
55    77    789      789   00000000   456456456
8888888      123    123    00    00  457
888888       123    123    00    00  123
11            456  456     00    00   45645645
11             789789      00    00    78979789
11              7410       00    00    15915915
11             8520        00    00         123
11             9630        00    00         123
11            7410         00000000  512312312
000         67410           000000    1591591   1.0

"""
    title2="""
#######
##    ##
##     #
##     #    
##     #   
##    ##   ##     ##  ####   ####
#######     ##   ##  #    # #    #
##           ## ##   #    # #
##            ###    #    #  ####
##            ##     #    #      #
##           ##      #    # #    #
###        ###        ####   ####  1.0
"""
    title3="""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@  @@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@  @@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@  @@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@  @@@@@@@  @@@@@  @@    @@@    @@@@@@@@@@@@@@@@
@  @@@@@@@@  @@@  @@  @@  @  @@  @@@@@@@@@@@@@@@
@  @@@@@@@@@  @  @@@  @@  @  @@ @@@@@@@@@@@@@@@@
@  @@@@@@@@@@   @@@@  @@  @   @@@@@@@@@@@@@@@@@@
@  @@@@@@@@@@  @@@@@  @@  @@    @@@@@@@@@@@@@@@@
@  @@@@@@@@@  @@@@@@  @@  @@@@@  @@@@@@@@@@@@@@@
@  @@@@@@@@  @@@@@@@      @@@@  @@@@@@@@=====@@@
    @@@@@@    @@@@@@@    @@@    @@@@@@@@|1.0|@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=====@@@
"""
    if TITLESTYLE==1:
        print(title1)
    elif TITLESTYLE==2:
        print(title2)
    elif TITLESTYLE==3:
        print(title3)
    #End If
    print("")
    print("PYOS - Python Optrating System")
    print("PYOS 1.0")
    print("Usage:python pyos.py")
    print("Using python version:\n"+sys.version)
    print("")
#End Function

#输出提示符
class stdout:
    LOG="[*]"
    WARN="[!]"
    ERROR="[X]"
    DEBUG="[/]"
    GUESS="[?]"
    global USERLIST,STDPATH
    USERLIST = ["OPERATOR","GUEST"]
    STDPATH = ["/"]
#End Class

#所有程序命令
class cmdfunc:
    def echo(echoin):
        print(echoin)
    #End Function
    def textread(option,readtext):
        try:
            with open(readtext,option) as readobj:
                print((readobj.read()).rstrip())
        except FileNotFoundError:
            print(stdout.ERROR+"File not found!")
        except ValueError as ERROR:
            print(ERROR)
            print("Options List:")
            print("""r;rb;r+;rb+;w;wb;w+;wb+;a;ab;a+;ab+""")
    #End Function
    def cd(cdpath):

        if os.path.exists(cdpath) and os.path.isdir(cdpath):
            STDPATH=cdpath
        else:
            print(stdout.ERROR+cdpath+":Not a dictonary")
    def lsf():
        print(os.listdir(STDPATH))

#输入                
def cmd():
    global stdin
#输入提示符
    stdin = input(USERLIST[USERINDEX]+"@pyos["+('/'.join(STDPATH))+"]-"+CMDOG)
    stdin = stdin.split(" ")
    try:
        if stdin[0]!="exit":
            optioncmd = stdin[1]
    except IndexError :
        print(stdout.WARN+"Please input option")
    if stdin[0]=="echo":
        try:
            print(stdin[1])
        except IndexError as ERROR:
            print(ERROR)
            pass
    elif stdin[0]=="exit":
        sys.exit()
    elif stdin[0]=="textread":
        try:
            cmdfunc.textread(stdin[1],stdin[2])
        except IndexError as ERROR:
            print(ERROR)
            pass
        except FileNotFoundError as ERROR:
            print(ERROR)
            pass
    elif stdin[0]=="cd":
        cmdfunc.cd(stdin[1])
    elif stdin[0]=="clear":
        r.run("cls",shell=True)
    else:
        print(stdout.ERROR+"-error:Command Not Found!")

#主程序运行
def main():
    global OSLOGIN,USERINDEX,CMDOG,INPASSWD
    global STDPATH
    while True:
        OSLOGIN=input("Login pyos:")
        if OSLOGIN=="OPERATOR":
            INPASSWD=input("Password from OPERATOR:")
            if INPASSWD == USERPASSWD["OPERATOR"]:
                CMDOG="#"
                USERINDEX=0
                break
            else:
                print("Password is incorrect!")
                print("Try again.")
                continue
        elif OSLOGIN=="GUEST":
            INPASSWD=input("Password from GUEST:")
            if INPASSWD == USERPASSWD["GUEST"]:
                CMDOG="$"
                USERINDEX=1
                break
            else:
                print("Password is incorrect!")
                print("Try again.")
                continue
        else:
            print("No user named "+OSLOGIN)
            print("Try again with \"OPERATOR\" or \"GUEST\"")
            continue
    while True:
        cmd()
    

if __name__ == "__main__":
    #Run command:r
    if os.path.exists('osvdisk'):
        r.run('cd /osvdisk',shell=True)
    else:
        r.run(r'.\\init.bat')

    print("Debug message:")
    print("[Working path]"+os.getcwd())
    print("[Time]"+time.asctime())
    
    r.run("cls",shell=True)
    print("===========[Starting pyos system]==============")
    printtitle(random.randint(1,3))
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print("You push the Control-C.")
            print("The program will stop!")
            sdsgefhhgh = input('Are you sure to stop?[y/n](Default=n)')
            if sdsgefhhgh.lower() == 'y':
                sys.exit()
            else:
                continue
        except:
            """
            print("There is an error while running.")
            print(stdout.DEBUG+"Application Shutdown!")
            print(stdout.ERROR+"pyos exited.")
            sys.exit()"""
            pass
        














