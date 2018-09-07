import os
import paramiko

# Для подключения к удаленному серверу по протоколу SSH прешил взять paramiko
# login и password получаем при помощи абстрактной функции def auth_data(ip_address)
local_file_path = "C:\\Users\\1\\Documents\\"

def download_log_file(ip, log_name):
	login, password = auth_data(ip)
	ssh = paramiko.SSHClient() 
	ssh.load_system_host_keys()
	ssh.connect(ip, username=login, password=password)
	sftp_client = ssh.open_sftp()
	remote_filename = "/Users/1/Documents/" + log_name + ".log"
	localpath = local_file_path + log_name + ".log"
	# для того, чтобы поиск и вывод строк происходил быстро, мы сначала скачиваем файл с логами на локальную машину
	sftp_client.get(remote_filename, localpath)
	ssh.close()

def get_log_lines_from_id(ip, log_name, search_id):
	download_log_file(ip, log_name)
	localpath = local_file_path + log_name + ".log"
	with open(localpath, "r") as f:
		searchlines = f.readlines()
	for i, line in enumerate(searchlines):
		if str(search_id) in line:
			for l in searchlines[i-100:i+100]: print(l)

if __name__ == '__main__':
	get_log_lines_from_id("192.168.1.47", "log_file_1", 1)


