import os
# Developed by: MasterkinG32
# Date: 2024
# Github: https://github.com/masterking32
# Telegram: https://t.me/MasterCryptoFarmBot

config = {
    "web_server": {
        # Host to listen on. For local, use "127.0.0.1".
        # For public access over the internet, use "0.0.0.0" or your public IP address.
        # Ensure the port is open in your firewall and router settings.
        "host": os.environ['HOST'],  # Default: 127.0.0.1
        # Port to listen on. Choose a port number between 1 and 65535.
        # Ensure the chosen port is not already in use by another application.
        "port": os.environ['PORT'],  # Default: 3232
    },
    "telegram_api": {
        # Telegram API credentials. Obtain your API ID and API Hash from https://my.telegram.org/apps.
        "api_id": os.environ['API_ID'],  # Your unique Telegram API ID
        # Your unique Telegram API Hash. Keep this value secure and do not share it publicly.
        "api_hash": os.environ['API_HASH'],  # Your unique Telegram API Hash
    },
    "auto_update": True,  # Automatically update the main bot. If set to True, the bot will restart after an update. Ensure you run the bot with start_linux.sh or start_windows.cmd.
    "auto_update_modules": True,  # Automatically update bot modules.
    "update_check_interval": 3600,  # Interval in seconds to check for updates. Default: 3600 seconds (1 hour).
    "run_delay": 60,  # Delay in seconds before starting the bot modules. Default: 60 second.
    "display_module_logs_in_console": False,  # If set to True, module logs will be displayed in the mcf console.
    "auto_setup_accounts": False,  # Automatically set up your Telegram accounts by adding a last name and profile picture. (Adding a username is mandatory)
}
