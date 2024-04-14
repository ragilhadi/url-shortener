# Stage 1: Build the application
FROM node:18-alpine AS builder

WORKDIR /app

COPY url-shortener-frontend/package*.json ./
RUN npm ci

COPY url-shortener-frontend/. .
RUN npm run build
RUN npm prune --production

# Stage 2: Serve the built application with a smaller image
FROM node:18-alpine

WORKDIR /app

# Copy only necessary files from the builder stage
COPY --from=builder /app/build url-shortener-frontend/build/
COPY --from=builder /app/node_modules url-shortener-frontend/node_modules/
COPY url-shortener-frontend/package.json .


EXPOSE 3000
ENV NODE_ENV=production
CMD [ "node", "build" ]
