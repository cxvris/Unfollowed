<h1 align="center">Unfollowed</h1>

## Project Info
Using Instagram's data download feature, this tool lets you see who hasn't followed you back on Instagram and vice versa. Unlike other online options, our program can handle big sets of follower/following data without being slowed down by Instagram's limits.

Plus, since this app works on your device, there's no risk of your Instagram account getting flagged as a bot or dealing with rate limits.

<br/>

### Installation
1. Install [Python3](https://www.python.org/downloads/)
2. Clone the repo<br/>
```git clone https://github.com/maodus/unfollowed.git```

<br/>

### Usage
Before using this app, you will want to obtain your **JSON** Instagram data in the `.zip` file format. This will **NOT** work if you select the **HTML** configuration when downloading.

1. Download your Instagram usage data. **Do not unzip the file**.
2. Run `unfollowed.py`
   * For Windows CMD: ```python unfollowed.py``` or ```unfollowed.py```
   * For UNIX (Mac/Linux): ```python3 unfollowed.py``` or ```python unfollowed.py```
3. When prompted, type in a valid file path that points to your zipped data file. The zip file does not have to be inside the same directory.
4. Check out your results in `/ig_results/`.

<br/>
