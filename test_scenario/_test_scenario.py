# This file should be imported and the following variables passed in
#iterations = { 100, 200, 500, 1000, 5000, 10000, 20000, 100000 }
#results_name = "basic_with"
#activemq_script = "run_activemq.sh"


import sys
import time
import datetime
import subprocess
import shlex

sys.path.append("../common")
import _common

def run(activemq_script):
	# Define variables to be used later on
	timestamp = _common.get_timestamp()

	# Start Active MQ
	print("Starting Active MQ")
	_common.run_command("sh ../common/active_mq_scripts/" + activemq_script)

	print("Waiting 8 seconds...")
	time.sleep(8)

	print("Starting tests");

	runner_receiver = _common.run_command_back("python2 ./message_queue_py/read.py")
	runner_sender = _common.run_command_back("python2 ./message_queue_py/run.py")
	print("Waiting for tests to finish");
	runner_sender.wait()

	# Get the results
	results_file = open("./message_queue_py/account.txt", "r")
	result = results_file.read()
	results_file.close()

	print("Finished tests")

	# Kill dead active MQ
	print("Killing Active MQ...")
	activemq_process_kill = _common.run_command('sh ./apache-activemq-5.13.2/bin/activemq stop')

	print("Waiting 3 seconds...")
	time.sleep(3)

	return result
