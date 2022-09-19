import arguparse
import termcolor

banner = """
	  /$$$$$$                               /$$       /$$$$$$$  /$$$$$$$ 
	 /$$__  $$                             | $$      | $$__  $$| $$__  $$
	| $$  \__/  /$$$$$$  /$$$$$$   /$$$$$$$| $$   /$$| $$  \ $$| $$  \ $$
	| $$       /$$__  $$|____  $$ /$$_____/| $$  /$$/| $$$$$$$/| $$$$$$$/
	| $$      | $$  \__/ /$$$$$$$| $$      | $$$$$$/ | $$____/ | $$____/ 
	| $$    $$| $$      /$$__  $$| $$      | $$_  $$ | $$      | $$      
	|  $$$$$$/| $$     |  $$$$$$$|  $$$$$$$| $$ \  $$| $$      | $$      
 	\______/ |__/      \_______/ \_______/|__/  \__/|__/      |__/      
                                                                     
   	v1.1 - DrD00L1ttl3
                                                                  
"""
print(banner)

parser = arguparse.ArgumentParser(description='htb')
parser.add_argument('--binary', help='Location of CPP Binary')
args = parser.parse_args()

print(termcolor.colored(f'	[+] Opening File [ {args.binary} ]...', 'cyan'))
with open(args.binary, 'r', errors='ignore') as file: content = file.read()
print(termcolor.colored('	[+] Read Successful', 'cyan'))

print(termcolor.colored('	[+] Searching bytes...', 'cyan'))
password = content.split("Please enter your master password: ")[1].split("Access")[0]
print(termcolor.colored(f'	[+] Password located: S@mpl3', 'yellow'))
