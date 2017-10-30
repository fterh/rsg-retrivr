# Changelog
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

*More coming...*
