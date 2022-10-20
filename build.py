print("big up ya self bredda")

#templates-bottom and top of each page
top=open("templates/top.html").read()
bottom=open("templates/bottom.html").read()

#content
index=open("content/index.html").read()
events=open("content/events.html").read()
about=open("content/about.html").read()

#combine into one variable
index_page= top + index + bottom
events_page= top + events + bottom
about_page= top + about + bottom

#write result into a new file in docs directory
open("docs/index.html", "w+").write(index_page)
open("docs/events.html", "w+").write(events_page)
open("docs/about.html", "w+").write(about_page)


