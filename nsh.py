#!/usr/bin/python

from openai import getCmd, getHelp
import subprocess
import os

basePrompt = '''Convert text into Ubuntu Linux bash command.
Text: create an archive called myfiles.tar.gz from folder /myfolder
Command: tar -cvzf myfiles.tar.gz /myfolder
Text: list files
Command: ls
Text: '''

def chdir(input):
    try:
        folder = input.split(' ')[1].strip()
        os.chdir(folder)
    except:
        pass

def runShellCmd(input):
    try:
        subprocess.run(input[1:], shell=True)
    except:
        pass


while True:
    print()
    print(f'{os.getcwd()}>', end=' ')
    inp = input()
    if inp == '' or inp == None: continue

    if inp.startswith('!'):
        if inp.startswith('!cd '): chdir(inp)
        else: runShellCmd(inp)
    
    elif inp.startswith('@'): print(getHelp(inp[1:]))
    
    else:
        cmd = getCmd(basePrompt + inp + '\n' + 'Command:')
        if cmd == None: continue
        print(cmd)
        if cmd.startswith('cd'): chdir(cmd)
        else:
            try:
                subprocess.run(cmd, shell=True)
            except:
                pass