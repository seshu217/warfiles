import subprocess
subprocess.call("docker run --name mydb -e MYSQL_ROOT_PASSWORD=seshu -d mysql:5",shell=True)
subprocess.call("docker run --name mywordpress -d -p 8888:80 --link mydb:mysql wordpress",shell=True)
