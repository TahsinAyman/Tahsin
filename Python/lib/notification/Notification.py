from win10toast import ToastNotifier
import sys
import os

def notification(message, description=''):
    notifier = ToastNotifier()
    notifier.show_toast(message, description)

n = int(input())

if n == 1
