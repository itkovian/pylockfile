#!/usr/bin/env python

V = "0.9.1.1"

import vsc.install.shared_setup as shared_setup

shared_setup.SHARED_TARGET.update({
    'url':'http://code.google.com/p/pylockfile/',
    'download_url':('http://code.google.com/p/pylockfile/downloads/'
                  'detail?name=lockfile-%s.tar.gz' % V),
})

PACKAGE = {
    'name':'lockfile',
    'author':['Skip Montanaro'],
    'author_email':'skip@pobox.com',
    'version':V,
    'description':"Platform-independent file locking module",
    'long_description':open("README").read(),
    'packages':['lockfile'],
    'license':'MIT License',
    'classifiers':[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows :: Windows NT/2000',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.0',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    'provides': ['python-vsc-packages-lockfile = 0.9.1'],
}

if __name__ == '__main__':
    shared_setup.action_target(PACKAGE)
