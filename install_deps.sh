#!/bin/bash
pip install -r requirements.txt
pyinstaller --hiddenimport "PIL._tkinter_finder" --add-data "imagens:imagens" main.py
