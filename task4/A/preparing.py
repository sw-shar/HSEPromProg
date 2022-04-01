import sys


if __name__ == '__main__':
  output_file = sys.argv[1]
  with open(output_file, 'w') as fp:
    fp.write('#define ADD(x, y) ((x) + (y))\n')
