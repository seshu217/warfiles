import subprocess
i=1
while i<=3:
    subprocess.call("docker run --name t%d -d -P tomcat"%i,shell=True)
    i=i+1
