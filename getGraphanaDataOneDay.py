import requests
import shutil
import time
import os

timestr = time.strftime("%Y%m%d")
print timestr

pathToFileWithResult='graphanaLogsFresh/'

folder = pathToFileWithResult
for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        #elif os.path.isdir(file_path): shutil.rmtree(file_path)
    except Exception as e:
        print(e)

		
payload = {'target':'alias(nagios.metrics_cpp_rprod.sync-commit-throughput.throughput, \'Synchronous\')','from':'-1d','until':'now','format':'csv','maxDataPoints':'1912'}
req = requests.post("http://ams2-umi-graph-101.flatns.net/render&format=csv", params=payload)
print(req.status_code, req.reason)
if req.status_code == 200:
	with open(pathToFileWithResult+'9-async-commit-throughput-overall-Synchronous' + timestr + '.csv', 'wb') as file:
		file.write(req.content)
	del req
	
	payload = {'target':'alias(nagios.metrics_cpp_rprod.async-commit-throughput.throughput, \'Asynchronous\')','from':'-1d','until':'now','format':'csv','maxDataPoints':'1912'}
req = requests.post("http://ams2-umi-graph-101.flatns.net/render&format=csv", params=payload)
print(req.status_code, req.reason)
if req.status_code == 200:
	with open(pathToFileWithResult+'8-async-commit-throughput-overall-Asynchronous' + timestr + '.csv', 'wb') as file:
		file.write(req.content)
	del req
	
payload = {'target':'alias(offset(scale(nagios.metrics_cpp_rprod.sync-commit-error-rate.error_rate, -1), 100), \'Synchronous\')','from':'-1d','until':'now','format':'csv','maxDataPoints':'1912'}
req = requests.post("http://ams2-umi-graph-101.flatns.net/render&format=csv", params=payload)
print(req.status_code, req.reason)
if req.status_code == 200:
	with open(pathToFileWithResult+'18-sync-commit-success-rate-Synchronous' + timestr + '.csv', 'wb') as file:
		file.write(req.content)
	del req
	
	payload = {'target':'alias(offset(scale(nagios.metrics_cpp_rprod.async-commit-error-rate.error_rate, -1), 100), \'Asynchronous\')','from':'-1d','until':'now','format':'csv','maxDataPoints':'1912'}
req = requests.post("http://ams2-umi-graph-101.flatns.net/render&format=csv", params=payload)
print(req.status_code, req.reason)
if req.status_code == 200:
	with open(pathToFileWithResult+'17-sync-commit-success-rate-Asynchronous' + timestr + '.csv', 'wb') as file:
		file.write(req.content)
	del req
	
payload = {'target':'alias(nagios.metrics_cpp_rprod.sync-commit-response-time.duration, \'Current\')','from':'-1d','until':'now','format':'csv','maxDataPoints':'1912'}
req = requests.post("http://ams2-umi-graph-101.flatns.net/render&format=csv", params=payload)
print(req.status_code, req.reason)
if req.status_code == 200:
	with open(pathToFileWithResult+'16-sync-commit-response-time-Current' + timestr + '.csv', 'wb') as file:
		file.write(req.content)
	del req
	
payload = {'target':'alias(nagios.metrics_cpp_rprod.sync-commit-response-time.reference_duration, \'Baseline\')','from':'-1d','until':'now','format':'csv','maxDataPoints':'1912'}
req = requests.post("http://ams2-umi-graph-101.flatns.net/render&format=csv", params=payload)
print(req.status_code, req.reason)
if req.status_code == 200:
	with open(pathToFileWithResult+'15-sync-commit-response-time-Baseline' + timestr + '.csv', 'wb') as file:
		file.write(req.content)
	del req
	
payload = {'target':'alias(nagios.metrics_cpp_rprod.async-commit-response-time.duration, \'Current\')','from':'-1d','until':'now','format':'csv','maxDataPoints':'1912'}
req = requests.post("http://ams2-umi-graph-101.flatns.net/render&format=csv", params=payload)
print(req.status_code, req.reason)
if req.status_code == 200:
	with open(pathToFileWithResult+'5-async-commit-response-time-Current' + timestr + '.csv', 'wb') as file:
		file.write(req.content)
	del req
	
payload = {'target':'alias(nagios.metrics_cpp_rprod.async-commit-response-time.reference_duration, \'Baseline\')','from':'-1d','until':'now','format':'csv','maxDataPoints':'1912'}
req = requests.post("http://ams2-umi-graph-101.flatns.net/render&format=csv", params=payload)
print(req.status_code, req.reason)
if req.status_code == 200:
	with open(pathToFileWithResult+'4-async-commit-response-time-Baseline' + timestr + '.csv', 'wb') as file:
		file.write(req.content)
	del req
	
payload = {'target':'alias(sumSeries(keepLastValue(exclude(nagios.metrics_cpp_rprod.*-commit-throughput.throughput, \'proc-commit-throughput\'), 2)), \'Current\')','from':'-1d','until':'now','format':'csv','maxDataPoints':'1912'}
req = requests.post("http://ams2-umi-graph-101.flatns.net/render&format=csv", params=payload)
print(req.status_code, req.reason)
if req.status_code == 200:
	with open(pathToFileWithResult+'11-live-commit-throughput-Current' + timestr + '.csv', 'wb') as file:
		file.write(req.content)
	del req
	
payload = {'target':'alias(sumSeries(keepLastValue(exclude(nagios.metrics_cpp_rprod.*-commit-throughput.reference_throughput, \'proc-commit-throughput\'), 2)), \'Baseline\')','from':'-1d','until':'now','format':'csv','maxDataPoints':'1912'}
req = requests.post("http://ams2-umi-graph-101.flatns.net/render&format=csv", params=payload)
print(req.status_code, req.reason)
if req.status_code == 200:
	with open(pathToFileWithResult+'10-live-commit-throughput-Baseline' + timestr + '.csv', 'wb') as file:
		file.write(req.content)
	del req
	
