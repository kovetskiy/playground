#!/usr/bin/python

values = [
"""func (walker FileWalker) Walk(
        path string, info os.FileInfo, err error,
) (blah, error) {
        if err != nil {
                return err
        }

        if info.IsDir() {
                return nil
        }
"""
,
"""func (walker FileWalker) Walk(
        path string, info os.FileInfo, err error,
) error {
        if err != nil {
                return err
        }

        if info.IsDir() {
                return nil
        }
"""

,
"""func Walk(
        path string, info os.FileInfo, err error,
) error {
        if err != nil {
                return err
        }

        if info.IsDir() {
                return nil
        }
""",
"""func Walk( path string, info os.FileInfo, err error,) error {
        if err != nil {
                return err
        }

        if info.IsDir() {
                return nil
        }
"""
,
"""func Walk(
    path string, info os.FileInfo, err error,
) (
    error, asdad,
) {
        if err != nil {
                return err
        }

        if info.IsDir() {
                return nil
        }
"""
,
]

import re

print "\n"*20
for value in values:
    print(value)
    matches = re.findall(r'^func\s(\(([\w\d_]+)\s+([*\w\d_]+)\)\s+)?([\w\d_]+)?([\s]+)?\(([^)]+)\)\s+?(\(([^\)]+)\)|(.*))\s+?{$', value, re.MULTILINE)
    #print(matches)
    if matches:
        matches = matches[0]
        instance = matches[1]
        type = matches[2]
        func = matches[3]
        args = matches[5].strip()
        returns = matches[7].strip()

        print "test.py:79 instance: %s" % instance
        print "test.py:79 type: %s" % type
        print "test.py:79 func: %s" % func
        print "test.py:79 args: %s" % args
        print "test.py:85 returns: %s" % returns











