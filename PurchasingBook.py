#!/media/fucksociety/UBUNTU20_0/RubenLeo/PurchasingBook.py
# This Program Was Created By Ben Leo
# Created On September 28 At 03:57 AM
# Good Luck and Have a Nice Day :)

# Create a Function To Display The Program Title
def this_function_for_display_the_program_author_profile():


	# Import Python3 Module
	import os
	import sys
	import time
	import datetime
	import math
	import requests
	import pyfiglet
	import socket
	import hashlib
	import base64
	import threading
	import httplib2
	import subprocess
	import webbrowser
	import json
	import telnetlib
	import urllib3
	import argparse
	from sys import argv
	from time import sleep, localtime, strftime
	from datetime import timezone
	from calendar import calendar


	# Clean Screen
	os.system("clear")
	os.system("")
	os.system("")
	time.sleep(2)
	print("")


	# About Program Writer
	print("""

░█▀▀█ █──█ █▀▀█ █▀▀ █──█ █▀▀█ █▀▀ ─▀─ █▀▀▄ █▀▀▀ 　 ░█▀▀█ █▀▀█ █▀▀█ █─█ 　 ░█▀▀█ █▀▀█ █▀▀█ █▀▀▀ █▀▀█ █▀▀█ █▀▄▀█ 
░█▄▄█ █──█ █▄▄▀ █── █▀▀█ █▄▄█ ▀▀█ ▀█▀ █──█ █─▀█ 　 ░█▀▀▄ █──█ █──█ █▀▄ 　 ░█▄▄█ █▄▄▀ █──█ █─▀█ █▄▄▀ █▄▄█ █─▀─█ 
░█─── ─▀▀▀ ▀─▀▀ ▀▀▀ ▀──▀ ▀──▀ ▀▀▀ ▀▀▀ ▀──▀ ▀▀▀▀ 　 ░█▄▄█ ▀▀▀▀ ▀▀▀▀ ▀─▀ 　 ░█─── ▀─▀▀ ▀▀▀▀ ▀▀▀▀ ▀─▀▀ ▀──▀ ▀───▀
""")
	print("\033[1m[!] Written By     : BenLeo Coders")
	print("[!] My Team        : fSociety Hacker Syndicate")
	print("[!] Inspired By    : https://youtu.be/67gYEK4FtzA")
	print("[!] Message        : I Hope You Like The Program and Have a Nice Day :)")
	print("")
this_function_for_display_the_program_author_profile()


# For example I want to make the variable of the color code in python3, I need ...
def make_the_variable_of_the_color_code_in_python3_I_need():
	color_code_in_python3 = """
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	"""
make_the_variable_of_the_color_code_in_python3_I_need()


# Make a Program To Display a Menu For The User To Choose The Book They Want To Buy
def program_menu():
	program_menu = """
	█▀▀ █▀▀█ ▀█─█▀ █▀▀█ █▀▀█ ─▀─ ▀▀█▀▀ █▀▀ 　 █▀▀▄ █▀▀█ █▀▀█ █─█ 
	█▀▀ █▄▄█ ─█▄█─ █──█ █▄▄▀ ▀█▀ ──█── █▀▀ 　 █▀▀▄ █──█ █──█ █▀▄ 
	▀── ▀──▀ ──▀── ▀▀▀▀ ▀─▀▀ ▀▀▀ ──▀── ▀▀▀ 　 ▀▀▀─ ▀▀▀▀ ▀▀▀▀ ▀─▀
	"""
	print(program_menu)
	print("[1] Basic Computer Programming Logic (Update Version) > IDR 77k")
	print("[2] Sql Server Programming 2019 > IDR 49k")
	print("[3] Vb.Net Programming For Beginners > IDR 52k")
	print("[4] PHP Programming Quick Guide, You Can > IDR 49.5k")
	print("[5] Learn Programming And Hacking Using Python > IDR 52k")
	print("[6] Learn Android Programming For All Needs > IDR 56k")
	print("[7] Matlab Programming Basics > IDR 120k")
	print("[8] Advanced PHP Programming Language > IDR 49k")
	print("[9] Creating a Robot Using Raspberry Pi + Python Programming > IDR 119.5k")
	print("[10] Basic Robot Programming Using Arduino + CD > IDR 110k")
	print("")

	# Make a Program To Input User Choice
	select = int(input("[+] Select Your Menu: \n"))
	print("")

	# Create Condition If User Enters Choice
	if select == 1:
		print("[!] You Are Going To Buy a Book Basic Computer Programming Logic (Update Version) > IDR 77k")
		print("")
		choose = int(input("[?] How Many Books Did You Buy? \n"))
		print("")
		if choose == 1:
			the_price_of_this_book_is = 77000
			ask_2 = int(input("[?] How Much Your Money? "))
			results = ask_2 - the_price_of_this_book_is
			print("")
			print("[!] Your Total Refund Is " + str(results))
			print("")
			
		elif choose == 2:
			the_price_of_this_book_is = 154000
			ask_2 = int(input("[?] How Much Your Money? "))
			results = ask_2 - the_price_of_this_book_is
			print("")
			print("[!] Your Total Refund Is " + str(results))
			print("")

		elif choose == 3:
			the_price_of_this_book_is = 231000
			ask_2 = int(input("[?] How Much Your Money? "))
			results = ask_2 - the_price_of_this_book_is
			print("")
			print("[!] Your Total Refund Is " + str(results))
			print("")

		elif choose == 4:
			the_price_of_this_book_is = 308000
			ask_2 = int(input("[?] How Much Your Money? "))
			results = ask_2 - the_price_of_this_book_is
			print("")
			print("[!] Your Total Refund Is " + str(results))
			print("")

		elif choose == 5:
			the_price_of_this_book_is = 385000
			ask_2 = int(input("[?] How Much Your Money? "))
			results = ask_2 - the_price_of_this_book_is
			print("")
			print("[!] Your Total Refund Is " + str(results))
			print("")

program_menu()


# Create a Program to Open a Website Address
def program_to_open_a_website_address():
	print("""
░█▀▀▀█ █▀▀█ █▀▀ █▀▀▄ 　 ░█──░█ █▀▀ █▀▀▄ ░█▀▀█ █▀▀█ █▀▀█ █───█ █▀▀ █▀▀ █▀▀█ 
░█──░█ █──█ █▀▀ █──█ 　 ░█░█░█ █▀▀ █▀▀▄ ░█▀▀▄ █▄▄▀ █──█ █▄█▄█ ▀▀█ █▀▀ █▄▄▀ 
░█▄▄▄█ █▀▀▀ ▀▀▀ ▀──▀ 　 ░█▄▀▄█ ▀▀▀ ▀▀▀─ ░█▄▄█ ▀─▀▀ ▀▀▀▀ ─▀─▀─ ▀▀▀ ▀▀▀ ▀─▀▀
""")
	print("[!] Program Writer     : BenLeo ft fSociety Hacker Syndicate")
	print("[!] Inspired By        : https://youtu.be/67gYEK4FtzA")
	print("[!] Program Version    : 1.0")
	print("[!] Message            : I Hope You Like The Program and Have a Nice Day :)")
	print("")
	# Import Python3 Module
	import webbrowser
	import os, sys, time, datetime, math
	from sys import argv
	from time import sleep
	open_browser = input("[?] Browser You Want To Open: ")
	webbrowser.open(open_browser)
program_to_open_a_website_address()
	