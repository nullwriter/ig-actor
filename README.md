# IG-Actor Bot

Simple instagram bot written in python for automating tasks. Access to Instagram's API is based on https://github.com/LevPasha/Instagram-API-python.git project.

NOTE: To successfully parse for a long time you should verify your phone number in your Instagram account. 
The new fake Instagram account with an unverified phone number after ~ 1-24 hours could not do any requests. All requests will be redirected to the page instagram.com/challenge

### Installation Instructions

1. Fork/Clone/Download this repo

    `git clone https://github.com/nullwriter/ig-actor.git`

2. Navigate to the directory

    `cd ig-actor`

3. Install the dependencies

    `pip install -r requirements.txt`

4. Modify `bot/config/account.dist.txt` into `account.txt` and add your own username and password

5. Navigate to the directory /bot/

    `cd bot`

6. Run the script

    `python bot.py`
    
7. Follow available options in terminal


### Current IG-Actor Bot can:

1) Like;

2) Comment (WIP);

3) Get Comments;

### TODO:

1) Follow;

2) Get Hashtags;

3) Get Users;

4) Like Users images (marketing);

5) Comment Users images;

6) ????
