## SSH connection part


import paramiko

ip = "192.168.50.105"
port = 22
user = "pi"
password = "Ericss0n"

#创建一个ssh对象
ssh = paramiko.SSHClient()
#自动选择yes
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 建立连接
ssh.connect(ip,port,user,password,timeout = 10)
#输入linux命令
ssh.exec_command('cd ERRR_OBU_Dev_API_PA1')
ssh.exec_command('cd ERRR_OBU_Dev_API')
print("success")
while True:
	#等待输入命令
    temp = str(input("input:"))
    print(temp)
    stdin,stdout,stderr = ssh.exec_command(temp)
    # 输出命令执行结果
    result = stdout.read()
    print(result)
#关闭连接
ssh.close()