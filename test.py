# %%

import os

# %%
print('Hello world!')
print('What is your name?')
myName = input()
print('It is good to meet you, ' +myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')

# %%

# %%

def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0
    print(ham, eggs)

spam()
# %%
def spam():
    eggs = 200
    print(eggs)
eggs = 42
spam()
print(eggs)

# %%
def spam():
    eggs = 'spam local'
    print(eggs) # prints 'spam local'

def bacon():
    eggs = 'bacon local'
    print(eggs) # prints 'bacon local
    spam()
    print(eggs) # prints 'bacon local'

eggs = 'global'
bacon()
print(eggs) # prints 'global


# %%
def spam ():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)

# %%
def spam():
    global eggs
    eggs = 'spam' # this is the global

def bacon():
    eggs = 'bacon' # this is a local

def ham():
    print(eggs) # this is the global

eggs = 42 # this is the global
spam()
print(eggs)

# %%
def spam():
    print(eggs) # ERROR
    eggs = 'spam local'

eggs = 'global'
spam()

# %%
