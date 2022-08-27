# Experiments on Sentence Boundary Detection in User-Generated Web Content

For more information about the implemented methods in this repository, you can read this [paper](https://roquelopez.com/resource/publications/CICLing2015_Lopez.pdf).


## Installation
We used Python 2.7.12 in this project. After you clone the repository or download the source code, you should install the prerequisite Python packages listed in the file `requirements.txt`.

With `pip`, this is done with:

    $ pip install -r requirements.txt


## Execution
The general way to run this script is the following:
```
 $ cd src/
 $ python main.py option
```
Where `option` could be:
- "proposal", to use the proposal of the paper.
- "punkt", to use Punkt.
- "mxterminator", to use MxTerminator.


## Example
```
 $ python main.py proposal
```

## Outputs
All the generated texts are located in the folder `resource/output_data/`. 
