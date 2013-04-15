from xml.dom import minidom
import json

def test_tmlanguage_is_valid():
    f = open('VBScript.tmLanguage')
    minidom.parse(f)
    
def test_sublime_build_is_valid():
    f = open('VBScript.sublime-build')
    json.load(f)
