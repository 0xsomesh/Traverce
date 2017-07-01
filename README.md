# Traverce

Tool which recursively traverses a directory and finds all the files with names matching the given wiildcard.

## Getting Started
### Install

```bash
sudo pip install traverce
```

### Use
```bash
traverce <path of directory> '<wildcard pattern>'
```
for example
```traverce my_folder '[a-z]*.py$'``` will find all the files in ```my_folder``` with ```.py``` extension and output their exact path with the sizes in Bytes on command line or in a file(Optional) 

```bash
+----------------+----------------------------------------------------------------------------------+----------------+
| Matched String |                                       File                                       | Size(In Bytes) |
+----------------+----------------------------------------------------------------------------------+----------------+
|       py       |                       /my_folder/.../manage.py                                   |      807       |
|       py       |                      /my_folder/.../tokenizer.py                                 |      836       |
|       py       |                      /my_folder/.../apps.py                                      |       94       |
|       py       |                                 ...                                              |       ...      |
```
### Options
You can output to a file via ```-o``` optional argument. For example ```-o output.txt``` will print the result in the output.txt

## Aim
Aim is to make a more robust tool with a number of functionalities such as extracting patterns from file, replacing patterns and many more.
Any suggestions/contributions are appreciated.

## Author

* **Somesh Chaturvedi**

## License

This project is licensed under the [MIT](LICENSE.md).
