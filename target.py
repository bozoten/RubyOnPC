import pyperclip

with open('todo.txt', 'a') as f:
    f.write('See my brother and play Fortnite with him at 6 today\n')

pyperclip.copy('See my brother and play Fortnite with him at 6 today')