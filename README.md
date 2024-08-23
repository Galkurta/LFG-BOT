# LFG Mining Script

## Table of Contents

1. [Description](#description)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Configuration](#configuration)
6. [Usage](#usage)
7. [Important Notes](#important-notes)
8. [Contributing](#contributing)
9. [License](#license)
10. [Disclaimer](#disclaimer)

## Description

The LFG Mining Script is an automation tool designed for mining on the LFG Web3 platform. This script streamlines the process of managing multiple accounts, performing ad-watching tasks, and upgrading mining machines automatically.

## Features

- 🔧 Multi-account management
- 📺 Automated ad-watching tasks
- ⚙️ Automatic mining machine upgrades
- ⏱️ Countdown timer between cycles
- Register [LFG](https://t.me/lfgweb3official_bot/lfgweb3officialapp?startapp=ref_6944804952)

## Requirements

- Python 3.7+
- pip (Python package manager)

## Installation

1. Clone this repository or download the source code:
   ```
   git clone https://github.com/Galkurta/LFG-BOT.git
   ```
2. Navigate to the project directory:
   ```
   cd LFG-BOT
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Configuration

### Edit `data.txt` file and add the query IDs for each account, one per line:

```
query_id=
query_id=
query_id=
```

## Usage

Run the script with the following command:

```
python main.py
```

The script will:

- Process each account listed in `data.txt`
- Perform mining operations and upgrades
- Wait for 10 minutes between cycles
- Continue running until manually stopped

To stop the script, press `Ctrl+C`.

## Important Notes

- ⚠️ Ensure you have permission to use this script with your LFG Web3 accounts.
- 🚫 Using automation scripts may violate the platform's Terms of Service. Use at your own risk.
- 🔒 This script does not store or transmit your account information to any third parties.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This script is provided "as is", without warranty of any kind, express or implied. The use of this script is entirely at the user's own risk. The authors and contributors of this script are not responsible for any potential damages or losses incurred from its use.
