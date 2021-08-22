import gdb

class Ps(gdb.Command):
	"""
	Usage: ps string
	"""
	def __init__(self):
		super(self.__class__, self).__init__("ps", gdb.COMMAND_USER)
	
	def invoke(self, args, from_tty):
		argv = gdb.string_to_argv(args)
		if len(argv) != 1:
	            raise gdb.GdbError('[ps] takes one arguments')
                argv0 = gdb.parse_and_eval(argv[0])
                if str(argv0.type) != 'char *':
                    raise gdb.GdbError('The type of ' + argv[0] + ' is not char * !')
		gdb.execute('printf \"%s\\n\", ' + argv[0])

# register command
Ps()
