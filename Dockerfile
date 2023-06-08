# Use the Microsoft's Playwright-ready Python image
FROM mcr.microsoft.com/playwright/python:v1.27.1-jammy

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./ /app

# Install any additional Python dependencies
RUN pip install -r data_scraping/requirements.txt

# RUN python -m data_scraping.main

# # The command to run your script. Replace `scraper.py` with the actual name of your script
CMD ["python", "-m", "data_scraping.main"]