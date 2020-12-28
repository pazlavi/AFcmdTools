

# AppsFlyer Commad-Line Help Tools
Add MD5 shortcuts and AppsFlyer logs filter commands to your mac terminal

*  [Installation](https://github.com/pazlavi/AFcmdTools#installation)
 *  [The Commands ](https://github.com/pazlavi/AFcmdTools#the-commands)
    *  [Install](https://github.com/pazlavi/AFcmdTools#install)
    *   [Android](https://github.com/pazlavi/AFcmdTools#android)
    *   [IOS](https://github.com/pazlavi/AFcmdTools#ios)
    *    [AppsFlyer Logs Filter](https://github.com/pazlavi/AFcmdTools#appsflyer-logs-filter)
 *  [License](https://github.com/pazlavi/AFcmdTools#license)



## Installation

1- clone this repo uning the teminal. 

2- run `cd MD5`   

3- run `./add-cmd {path to rc file}`

4- close and open the terminal. 

5- now you can run the commands on every terminal session. 

* path to rc file (bash: `~/.bash_profile` or `~/.bashrc` Z shell `~/.zshrc`)
* Typing echo `$SHELL` in your Terminal tells you which shell you’re using


## The Commands
#### Install
*  `add-cmd` 
 add the commands to path 

#### Android
*  `md5-android n` 
 run the commands 'shasum -a 256' and 'md5' on the last n .aar files in descending order. if n not provided the command will be executed on all .aar files in the directory in descending order
*  `md5-android-url {url1} {url2} ...` 
 run the commands 'shasum -a 256' and 'md5' on files that will be downloaded from supplied URLs. please provide a direct download URL
#### IOS
*  `md5-ios n` 
 run the command 'md5' on the last n .zip files in descending order. if n not provided the command will be executed on all .zip files in the directory in descending order

* `md5-android-url {url1} {url2} ...` 
run the command 'md5' on files that will be downloaded from supplied URLs. please provide a direct download URL

#### AppsFlyer Logs Filter
* `aflogs {file1} {file2} ...`
 script for filtering logs files and extract only AppsFlyer related logs. Pass files path (or name if the file is in the current directory )as command-line arguments.  After the file is filtered, follow the instructions and select if you want to print the result to the console or save it as a new file.
## License

```

Copyright 2020 Paz Lavi

Licensed under the Apache License, Version 2.0 (the "License");

you may not use this file except in compliance with the License.

You may obtain a copy of the License at

https://github.com/paz-lavi/AFcmdTools/blob/master/LICENSE

Unless required by applicable law or agreed to in writing, software

distributed under the License is distributed on an "AS IS" BASIS,

WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

See the License for the specific language governing permissions and

limitations under the License.

```
