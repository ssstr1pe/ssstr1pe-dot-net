from flask import Flask, render_template, url_for

app = Flask(__name__)

# what endpoints?
# Music
# Programming
# Projects
# Blog
# Contact / socials
# ssstr1peOS
# Mailing list
# Sampling moodboard / easter egg hunt thing

# do like an enter page with the str1pe face and just an enter button
# maybe str1pe face rotating that'd be cool
# enter takes you to /home/

# Start with home page design

def render(template, code, **kwargs):
    return (
        render_template(
            template,
            base_url=url_for("route"),
            # static_url=url_for("static", filename=""),
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

@app.route('/programming')
def programming():
    return render("programming.html", 200)

@app.route('/socials')
def socials():
    return render("home.html", 200)

@app.route('/blog')
def blog():
    return render("home.html", 200)

@app.route('/contact')
def contact():
    return render("home.html", 200)

@app.route('/ssstr1peOS')
def ssstr1peOS():
    return render("home.html", 200)

@app.route('/mailing_list')
def mailing_list():
    return render("home.html", 200)
