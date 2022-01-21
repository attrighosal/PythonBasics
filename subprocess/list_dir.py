import subprocess 


## List all the files in cwd
# subprocess.run('ls') 

## List all the files with more specfic details in cwd 
lt = subprocess.run('ls -la', capture_output=True, shell=True, text=True)
print(lt.returncode)
print(lt.stderr)

## Using shell is vulnerable to security leaks hence using list []
## where lst[0] is command and lst[1...n] are arguments 
# subprocess.run(['ls', '-la'])

## Store the output of a subprocess in a python variable 
# list_of_dir = subprocess.run(['ls', '-z'], capture_output=True, text=True)
# print(list_of_dir.stderr) 

## Capture output as text
# list_of_dir = subprocess.run(['ls', '-la'], capture_output=True, text=True)
# print(list_of_dir.stdout) 

