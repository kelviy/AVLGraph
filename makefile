JC = javac
JAVA = java
# flags for java command
JFLAGS =  -cp "bin/"
# flags for javac command, .class files outputted to bin/classes
JCFLAGS = -d "bin/"
# .java files of the project
SOURCES = $(wildcard src/*.java)

# python virtual environment
VENV = .env
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

all: run

run: build_java $(VENV)/bin/activate
	$(JAVA) $(JFLAGS) Experiment
	$(PYTHON) src/plotting.py a

build_java: 
	$(JC) $(JCFLAGS) $(SOURCES)

$(VENV)/bin/activate: requirements.txt
	virtualenv $(VENV)
	$(PIP) install -r requirements.txt

clean:
	rm -rf bin
	rm -rf src/__pycache__
	rm -rf $(VENV)

javadoc:
	javadoc -d doc $(SOURCES)

plot_ani: $(VENV)/bin/activate
	$(PYTHON) src/plotting.py a

plot_save: $(VENV)/bin/activate
	$(PYTHON) src/plotting.py s

plot: $(VENV)/bin/activate
	$(PYTHON) src/plotting.py