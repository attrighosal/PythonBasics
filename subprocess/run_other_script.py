import subprocess

cfile = "program.c"
javafile = "Program.java"
# cppfile = "program.cpp"
subprocess.run(f"gcc {cfile} -o out; ./out", shell=True)
subprocess.run(f"javac {javafile}; java Program", shell=True)

## Pass data to a script in runtime
# subprocess.run(f"g++ {cppfile} -o out2; ./out2", shell=True, input="4 5\n", encoding="ascii")

## timeout
# subprocess.run(f"javac {javafile}; java Program", shell=True, timeout=0.000000003)