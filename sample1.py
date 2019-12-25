import subprocess
subprocess.call("docker run --name tomcat -d -p 8080:8080 tomcat",shell=True)
