# Airbnb Clone

A clone of the popular vacation rental website, [Airbnb](https://www.airbnb.com), built with Python. Currently in beta, this project aims to clone the website of airbnb as a project of ALX School.

## Features

- Command line interface for testing and managing objects
- Classes representing objects, such as Place
- JSON storage for storing object instances
- Additional features will be added in the future.

## Requirements and Dependencies

- Python 3.x

## Installation and Set-up

1. Clone this repository to your local machine:
```bash
$ git clone https://github.com/arfs6/AirBnB_clone.git
```
2. Change into the project directory:
```bash
$ cd AirBnB_clone
```

## Usage

This project can be run in the console using `console.py` located in the root directory. To start the interpreter, run the following command in your terminal:
```bash
$ python console.py
```

The following commands are available in the interpreter:
- `help`: Displays a list of all available commands
- `quit`: Exits the interpreter
- `all [class]`: Views all currently stored objects of the specified class. If no class is specified, all objects will be displayed.
- `create class`: Creates an instance of the given class.
- `destroy class id`: Destroys an instance of class `class` with the id `id`.
- `show class id`: Shows the instance of `class` with id `id`.
- `update class id attr value`: Sets the attribute `attr` of the instance of the class `class` with id `id` to the value `value`.
- `class.command(options)`: Run a command on an instance of the specified class. `options` should be a valid Python basic object.

## Tests

Tests for the project can be found in the `tests` directory.

## License

This project is licensed under the GNU Affero General Public License.

## Authors

- Abdulqadir Ahmad arfs6.mail@gmail.com
- Mubarak Yahaya mubarakg4u@gmail.com

