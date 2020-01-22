#!/usr/bin/python

import socket, logging

class SOSConnection:
    HOST = 'localhost'
    PORT = 2468
    TIMEOUT = 30

    ENABLER = 'enable'

    logging.basicConfig(
        filename='auto_sos.log',
        filemode='w',
        format='%(asctime)s: %(message)s',
        datefmt='%m-%d-%Y %I:%M:%S %p',
        level=logging.INFO)

    # This is our class constructor
    # Use this to specify non-default settings
    # EX: SOSConnection("10.1.1.32", 2468, 60)
    def __init__(self,
                 host=HOST,
                 port=PORT,
                 timeout=TIMEOUT,
                 port_enabling_str=ENABLER):
        self.host = host
        self.port = port
        self.port_enabling_str = port_enabling_str
        self.socket = self.create_socket()
        self.socket.settimeout(timeout)

    # Make sure command ends with a newline character
    # This simulates pressing the Enter key from a console
    # This function isn't really meant for use by clients
    def format_cmd(self, cmd):
        if not cmd.endswith('\n'):
            cmd = cmd + '\n'
        return cmd
    
    # Create and return a socket that can be used to connect
    # to an SOS machine
    # This function isn't really meant for use by clients
    def create_socket(self):
        logging.info('Creating new socket')
        return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Give SOS the special word 'enable' to it will
    # listen to our commands
    # This function isn't really meant for use by clients
    def enable(self):
        self.send(self.port_enabling_str)

    # Connect to the host and port specified in the constructor
    # Pass it the enabling string
    # Requires SOS to be running
    def connect(self):
        logging.info('Connecting to {0}:{1}'.format(self.host, self.port))
        if not self.socket:
            self.socket = self.create_socket()
        self.socket.connect((self.host, self.port))
        self.enable()

    # Close our connection
    def close(self):
        logging.info('Closing socket')
        self.socket.close()

    # Send a command to SOS, capture any response and write
    # it out.
    #     EX: To play the first clip of a presentation playlist...
    #
    #         send("play 1")
    #
    def send(self, cmd):
        cmd = self.format_cmd(cmd)
        logging.info("Sending command: '{0}'".format(cmd.strip()))
        self.socket.send(cmd)
        response = self.socket.recv(4096).strip()
        logging.info("RESPONSE: '{0}'".format(response))
        return response
