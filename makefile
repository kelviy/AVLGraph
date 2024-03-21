JC = javac
JAVA = java

# flags for java command
JFLAGS =  -cp "bin/"
# flags for javac command, .class files outputted to bin/classes
JCFLAGS = -d "bin/"

# .java files of the project
SOURCES = $(wildcard src/*.java)

all: build run_array

run_array:
	$(JAVA) $(JFLAGS) Main

build:
	$(JC) $(JCFLAGS) $(SOURCES)

clean:
	$(RM) bin/*.class

javadoc:
	javadoc -d doc $(SOURCES)