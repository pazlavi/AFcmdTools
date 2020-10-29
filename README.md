# MD5
add MD5 shortcut command to your mac

# INSTALLATION

1- clone this repo uning teminal. 

2- run "cd MD5"   

3- run "./add-cmd {path to rc file}". 

4- close and open the terminal. 

5- now you can run the commands on every terminal session. 

* path to rc file (bash: ~/.bash_profile or ~/.bashrc Z shell ~/.zshrc)
* Typing echo $SHELL in your Terminal tells you which shell you’re using


# THE COMMANDS 
1- add-cmd : add the commands to path 

2- md5-android n : run the commands 'shasum -a 256' and 'md5' on the last n .aar files in descending order. if n not provided the command will be executed on all .aar files in the directory in descending order

3- md5-ios n : run the command 'md5' on the last n .zip files in descending order. if n not provided the command will be executed on all .zip files in the directory in descending order

4- md5-android-url {url1} {url2} ... : run the commands 'shasum -a 256' and 'md5' on files that will be downloaded from supplied URLs. please provide a direct download URL

5- md5-android-url {url1} {url2} ... : run the command 'md5' on files that will be downloaded from supplied URLs. please provide a direct download URL

