# Changelog
Hi there! Thanks for checking out my project. Unfortunately, this bot is indefinitely retired (ever since Straits Times implemented a hard paywall). I might relaunch it (or a modified version of it) in the future if I have the time.

## v4.0
* The bot can now be summoned at will: `/u/rsg-retrivr summon` (case-sensitive)
* Further modularized the code
## v3.1
* Added site support functionality - the bot only posts where the submission URL is on the list of "approved" URLs (`sites.txt`).
## v3.0
* Completely rewrote the parsing mechanism - the bot now relies on the Mercury Web Parser. It should now support virtually every news site without having to individually write the rules for each site.
* The bot should also retrieve *some* information from sites like Youtube (to the extent that Mercury is able to parse *some* information out of it). But the bot should ignore sites like Imgur (where Mercury is unable to parse any *useful* information).
## v2.0
* Fixed broken mothership content selector (body_selector)
* Bot now supports hyperlinks
* Requests are made with a user-agent header (this should fix 403 forbidden responses encountered during testing)
## v1.2
* Support for todayonline and mothership
## v1.1
* Refined straitstimes content selector
  * Previously, some straitstimes article formats were not compatible. The content selector has been tweaked to fix this.
* Bot will no longer post that the article is too long when the article is too long. It'll just skip posting anything at all.

## v1.0
* Genesis
  * Support for straitstimes, channelnewsasia, and bloomberg

# FAQ
## 1. What are you?

I'm a bot that retrieves news articles (at the moment) and posts them as a top-level comment. **I am designed to never spam.**
If the post is too long to post in a single comment, I'll skip it.

## 2. How do you work?

I rely on the [Mercury Web Parser](https://mercury.postlight.com/web-parser/) API to break down a webpage into useful chunks of information (e.g. title, content, etc.). I use those information to create and format a post comment and then post it.

# Running the bot
1. Install python dependencies by running `pip install -r requirements.txt`.

2. Rename `replied.sample.txt` to `replied.txt`.

3. Rename `.env.sample` to `.env`. The descriptions of each value are as follows:
    * **mercury_api_key**: The API key you get after creating an account at [Mercury Web Parser](https://mercury.postlight.com/web-parser/).
    * **dev_subreddit**: The name (e.g. testsubreddit for /r/testsubreddit) of the subreddit for development/testing environment.
    * **prod_subreddit**: The name (e.g. livesubreddit for /r/livesubreddit) of the subreddit that the live bot will run in.

4. Create a Reddit script app at https://www.reddit.com/prefs/apps/.

5. Rename `praw.sample.ini` to `praw.ini`. The descriptions of each value are as follows:
    * **client_id**: The 14 character string listed just under "personal use script" for the desired [developed application](https://www.reddit.com/prefs/apps/).
    * **client_secret**: The 27 character string listed adjacent to `secret` for the application.
    * **password**: The password for the Reddit account used to register the script application.
    * **username**: The username of the Reddit account used to register the script application.
    * **user_agent**: A unique and descriptive string that helps the Reddit server identify the source of the requests. The recommended format is `<platform>:<app ID>:<version string> (by /u/<Reddit username>)`. For example, `android:com.example.myredditapp:v1.2.3 (by /u/kemitche)`. Read more about user-agent strings on [Reddit’s API wiki page](https://github.com/reddit/reddit/wiki/API).

# Credits
* [Fabian Terh](https://github.com/fterh) (creator)
* [changhuapeng](https://github.com/changhuapeng) ([contributor](https://github.com/fterh/rsg-retrivr/commit/19c5b9db569d7bd082f3f8577e953b5bec904519))
