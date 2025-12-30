# TODO Comment Age Checker

A "technical debt" scanner that finds `TODO` comments in your code and checks their age using `git blame`. It helps you identify forgotten tasks that were supposed to be "temporary."

<!-- Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742 -->

## Features

*   **Git Integration**: accurate age detection using `git blame`.
*   **Thresholds**: Configurable age limit (default 30 days).
*   **Scan Mode**: Can run without git to simply list all TODOs.

## Usage

```bash
python run_checker.py [path] [options]
```

### Options

*   `--days`, `-d`: Warn if TODO is older than N days.
*   `--no-git`: Skip age check, just list identifiers.

### Examples

**1. Find Old Debt**
```bash
python run_checker.py src/ -d 60
# Output: [src/main.py:42] TODO: Refactor this mess (120 days old)
```

**2. List All**
```bash
python run_checker.py --no-git
```

## Requirements

*   Python 3.x
*   Git (command line tool)

## Contributing

Developed for Anunzio International by Anzul Aqeel.
Contact: +971545822608 or +971585515742

## License

MIT License. See [LICENSE](LICENSE) for details.


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel-anunzio/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.
