# -*- coding: utf-8 -*-
"""
    pygments.styles.vibrantink
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    pygments version of the "vibrantink" textmate theme.

"""

from pygments.style import Style
from pygments.token import Token, Comment, Name, Keyword, \
    Generic, Number, String, Whitespace, Error, Operator

class VibrantinkStyle(Style):
    """
    Pygments version of the "vibrantink" textmate theme.
    """

    background_color = '#000'
    highlight_color  = '#FFF'

    styles = {
        Comment:                    'italic #93C',
        Comment.Multiline:          'italic bg:#070707 #772CB7',
        Comment.Preproc:            'bold #EDF8F9',
        Comment.Special:            'bold italic #93C',
        
        Error:                      'bg:#e3d2d2 #a61717',
        
        Keyword:                    'bold #F60',
        Keyword.Type:               'bold #458',
        
        Operator:                   'bold',

        Generic.Deleted:            'bg:#fdd #000',
        Generic.Deleted.Specific:   'bg:#faa #000',
        Generic.Emph:               'italic',
        Generic.Error:              '#a00',
        Generic.Heading:            '#999',
        Generic.Inserted:           'bg:#dfd #000',
        Generic.Inserted.Specific:  'bg:#afa #000',
        Generic.Output:             '#888',
        Generic.Prompt:             '#555',
        Generic.Strong:             'bold',
        Generic.Subheading:         '#aaa',
        Generic.Traceback:          '#a00',

        Name.Attribute:             '#9C9',
        Name.Builtin:               '#FFF',
        Name.Builtin.Pseudo:        '#999',
        Name.Class:                 'underline #FFF',
        Name.Constant:              '#399',
        Name.Entity:                '#399',
        Name.Exception:             'bold #900',
        Name.Function:              'bold #FC0',
        Name.Namespace:             '#555',
        Name.Tag:                   '#F60',
        Name.Variable:              '#008080',

        Whitespace:                 '#BBB',
        
        Number:                     '#CF3',

        String:                     '#6F0',
        String.Backtick:            'bg:#CC3 #000',
        String.Interpol:            '#D55555',
        String.Regex:               '#44B4CC',
        String.Symbol:              '#399'
    }
