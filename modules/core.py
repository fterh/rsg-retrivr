from modules.mercury import mercury

def core(submission, replied, settings, mention=None, summoned=False):

    print("Running core()")

    a = mercury(submission.url, settings.mercury_api_key)

    if a.title is not "" and a.body is not "":
        # link to article
        post_footer = "> [Source](" + submission.url + ")\n\n---\n"
        print("post_footer created")

        # footer meta information
        print("Opening footer_meta.md")
        with open("footer_meta.md", "r") as f:
            post_footer += f.read()
            print("footer_meta.md loaded")

        # article author information
        post_author = ""
        if a.author is not None:
            post_author = "> #####By " + a.author + "\n\n"
            print("post_author crated")

        post = "> #" + a.title + "\n\n" + post_author + a.body + post_footer
        print("post created")

        # post my comment subject to character limits
        if (len(post) <= 9900):
            if summoned is False:
                submission.reply(post)

            elif summoned is True:
                mention.reply(post)

            posted = True
            print("Replied (success) to " + submission.id)

        else:
            print("Skipped (too long) to " + submission.id)
            posted = False

        replied.append(submission.id)
        print("Appended submission.id to replied")

        with open("replied.txt", "w") as f:
            for id in replied:
                f.write(id + "\n")
            print("Written replied to replied.txt")

        if summoned is True and posted is False:
            return False
