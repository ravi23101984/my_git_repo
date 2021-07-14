#!/bin/python
import json
import sys
try:
  import boto
except EXCEPTION as e:
  print(e)
  print("Please rectify above exception and then try again!")
  sys.exit(1)
 
def get_hosts(ec2_ob,fv):
   f={"Name":"tag:Env" , "Values": [fv]}
   hosts=[]
   for each_in in ec2_ob.instances.filter(Filters=[f]):
       #print(each_in.private_ip_address)
       hosts.append(each_in.private_ip_address)
   return hosts
def main():
   ec2_ob=boto.resource("ec2","us-east-1")
   db_group=get_hosts(ec2_ob,'db')
   app_group=get_hosts(ec2_ob,'app')
   all_groups={ 'db': db_group, 'app': app_group }
   print(json.dumpls(all_groups))
   return None

if __name__=="__main__":
   main()
   
