# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1525136902.530593
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/linux/syscalls/execve.asm'
_template_uri = 'i386/linux/syscalls/execve.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u"execve(path, argv, envp) -> str\n\nInvokes the syscall execve.\n\nSee 'man 2 execve' for more information.\n\nArguments:\n    path(char*): path\n    argv(char**): argv\n    envp(char**): envp\nReturns:\n    int\n"
def render_body(context,path=0,argv=0,envp=0,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(path=path,pageargs=pageargs,envp=envp,argv=argv)
        Exception = context.get('Exception', UNDEFINED)
        str = context.get('str', UNDEFINED)
        zip = context.get('zip', UNDEFINED)
        tuple = context.get('tuple', UNDEFINED)
        list = context.get('list', UNDEFINED)
        len = context.get('len', UNDEFINED)
        dict = context.get('dict', UNDEFINED)
        syscalls = context.get('syscalls', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        hasattr = context.get('hasattr', UNDEFINED)
        __M_writer = context.writer()

        import collections
        import pwnlib.abi
        import pwnlib.constants
        import pwnlib.shellcraft
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['collections','pwnlib'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')

        abi = pwnlib.abi.ABI.syscall()
        stack = abi.stack
        regs = abi.register_arguments[1:]
        allregs = pwnlib.shellcraft.registers.current()
        
        can_pushstr = ['path']
        can_pushstr_array = ['argv', 'envp']
        
        argument_names = ['path', 'argv', 'envp']
        argument_values = [path, argv, envp]
        
        # Load all of the arguments into their destination registers / stack slots.
        register_arguments = dict()
        stack_arguments = collections.OrderedDict()
        string_arguments = dict()
        dict_arguments = dict()
        array_arguments = dict()
        syscall_repr = []
        
        for name, arg in zip(argument_names, argument_values):
            if arg is not None:
                syscall_repr.append('%s=%r' % (name, arg))
        
            # If the argument itself (input) is a register...
            if arg in allregs:
                index = argument_names.index(name)
                if index < len(regs):
                    target = regs[index]
                    register_arguments[target] = arg
                elif arg is not None:
                    stack_arguments[index] = arg
        
            # The argument is not a register.  It is a string value, and we
            # are expecting a string value
            elif name in can_pushstr and isinstance(arg, str):
                string_arguments[name] = arg
        
            # The argument is not a register.  It is a dictionary, and we are
            # expecting K:V paris.
            elif name in can_pushstr_array and isinstance(arg, dict):
                array_arguments[name] = ['%s=%s' % (k,v) for (k,v) in arg.items()]
        
            # The arguent is not a register.  It is a list, and we are expecting
            # a list of arguments.
            elif name in can_pushstr_array and isinstance(arg, (list, tuple)):
                array_arguments[name] = arg
        
            # The argument is not a register, string, dict, or list.
            # It could be a constant string ('O_RDONLY') for an integer argument,
            # an actual integer value, or a constant.
            else:
                index = argument_names.index(name)
                if index < len(regs):
                    target = regs[index]
                    register_arguments[target] = arg
                elif arg is not None:
                    stack_arguments[target] = arg
        
        # Some syscalls have different names on various architectures.
        # Determine which syscall number to use for the current architecture.
        for syscall in ['SYS_execve']:
            if hasattr(pwnlib.constants, syscall):
                break
        else:
            raise Exception("Could not locate any syscalls: %r" % syscalls)
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['index','dict_arguments','can_pushstr','name','syscall','abi','stack_arguments','v','regs','argument_names','argument_values','array_arguments','target','can_pushstr_array','arg','k','allregs','register_arguments','stack','string_arguments','syscall_repr'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n    /* execve(')
        __M_writer(unicode(', '.join(syscall_repr)))
        __M_writer(u') */\n')
        for name, arg in string_arguments.items():
            __M_writer(u'    ')
            __M_writer(unicode(pwnlib.shellcraft.pushstr(arg, append_null=('\x00' not in arg))))
            __M_writer(u'\n    ')
            __M_writer(unicode(pwnlib.shellcraft.mov(regs[argument_names.index(name)], abi.stack)))
            __M_writer(u'\n')
        for name, arg in array_arguments.items():
            __M_writer(u'    ')
            __M_writer(unicode(pwnlib.shellcraft.pushstr_array(regs[argument_names.index(name)], arg)))
            __M_writer(u'\n')
        for name, arg in stack_arguments.items():
            __M_writer(u'    ')
            __M_writer(unicode(pwnlib.shellcraft.push(arg)))
            __M_writer(u'\n')
        __M_writer(u'    ')
        __M_writer(unicode(pwnlib.shellcraft.setregs(register_arguments)))
        __M_writer(u'\n    ')
        __M_writer(unicode(pwnlib.shellcraft.syscall(syscall)))
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"128": 97, "129": 97, "130": 97, "131": 99, "132": 99, "133": 99, "134": 100, "140": 134, "16": 7, "17": 20, "32": 1, "41": 6, "42": 19, "43": 20, "44": 21, "114": 87, "115": 88, "116": 88, "117": 89, "118": 90, "119": 90, "120": 90, "121": 91, "122": 91, "123": 93, "124": 94, "125": 94, "126": 94, "127": 96}, "uri": "i386/linux/syscalls/execve.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/linux/syscalls/execve.asm"}
__M_END_METADATA
"""
