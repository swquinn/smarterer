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

## Installing / Running the Server

### DevOps
Or "_How I Learned to Stop Worrying and Love Vagrant_".

[Vagrant](https://www.vagrantup.com/) is used as the development environment, the benefit to this is that no matter whether you're on a Windows, Mac OSX, or Linux environment, as long as you can run Vagrant you should find yourself in an as-close-to-identical-as-possible development environment as anyone else running this code. It also isolates the code for this exercise, so that you (the end-user or developer) don't have to worry about what version of python you're running.

### Pre-requisites
Before you can bring the server up, you'll need some pre-requisite software:

1. Download and install [Vagrant](https://www.vagrantup.com/downloads.html) for your OS
2. Download and install [VirtualBox](https://www.virtualbox.org/)
3. Download and install [Git](http://www.git-scm.com/) for accessing the code

> **NB:** You could, theoretically, use any other virtual machine software, _Parallels_ or _VMWare_ for instance, but you'll have to hack the `Vagrantfile` if you want to use anything other than VirtualBox and have things work. Further, I can't make any guarantees that anything _will_ actually work on anything other than VirtualBox, as that's what I've tested on.
>
> It's also worth noting that **VirtualBox 5.0** was just released but all of these virtual machines were built against VirtualBox 4.x, so please bear that in mind when choosing which VirtualBox release to install.

### Cloning the Repository
Change directories into a location where you'd like to clone the project and then issue the command:

```
$ git clone https://github.com/swquinn/smarterer.git
```

Once completed you should successfully have cloned the repository into the `/smarterer` directory, local to the location you were in.

### Vagrant Up
Once you have installed all of the pre-requisite software and cloned the repository you can build (and at the same time launch) the server.

1. Change directory into the project directory:
```
$ cd ./smarterer
```
2. Issue the `vagrant up` command:
```
$ vagrant up
```

Once `vagrant up` has finished, the server will have been provisioned and the Python web application started.

### Testing access to the server
Navigate your browser to: http://localhost:5000/, if the server is running you should see instructions detailing the usage of the API.

## API Reference
The API is wholly JSON centric, this means that all requests and responses should (unless I missed something!) be in JSON. Any action that is a `POST`, `PUT`, or `PATCH` should be sending a JSON object as its payload, e.g.

```
{
  'text': 'What is your favorite color?',
  'answer': 'blue',
  'choices': 'yellow,green'
}
```

#### GET `/questions`
Returns a list of all the questions that are tracked by the service. This resource can take optional query parameters in the form of:

**GET** `/questions?[limit=n][&page=n][&sortby=str][&sort=n|str]`

> **Optional Query Params:**
> * `limit` - allows you to limit the number of results. The parameter should be a number, e.g. 50. If both `limit` and `page` are specified `limit` will act as the throttle for the number of items to show per page.
> * `page` - forces pagination of the data results and displays the page number specified. If both `limit` and `page` are specified the number of results per `page` will be restricted to the value specified for `limit`, otherwise a default value of 10 will be used.
> * `sortby` - the questions can be sorted by the field names of a question e.g. _text_, _answer_, or _choices_.
> * `sort` - the direction that the ordering should be displayed in. Accepts either `1` or `-1` for ascending and descending respectively, `sort` will also accept values: _asc_, _ascending_, _desc_, and _descending_.

#### POST `/questions/create`
Creates a new question, with the data passed along to the server.

**POST** `/questions`

```
{
  'text': 'What is your favorite color?',
  'answer': 'blue',
  'choices': 'yellow,green'
}
```

#### DELETE `/question/<question_id>`
Deletes the question whose ID is specified by `<question_id>`. The API expects a positive integer (_1,2,3,..n_) as the `<question_id>` parameter. If no question is found matching the passed ID, a `404` error will be returned.

**DELETE** `/question/1`

#### GET `/question/<question_id>`
Returns the question with the matching `<question_id>`. The API expects a positive integer (_1,2,3,..n_) as the `<question_id>` parameter. If no question is found matching the passed ID, a `404` error will be returned.

**GET** `/question/1`

#### PUT,PATCH `/question/<question_id>`
Updates the question whose ID is specified by `<question_id>`. The API expects a positive integer (_1,2,3,..n_) as the `<question_id>` parameter. If no question is found matching the passed ID, a `404` error will be returned.

The update request may contain some-or-all of the question attributes (i.e. _text_, _answer_, _choices_) only those supplied in the update will be modified. If you supply an unknown key and value, it will be ignored.

**PUT** `/question/1`

or

**PATCH** `/question/1`

```
{
  'answer': 'purple',
  'choices': 'yellow,green,blue'
}
```

## References

1. http://flask.pocoo.org/
2. http://mattupstate.com/python/2013/06/26/how-i-structure-my-flask-applications.html
3. http://pythonhosted.org/Flask-SQLAlchemy/
4. https://www.python.org/dev/peps/pep-0008/
5. https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions
