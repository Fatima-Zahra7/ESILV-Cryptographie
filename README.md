# ESILV-Cryptographie
# Password Hashing
(or how to securely store your user passwords).

# How to calculate the strength of a password?
We specify password strength in terms of information entropy which is measured in bits. Instead of the number of guesses needed to find the password, the base-2 logarithm of that number is given, which is commonly referred to as the number of entropy bits in a password.

For example, a password with an entropy of 42 bits would require 242 attempts to exhaust all possibilities during a brute force search.

64-80-bit of entropy would be strong for most online services.

## How do we calculate the entropy of a password?
H= L (logN / log2)

where
- N : is the number of possible symbols and
- L : is the number of symbols in the password.
- H : is measured in bits.

Question 1: What is minimum length of a password created from case-insensitive alphanumeric and having 64-bit of entropy?

<span style="color:green">***Answer :***</span> 
L = H / (log2 / log N)  
L = 64 / (log 2 / log 36)  
**L =12.379**


# How to securely store user passwords?
Threats:

Mass password cracking. The attacker wants to crack as many passwords as possible.
Targeted password cracking. The attacker wants to crack only a handful of passwords.
Database breaches. The attacker obtains a database containing (hash of) user passwords.

## Attempt 1 (Naive solution)
How would you store your user passwords?

<span style="color:green">***Answer :***</span>
to prevent the attacker from cracking the passwords, we have to hash and salt the passwords.  
Hashing is a cryptographic technique where a hash function is applied to the plaintext password to produce a fixed-size string of characters. Commonly used hashing algorithms include SHA-256, SHA-512.  
Salting involves adding a random and unique value (salt) to each password before hashing. 

## Attempt 2 (Increasing the entropy)
Most user passwords, however, are weak, taking fewer than
240 guesses to crack.  
How would you increase the entropy of the password?

<span style="color:green">***Answer :***</span> To increase the entropy of passwords, you can encourage users to use a combination of uppercase and lowercase letters, numbers, and special characters.  
Additionally, enforcing a minimum password length requirement and promoting the use of passphrases, which are longer and easier to remember, can significantly increase password entropy and strengthen security.

## Attempt 3 (Which hashing algorithm to use)
Hashing (by design) is fast, but the goal here is to slow down the brute force time of a user's password. Say, a legitimate user can wait for 100ms of delay. But an attacker who needs to brute force as fast as possible, 100ms times the number of all possible guesses is the barrier.  
This opens the possibility of using some slow memory-hard hash function (of course, it can't be too slow because of usability).  
Which hashing algorithm would you use ?

<span style="color:green">***Answer :***</span> Argon2.

## Attempt 4 (Data breaches and how to deal with it)
Finally, we come to the typical problem of online services: database breaches. In contrast to online attack, where we can prevent by limiting the number of failed logins, offline attack allows attacker to run bruteforce locally without no limitations. Because the hashes can be cracked offline, there's nothing we can do to stop the attackers.  
Or can we? Find something that provide us some kind of asymmetry in our favor! Encryption! How would you use encryption to secure your user passwords?

<span style="color:green">***Answer :***</span> To enhance security against database breaches, use asymmetric encryption alongside hashing:

- Asymmetric Encryption: Generate a public/private key pair for each user. Keep the private key secret and store the public key in the database.
- Hashing with Salt: Hash the user's password with a unique salt and store the hashed result in the database.
- Encryption of Hash: Encrypt the hashed password with the user's public key and store the encrypted hash in the database.

This way, even if attackers access the encrypted hashes, they would need the user's private key to decrypt them, significantly increasing the difficulty of an attack.

# Project Implementation
Requirement for the implementation: password storage. Think about it as you are building some application that has user system (username and password) and you need to store the password securely.  
You should implement your solution, taking into accounts all the attack scenarios we have discussed. Basically the grade will be scored according to how secure your implementation is.   
The implementation needs to be runnable, where I can enter my username and password for registration and logging in (the interface can be a web app, or terminal etc).

If you are using any cryptographic encryption implementation, you need to use google tink library (except for the hash functions). Implementation using other libraries does not count.
