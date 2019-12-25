import subprocess
subprocess.call("docker run --name dev -p 5050:8080 -d jenkins",shell=True)
subprocess.call("docker run --name qa -p 6060:8080 -d --link dev:jenkins tomcat",shell=True)
subprocess.call("docker run --name prod -p 7070:8080 -d --link dev:jenkins tomcat",shell=True)
