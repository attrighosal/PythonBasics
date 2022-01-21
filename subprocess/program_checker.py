import subprocess

program = 'gits'

process = subprocess.run(['which', program], capture_output=True, text=True)

if process.returncode == 0: 
    print(f'The program "{program}" is installed')

    print(f'The location of the binary is: {process.stdout}')
else:
    print(f'Sorry the {program} is not installed')

    print(process.stderr)