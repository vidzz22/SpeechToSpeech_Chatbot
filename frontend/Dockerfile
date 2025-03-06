# Use an official Node runtime as a parent image
FROM node:18-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package files and install dependencies
COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile

# Copy the rest of your code into the container
COPY . .

# Build the Next.js app
RUN yarn build

# Expose port 3000 for the app
EXPOSE 3000

# Start the Next.js server
CMD ["yarn", "start"]
