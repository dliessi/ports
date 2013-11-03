"""
A setup file to build Frescobaldi.app with py2app.

Initial version by Henning Hraban Ramm.
"""

from setuptools import setup

APPNAME = 'frescobaldi'
APP = ['%%PREFIX%%/bin/{0}'.format(APPNAME)]
NAME = 'Frescobaldi'
VERSION = '%%VERSION%%'

plist = dict(
    CFBundleName                  = NAME,
    CFBundleDisplayName           = NAME,
    CFBundleShortVersionString    = VERSION,
    CFBundleVersion               = VERSION,
    CFBundleExecutable            = NAME,
    CFBundleIdentifier            = 'org.{0}.{0}'.format(APPNAME),
    CFBundleIconFile              = '{0}.icns'.format(APPNAME),
    NSHumanReadableCopyright      = 'Copyright 2008-2012 Wilbert Berendsen.',
    CFBundleDocumentTypes         = [
        {
            'CFBundleTypeExtensions': ['ly', 'lyi', 'ily'],
            'CFBundleTypeName':'LilyPond file',
            'CFBundleTypeRole':'Editor',
            'LSItemContentTypes': ['org.lilypond.lilypond']
        },
        {
            'CFBundleTypeExtensions': ['tex', 'lytex', 'latex'],
            'CFBundleTypeName':'LaTeX file',
            'CFBundleTypeRole':'Editor',
            'LSItemContentTypes': ['org.tug.tex']
        },
        {
            'CFBundleTypeExtensions': ['docbook', 'lyxml'],
            'CFBundleTypeName':'DocBook file',
            'CFBundleTypeRole':'Editor',
            'LSItemContentTypes': ['org.docbook.docbook']
        },
        {
            'CFBundleTypeExtensions': ['html'],
            'CFBundleTypeName':'HTML file',
            'CFBundleTypeRole':'Editor',
            'LSItemContentTypes': ['public.html']
        },
        {
            'CFBundleTypeExtensions': ['xml'],
            'CFBundleTypeName':'XML file',
            'CFBundleTypeRole':'Editor',
            'LSItemContentTypes': ['public.xml']
        },
        {
            'CFBundleTypeExtensions': ['itely', 'tely', 'texi', 'texinfo'],
            'CFBundleTypeName':'Texinfo file',
            'CFBundleTypeRole':'Editor',
            'LSItemContentTypes': ['org.gnu.texinfo']
        },
        {
            'CFBundleTypeExtensions': ['scm'],
            'CFBundleTypeName':'Scheme file',
            'CFBundleTypeRole':'Editor',
            'LSItemContentTypes': ['org.scheme.scheme']
        },
        {
            'CFBundleTypeExtensions': ['*'],
            'CFBundleTypeName':'Text file',
            'CFBundleTypeRole':'Editor',
            'LSItemContentTypes': ['public.text']
        }
    ],
    UTExportedTypeDeclarations    = [
        {
            'UTTypeTagSpecification': { 'public.filename-extension': ['ly', 'lyi', 'ily'] },
            'UTTypeDescription':'LilyPond file',
            'UTTypeIdentifier': ['org.lilypond.lilypond'],
            'UTTypeConformsTo': ['public.text', 'public.plain-text', 'public.source-code']
        },
        {
            'UTTypeTagSpecification': { 'public.filename-extension': ['tex', 'lytex', 'latex'] },
            'UTTypeDescription':'LaTeX file',
            'UTTypeIdentifier': ['org.tug.tex'],
            'UTTypeConformsTo': ['public.text', 'public.plain-text', 'public.source-code']
        },
        {
            'UTTypeTagSpecification': { 'public.filename-extension': ['docbook', 'lyxml'] },
            'UTTypeDescription':'DocBook file',
            'UTTypeIdentifier': ['org.docbook.docbook'],
            'UTTypeConformsTo': ['public.text', 'public.plain-text', 'public.source-code']
        },
        {
            'UTTypeTagSpecification': { 'public.filename-extension': ['itely', 'tely', 'texi', 'texinfo'] },
            'UTTypeDescription':'Texinfo file',
            'UTTypeIdentifier': ['org.gnu.texinfo'],
            'UTTypeConformsTo': ['public.text', 'public.plain-text', 'public.source-code']
        },
        {
            'UTTypeTagSpecification': { 'public.filename-extension': ['scm'] },
            'UTTypeDescription':'Scheme file',
            'UTTypeIdentifier': ['org.scheme.scheme'],
            'UTTypeConformsTo': ['public.text', 'public.plain-text', 'public.source-code']
        }
    ]
)

OPTIONS = {
    'argv_emulation': True,
    'semi_standalone': True,
    'alias': True,
    'plist': plist,
}

setup(
    app=APP,
    name=NAME,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
