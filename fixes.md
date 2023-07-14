# FIX ME!

## 1. Business Logic
__What?__: Nslookup 
__Problem__: Needs to be more verbose 
__Possible_Fixes__: Implement additional functions or use existing libraries
__Any Affected?__: None
__Fix__: 

## 2. Propagation endpoint
__What?__: Needs a better implementation. Missing Timings for regions. Need to add regions
__Problem__: Implementations are not up to the mark
__Possible_Fixes__: Researching... TBD
__Any Affected?__: None
__Fix__: 




# SOLVED!

## 1. check_dns_propogation() method in api.dns
__What?:__ Needs to be implemented 

__Problem:__ Dnspython library support 

__Possible_Fixes:__ Different library(dns-crawler) or subprocess command or a workaround?

__Any Affected?:__ Changes need to be made to the test implementation

__Solved__: Used dnsdiag and installed locally 


## 2. Python version
__What?__: Doesnt run due to a regex error
__Problem__: Python 3.9 issue 
__Possible_Fixes__: Use Python 3.6 env always in our docker or conda 
__Any Affected?__: None
__Fix__: Switched to Python 3.8.17
