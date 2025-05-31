FROM python:3.12.10-slim

WORKDIR /app

COPY requirements.txt .
# Copy the application code to the working directory
COPY . /app

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Expose the port on which the application will run
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
