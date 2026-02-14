import os
import sys
import webbrowser
from threading import Timer
from django.core.management import execute_from_command_line

def open_browser():
    webbrowser.open_new("http://127.0.0.1:8000")

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restotup.settings')
    
    # Override sys.argv to force runserver
    # --noreload is important for PyInstaller environments to avoid spawning new processes incorrectly
    sys.argv = [sys.argv[0], 'runserver', '--noreload', '--insecure']
    
    # Schedule browser to open after 1.5 seconds
    Timer(1.5, open_browser).start()
    
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
