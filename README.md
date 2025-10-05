# Markov Text Generator

This project contains a simple Python program that generates random text using a Markov chain, based on an example input file.

## Usage

1. Place your example text in a file (e.g., `example.txt`).
2. Run the program:

   ```
   python markov.py example.txt [length]
   ```

   - `example.txt`: Path to your input text file.
   - `[length]`: (Optional) Number of words to generate (default: 50).

## Files
- `markov.py`: Main Python script.
- `example.txt`: Example input file.

## Example
```
python markov.py example.txt 30
```

This will print 30 words of randomly generated text based on the input file.