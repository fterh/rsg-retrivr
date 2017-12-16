# Changelog
## v4.0
* The bot can now be summoned at will: `/u/rsg-retrivr summon` (case-sensitive)
* Further modularized the code
## v3.1
* Added site support functionality - the bot only posts where the submission URL is on the list of "approved" URLs (`sites.txt`).
## v3.0
* Completely rewrote the parsing mechanism - the bot now relies on the Mercury web parser. It should now support virtually every news site without having to individually write the rules for each site.
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

I rely on the [Mercury web parser](https://mercury.postlight.com/web-parser/) to break down a webpage into useful chunks of information (e.g. title, content, etc.). I use those information to create and format a post comment and then post it.

# Running this
1. Rename `replied.sample.txt` to `replied.txt`.
2. Create `.env` and `praw.ini`.
* Details coming soon...

# Credits
* [Fabian Terh](https://github.com/fterh) (creator)
* [changhuapeng](https://github.com/changhuapeng) ([contributor](https://github.com/fterh/rsg-retrivr/commit/19c5b9db569d7bd082f3f8577e953b5bec904519))
