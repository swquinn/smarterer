# Smarterer Code Challenge
This project represents a code submission to Smarterer for their interview process.

The decision to use challenge myself by using Python was made for several reasons, chiefly among them was to gain more exposure to python development in general.

## Overview
Having no previous "practical" experience writing Python applications, I have taken inspiration from other projects in how I structure my code base. That is, represent the project (as it exists in source control) as a project that has different components to it, including: the application, documentation, and any tools to support the project. This results in a structure something like the following:

```
<root>
  ∟ /app
  ∟ /docs
  ∟ /tools
```

Following the above, the idea becomes:

* Use `/app` to contain all of the application-specific code and to setup the directory structure underneath that in a way that, would ideally, conform to some standard.
* Use `/docs` for any documentation of the application.
* Use `/tools` for the collection of code and scripts that support an end user launching the application or getting their development environment up and running.

### Why Flask?
The choice of [Flask](http://flask.pocoo.org/) was made after a conversation with Paul Anderson, wherein he likened Smarterer's internal (proprietary) framework to Flask.

## Setting up the Development Environment
TBW

## References

1. http://flask.pocoo.org/
2. http://mattupstate.com/python/2013/06/26/how-i-structure-my-flask-applications.html
3. http://pythonhosted.org/Flask-SQLAlchemy/
4. https://www.python.org/dev/peps/pep-0008/
