# ad4a-intro-to-programming

An introductory course in Java programming for Android. This repository
is the source for the course, in Markdown format. It can be generated
into a PDF or HTML pages using scripts.

## Setup

### Recommended Setup, Using Hatch

You can install Hatch in a virtual environment, if you want. However,
since Hatch is the only prerequisite, and since it sets up virtual
environments automatically when building, starting shells, or running
scripts, I don't find that it's necessary. That is, Hatch is the only
thing I install in the global environment.

1. Install Hatch: `pip install hatch`

### Alternate Install, without Hatch

1. Create a virtual environment: `pip -m venv venv`
2. Enter the virtual environment: `source venv/bin/activate`\
(Windows: `venv/bin/activate`)
3. Install the package: `pip install -e .`

For subsequence use, just go to the package directory and enter the
virtual environment: `source venv/bin/activate`\
(Windows: `venv/bin/activate`)

## Viewing or converting the course

While editing the content, it is convienient to convert the course to
HTML, then open `index.html` as a file in the browser. After making
changes, re-generate the HTML and refresh the browser window to see
the changes.

### If using Hatch

* Viewing content as HTML: `hatch run course:serve`\
    Then browse to: http://localhost:8000/
* Converting content to a PDF in `site/`: `hatch run course:pdf`\
* Converting content to HTML in `dist/html/`: `hatch run course:html`\
    Then open: `site/index.html`

### If not using Hatch

First, start the virtual environment as indicated above.

* Viewing content as HTML: `mkdocs serve`
* Converting content to a PDF in `dist/`: `python ad4a.util.genpdf:main mkdocs.yml dist/intro-to-programming.pdf``
* Converting content to HTML in `site/`: `mkdocs build`
