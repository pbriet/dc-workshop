FROM node:16

WORKDIR /app

RUN npm install -g nodemon express mysql

COPY src/* /app

EXPOSE 3000

ENV NODE_PATH=/usr/local/lib/node_modules

CMD ["nodemon", "app.js"]