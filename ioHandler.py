#!/usr/bin/env python

import socket

class ircConnection:
	def __init__(self, serverName, port=6667):
		self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.connection.connect((serverName, port))
	
	def sendMessage(self, toSend):
		'''Helper function that sends the given string as an IRC message, appending \r\n.'''
		self.connection.send(str(toSend + "\r\n")) #, "utf-8"))
		
	def receive(self):
		'''Recieve 512 bytes from the connection (512 bytes == 1 message)'''
		return str(self.connection.recv(512)) #, "utf-8")
		
	def setNick(self, nick):
		'''Sets the nick on this connection.'''
		self.sendMessage("NICK " + nick)
		
	def setUser(self, userName, hostName, serverName, realName):
		'''Set the user'''
		self.sendMessage("USER " + userName + " " + hostName + " " + serverName + " :" + realName)
		
	def close(self):
		'''Close the connection.''' 
		self.connection.close()
