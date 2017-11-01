ArghEx: Extensions for Argh, the "Natural CLI"
=========

This module contains some extensions to the Python CLI package
[`argh`][1]. Currently the only extension provided is a command-line parser
which collects unknown arguments in a list.


### Installation

Just use `arghex.py` in your Python project.

### Parser With Unknown Arguments

`ArghParserWithUnknownArgs` is a class derived from [`ArghParser`][2]
and it collects unknown arguments in a list for further
processing. 

When you instantiate `ArghParserWithUnknownArgs` you give it the name of the
variable holding the list of unknown arguments. See the following code
snippet:

```
def main(my_arg=42, other_args=[]):
    # use my_arg here
    # and pass other_args through

if __name__ == '__main__':
    parser = arghex.ArghParserWithUnknownArgs('other_args')
```

### Licensing

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

[1]: https://github.com/neithere/argh
[2]: http://argh.readthedocs.io/en/latest/reference.html#argh.helpers.ArghParser
