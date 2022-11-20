import getpass
import os
import socket
import select
import sys
import threading

import paramiko

# research which port # to use
ssh_port = 22

class setup():
    '''
    Define the target (server), user, password etc
    '''    
    def __init__(self,client, args, channel, socket, thread):
        self.client = client
        self.client = Paramiko.SSHClient()
        self.args = args
        self.channel = channel
        self.thread = thread
        self.socket = socket

    def determine_port(self, target, default_port):
        self.args = (target.split(":", 1) + [default_port])[:2]
        self.args[1] = int(self.args[1])
        return self.args[0], self.args[1]

    def handleChannelConnection(self,channel,host,port):
        socket = self.socker.socket()
        try:
            self.socket.connect(host,port)
        except Exception as e:
                return

        while True:
            rData = select.select([self.socket, self.channel], [], [])
        if self.socket in rData:
            data = self.socket.recv(1024)
            if len(data) == 0:
                return
            self.channel.send(data)

        if self.channel in rData:
            data = self.channel.recv(1024)
            if len(data) == 0:
                return
            self.socket.send(data)
    self.channel.close()
    self.socket.close()

    '''
        transport: Defined in paramiko/auth_handler.py
    '''
    def tunnel(self,server_port,rHost,transport)->...:
        transport.request_port_forward("", server_port)
        while True:
            self.channel = transport.accept(1000)
        if self.channel is None:
            return
        self.thread = threading.Thread(
            target=handler, args=(channel, rHost, remote_port)
        )
        self.thread.setDaemon(True)
        self.thread.start()







