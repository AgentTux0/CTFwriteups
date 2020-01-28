#### riceteacatpanda 2020
#### - Category: general
#### - Challenge: classic c4
#### - Points: 30
#### - Author: c4melman

- - -
*If you use that bomb, you might cause an Avalanche... Let's not destroy my IO, ok?*
- - -
The flag starts with c4
Submit in the format: rtcp{90-char-flag}
- - -

In this challenge we are supplied with a text file called da_bomb.txt. Having a quick look at it we can see some strings that looks like they are encoded with base64. I wrote a quick python script to decode them all, which revealed this:

'Hah, you thought'
'Really? Did you actually keep going'
'lowkey dissapointed...'
'fun fact: Jess is actually a cat'
'merp'
'*insert filler material here*'
'welp that should be enough data'
"if you can't tell already, decoding this isn't the answer"

So that didn't get us anywhere. But in the hint it says that the flag starts with c4, time to do some google-fu and see if we can learn something about this. After some different searches I found something promising:

"C4 IDs are an encoding of a SHA-512 hash that is shorter and more ergonomic than hex and yet packed with features. [...] Starts with 'c4', and is 90 characters long."

This page also allows us to drop files, and dropping our .txt file gives us:
c42CW3TbiGhvptM36RJJ9ScctgkskjvZPo6dG8JexzZRvzQR6hwovZJLDkYK5pZ6cq9e7fX1ShUiYUdM7H1Uuqj64G

starts with c4, is 90 chars long.
This is the flag!
- - -
### Flag: rtcp{c42CW3TbiGhvptM36RJJ9ScctgkskjvZPo6dG8JexzZRvzQR6hwovZJLDkYK5pZ6cq9e7fX1ShUiYUdM7H1Uuqj64G}
