# getprotobyname.py

import socket


def get_constant(prefix):
    """Create a dictionary mapping socket module
       constants to their names."""
    return {
        getattr(socket, n): n
        for n in dir(socket)
        if n.startswith(prefix)
    }

protocols = get_constant('IPPROTO_')

for name in ['icmp', 'udp', 'tcp']:
    proto_num = socket.getprotobyname(name)
    const_name = protocols[proto_num]
    print('{:>4} -> {:2d} (socket.{:<12} = {:2d})'.format(
        name, proto_num, const_name,
        getattr(socket, const_name)))
