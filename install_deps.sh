#!/bin/bash
pip install -r requirements.txt
pyinstaller --onefile --add-data "imagens:imagens" main.py