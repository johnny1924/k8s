FROM node:16.20.2-alpine3.18

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY public public
COPY src src

EXPOSE 3000

USER node
RUN chown -R node:0 /app
RUN chmod -R 400 /app

ENTRYPOINT [ "npm", "start" ]

