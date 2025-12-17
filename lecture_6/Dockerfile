# Use a lightweight official Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Install required Python packages
RUN pip install --no-cache-dir fastapi uvicorn

# Copy the application source code into the container
COPY main.py .

# Expose the port the app will run on
EXPOSE 8000

# Command to run the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
