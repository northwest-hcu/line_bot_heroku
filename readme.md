# How to set up line bot with heroku

### When execute `～`, I want you to type `～` and Enter on Console like command prompt, Terminal, and other.

## 1. Set up LINE Messaging API

### 1. [Create LINE Developper Account.](https://developers.line.biz/ja/services/line-login/)
### 2. Create new Group and new Channel.
### 3. In Messaging API, set up as below.
* [x] Use webhook
* [x] Webhook redelivery
* Allow bot to join group chats >> Disabled
  * This meaning is this bot can't join group chat room.
* Auto-reply messages >> Disabled
  * This meaning is all responses have Default message like `Thank you message`.
* Greeting messages >> Disabled
  * This meaning is when this bot add your acount freiends, bot speak Default message.
### 4. Get Channel access token from Messaging API and Channel secret from Basic settings.


## 2. Set up heroku

### 1. [Sign up heroku](https://id.heroku.com/login)
### 2. [Download heroku CLI](https://devcenter.heroku.com/ja/articles/heroku-cli)
* If your PC's OS is Windows, you can download [here](https://cli-assets.heroku.com/heroku-x64.exe).
### 3. [Download Git](https://www.atlassian.com/ja/git/tutorials/install-git)
* If your PC's OS is Windows, you can execute `winget install Git.Git` and get Git.
* If your PC's OS is Linux, you can execute `sudo apt-get update` and `sudo apt-get install git`. You can get Git.
* If your PC's OS is Mac, you can execute `brew install git` on homebrew and get Git.
### 4. Execute `heroku login` to login heroku, and sign in your account on browser. Maybe after execute command, Pop up Web page to sign in heroku.
* If your heroku account is set 2-step verification, you can't login with -i option. Be careful.

## 3. Set up Work directory

### 1. On Console, move to your directory you want to work by `cd` command.
### 2. Execute `git init` to initialize work derectory.
### 3. Execute `heroku create <your app name>`. <your app name> is like `example-app`.
### 4. Execute `heroku git:remote -a <your app name>`.
### 5. Execute `heroku config:set CHANNEL_ACCESS_TOKEN="<your line bot channel access token>"` to set channel access token as enviroment argument. (Not need <>, but need "")
### 6. Execute `heroku config:set CHANNEL_ACCESS_TOKEN="<your line bot channel secret>"` to set channel secret as enviroment argument. (Not need <>, but need "")

## 4. Copied files from this repository.

### 1. Execute `curl https://raw.githubusercontent.com/northwest-hcu/line_bot_heroku/main/Procfile > Procfile` to copy `Procfile`.
### 2. Execute `curl https://raw.githubusercontent.com/northwest-hcu/line_bot_heroku/main/main.py > main.py` to copy `main.py`.
### 3. Execute `curl https://raw.githubusercontent.com/northwest-hcu/line_bot_heroku/main/requirements.txt` to copy `requirements.txt`.
### 4. Execute `curl https://raw.githubusercontent.com/northwest-hcu/line_bot_heroku/main/runtime.txt` to copy `runtime.txt`.
### 5. Execute `git add .`
### 6. Execute `git commit -am "copied from northwest-hcu"`
### 7. Execute `git push heroku master`
### 8. Execute `heroku ps:scale web=1` to set up

## 5. Setup callback URL.
### 1. Back to your LINE developper account page. and go Messaging API Tab.
### 2. In Webhook settings, Edit Webhook URL to `https://<your app name>.herokuapp.com/callback`. and Update.
### 3. This process was sucesss, set up is end. But if `Verify` has error, you have some bugs. Please execute `heroku logs --tail` to check problems. 

## 6. Check Access.
### 1. Execute `heroku open`, if you can show `check1`, maybe bot is working correctly.
### 2. Try add bot from QRcode and send message. You may get message(`テキストを受け取りました.`). 


