FROM python:3.11-slim


# Set working directory
WORKDIR /app


# Copy files into working directory
COPY files/ ./files/
COPY main.py .
COPY wordle_functions.py .


# Install dependencies
RUN pip install --no-cache-dir -r files/requirements.txt


# Expose port 8000 for app
EXPOSE 8000


# Command to run FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]