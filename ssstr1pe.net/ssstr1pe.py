from flask import Flask, render_template, url_for, send_file, request

from pathlib import Path

import hashlib
import os

app = Flask(__name__)


APP_PATH = os.path.dirname(os.path.realpath(__file__))

# future endpoints?
# ssstr1peOS
# Mailing list

def render(template, code, **kwargs):
    return (
        render_template(
            template,
            base_url=url_for("route"),
            **kwargs,
        ),
        code,
    )

@app.route('/')
def route():
    return render("entry.html", 200)

@app.route('/home')
def home():
    return render("home.html", 200)

@app.route('/music')
def music():
    return render("music.html", 200)

@app.route('/code')
def code():
    return render("code.html", 200)

@app.route('/socials')
def socials():
    return render("socials.html", 200)

@app.route('/blog')
def blog():
    posts = os.listdir(f"{APP_PATH}/templates/blog_posts")
    posts = [post.replace(".html", "") for post in posts]
    posts.reverse()
    return render("blog.html", 200, posts=posts)

@app.route('/blog_posts/<post>/')
def blog_posts(post):
    return render(f"blog_posts/{post}.html", 200)

@app.route('/contact')
def contact():
    return render("contact.html", 200)

@app.route('/downloads')
def downloads():
    return render("downloads.html", 200)

@app.route('/breakbeats')
def breakbeats():
    breakbeats = os.listdir(f"{APP_PATH}/static/breakbeats/wav/")
    breakbeats = [breakbeat.replace(".wav", "") for breakbeat in breakbeats]
    return render("breakbeats.html", 200, breakbeats=breakbeats)

@app.route('/breakbeat/<breakbeat>/')
def breakbeat(breakbeat):
    try:
        if breakbeat == "all":
            return send_file(f"{APP_PATH}/static/breakbeats/all-breakbeats.zip")
        else:
            return send_file(f"{APP_PATH}/static/breakbeats/wav/{breakbeat}.wav")
    except Exception as e:
        return str(e)

@app.route('/downloads/my_music/')
def my_music():
    music_path = f"{APP_PATH}/static/my_music/"
    releases = os.listdir(music_path)
    music={}
    for release in releases:
        if ".zip" in release:
            continue
        else:
            music[release] = {}
            music[release]["tracks"] = [track for track in os.listdir(f"{music_path}{release}/") if track.endswith(".wav")]
    return render("my_music.html", 200, music=music)

@app.route('/bugle')
def bugle():
    return render("bugle.html", 200)

@app.route("/library")
def library():
    return render("library.html", 200)

@app.route("/library_dl")
def library_dl():
    password = request.args.get('password')
    m = hashlib.sha256()
    m.update(password.encode("utf-8"))
    accepted_pw = Path(f"{APP_PATH}/static/library-pwd").read_text().rstrip()
    if m.hexdigest() == accepted_pw:
        return send_file(f"{APP_PATH}/static/library.tar.gz")
    return render("wrong_password.html", 200)
