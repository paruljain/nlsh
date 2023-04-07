# nsh

nsh is a Natural Language Shell for Linux. Instead of remembering BASH commands, you can type your intent in natural language. nsh converts the intent to BASH command using OpenAI GPT-3, the same technology used by ChatGPT. You can type things like:

* create a file hello.txt with contents "hello world"
* what is the dns config?
* add dns 1.1.1.1 to DNS config. Use sudo
* what is the time?
* list users
* is there a user called backup?
* create archive test.tar.gz from folder test
* get www.google.com
* show available disk space
* show available disk space. show only the 5th column
* !cd /
    * Commands prefixed with ! are executed without translation
* @how do I mount a nfs share on an Ubuntu server?
    * Commands prefixed with @ get help

# Prerequisites
* A Linux system
* Python 3
* API key from OpenAI. You can [get one here](https://platform.openai.com/playground) for free. Sign up, then click on *Personal* top right corner, then *View API keys*.

# Installing nsh
Download the zip of this repo on your Linux machine. Extract to any folder.

# Running nsh
*python nsh.py*