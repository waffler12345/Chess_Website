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

##################################  

#  Phase 3

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


#######################################








# (Phase 4) Now, time to refactor the code so it is more neat, efficient, and reusable: 


'''
def main():

	template_opened=template()

	for page in pages:
		filename= page['filename']
		filename=open(filename).read()
		filename= template_opened.replace("{{Content}}", filename)
		output= page['output']
		open(output, "w+").write(filename)


#templates-bottom and top of each page
def template():
	template_opened=open("templates/base.html").read()
	return template_opened

'''


def main():

	template_opened=template()
	page_dict=pages()

	for page in page_dict:
		filename= page['filename']
		filename=open(filename).read()
		title_name=page['title']
		filename= template_opened.replace("{{title}}", title_name).replace("{{Content}}", filename)
		output= page['output']
		open(output, "w+").write(filename)
	
	for page in page_dict:
		filename= page['title']




#templates-bottom and top of each page
def template():
	template_opened=open("templates/base.html").read()
	return template_opened

def pages ():

	pages=[
		{
			"filename": "content/index.html",
			"output": "docs/index.html",
			"title": "Home",
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


main()














