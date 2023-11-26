#!/usr/bin/env python
import argparse
import socket
import struct
import logging
import time


LOG = logging.getLogger(__name__)


def create_magic_packet(macaddress):
    if len(macaddress) == 12:
        pass
    elif len(macaddress) == 17:
        sep = macaddress[2]
        macaddress = macaddress.replace(sep, '')
    else:
        raise ValueError('Incorrect MAC address format')

    data = b'FFFFFFFFFFFF' + (macaddress * 16).encode()
    send_data = b''

    for i in range(0, len(data), 2):
        send_data += struct.pack(b'B', int(data[i:i+2], 16))
    return send_data

def send_magic_packet(macs, broadcast='255.255.255.255',
                      port=7, send_times=3):
    packets = []
    for mac in macs:
        packet = create_magic_packet(mac)
        packets.append(packet)

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except BaseException as e:
        LOG.error("Wake up, Create sock failed: {err}".format(err=str(e)))
        return False

    ret = True
    try:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        for idx,packet in enumerate(packets):
            if idx % 10 == 0:
                time.sleep(0.1)
            for i in range(send_times):
                sock.sendto(packet, (broadcast, port))
    except BaseException as e:
        LOG.error("Wake up failed: {err}".format(err=str(e)))
        ret = False
    finally:
        sock.close()

    return ret

BROADCAST_IP = '255.255.255.255'
DEFAULT_PORT = 7
def main(argv=None):
    parser = argparse.ArgumentParser(
        description='Wake one or more computers using the wake on lan'
                    ' protocol.')
    parser.add_argument(
        'macs',
        metavar='mac address',
        nargs='+',
        help='The mac addresses or of the computers you are trying to wake.')
    parser.add_argument(
        '-i',
        metavar='ip',
        default=BROADCAST_IP,
        help='The ip address of the host to send the magic packet to.'
             ' (default {})'.format(BROADCAST_IP))
    parser.add_argument(
        '-p',
        metavar='port',
        type=int,
        default=DEFAULT_PORT,
        help='The port of the host to send the magic packet to (default 7)')
    args = parser.parse_args(argv)
    send_magic_packet(args.macs, broadcast=args.i, port=args.p)

if __name__ == '__main__':
    main()