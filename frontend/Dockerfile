# frontend/Dockerfile using npm
FROM node:18-alpine

WORKDIR /app

# Copy package.json and install dependencies using npm
COPY package.json ./
RUN npm install

# Copy the rest of your code
COPY . .

# Build the Next.js app
RUN npm run build

EXPOSE 3000

# Start the Next.js server
CMD ["npm", "start"]
