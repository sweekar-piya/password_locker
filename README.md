# Password Locker

- Simple password locker system.
- Able to encrypt your passwords and copy them into your clipboard for ease.

## How to use?
1. Generate virtual env, activate it and install dependencies using `requirements.txt`.

2. Create `creds.py` file under `data` directory and add your credentials in a dictionary as:

```python
CREDENTIALS = {
    "gmail" : b"your_password_here",
    "facebook" : b"anotherpasswordhere",
}
```

3. Run the following command to encrypt your passwords. Duplicate `.env.sample`, rename as `.env` and copy the fernet key.
Then you can remove `creds.py`.

```
src/scripts/pass.py 
```

4. Then, you can run the following command:

```
src/scripts/pass.py <account_to_copy_password>
```

- for example, if you want to copy gmail's passord, run

```
src/scripts/pass.py gmail
```
