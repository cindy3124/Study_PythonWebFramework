#!/usr/bin/python
# -*- coding: utf-8 -*-

urls = (
    '/database', 'database',
    '/index', 'index',
    '/error', 'error',
    '/formpage', 'formpage',
    '/formdeal', 'formdeal',
    '/(test1|test2)', 'test',
    '/(.*)', 'default'
)
