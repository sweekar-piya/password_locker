# base shell
SHELL := /bin/bash

# python version
PYTHON := ${shell which python3}

# venv 
VENV_NAME := ./.venv
VENV_BIN_PATH := $(VENV_NAME)/bin
VENV_ACTIVATE := $(VENV_BIN_PATH)/activate
VENV_PYTHON := $(VENV_BIN_PATH)/python

venv:
	(\
	${PYTHON} -m venv ${VENV_NAME} ;\
	pip install --upgrade pip ;\
	pip -V ;\
	)

install : venv
	. $(VENV_ACTIVATE) && (\
		pip install --upgrade setuptools ;\
		pip install -r ./requirements.txt \
	)

clean:
	rm -rf .venv;

.PHONY: venv install clean