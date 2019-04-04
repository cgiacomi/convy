# Convy

Conventional commit messages git pre-commit hook.

Based on Karma's commit message convention.

http://karma-runner.github.io/0.10/dev/git-commit-msg.html

## Limitation

Currently only supports the header with a <subject>.

<body> and <footer> parts of conventional commit messages are not supported.


## Requirements

- Python 2.6


## Installation

Copy the following files to the .git/hook directory in the repository you are going to use the commit-msg hook.

```
commit-msg
convy-commit-msg.py
```

Both files have to be executables.

```
$ chmod +x commit-msg
$ chmod +x convy-commit-msg.py
```


## Naming standard

Currently the naming standard is based on a simple regex.

A sample commit message should look like this

```
<type>(<scope>): <subject>
```

eg.

```
feat(lang): add japanese language
```


## Customize

To customize the message validation to your liking simply modify the existing regular expressions in convy-commit-msg.py

```
MESSAGE_REGEX = '(feat|fix|perf|docs|chore|style|refactor|test)(?:\(([\w$.\-* ]*)\))?: [\w\d ().,:;+]*'
```

To test your regex you can simply do so [here](http://pythex.org/)


## License

Convy is released under the MIT license.
