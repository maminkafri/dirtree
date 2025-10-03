# Dirtree

Dirtree is a small command-line tool that displays directory contents in a tree-like structure with colors for directories.

```

example/
├── file1.txt
├── file2.txt
└── subdir
    └── file3.txt

```
---

## 🚀 Installation

The recommended way to install Dirtree is with [pipx](https://pypa.github.io/pipx/).  
This keeps the tool isolated in its own environment while still being available globally.

### Using pipx (recommended)

```bash
pipx install dirtree
````

### Using pip (not recommended system-wide)

If you don’t use pipx, you can install it with pip inside a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate   # on Linux/macOS
.venv\Scripts\activate      # on Windows (PowerShell)

pip install dirtree
```

---

## 🖥️ Usage

After installation, run:

```bash
dirtree [directory]
```

### Examples

Show current directory (default):

```bash
dirtree
```

Show a specific directory:

```bash
dirtree ~/Documents
```
---

## 📦 Development / Local Install

If you’re working on the source code, install it in editable mode:

```bash
pipx install --editable .
```

Uninstall:

```bash
pipx uninstall dirtree
```

## 🛠️ Requirements

* Python 3.7 or higher
* Linux, macOS, or Windows
