"""It turns out that (most) YouTube videos can be embedded in other websites.
For instance, if you visit https://youtu.be/xvFZjo5PgG0 on a laptop or
desktop, click Share, and then click Embed, you'll see HTML (the language in
which web pages are written) like the below, which you could then copy into
your own website's source code, wherein iframe is an HTML “element,” and src
is one of several HTML “attributes” therein, the value of which, between
quotes, is https://www.youtube.com/embed/xvFZjo5PgG0.

<iframe width="560" height="315"
src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player"
frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Because some HTML attributes are optional, you could instead minimally embed
just the below.

<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>

Suppose that you'd like to extract the URLs of YouTube videos that are
embedded in pages (e.g., https://www.youtube.com/embed/xvFZjo5PgG0),
converting them back to shorter, shareable youtu.be URLs (e.g.,
https://youtu.be/xvFZjo5PgG0) where they can be watched on YouTube itself.

This program implements a function called parse() that expects a str of HTML
as input, extracts any YouTube URL that's the value of a src attribute of an
iframe element therein, and returns its shorter, shareable youtu.be
equivalent as a str. The program expects that any such URL will be in one of
the formats below. This program assumes that the value of src will be
surrounded by double quotes. And assumes that the input will contain no more
than one such URL. If the input does not contain any such URL at all, the 
function returns None.

http://youtube.com/embed/xvFZjo5PgG0
https://youtube.com/embed/xvFZjo5PgG0
https://www.youtube.com/embed/xvFZjo5PgG0"""

import re

html_pattern: str = r"^<iframe(?:.| )*src=\"(?P<src_url>[^\"]+)\"(?:.| )*</iframe>$"
youtube_url_pattern: str = r"(?:https?://)?(?:www\.)?youtu\.?be\.com/embed/(?P<video_id>[a-zA-Z0-9]*)"

def main() -> None:
    print(parse(input("HTML: ")))

def parse(html: str) -> str | None:
    if html_match := re.search(html_pattern, html):
        src_url = html_match.group("src_url")
        youtube_url_match = re.fullmatch(youtube_url_pattern, src_url)

        if youtube_url_match:
            video_id = youtube_url_match.group("video_id")
            return f"https://youtu.be/{video_id}"
        else:
            return None
    else:
        return None

if __name__ == "__main__":
    main()