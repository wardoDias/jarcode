import os
from pathlib import Path
from datetime import datetime as dt
from datetime import timedelta as delta

rel_path = r'\WARDONUT\DeadBy\main.py'
cursor_path = Path.cwd()
parents = cursor_path.parent._str.split("\\")

while parents[-1] != "beManPromise": 
  cursor_path = cursor_path.parent
  parents = cursor_path.parent._str.split("\\")


target_path = Path("\\".join(parents)+rel_path) 


last_modified = os.path.getmtime(target_path)
readable = dt.fromtimestamp(last_modified)

delta = delta(minutes=2)

def detect_change(filepath, last_mod):
	with open(filepath, "r+") as logs:
		log_arr = logs.readlines()
		log_arr = [log.strip() for log in log_arr]
		print(log_arr)
		for order, log in enumerate(log_arr):
			if log:
				continue

			del log_arr[order]

		try: 
			if last_mod - dt.strptime(log_arr[-1], "%m/%d/%Y %H:%M %p") >= delta:
				
				logs.write(dt.strftime(dt.now(), "\n%m/%d/%Y %H:%M %p"))
				print("Changed")
		except IndexError:
			logs.write(dt.strftime(dt.now(), "%m/%d/%Y %H:%M %p\n"))
		
		logs.close()


def prettify(filepath):
	lines = None
	with open(filepath, "r+") as mush:
		lines = mush.readlines()
		print(lines)
		
		
	with open(filepath, "w") as logs:
		for l in lines:
			if l.strip():
				logs.write(l+'\n')
		
		logs.close()
		
def progress():
	pass


detect_change('modlog.txt', readable)
prettify('modlog.txt')