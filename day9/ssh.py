__author__ = "Alex Li"

import paramiko
# 创建SSH对象
ssh = paramiko.SSHClient()

# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='192.168.0.233', port=22, username='root', password='root')
# 执行命令
stdin, stdout, stderr = ssh.exec_command('ls')
# 获取命令结果
res,err = stdout.read(),stderr.read()
#三元运算符,
result = res if res else err

print(result.decode())#解码
# 关闭连接
ssh.close()

#ssh konwn_host  .ssh 里面有个加密算法,安全的签名认证
