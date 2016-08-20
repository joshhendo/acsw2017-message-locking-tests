import sys
import time
import datetime
import subprocess
import shlex

def get_timestamp():
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
	return st

def run_command(cmd):
	cmd_args = shlex.split(cmd)
	print(cmd_args)
	subprocess.call(cmd_args)

def run_command_back(cmd):
	return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

def get_memory_usage(pid):
	command = run_command('ps -p ' + str(pid) + '-o %mem | head -2 | tail -1')
	result = command.communicate()[0].decode('utf-8').rstrip() 
	return result

def get_activemq_pid():
	result = run_command_back("sh ./helper_scripts/activemq_pid.sh")
	result.wait()
	result = pid.communicate()[0].decode('utf-8').rstrip()
	return result