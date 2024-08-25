import argparse

def add_fuzz(input_file, output_file):
  """
  Reads lines from input_file, adds "/FUZZ" to each line, and writes the results to output_file.
  Args:
      input_file: Path to the file containing subdomains.
      output_file: Path to the file where the modified subdomains will be written.
  """
  with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
    for line in in_file:
      modified_line = line.strip() + "/FUZZ\n"  # Add "/FUZZ" and newline
      out_file.write(modified_line)

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Add /FUZZ to subdomains in a file.")
  parser.add_argument("-i", "--input", required=True, help="Path to the input file containing subdomains.")
  parser.add_argument("-o", "--output", required=True, help="Path to the output file where modified subdomains will be written.")
  args = parser.parse_args()

  add_fuzz(args.input, args.output)
  print(f"Successfully added /FUZZ to lines in {args.input} and wrote the results to {args.output}.")