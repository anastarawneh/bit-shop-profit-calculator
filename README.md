# bit-shop-profit-calculator
A script to calculate possible profits from selling Hypixel Skyblock Bit Shop items to the Auction House.

## Prerequisites
You need to have Python 3.x installed. I cannot guarantee that older versions will execute the script correctly. I only ever ran the script on Windows 10 using Python 3.8.2. You also need the library `requests`, which you can get using `pip install requests`.

## How to use
1. Download the `main.py` file and save it.
2. Open a Command Prompt in the directory that contains the script (you can enter `cmd` in your Windows Explorer address bar to open a Command Prompt in your current directory).
3. Run the command `python main.py` in your Command Prompt.
4. Enter the amount of bits you get per cookie, which you can check by opening your **Skyblock Menu**, then going to **Cookie Buff**. Alternatively, you can open the script in a text editor and manually change the marked `bits_per_cookie` variable to skip the prompt. You can use the `--setbits` argument to show the prompt regardless of the set value.
5. Wait for the script to download the auctions. This process depends on your internet speed, but it shouldn't take more than two minutes at most.
6. The final output will contain an ordered list of items and their prices, and the best item you should sell at that time. Stonks!

## Future Plans
* Adding enrichments and stacking enchantment books.
