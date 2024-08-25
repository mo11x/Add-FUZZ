# addFuzz

This Python script is designed to add the string "/FUZZ" to the end of each line in a text file. This is often useful for generating fuzzing inputs for testing applications or systems.

## Usage:

```bash
python3 addFuzz.py -i <input_file> -o <output_file>
```

## Arguments:

- `-i` or `--input`: Specifies the path to the input text file containing the lines to be modified.
- `-o` or `--output`: Specifies the path to the output text file where the modified lines will be written.


## Example:

#### Input file (subdomains.txt):
```https
https://cl.info.example.12.com
http://click.e.example.com.com
http://click.info.example.oceania.com
http://click.info.example.com.com
http://click.info.example.fet.com
http://cl.info.example.17.com
http://click.info.example.singed.com
```


#### Command:

```bash
python3 addFuzz.py -i subdomains.txt -o fuzzed_subdomains.txt
```


#### Output file (fuzzed_subdomains.txt):

```https
https://cl.info.example.12.com/FUZZ
http://click.e.example.com.com/FUZZ
http://click.info.example.oceania.com/FUZZ
http://click.info.example.com.com/FUZZ
http://click.info.example.fet.com/FUZZ
http://cl.info.example.17.com/FUZZ
http://click.info.example.singed.com/FUZZ
```



