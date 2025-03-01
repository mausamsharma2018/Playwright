# Use the official Playwright image with Python
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app


# Copy all project files into the container
COPY . .

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget curl unzip \
    libnss3 libatk1.0-0 libatk-bridge2.0-0 libcups2 \
    libxcomposite1 libxrandr2 libasound2 libpangocairo-1.0-0 \
    libxdamage1 libgbm-dev libpango-1.0-0 libxshmfence1 libgtk-3-0 xvfb && \
    apt-get clean


COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Install Playwright Browsers
RUN python -m playwright install --with-deps

RUN python -m playwright install chromium

# Default command to run Playwright tests.
CMD ["pytest", "--browser=chromium"]
#USER root  # Ensures you have root privileges
