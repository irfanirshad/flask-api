# FIX ME!
## 1) check_dns_propogation() method in api.dns
__What?:__ Needs to be implemented 

__Problem:__ Dnspython library support 

__Fix:__ Different library(dns-crawler) or subprocess command or a workaround?

__Any Affected?:__ Changes need to be made to the test implementation


## 2) Python version
__What?:__ Doesnt run due to a regex error
__Problem:__ Python 3.9 issue 
__Fix:__ Use Python 3.6 env always in our docker or conda 
__Any Affected?:__ None
