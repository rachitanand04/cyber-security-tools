import socket 
import termcolor 

def scan(target,ports): 
	print(termcolor.colored(('\n' + ' Starting scan for ' + str(target)),'green'))
	for port in range (1,ports):
		scan_port(target,port)


def scan_port(ipaddress, port): 
	try: 
		sock = socket.socket() 
		sock.connect((ipaddress, port))
		print("[+]Port Opened "+str(port))
		sock.close()
	except:
		pass

targets = input("Enter targets to scan(Split them by ',': ")
ports =int(input("Enter the number of ports to scan: "))

if ',' in targets: 
	print(termcolor.colored(("[*] Scanning multiple targets"), 'cyan'))
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '),ports)
else:
	scan(targets,ports)