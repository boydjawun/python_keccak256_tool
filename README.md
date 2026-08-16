# Keccak256 Hash Tool

<img src="https://github.com/boydjawun/python_keccak256_tool/blob/main/assets/Screenshot%202026-08-09%20110441.png" width="400" height="300">

A simple Python CLI that converts any text into a **Keccak-256** hash (the same hash function used by Ethereum).

---

## Features

- Hashes any string with Keccak-256
- Terminal banner via `pyfiglet`
- Lightweight and easy to run

---

## Requirements

```
pip install pycryptodome pyfiglet

## Files
- `keccak.py` — main script

## License
This project is free to use and modify.
```
## Usage
```python keccak.py <text> ```
## Example Input
```
Enter a word to hash with Keccak256: hello
keccak256 hash: 1c8aff950685c2ed4bc3174f3472287b56d9517b9c948127319a09a7a36deac8
```
## Project Structure
```
python_keccak256_tool/
├── keccak.py          # Main script
├── assets/
│   └── Screenshot ...
└── README.md
```
## Tech stack

| Layer | Technology |
|-------|------------|
| **Language** | Python 3 |
| **Hashing** | [pycryptodome](https://pypi.org/project/pycryptodome/) (`Crypto.Hash.keccak`) |
| **CLI banner** | [pyfiglet](https://pypi.org/project/pyfiglet/) |
| **Algorithm** | Keccak-256 (Ethereum-compatible) |
