import os
import sys
import re
import importlib

def load_apis():
    pysearchre = re.compile('.py$', re.IGNORECASE)
    apifiles = filter(pysearchre.search, os.listdir(os.path.join(os.path.dirname(__file__), '../apis')))
    form_module = lambda fp: '.' + os.path.splitext(fp)[0]
    apis = map(form_module, apifiles)
    # import parent module / namespace
    importlib.import_module('apis')
    modules = []
    for api in apis:
             if not api.startswith('.__'):
                 modules.append(importlib.import_module(api, package="apis"))

    return modules