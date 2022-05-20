#!/usr/bin/python

import re
import subprocess
import sys

MESSAGE_REGEX = '^(feat|fix|perf|docs|chore|style|refactor|test|wip)(?:\(([\w$.\-* ]*)\))?: [\w\d r\n \- <@>().,:;+]*$'

# Based on https://stackoverflow.com/a/45427753/772175
class Colors:
    Green, Red, White = '\033[92m', '\033[91m', '\033[0m'
    Bold, Italics = '\033[1m', '\x1B[3m'
    Reset = '\033[0m'

def valid_commit_message(message):
  """Function to validate the commit message.

  Args:
    message (str): The message to validate.

  Returns:
    bool: True for valid messages, False otherwise.
  """
  if not re.match(MESSAGE_REGEX, message):
    print(Colors.Red + Colors.Bold + 'ERROR: Commit message does not follow conventional commits style.' + Colors.Reset)
    print('Convention: <type>(<scope>): <subject>')
    print('Hint: feat(lang): add japanese language')
    return False

  print(Colors.Green + 'Valid commit message.' + Colors.Reset)
  return True


def main():
  """Main function."""
  message_file = sys.argv[1]
  try:
    txt_file = open(message_file, 'r')
    commit_message = txt_file.read()
  finally:
    txt_file.close()

  if not valid_commit_message(commit_message):
    sys.exit(1)

  sys.exit(0)


if __name__ == "__main__":
  main()
