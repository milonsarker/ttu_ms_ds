#Request Library
import requests as r

#Request a page
res = r.get('https://www.depts.ttu.edu/rawlsbusiness/people/faculty/isqs/david-lucus/index.php')

#Let's see our HTML
res.text #response in unicode
res.content #response in bytes


#Check HTML Status Code
res.status_code

#How long did the request take?
res.elapsed

#odd format, what does this mean?
#Note, this is a timedelta.  
#Run in order: days, seconds, microseconds, milleseconds, minutes, hours, weeks 

#Can access each item as necessary
res.elapsed.microseconds

#Pull encoding
res.encoding

#Returns server response headers
#note, the reported IIS server (tells you the server is microsoft based)
res.headers

#Let's look at some other sites
new_res = r.get("http://apache.org")
new_res.headers

new_res = r.get("http://amazon.com")
new_res.headers

#Let's look at redirects.  Notice, the request for non-ssl
new_res = r.get("http://github.com")
new_res.history
new_res.url

#Note, this redirected to the SSL site.  We can stop this with
new_res = r.get("http://github.com", allow_redirects=False)
new_res.history
new_res.status_code
#code 301 is:  Move Permanently
new_res.is_redirect
new_res.is_permanent_redirect

#Image request
img_res = r.get('https://www.depts.ttu.edu/rawlsbusiness/people/faculty/isqs/david-lucus/images/Photo-David-Lucas.jpg')
img_res.headers

json_res = r.get("https://data.cityofnewyork.us/api/views/kku6-nxdu/rows.json?accessType=DOWNLOAD")
json_res.headers
json_res.content


