# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1525136902.518643
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/linux/sh.asm'
_template_uri = 'i386/linux/sh.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u"\nExecute a different process.\n\n    >>> p = run_assembly(shellcraft.i386.linux.sh())\n    >>> p.sendline('echo Hello')\n    >>> p.recv()\n    'Hello\\n'\n\n"
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        from pwnlib.shellcraft import i386 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['i386'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(unicode(i386.linux.execve('/bin///sh', ['sh'], 0)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"35": 29, "16": 2, "17": 0, "22": 1, "26": 1, "27": 10, "28": 11, "29": 11}, "uri": "i386/linux/sh.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/linux/sh.asm"}
__M_END_METADATA
"""
