# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
It looked like a guessing the number game
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

1. When I guess the secret key and I choose a number that is lower then the secret key the program will then tell me guess lower. However, when I click on the button another time it will tell me to guess higher. Every time I press on the button it would switch between high or low even though my chosen number remains the same.
2. The new game button does not work. It does not restart the game and it does not take the previous number out of the text box.
3. The hard and medium difficulty ranges should be swapped.
4. The easy and normal attempts needed to be swapped.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
One thing that AI suggested that was correct is fixing the issue of the new game button not working when we would win. I verified the result by running the app again and using the button. Once I clicked on the button it got rid of the previous number I guessed and generated a new number to guess.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
One suggestion that the AI gave that was incorrect when fixing the issue of when I guessed lower than the secret number it would tell me to go guess lower rather then higher. I changed the code however when running the app I realized that if the secret number is 73 and I guessed 71 it would first ask to guess lower then when I click the button again it would then ask to guess higher.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided whether the bug is really fixed or not by asking claude questions such as why did you impliment this in the code. Also through running the test cases.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
One of the test I ran was testing that hint direction is correct for both directions meaning if I guessed a number lower than the secret it would tell me to guess higher. I used pytest where it confirmed that my test passed. 

- Did AI help you design or understand any tests? How?
Yes the AI helpedme design the tests as it was instructed in the project where it asked me to ask copilot to generate a pytest. 

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
The secret number is changing because streamlit re=ran the entire code and because it was not stored anywhere so it chose a random number. 

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit? Streamlit automatically reruns the entire code every time you interact with the button new game. It is like the page reloads every time. Session state stores values between the reruns.

- What change did you make that finally gave the game a stable secret number?
In the code I changed the 1 to 100 for guessing the number to low and high variables so it shows the ranges matching the selected difficulty. I also replaced the 1 to 100 for the secret key to the low and high variables so the secret stays between the selected diffculty ranges. 


---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

One habit of this project that I want to keep reusing is letting the AI know to not make changes in the code until I approve of the changes so I can see if the code is right.

- What is one thing you would do differently next time you work with AI on a coding task?
One thing I would do differently is to make my prompts more specific so the AI does not go above and beyond from what I did ask. 

- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project made me realize to always double check anything that the AI does before adding those edits into the code because sometimes it can be wrong or it adds things you do not want.
