# Java concepts

## Starting the jshell

If a project is open, close it. Then click _Exit_ to go to the main menu.

From the main menu, click the _Terminal_ button. This should change the screen to look like this:

![main terminal window](images/main-terminal-window.jpg)

## The Android terminal window

The terminal window is called a _shell_ window. It allows you to perform command-line operations in the underlying Linux operating system. One such command is `ls`, which stands for "list files." (Linux has many commands with very short abbreviations like this.) Try that command out by typing `ls` followed by Enter like this:

```
- $ ls
android-sdk  maven
- $
```

Your result should look something like this, but may not match exactly. In this case there re two items in the current directory, `android-sdk` and `maven`.

We will cover other useful shell commands later. But for now we want to run a special command that starts a _Java shell_ called `jshell` where we can try out Java features. Start `jshell` by typing `jshell` followed by Enter.

```
- $ jshell
|  Welcome to JShell -- Version 21.0.7
|  For an introduction type: /help intro

jshell>
```

## Variables and objects

## Exiting the shell and terminal

Stop `jshell` by typing the command `/exit`. Then, at the shell `$` prompt type `exit` (without the slash this time). (Or you can enter Ctrl-D, if you keyboard allows it. Ctrl-D in Linux and Android means "end of file," and tells the shell you are finished inputing commands.) This will return you to the _Code on the Go_ main menu.

## Further reading

Read chapters 1 and 2 in _Think Java_.

## Things to try

TBD
