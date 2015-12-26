#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import render_template

from . import main_blueprint


@main_blueprint.route('/')
def index():

    test_code = """#include <iostream>
#define IABS(x) ((x) < 0 ? -(x) : (x))

int main(int argc, char *argv[]) {

  /* An annoying "Hello World" example */
  for (auto i = 0; i < 0xFFFF; i++)
    cout << "Hello, World!" << endl;

  char c = '\n';
  unordered_map <string, vector<string> > m;
  m["key"] = "\\\\"; // this is an error

  return -2e3 + 12l;
}"""

    return render_template('main/index.html',
                           testing=range(0, 8),
                           testcode=test_code
                           )
