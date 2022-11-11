'''
def main():

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

#main()
'''
'''
def main():

	for page in pages:
		filename= page['filename']
		filename=open(filename).read()
		filename= top + filename + bottom
		output= page['output']
		open(output, "w+").write(filename)

#templates-bottom and top of each page
top=open("templates/top.html").read()
bottom=open("templates/bottom.html").read()


pages=[
	{
		"filename": "content/index.html",
		"output": "docs/index.html",
		"title": "Chess Events and Instruction in Pittsburgh",
	},
	{
		"filename": "content/events.html",
		"output": "docs/events.html",
		"title": "Events",
	},
	{
		"filename": "content/about.html",
		"output": "docs/about.html",
		"title": "About Me",
	},
]

main()
'''



#STEP 3
'''
def main():

	for page in pages:
		filename= page['filename']
		filename=open(filename).read()
		filename= template.replace("{{Content}}", filename)
		output= page['output']
		open(output, "w+").write(filename)

#templates-bottom and top of each page
template=open("templates/base.html").read()


pages=[
	{
		"filename": "content/index.html",
		"output": "docs/index.html",
		"title": "Chess Events and Instruction in Pittsburgh",
	},
	{
		"filename": "content/events.html",
		"output": "docs/events.html",
		"title": "Events",
	},
	{
		"filename": "content/about.html",
		"output": "docs/about.html",
		"title": "About Me",
	},
]

main()
'''


#STEP 4: Templating 

def main():

	open(output, "w+").write(filename)


def template(base):
	template=open(base).read()
	each_page=pages()
	
	for page in each_page:
		filename= page['filename']
		filename=open(filename).read()
		filename= template.replace("{{Content}}", filename)
		output= page['output']
		return output	



def pages():
	pages=[
		{
			"filename": "content/index.html",
			"output": "docs/index.html",
			"title": "Chess Events and Instruction in Pittsburgh",
		},
		{
			"filename": "content/events.html",
			"output": "docs/events.html",
			"title": "Events",
		},
		{
			"filename": "content/about.html",
			"output": "docs/about.html",
			"title": "About Me",
		},
	]
	return pages

template("templates/base.html")
main()





















