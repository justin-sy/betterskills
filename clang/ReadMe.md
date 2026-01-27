# C Language

## C and vs code

## C and gcc

Steps:
1. Compile the C files into object files
2. Link the object files into a executable file
3. Run the executable file

### Compile

We have a sample project with a main.c that will call a function declared in a header file "util.h" and implemented in a C file "util.c".
```
gcc -c *.c
```
This is the command to compile all of the local .c files into object files

### Linking

```
gcc *.o -o main
```

This is the command to link all of the local object files into a executable file called "main". You can customize the name of the executable file. You can run the executable file.

## c and make 