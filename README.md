# challenge2Day5
[![Build Status](https://travis-ci.org/AineKiraboMbabazi/challenge2Day5.svg?branch=master)](https://travis-ci.org/AineKiraboMbabazi/challenge2Day5)

[![Coverage Status](https://coveralls.io/repos/github/AineKiraboMbabazi/challenge2Day5/badge.svg?branch=master)](https://coveralls.io/github/AineKiraboMbabazi/challenge2Day5?branch=master)

#Bank account#
Simulate a bank account supporting opening/closing, withdrawals, and deposits of money.
Ignore the possibility of concurrent transactions! A bank account can be accessed in multiple ways. Clients can make deposits and withdrawals using the internet, mobile phones, etc. Shops can charge against the account.
It should be possible to close an account; operations against a closed account must fail.
In ​ account.py there is a skeleton of the bankAccount class with unimplemented methods and in ​ tests.py there are tests for the methods in the ​ bankAccount ​ class.
The challenge is to implement the methods

# Installation and settup
## Clone the repository ##
```

$ git clone https://github.com/AineKiraboMbabazi/challenge2Day5.git
$ cd challenge2Day5
```
## Installing virtualenv ##

If you do not have virtualenv installed. Use the command below to install it
```
pip install virtualenv
```
Create a virtual environment using virtualenv

For mac os, linux and windows users
```
$ virtualenv venv
```
Install the project dependancies
```
pip install -r requirements.txt
```
## Activating the virtual environment and setting environment variables ##
For windows users, you can activate the virtual environment by following the steps below
    
If you are using windows command prompt
```
cd venv/scripts && activate && cd ../..
```
if you are using git bash
```
source venv/scripts/activate
```
if you are using linux
```
source venv/bin/activate
```