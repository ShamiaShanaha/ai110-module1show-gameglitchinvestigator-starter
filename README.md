# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

The purpose of the game was to guess the secret key. You get to difficulty from normal to hard. Each level has the range of numbers you can guess from and also the amount of attempts you can commit. 

The bugs that I found in the glitch game:
1. When I guess the secret key and I choose a number that is lower then the secret key the program will then tell me guess lower. However, when I click on the button another time it will tell me to guess higher. Every time I press on the button it would switch between high or low even though my chosen number remains the same.
2. The new game button does not work. It does not restart the game and it does not take the previous number out of the text box.
3. The hard and medium difficulty ranges should be swapped.
4. The easy and normal attempts needed to be swapped.

Fixes I applied:
1. For the first bug the fix was to make sure the comparison was in integers rather then string. Also to change the hint original message to this if the guess is higher than the secret it says “Go LOWER!”, and if the guess is lower than the secret it says “Go HIGHER!”.
2. For the second bug the fix was to reset the attempt counter, generate a new secret within the current difficulty range, reset the game status to playing and change the text input widgets key so Streamlit clears the input field.
3. For the third bug I just swapped the ranges so normal is from 1-50 and hard is 1-100.
4. For the fourth bug I just swapped the attempts of easy and normal. 


## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

Bug 1 Solved:
![image alt](https://github.com/ShamiaShanaha/ai110-module1show-gameglitchinvestigator-starter/blob/main/Bug1.png?raw=true)

Bug 2 Solved:
![image alt](https://github.com/ShamiaShanaha/ai110-module1show-gameglitchinvestigator-starter/blob/main/Bug2.png?raw=true)


My pytests:
![image alt](https://github.com/ShamiaShanaha/ai110-module1show-gameglitchinvestigator-starter/blob/main/pytest.png?raw=true)




## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
