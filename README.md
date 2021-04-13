# WhatsApp: Top 3 messages per user

# Description
Simple whacky tool to analyze the most common messages for a specific user in a group chat. 

# Usage
1. Go to WhatsApp.
2. Go to a group chat.
3. Options > More > Export Chat > 'Without Files'.
4. Choose how to get the .txt file to your computer and place it in the same directory as the script.
5. Open the script and define the name of the file in the variable ```file```.
6. Define the contact name of the user in the variable ```user```.
7. Define the top n of messages you'd like to display.
8. Run the script*.

*I've written this script to be able to run in bare python, but if it's not installed, there might be some issues. I don't think this is going to be used by many, but if you're interested in running let me know and I'll expand it.


# How it works
## Structure of the inputs
Facebook didn't spend much time formatting the chat. Here's an example of a couple of messages, each is a line of the exported .txt file:

  ```
  21/11/19 12:08 - Jane Doe: that's it?
  21/11/19 12:09 - Max Doe: Yup
  21/11/19 12:09 - Will Doe: From ryanair:
  8 ppl - 55 bucks
  9 ppl - 55 bucks
  10 ppl- 67 bucks
  21/11/19 12:09 - Jane Doe: we can get them in two batches
  ```
We can say that data comes in the following format:

  ```
  <dd/mm/yyyy hh:mm> - <contact name>:<message>
  <dd/mm/yyyy hh:mm> - <contact name>:<message>
  <message continuation>
  <message continuation>
  <dd/mm/yyyy hh:mm> - <contact name>:<message>
  ```

Datetime is not consistent, no padding for days, months or hours, which is sad for the lazy programmer. Messages can also be in different lines, but we can classify each line as a 'header' or as 'body':
- Header: There's a data and an hour followed by a dash. That's enough to id it as a header (it'd be weird that someone sent a message with that structure, but it's possible).
- Body: just text, hopefully without what we described in the header.

## Algorithm
1. Open the file.
2. Read all lines, normalize them (no caps), keep only the user's.
3. Extract the message bodies.
4. Count the most popular message bodies.
5. Display results.

# Issues
A lot, not gonna spend time listing them here, it's a low effort thing.

Have a nice day.
