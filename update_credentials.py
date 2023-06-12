import subprocess
import json
import os
import configparser
import argparse
import sys

def update_aws_credentials():
    # Check if settings.ini exists
    if os.path.exists("settings.ini"):
        # Read parameters from settings.ini
        settings = configparser.ConfigParser()
        settings.read("settings.ini")
        if "settings" in settings:
            serial_number = settings.get("settings", "serial_number")
            profile = settings.get("settings", "profile")

            if not serial_number or not profile:
                print("Parameters not provided. Please provide --serial-number and --profile arguments.")
                return

    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--serial-number", help="The MFA device serial number")
    parser.add_argument("--profile", help="The AWS profile name")
    args = parser.parse_args()

    try:
        # Use stored parameters if not provided
        serial_number = args.serial_number or serial_number
        profile = args.profile or profile
    except:
        print("Provide --serial_numnber and --profile arguments")
        sys.exit(1)
    
    # Prompt the user for the MFA token
    mfa_token = input("Enter your six-digit MFA token: ")

    # Run the AWS CLI command and capture the output
    command = f"aws sts get-session-token --duration-seconds 129600 --serial-number {serial_number} --profile {profile} --token-code {mfa_token}"
    output = subprocess.check_output(command, shell=True)

    # Parse the output JSON
    credentials = json.loads(output)["Credentials"]

    # Get the path to the AWS credentials file
    credentials_file = os.path.expanduser("~/.aws/credentials")

    # Load the existing AWS credentials file
    config = configparser.ConfigParser()
    config.read(credentials_file)

    # Remove the existing [default] profile
    if "default" in config:
        config.remove_section("default")

    # Create the [default] profile with the new credentials
    config["default"] = {
        "aws_access_key_id": credentials["AccessKeyId"],
        "aws_secret_access_key": credentials["SecretAccessKey"],
        "aws_session_token": credentials["SessionToken"],
        "expiration": credentials["Expiration"],
    }

    # Save the updated AWS credentials file
    with open(credentials_file, "w") as config_file:
        config.write(config_file)

    # Save the arguments to the settings.ini file
    settings = configparser.ConfigParser()
    settings["settings"] = {
        "serial_number": serial_number,
        "profile": profile
    }
    with open("settings.ini", "w") as settings_file:
        settings.write(settings_file)

if __name__ == "__main__":
    update_aws_credentials()
