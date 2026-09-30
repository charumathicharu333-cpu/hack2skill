# Build the React frontend
FROM node:20-slim AS fe
WORKDIR /fe
COPY frontend/package.json ./
RUN npm install
COPY frontend ./
RUN npm run build

# Run FastAPI and serve the built frontend from the same container
FROM python:3.12-slim
WORKDIR /app
COPY backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY backend/app ./app
COPY --from=fe /fe/dist ./static
ENV PORT=8080
CMD ["sh","-c","uvicorn app.main:app --host 0.0.0.0 --port ${PORT}"]