payload = {'target':'alias(nagios.metrics_cpp_rprod.sync-commit-throughput.throughput, \'Current\')','from':'-1d','until':'now','format':'csv','maxDataPoints':'1912'}
req = requests.post("http://ams2-umi-graph-101.flatns.net/render&format=csv", params=payload)
print(req.status_code, req.reason)
if req.status_code == 200:
	with open(pathToFileWithResult+'20-sync-commit-throughput-Current' + timestr + '.csv', 'wb') as file:
		file.write(req.content)
	del req
	
payload = {'target':'alias(nagios.metrics_cpp_rprod.sync-commit-throughput.reference_throughput, \'Baseline\')','from':'-1d','until':'now','format':'csv','maxDataPoints':'1912'}
req = requests.post("http://ams2-umi-graph-101.flatns.net/render&format=csv", params=payload)
print(req.status_code, req.reason)
if req.status_code == 200:
	with open(pathToFileWithResult+'19-sync-commit-throughput-Baseline' + timestr + '.csv', 'wb') as file:
		file.write(req.content)
	del req
		
payload = {'target':'alias(nagios.metrics_cpp_rprod.async-commit-throughput.throughput, \'Current\')','from':'-1d','until':'now','format':'csv','maxDataPoints':'1912'}
req = requests.post("http://ams2-umi-graph-101.flatns.net/render&format=csv", params=payload)
print(req.status_code, req.reason)
if req.status_code == 200:
	with open(pathToFileWithResult+'7-async-commit-throughput-Current' + timestr + '.csv', 'wb') as file:
		file.write(req.content)
	del req
	
payload = {'target':'alias(nagios.metrics_cpp_rprod.async-commit-throughput.reference_throughput, \'Baseline\')','from':'-1d','until':'now','format':'csv','maxDataPoints':'1912'}
req = requests.post("http://ams2-umi-graph-101.flatns.net/render&format=csv", params=payload)
print(req.status_code, req.reason)
if req.status_code == 200:
	with open(pathToFileWithResult+'6-async-commit-throughput-Baseline' + timestr + '.csv', 'wb') as file:
		file.write(req.content)
	del req

payload = {'target':'alias(nagios.metrics_cpp_rprod.sync-commit-queue-time.queue_time, \'Current\')','from':'-1d','until':'now','format':'csv','maxDataPoints':'1912'}
req = requests.post("http://ams2-umi-graph-101.flatns.net/render&format=csv", params=payload)
print(req.status_code, req.reason)
if req.status_code == 200:
	with open(pathToFileWithResult+'14-sync-commit-queue-time-Current' + timestr + '.csv', 'wb') as file:
		file.write(req.content)
	del req
	
payload = {'target':'alias(nagios.metrics_cpp_rprod.sync-commit-queue-time.reference_queue_time, \'Baseline\')','from':'-1d','until':'now','format':'csv','maxDataPoints':'1912'}
req = requests.post("http://ams2-umi-graph-101.flatns.net/render&format=csv", params=payload)
print(req.status_code, req.reason)
if req.status_code == 200:
	with open(pathToFileWithResult+'13-sync-commit-queue-time-Baseline' + timestr + '.csv', 'wb') as file:
		file.write(req.content)
	del req
	
payload = {'target':'alias(diffSeries(nagios.metrics_cpp_rprod.sync-commit-response-time.duration, nagios.metrics_cpp_rprod.sync-commit-queue-time.queue_time), \'Backend duration\')','from':'-1d','until':'now','format':'csv','maxDataPoints':'1912'}
req = requests.post("http://ams2-umi-graph-101.flatns.net/render&format=csv", params=payload)
print(req.status_code, req.reason)
if req.status_code == 200:
	with open(pathToFileWithResult+'12-sync-backend-commit-time' + timestr + '.csv', 'wb') as file:
		file.write(req.content)
	del req

payload = {'target':'alias(nagios.metrics_cpp_rprod.async-commit-queue-time.queue_time, \'Current\')','from':'-1d','until':'now','format':'csv','maxDataPoints':'1912'}
req = requests.post("http://ams2-umi-graph-101.flatns.net/render&format=csv", params=payload)
print(req.status_code, req.reason)
if req.status_code == 200:
	with open(pathToFileWithResult+'3-async-commit-queue-time-Current' + timestr + '.csv', 'wb') as file:
		file.write(req.content)
	del req
	
payload = {'target':'alias(nagios.metrics_cpp_rprod.async-commit-queue-time.reference_queue_time, \'Baseline\')','from':'-1d','until':'now','format':'csv','maxDataPoints':'1912'}
req = requests.post("http://ams2-umi-graph-101.flatns.net/render&format=csv", params=payload)
print(req.status_code, req.reason)
if req.status_code == 200:
	with open(pathToFileWithResult+'2-async-commit-queue-time-Baseline' + timestr + '.csv', 'wb') as file:
		file.write(req.content)
	del req	
	
payload = {'target':'alias(diffSeries(nagios.metrics_cpp_rprod.async-commit-response-time.duration, nagios.metrics_cpp_rprod.async-commit-queue-time.queue_time), \'Backend duration\')','from':'-1d','until':'now','format':'csv','maxDataPoints':'1912'}
req = requests.post("http://ams2-umi-graph-101.flatns.net/render&format=csv", params=payload)
print(req.status_code, req.reason)
if req.status_code == 200:
	with open(pathToFileWithResult+'1-async-backend-commit-time' + timestr + '.csv', 'wb') as file:
		file.write(req.content)
	del req