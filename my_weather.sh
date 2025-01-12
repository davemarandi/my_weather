#!/bin/bash

# Define log directory and output file
LOG_DIR="./output/.log"
OUTPUT_FILE="./output/output.txt"

# Create log directory if it doesn't exist
mkdir -p $LOG_DIR

# Step 1: Run weather.py
echo "Running weather.py..."
python weather.py

# Check if weather.py ran successfully
if [ $? -eq 0 ]; then
    echo "weather.py completed successfully."

    # Step 2: Run telegrambot.py
    echo "Running telegram_bot.py..."
    python telegram_bot.py

    if [ $? -eq 0 ]; then
        echo "telegram_bot.py completed successfully."
    else
        echo "Error: telegram_bot.py failed."
    fi
else
    echo "Error: weather.py failed. Skipping telegram_bot.py."
fi

# Step 3: Move output.txt to the log directory (without keeping the original)
if [ -f "$OUTPUT_FILE" ]; then
    TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
    mv $OUTPUT_FILE "$LOG_DIR/output_$TIMESTAMP.txt"  # Move the file (not copy)
    echo "Moved $OUTPUT_FILE to $LOG_DIR/output_$TIMESTAMP.txt"
else
    echo "Error: $OUTPUT_FILE not found. Nothing to move."
fi
