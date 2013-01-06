#New Resume
01/06/2013

##[github repo](https://github.com/Stonelinks/resume)

Over the holidays I finally got around to implementing what I wish existed back when I was looking for a job: a quick, easy and flexible way to write and publish a resume in many formats. When looking for a job, the more people who see your resume, the better your chances of getting that interview or call back from a potential employer. This means that the more formats and places that your resume is viewable in, the better. I tried to follow this strategy, however I got tired making the same change on multiple versions of my resume.

Like any programmer that has to do anything more than once, I wanted to automate this tediousness. More specifically, I wanted these features:

- Separate resume content from resume formatting
- Stored content in an intuitive and easy to manipulate format
- Write once, publish and deploy resume everywhere

In order to separate content from formatting, I decided the best thing would be to store the content in a JSON file and then use a python script to print out different views of the content. I called this program the "generator" since it essentially generated resume's from a given JSON file. The generator uses different "writers" to print it back out in different formats. Here is a breakdown of the different formats supported using a combination of the generator and a Makefile:

- text
- html
- pdf (using [wkhtmltopdf](http://code.google.com/p/wkhtmltopdf/))
- markdown
- stonelinks markdown (which is what is used to generate the html for my resume on this website)

Anyhow it is finished and it works great for my purposes. The code is available [here](https://github.com/Stonelinks/resume) on github. If someone else wants to use it, they can modify the JSON with their resume content and use the generator to re-generate a resume just for them.
