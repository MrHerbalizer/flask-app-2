FROM node:18

WORKDIR /app
COPY . .

RUN npm init -y
RUN npm install express ejs

EXPOSE 3000
CMD ["node", "app.js"]
