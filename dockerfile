# Use the official Playwright image with Python
FROM mcr.microsoft.com/playwright/python:v1.42.0-focal

# Set the working directory inside the container
WORKDIR /app


# Copy all project files into the container
COPY . .

# Install Playwright browsers
RUN python -m playwright install
RUN python -m playwright install-deps

# Default command to run Playwright tests
CMD ["pytest", "--browser=chromium"]
