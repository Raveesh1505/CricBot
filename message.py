"""
Copyright © Raveesh Yadav 2021 - htts://github.com/Raveesh1505
Description:
A Discord bot that plays cricket with the user.

Version: 1.0
"""

RULES = "**__CricBot Game Rules__**\n\n1. To start the game, user must type `>cric play` in the channel. By *default*, the user will get to **bat first**.\n\n2. You can enter **any number from 1 to 6**. At the same time, the system will also choose a random number anywhere from 1 to 6.\n\n3. If the number **matches** with the number that system chose, the user is **OUT**. In case it does not match, the runs will keep on adding to user's scoreboard.\n\n4. After **first innings**, the user will have to bowl. The rules mentioned as above apply for bowling also.\n\n5. Game will end if the **system gets out** or has **scored more runs than the user** (won the game).\n\n6. The user will get a maximum of 15 seconds to give his/her input. Failing to do so will end the game.\n\n\n**__COMMANDS__**\n\n1. `>cric`: Main page of tthe bot. It will give all the details.\n2. `>cric play`: Starts the game.\n3. `>cric help`: Opens help page."

OPEN = "Hello 👋. I see you have come to have some of the best cricket experience on Discord. well, you've landed at the right place.\n\n1. Enter `>cric play` to start the game\n2. Enter `>cric help` to visit the help page and know all the rules."