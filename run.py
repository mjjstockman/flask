import os
import json
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    # use with block to open file, readonly and call it json_data
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    # return the data as value for company key
    return render_template("about.html", page_title="About", company=data)


# pass member_name as an arg for when user goes to /about/<member_name>
# could use Jinja built in filters lower() and replace() instead of adding url
# as a property of the member obj
@app.route("/about/<member_name>")
def about_member(member_name):
    # empty member var to hold member data
    member = {}
    # use with block to open file, readonly and call it json_data
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        # loop through data obj's and check if its url is same as member_name
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    # return the rendrered mebmer.html template and pass the member obj as a value for the member key
    # the 1st member is the var name passed through html, 2nd is the member obj created above
    return render_template("member.html", member=member)


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)