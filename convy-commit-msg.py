#!/usr/bin/python

import sys
import re
import subprocess


MESSAGE_REGEX = '^(feat|fix|perf|docs|chore|style|refactor|test)(?:\(([\w$.\-* ]*)\))?: [\w\d ().,:;+]*$'


def valid_commit_message(message):
  """Function to validate the commit message.

  Args:
    message (str): The message to validate.

  Returns:
    bool: True for valid messages, False otherwise.
  """
  if not re.match(MESSAGE_REGEX, message):
    print 'ERROR: Commit message does not follow conventional commits style.'
    print 'Convention: <type>(<scope>): <subject>'
    print 'Hint: feat(lang): add japanese language'
    return False

  print 'Valid commit message.'
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
